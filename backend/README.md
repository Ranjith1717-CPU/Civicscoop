# CivicScoop Backend

Complete backend system for the CivicScoop AI-Powered Civic Intelligence Platform.

## Features

### Core Functionality
- **Meeting URL Analysis**: Insert any meeting URL and get AI-powered analysis
- **Real-time AI Processing**: Extract topics, quotes, priorities, and engagement metrics
- **Database Management**: SQLite database with full CRUD operations
- **RESTful API**: Complete API for frontend integration
- **Admin Dashboard**: Web interface for managing meetings and reports

### AI Analysis Capabilities
- **Content Extraction**: Smart content parsing from any website
- **Topic Detection**: Automatic identification of civic topics (Housing, Budget, Climate, etc.)
- **Priority Assessment**: Critical/High/Medium/Low priority classification
- **Quote Extraction**: AI-powered extraction of key quotes with speaker identification
- **Engagement Prediction**: Estimate citizen engagement potential
- **Summary Generation**: Automated meeting summaries

### Meeting Link Insertion
- **Universal URL Support**: Analyze any meeting URL or webpage
- **Custom Title Override**: Option to set custom meeting titles
- **Additional Notes**: Add context and notes for meetings
- **Real-time Feedback**: Live analysis status and progress indicators
- **Error Handling**: Comprehensive error reporting and suggestions

## Quick Start

### 1. Installation

```bash
# Clone or copy the backend folder
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Initialize the database
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### 2. Run the Development Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

### 3. Access the Interface

- **Dashboard**: http://localhost:5000/
- **Add Meeting**: http://localhost:5000/add_meeting
- **Analytics**: http://localhost:5000/analytics
- **Reports**: http://localhost:5000/reports
- **Settings**: http://localhost:5000/settings

## API Endpoints

### Meeting Management

#### Analyze New Meeting
```http
POST /api/analyze_meeting
Content-Type: application/json

{
  "url": "https://example.com/city-council-meeting",
  "custom_title": "Optional custom title",
  "notes": "Optional additional notes"
}
```

#### Get All Meetings
```http
GET /api/meetings
```

#### Get Specific Meeting
```http
GET /api/meeting/{id}
```

#### Delete Meeting
```http
DELETE /api/delete_meeting/{id}
```

### Example Response

```json
{
  "success": true,
  "meeting_id": 1,
  "analysis": {
    "title": "Austin City Council Meeting: Housing Crisis Response",
    "location": "Austin",
    "date": "December 2, 2024",
    "topics": ["Housing", "Crisis Response", "Public Policy"],
    "priority": "critical",
    "engagement_estimate": "85%",
    "key_quotes": [
      {
        "text": "We need immediate action on the housing affordability crisis.",
        "speaker": "Council Member Johnson",
        "confidence": 95.5,
        "timestamp": "00:00:00"
      }
    ],
    "ai_accuracy": 96.8,
    "summary": "Meeting focused on addressing critical housing challenges..."
  }
}
```

## Database Schema

### Meetings Table
- **id**: Primary key
- **title**: Meeting title
- **location**: City/location
- **date**: Meeting date
- **url**: Source URL
- **priority**: critical/high/medium/low
- **priority_score**: Percentage score
- **engagement**: Engagement estimate
- **ai_accuracy**: AI confidence score
- **topics**: JSON array of topics
- **quotes**: JSON array of quotes
- **analysis**: JSON object with full analysis
- **created_at**: Timestamp

### Users Table
- **id**: Primary key
- **username**: Unique username
- **email**: Unique email
- **role**: user/admin
- **created_at**: Timestamp

### Reports Table
- **id**: Primary key
- **name**: Report name
- **type**: Report type
- **status**: pending/processing/ready
- **file_path**: Generated file path
- **config**: JSON configuration

## Configuration

### Environment Variables
```bash
# Database
DATABASE_URL=sqlite:///civicscoop.db

# Security
SECRET_KEY=your-secret-key-here

# Development settings
FLASK_ENV=development
FLASK_DEBUG=1
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

#### Using Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## File Structure

```
backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── config/
│   └── settings.py       # Configuration settings
│
├── models/
│   └── database.py       # Database models
│
├── utils/
│   └── ai_analyzer.py    # AI analysis engine
│
├── templates/
│   ├── dashboard.html    # Main dashboard
│   └── add_meeting.html  # Meeting insertion form
│
└── static/
    ├── css/             # Stylesheets
    ├── js/              # JavaScript files
    └── uploads/         # File uploads
```

