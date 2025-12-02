from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
import re
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'civicscoop-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civicscoop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# Enhanced CORS configuration for frontend integration
CORS(app, origins=['*'],
     allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

# Database Models
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(500), nullable=False)
    priority = db.Column(db.String(20), default='medium')
    priority_score = db.Column(db.String(10), default='50%')
    segments = db.Column(db.String(50), default='0:0 high segments')
    engagement = db.Column(db.String(50), default='0% high engagement')
    ai_accuracy = db.Column(db.Float, default=95.0)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # JSON fields
    topics = db.Column(db.Text, default='[]')  # JSON array
    quotes = db.Column(db.Text, default='[]')  # JSON array
    analysis = db.Column(db.Text, default='{}')  # JSON object

    def get_topics(self):
        return json.loads(self.topics) if self.topics else []

    def set_topics(self, topics_list):
        self.topics = json.dumps(topics_list)

    def get_quotes(self):
        return json.loads(self.quotes) if self.quotes else []

    def set_quotes(self, quotes_list):
        self.quotes = json.dumps(quotes_list)

    def get_analysis(self):
        return json.loads(self.analysis) if self.analysis else {}

    def set_analysis(self, analysis_dict):
        self.analysis = json.dumps(analysis_dict)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='pending')
    file_path = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    config = db.Column(db.Text, default='{}')  # JSON object

# AI Analysis Functions
class MeetingAnalyzer:
    @staticmethod
    def analyze_meeting_url(url):
        """Analyze a meeting URL and extract information"""
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract basic information
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "Meeting Analysis"

            # Try to find meeting-specific content
            content = soup.get_text()

            # Simple AI simulation - extract key information
            analysis_result = {
                'title': title_text,
                'location': MeetingAnalyzer._extract_location(content),
                'topics': MeetingAnalyzer._extract_topics(content),
                'priority': MeetingAnalyzer._calculate_priority(content),
                'engagement_estimate': MeetingAnalyzer._estimate_engagement(content),
                'key_quotes': MeetingAnalyzer._extract_quotes(content),
                'ai_accuracy': 95.5
            }

            return analysis_result
        except Exception as e:
            return {
                'title': 'Analysis Failed',
                'location': 'Unknown',
                'topics': ['General'],
                'priority': 'low',
                'engagement_estimate': '25%',
                'key_quotes': [],
                'ai_accuracy': 0.0,
                'error': str(e)
            }

    @staticmethod
    def _extract_location(content):
        """Extract location from content"""
        cities = ['Austin', 'Seattle', 'Miami', 'Denver', 'Portland', 'Richmond', 'Houston', 'Phoenix']
        for city in cities:
            if city.lower() in content.lower():
                return city
        return 'Unknown'

    @staticmethod
    def _extract_topics(content):
        """Extract relevant topics from content"""
        topic_keywords = {
            'Housing': ['housing', 'affordable', 'homeless', 'rent', 'development'],
            'Budget': ['budget', 'funding', 'finance', 'allocation', 'spending'],
            'Climate': ['climate', 'environment', 'green', 'sustainability', 'carbon'],
            'Transit': ['transit', 'transportation', 'bus', 'rail', 'traffic'],
            'Public Safety': ['police', 'safety', 'crime', 'emergency', 'security'],
            'Education': ['school', 'education', 'student', 'teacher', 'learning']
        }

        found_topics = []
        content_lower = content.lower()

        for topic, keywords in topic_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                found_topics.append(topic)

        return found_topics[:3] if found_topics else ['General']

    @staticmethod
    def _calculate_priority(content):
        """Calculate priority based on content analysis"""
        critical_keywords = ['emergency', 'crisis', 'urgent', 'immediate', 'critical']
        high_keywords = ['important', 'significant', 'major', 'priority']

        content_lower = content.lower()

        if any(keyword in content_lower for keyword in critical_keywords):
            return 'critical'
        elif any(keyword in content_lower for keyword in high_keywords):
            return 'high'
        else:
            return 'medium'

    @staticmethod
    def _estimate_engagement(content):
        """Estimate engagement based on content length and complexity"""
        word_count = len(content.split())

        if word_count > 5000:
            return '85%'
        elif word_count > 2000:
            return '65%'
        elif word_count > 1000:
            return '45%'
        else:
            return '25%'

    @staticmethod
    def _extract_quotes(content):
        """Extract potential quotes from content"""
        # Simple quote extraction
        sentences = re.split(r'[.!?]+', content)
        quotes = []

        for sentence in sentences[:10]:  # Check first 10 sentences
            sentence = sentence.strip()
            if len(sentence) > 50 and len(sentence) < 200:
                if any(word in sentence.lower() for word in ['will', 'need', 'important', 'council', 'community']):
                    quotes.append({
                        'text': sentence,
                        'speaker': 'Council Member',
                        'confidence': 85.0,
                        'timestamp': '00:00:00'
                    })
                    if len(quotes) >= 3:
                        break

        return quotes

# Routes
@app.route('/')
def dashboard():
    meetings = Meeting.query.order_by(Meeting.created_at.desc()).limit(10).all()
    return render_template('dashboard.html', meetings=meetings)

@app.route('/add_meeting')
def add_meeting_page():
    return render_template('add_meeting.html')

