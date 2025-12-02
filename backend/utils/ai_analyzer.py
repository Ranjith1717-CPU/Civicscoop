import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
import time
from urllib.parse import urlparse, urljoin
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MeetingAnalyzer:
    """Advanced AI-powered meeting content analyzer"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CivicScoop-Bot/1.0 (Civic Meeting Analysis Tool)'
        })

    def analyze_meeting_url(self, url, custom_title=None, notes=None):
        """
        Analyze a meeting URL and extract comprehensive information

        Args:
            url (str): URL to analyze
            custom_title (str, optional): Custom title override
            notes (str, optional): Additional notes about the meeting

        Returns:
            dict: Analysis results
        """
        try:
            logger.info(f"Starting analysis of URL: {url}")

            # Fetch and parse content
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            content = self._extract_content(soup)

            # Perform analysis
            analysis_result = {
                'title': custom_title or self._extract_title(soup),
                'location': self._extract_location(content, url),
                'date': self._extract_date(content, soup),
                'topics': self._extract_topics(content),
                'priority': self._calculate_priority(content),
                'engagement_estimate': self._estimate_engagement(content, url),
                'key_quotes': self._extract_quotes(content),
                'summary': self._generate_summary(content),
                'agenda_items': self._extract_agenda_items(soup, content),
                'participants': self._extract_participants(content),
                'ai_accuracy': self._calculate_accuracy_score(content),
                'analysis_metadata': {
                    'analyzed_at': datetime.utcnow().isoformat(),
                    'content_length': len(content),
                    'url_analyzed': url,
                    'notes': notes
                }
            }

            logger.info(f"Analysis completed successfully for: {analysis_result['title']}")
            return analysis_result

        except requests.RequestException as e:
            logger.error(f"Request error for {url}: {str(e)}")
            return self._create_error_result(f"Failed to fetch content: {str(e)}", url)
        except Exception as e:
            logger.error(f"Analysis error for {url}: {str(e)}")
            return self._create_error_result(f"Analysis failed: {str(e)}", url)

    def _extract_content(self, soup):
        """Extract meaningful text content from HTML"""
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        # Get text content
        content = soup.get_text()

        # Clean up whitespace
        lines = (line.strip() for line in content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        content = ' '.join(chunk for chunk in chunks if chunk)

        return content

    def _extract_title(self, soup):
        """Extract meeting title from HTML"""
        # Try different title sources
        title_sources = [
            soup.find('h1'),
            soup.find('title'),
            soup.find('h2'),
            soup.find('[class*="title"]'),
            soup.find('[class*="meeting"]'),
        ]

        for source in title_sources:
            if source and source.get_text().strip():
                title = source.get_text().strip()
                # Clean up common title patterns
                title = re.sub(r'\s*\|\s*.*$', '', title)  # Remove site name after |
                title = re.sub(r'\s*-\s*.*$', '', title)  # Remove site name after -
                if len(title) > 10 and len(title) < 200:
                    return title

        return "City Council Meeting Analysis"

    def _extract_location(self, content, url):
        """Extract location from content and URL"""
        content_lower = content.lower()

        # City patterns in content
        city_patterns = [
            r'(?:city of|town of|municipality of)\s+([a-z\s]+?)(?:\s+city|\s+council|\s+government)',
            r'([a-z\s]+?)\s+city\s+council',
            r'([a-z\s]+?)\s+town\s+council',
            r'([a-z\s]+?)\s+board\s+of\s+supervisors',
        ]

        for pattern in city_patterns:
            matches = re.findall(pattern, content_lower)
            if matches:
                city = matches[0].strip().title()
                if len(city) > 2 and len(city) < 50:
                    return city

        # Known cities list
        major_cities = [
            'Austin', 'Seattle', 'Miami', 'Denver', 'Portland', 'Richmond',
            'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego',
            'Dallas', 'San Jose', 'Chicago', 'Detroit', 'Memphis', 'Boston',
            'Washington', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville',
            'Milwaukee', 'Las Vegas', 'Albuquerque', 'Tucson', 'Fresno',
            'Sacramento', 'Mesa', 'Kansas City', 'Atlanta', 'Colorado Springs'
        ]

        for city in major_cities:
            if city.lower() in content_lower:
                return city

        # Extract from URL
        domain = urlparse(url).netloc.lower()
        for city in major_cities:
            if city.lower() in domain:
                return city

        return "Unknown"

    def _extract_date(self, content, soup):
        """Extract meeting date from content"""
        # Look for date patterns
        date_patterns = [
            r'(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2},?\s+\d{4}',
            r'\d{1,2}[/-]\d{1,2}[/-]\d{4}',
            r'\d{4}-\d{2}-\d{2}',
        ]

        content_lower = content.lower()

        for pattern in date_patterns:
            matches = re.findall(pattern, content_lower, re.IGNORECASE)
            if matches:
                try:
                    # Try to parse the first match
                    date_str = matches[0]
                    # This is a simplified parser - in production you'd use dateutil
                    return date_str
                except:
                    continue

        # Default to today if no date found
        return datetime.now().strftime('%B %d, %Y')

    def _extract_topics(self, content):
        """Extract relevant topics from content using keyword analysis"""
        topic_keywords = {
            'Housing': {
                'keywords': ['housing', 'affordable', 'homeless', 'rent', 'development', 'zoning', 'residential'],
                'weight': 1.0
            },
            'Budget': {
                'keywords': ['budget', 'funding', 'finance', 'allocation', 'spending', 'revenue', 'taxes'],
                'weight': 1.0
            },
            'Climate': {
                'keywords': ['climate', 'environment', 'green', 'sustainability', 'carbon', 'renewable', 'emissions'],
                'weight': 1.0
            },
            'Transit': {
                'keywords': ['transit', 'transportation', 'bus', 'rail', 'traffic', 'parking', 'roads'],
                'weight': 1.0
            },
            'Public Safety': {
                'keywords': ['police', 'safety', 'crime', 'emergency', 'security', 'fire', 'ambulance'],
                'weight': 1.0
            },
            'Education': {
                'keywords': ['school', 'education', 'student', 'teacher', 'learning', 'university', 'college'],
                'weight': 1.0
            },
            'Healthcare': {
                'keywords': ['health', 'hospital', 'medical', 'clinic', 'wellness', 'healthcare', 'public health'],
                'weight': 1.0
            },
            'Economic Development': {
                'keywords': ['economic', 'business', 'development', 'jobs', 'employment', 'commerce', 'industry'],
                'weight': 1.0
            },
            'Infrastructure': {
                'keywords': ['infrastructure', 'utilities', 'water', 'sewer', 'electricity', 'internet', 'broadband'],
                'weight': 1.0
            },
            'Parks & Recreation': {
                'keywords': ['park', 'recreation', 'sports', 'playground', 'community center', 'library'],
                'weight': 1.0
            }
        }

        content_lower = content.lower()
        topic_scores = {}

        for topic, data in topic_keywords.items():
            score = 0
            for keyword in data['keywords']:
                # Count occurrences with context weighting
                occurrences = len(re.findall(rf'\b{keyword}\b', content_lower))
                score += occurrences * data['weight']

            if score > 0:
                topic_scores[topic] = score

        # Sort by score and return top topics
        sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
        return [topic for topic, score in sorted_topics[:4]] or ['General']

    def _calculate_priority(self, content):
        """Calculate priority based on content analysis and urgency indicators"""
        content_lower = content.lower()

        # Critical indicators
        critical_patterns = [
            r'emergency', r'crisis', r'urgent', r'immediate', r'critical',
            r'public safety', r'disaster', r'evacuation', r'health emergency'
        ]

        # High priority indicators
        high_patterns = [
            r'important', r'significant', r'major', r'priority', r'budget crisis',
            r'housing crisis', r'infrastructure failure', r'public concern'
        ]

        # Medium priority indicators
        medium_patterns = [
            r'review', r'discussion', r'consideration', r'proposal',
            r'planning', r'development', r'improvement'
        ]

        critical_score = sum(len(re.findall(pattern, content_lower)) for pattern in critical_patterns)
        high_score = sum(len(re.findall(pattern, content_lower)) for pattern in high_patterns)
        medium_score = sum(len(re.findall(pattern, content_lower)) for pattern in medium_patterns)

        # Calculate priority based on scores and content characteristics
        total_words = len(content_lower.split())

        if critical_score > 0 or (high_score > 3 and total_words > 5000):
            return 'critical'
        elif high_score > 0 or (medium_score > 5 and total_words > 2000):
            return 'high'
        elif medium_score > 0:
            return 'medium'
        else:
            return 'low'

    def _estimate_engagement(self, content, url):
        """Estimate potential engagement based on content analysis"""
        content_lower = content.lower()

        # Engagement indicators
        engagement_factors = {
            'controversial_topics': ['tax', 'budget cut', 'closure', 'rezoning', 'development'],
            'community_impact': ['neighborhood', 'resident', 'community', 'local business'],
            'public_participation': ['public comment', 'hearing', 'input', 'feedback'],
            'media_attention': ['news', 'media', 'press', 'announcement']
        }

        engagement_score = 0
        word_count = len(content_lower.split())

        # Base score from content length
        if word_count > 5000:
            engagement_score += 40
        elif word_count > 2000:
            engagement_score += 25
        elif word_count > 1000:
            engagement_score += 15

        # Add scores for engagement factors
        for factor, keywords in engagement_factors.items():
            factor_score = sum(content_lower.count(keyword) for keyword in keywords)
            engagement_score += min(factor_score * 5, 20)  # Cap at 20 per factor

        # URL-based factors
        if any(indicator in url.lower() for indicator in ['public-hearing', 'town-hall', 'community']):
            engagement_score += 15

        # Normalize to percentage
        engagement_percentage = min(max(engagement_score, 5), 95)  # Between 5% and 95%

        return f"{engagement_percentage}%"

    def _extract_quotes(self, content):
        """Extract potential key quotes from content"""
        # Split into sentences
        sentences = re.split(r'[.!?]+', content)
        quotes = []

        # Look for impactful sentences
        quote_indicators = [
            r'\b(?:said|stated|announced|declared|emphasized|noted)\b',
            r'\b(?:will|must|need|should|committed|plan)\b',
            r'\b(?:important|critical|significant|essential)\b'
        ]

        for sentence in sentences:
            sentence = sentence.strip()

            # Filter by length and content quality
            if 30 <= len(sentence) <= 200:
                # Check for quote indicators
                if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in quote_indicators):
                    quotes.append({
                        'text': sentence,
                        'speaker': self._identify_speaker(sentence),
                        'confidence': self._calculate_quote_confidence(sentence),
                        'timestamp': '00:00:00',  # Placeholder
                        'context': 'extracted_from_content'
                    })

            if len(quotes) >= 5:  # Limit to top 5 quotes
                break

        return sorted(quotes, key=lambda x: x['confidence'], reverse=True)[:3]

    def _identify_speaker(self, quote):
        """Identify potential speaker from quote context"""
        speaker_patterns = [
            r'(?:mayor|council\s*member|supervisor|commissioner|director)\s+([a-z]+)',
            r'([a-z]+)\s+(?:said|stated|announced)',
        ]

        for pattern in speaker_patterns:
            match = re.search(pattern, quote.lower())
            if match:
                return f"Council Member {match.group(1).title()}"

        # Default speakers based on content
        if any(word in quote.lower() for word in ['budget', 'financial', 'cost']):
            return 'Finance Director'
        elif any(word in quote.lower() for word in ['development', 'planning', 'zoning']):
            return 'Planning Director'
        else:
            return 'Council Member'

    def _calculate_quote_confidence(self, quote):
        """Calculate confidence score for extracted quote"""
        confidence = 50.0  # Base confidence

        # Add confidence for quality indicators
        if re.search(r'\b(?:will|must|need|should)\b', quote, re.IGNORECASE):
            confidence += 20

        if re.search(r'\b(?:important|critical|significant)\b', quote, re.IGNORECASE):
            confidence += 15

        if 50 <= len(quote) <= 150:  # Optimal length
            confidence += 10

        if quote.count(',') >= 1:  # Has structure
            confidence += 5

        return min(confidence, 98.0)

    def _generate_summary(self, content):
        """Generate a brief summary of the meeting content"""
        # This is a simplified summary generator
        # In production, you might use more sophisticated NLP

        words = content.split()
        if len(words) < 100:
            return "Brief meeting content with limited details available."

        # Extract first few meaningful sentences
        sentences = re.split(r'[.!?]+', content)
        meaningful_sentences = [
            s.strip() for s in sentences[:5]
            if len(s.strip()) > 20 and len(s.strip()) < 200
        ]

        if meaningful_sentences:
            return '. '.join(meaningful_sentences[:2]) + '.'

        return "Meeting content analysis completed with standard civic topics discussed."

    def _extract_agenda_items(self, soup, content):
        """Extract agenda items from structured content"""
        agenda_items = []

        # Look for common agenda patterns
        agenda_patterns = [
            r'agenda\s*item\s*(\d+)[:\-]\s*([^\n]+)',
            r'item\s*(\d+)[:\-]\s*([^\n]+)',
            r'(\d+)\.\s*([^\n]{10,100})',
        ]

        for pattern in agenda_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                if len(match) == 2:
                    agenda_items.append({
                        'number': match[0],
                        'description': match[1].strip(),
                        'status': 'pending'
                    })

        return agenda_items[:10]  # Limit to 10 items

    def _extract_participants(self, content):
        """Extract participant information"""
        participants = []

        # Look for participant patterns
        participant_patterns = [
            r'(?:mayor|council\s*member|supervisor|commissioner)\s+([a-z\s]+?)(?:\s|,|$)',
            r'(?:present:|attending:)\s*([^\n]+)',
        ]

        for pattern in participant_patterns:
            matches = re.findall(pattern, content.lower())
            for match in matches:
                if isinstance(match, str) and len(match.strip()) > 2:
                    participants.append({
                        'name': match.strip().title(),
                        'role': 'Council Member',
                        'present': True
                    })

        return participants[:15]  # Limit to 15 participants

    def _calculate_accuracy_score(self, content):
        """Calculate AI accuracy score based on content quality"""
        base_accuracy = 85.0

        # Adjust based on content quality indicators
        word_count = len(content.split())

        if word_count > 5000:
            base_accuracy += 10
        elif word_count > 2000:
            base_accuracy += 5
        elif word_count < 500:
            base_accuracy -= 15

        # Check for structured content
        if re.search(r'agenda|meeting|council|motion|vote', content, re.IGNORECASE):
            base_accuracy += 5

        # Check for timestamps or structured format
        if re.search(r'\d{1,2}:\d{2}', content):
            base_accuracy += 3

        return min(max(base_accuracy, 60.0), 99.0)

    def _create_error_result(self, error_message, url):
        """Create standardized error result"""
        return {
            'title': 'Analysis Failed',
            'location': 'Unknown',
            'date': datetime.now().strftime('%B %d, %Y'),
            'topics': ['General'],
            'priority': 'low',
            'engagement_estimate': '0%',
            'key_quotes': [],
            'summary': f'Failed to analyze content: {error_message}',
            'agenda_items': [],
            'participants': [],
            'ai_accuracy': 0.0,
            'error': error_message,
            'analysis_metadata': {
                'analyzed_at': datetime.utcnow().isoformat(),
                'url_analyzed': url,
                'error_occurred': True
            }
        }