## Usage Examples

### Adding a New Meeting

1. **Via Web Interface**:
   - Go to http://localhost:5000/add_meeting
   - Enter meeting URL
   - Optionally add custom title and notes
   - Click "Analyze Meeting with AI"

2. **Via API**:
```python
import requests

response = requests.post('http://localhost:5000/api/analyze_meeting', json={
    'url': 'https://austin.gov/council-meeting-2024-12-02',
    'custom_title': 'Austin Housing Emergency Session',
    'notes': 'Special session called for housing crisis'
})

result = response.json()
print(f"Meeting ID: {result['meeting_id']}")
```

### Retrieving Analysis Results

```python
import requests

# Get all meetings
meetings = requests.get('http://localhost:5000/api/meetings').json()

# Get specific meeting
meeting_id = 1
meeting = requests.get(f'http://localhost:5000/api/meeting/{meeting_id}').json()

print(f"Title: {meeting['title']}")
print(f"Topics: {', '.join(meeting['topics'])}")
print(f"Priority: {meeting['priority']}")
```

## AI Analysis Details

### Content Processing Pipeline

1. **URL Fetching**: Retrieves webpage content with proper headers
2. **Content Extraction**: Removes navigation, ads, and extracts main content
3. **Text Processing**: Cleans and normalizes text for analysis
4. **Topic Detection**: Uses keyword matching and context analysis
5. **Priority Assessment**: Analyzes urgency indicators and impact
6. **Quote Extraction**: Identifies key statements and speakers
7. **Engagement Prediction**: Estimates public interest based on content
8. **Summary Generation**: Creates concise meeting overview

### Supported Content Types

- **City Council Meetings**: Full agenda and discussion analysis
- **Public Hearings**: Topic extraction and public comment analysis
- **Board Meetings**: Organizational and policy discussion analysis
- **Town Halls**: Community engagement and issue identification
- **Committee Meetings**: Specialized topic and recommendation analysis

## Team Collaboration

### Sharing the System

1. **Code Sharing**: Copy the entire `backend/` folder to share with your team
2. **Database Sharing**: The SQLite database file contains all meeting data
3. **Configuration**: Update settings in `config/settings.py` for your environment
4. **Deployment**: Use the provided Docker or Gunicorn instructions for production

### Development Workflow

1. **Local Development**: Each team member runs their own instance
2. **Shared Database**: Use PostgreSQL or MySQL for team collaboration
3. **API Integration**: Frontend developers can use the REST API
4. **Testing**: Comprehensive error handling and validation included

## Support and Customization

### Extending the AI Analysis

The AI analyzer in `utils/ai_analyzer.py` can be extended with:

- **Custom Topic Categories**: Add new topic detection rules
- **Advanced NLP**: Integrate with OpenAI GPT, Hugging Face, or other models
- **Language Support**: Add multi-language analysis capabilities
- **Custom Priority Rules**: Modify priority calculation logic

### Adding Features

The modular structure allows easy extension:

- **New API Endpoints**: Add routes in `app.py`
- **Database Models**: Extend models in `models/database.py`
- **UI Components**: Add templates in `templates/`
- **Background Tasks**: Add Celery or similar for async processing

## Security Considerations

- **Input Validation**: All URLs and inputs are validated
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **CORS Configuration**: Properly configured for frontend integration
- **Rate Limiting**: Consider adding rate limiting for production use
- **Authentication**: Basic user model included for future auth implementation

## Troubleshooting

### Common Issues

1. **Database Errors**: Ensure SQLite file permissions are correct
2. **URL Fetching Failures**: Check internet connectivity and URL accessibility
3. **Analysis Failures**: Some websites block automated access
4. **Port Conflicts**: Change port in `app.py` if 5000 is occupied

### Debug Mode

Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Optimization

- **Content Caching**: Cache analyzed content to avoid re-processing
- **Database Indexing**: Add indexes for frequently queried fields
- **Background Processing**: Move analysis to background tasks for large content
- **CDN Integration**: Use CDN for static assets in production

This backend system provides a complete foundation for your CivicScoop platform and can be easily shared with your team for collaborative development.