@app.route('/api/analyze_meeting', methods=['POST'])
def analyze_meeting():
    """API endpoint to analyze a meeting URL"""
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Analyze the meeting
        analysis = MeetingAnalyzer.analyze_meeting_url(url)

        if 'error' in analysis:
            return jsonify({'error': analysis['error']}), 400

        # Create meeting record
        meeting = Meeting(
            title=analysis['title'],
            location=analysis['location'],
            url=url,
            priority=analysis['priority'],
            priority_score=f"{min(95, max(20, len(analysis['title']) + 50))}%",
            engagement=f"{analysis['engagement_estimate']} high engagement",
            ai_accuracy=analysis['ai_accuracy'],
            date=datetime.now(),
            status='analyzed'
        )

        meeting.set_topics(analysis['topics'])
        meeting.set_quotes(analysis['key_quotes'])
        meeting.set_analysis(analysis)

        db.session.add(meeting)
        db.session.commit()

        # Format analysis to match frontend expectations
        formatted_analysis = {
            'title': analysis['title'],
            'location': analysis['location'],
            'date': datetime.now().strftime('%B %d, %Y'),
            'topics': analysis['topics'],
            'priority': analysis['priority'],
            'engagement_estimate': analysis['engagement_estimate'],
            'key_quotes': analysis['key_quotes'],
            'ai_accuracy': analysis['ai_accuracy'],
            'summary': f"Meeting focused on {', '.join(analysis['topics'][:2])} with {analysis['priority']} priority level."
        }

        return jsonify({
            'success': True,
            'meeting_id': meeting.id,
            'analysis': formatted_analysis
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/meetings')
def get_meetings():
    """API endpoint to get all meetings"""
    meetings = Meeting.query.order_by(Meeting.created_at.desc()).all()

    meetings_data = []
    for meeting in meetings:
        meetings_data.append({
            'id': meeting.id,
            'title': meeting.title,
            'location': meeting.location,
            'date': meeting.date.strftime('%Y-%m-%d'),
            'priority': meeting.priority,
            'priority_score': meeting.priority_score,
            'engagement': meeting.engagement,
            'topics': meeting.get_topics(),
            'status': meeting.status,
            'url': meeting.url
        })

    return jsonify(meetings_data)

@app.route('/api/meeting/<int:meeting_id>')
def get_meeting(meeting_id):
    """API endpoint to get a specific meeting"""
    meeting = Meeting.query.get_or_404(meeting_id)

    return jsonify({
        'id': meeting.id,
        'title': meeting.title,
        'location': meeting.location,
        'date': meeting.date.strftime('%Y-%m-%d'),
        'priority': meeting.priority,
        'priority_score': meeting.priority_score,
        'engagement': meeting.engagement,
        'topics': meeting.get_topics(),
        'quotes': meeting.get_quotes(),
        'analysis': meeting.get_analysis(),
        'status': meeting.status,
        'url': meeting.url,
        'ai_accuracy': meeting.ai_accuracy
    })

@app.route('/api/delete_meeting/<int:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    """API endpoint to delete a meeting"""
    meeting = Meeting.query.get_or_404(meeting_id)
    db.session.delete(meeting)
    db.session.commit()

    return jsonify({'success': True})

@app.route('/meeting/<int:meeting_id>')
def meeting_detail(meeting_id):
    """Meeting detail page"""
    meeting = Meeting.query.get_or_404(meeting_id)
    return render_template('meeting_detail.html', meeting=meeting)

@app.route('/analytics')
def analytics():
    """Analytics dashboard"""
    meetings = Meeting.query.all()

    # Calculate analytics
    total_meetings = len(meetings)
    avg_accuracy = sum(m.ai_accuracy for m in meetings) / total_meetings if meetings else 0

    priority_counts = {}
    location_counts = {}

    for meeting in meetings:
        priority_counts[meeting.priority] = priority_counts.get(meeting.priority, 0) + 1
        location_counts[meeting.location] = location_counts.get(meeting.location, 0) + 1

    analytics_data = {
        'total_meetings': total_meetings,
        'avg_accuracy': round(avg_accuracy, 1),
        'priority_distribution': priority_counts,
        'location_distribution': location_counts
    }

    return render_template('analytics.html', analytics=analytics_data, meetings=meetings)

@app.route('/reports')
def reports():
    """Reports page"""
    reports = Report.query.order_by(Report.created_at.desc()).all()
    return render_template('reports.html', reports=reports)

@app.route('/settings')
def settings():
    """Settings page"""
    return render_template('settings.html')

# Initialize database
def create_tables():
    with app.app_context():
        db.create_all()

        # Add sample data if no meetings exist
        if Meeting.query.count() == 0:
        sample_meetings = [
            {
                'title': 'Austin City Council Meeting: Housing Crisis Response',
                'location': 'Austin',
                'date': datetime(2024, 8, 15),
                'url': 'https://austin.gov/meetings/housing-crisis',
                'priority': 'critical',
                'priority_score': '95%',
                'engagement': '85.3% high engagement',
                'topics': ['Housing', 'Crisis Response', 'Public Policy']
            },
            {
                'title': 'Seattle City Council Session: 2025 Budget Allocation',
                'location': 'Seattle',
                'date': datetime(2024, 7, 22),
                'url': 'https://seattle.gov/meetings/budget-2025',
                'priority': 'high',
                'priority_score': '73%',
                'engagement': '73.2% high engagement',
                'topics': ['Budget', 'Finance', 'Public Services']
            }
        ]

        for meeting_data in sample_meetings:
            meeting = Meeting(**meeting_data)
            meeting.set_topics(meeting_data['topics'])
            db.session.add(meeting)

        db.session.commit()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)