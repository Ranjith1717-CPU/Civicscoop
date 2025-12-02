# CivicScoop - AI-Powered Civic Intelligence Platform

🏛️ **Complete platform for analyzing city council meetings with advanced AI capabilities**

![CivicScoop Platform](https://img.shields.io/badge/Platform-CivicScoop-blue) ![AI Powered](https://img.shields.io/badge/AI-Powered-green) ![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## 🌟 Overview

CivicScoop is a comprehensive AI-powered civic intelligence platform that transforms how city council meetings are analyzed, understood, and shared with the public. The platform combines cutting-edge AI analysis with beautiful, professional interfaces to deliver real-time civic insights.

### ✨ Key Features

- **🤖 AI-Powered Analysis**: Automatic extraction of topics, quotes, priorities, and engagement metrics
- **🔗 URL Analysis**: Insert any meeting URL for instant AI analysis
- **📊 Real-time Dashboard**: Professional interface showing all analyzed meetings
- **📈 Analytics & Reports**: Comprehensive data visualization and report generation
- **🎯 Priority Assessment**: Automatic classification of meeting importance levels
- **💬 Quote Extraction**: AI-powered extraction of key statements and speakers
- **🏷️ Topic Detection**: Automatic identification of civic topics (Housing, Budget, Climate, etc.)
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## 🚀 Live Demo

**🌐 Website**: https://ranjith1717-cpu.github.io/Civicscoop/

### Access Points:
- **Dashboard**: https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Dashboard.html
- **Analytics**: https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Analytics.html
- **Reports**: https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Reports.html
- **Settings**: https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Settings.html

## 📁 Project Structure

```
CivicScoop/
├── 🌐 Frontend (GitHub Pages)
│   ├── index.html                          # Landing page
│   ├── CivicScoop_Dashboard.html            # Main dashboard with URL analysis
│   ├── CivicScoop_Analytics.html            # Analytics & data visualization
│   ├── CivicScoop_Reports.html              # Report generation & management
│   ├── CivicScoop_Settings.html             # Settings & configuration
│   └── CivicScoop_Interactive_Professional.html  # Meeting analysis interface
│
├── 🔧 Backend (Flask API)
│   ├── app.py                              # Main Flask application
│   ├── requirements.txt                    # Python dependencies
│   ├── run.bat / run.sh                    # Quick start scripts
│   ├── config/
│   │   └── settings.py                     # Configuration management
│   ├── models/
│   │   └── database.py                     # Database models & schemas
│   ├── utils/
│   │   └── ai_analyzer.py                  # AI analysis engine
│   └── templates/
│       ├── dashboard.html                  # Backend dashboard interface
│       └── add_meeting.html                # Meeting URL submission form
│
├── 📱 Streamlit App
│   ├── streamlit_app.py                    # Complete Streamlit version
│   └── requirements.txt                    # Streamlit dependencies
│
└── 📚 Documentation
    ├── README.md                           # This file
    └── backend/README.md                   # Backend-specific documentation
```

## 🎯 Features Overview

### 🏛️ **Dashboard (Main Interface)**
- **URL Analysis**: Enter any meeting URL for instant AI analysis
- **Meeting Grid**: Professional display of all analyzed meetings
- **Search & Filter**: Find meetings by topic, location, or priority
- **Real-time Stats**: Live metrics and engagement data
- **Add Meetings**: One-click addition of analyzed meetings to dashboard

### 🤖 **AI Analysis Engine**
- **Content Extraction**: Smart parsing of meeting content from any website
- **Topic Detection**: Automatic identification of civic topics
- **Priority Assessment**: Critical/High/Medium/Low classification
- **Quote Extraction**: Key statements with speaker identification
- **Engagement Prediction**: Estimate citizen interest and participation
- **Summary Generation**: AI-generated meeting summaries
- **Accuracy Scoring**: Confidence levels for all AI analysis

### 📊 **Analytics Dashboard**
- **Meeting Trends**: Visualize analysis volume over time
- **Topic Distribution**: See which civic topics are most discussed
- **Engagement Analysis**: Track citizen participation patterns
- **Performance Metrics**: Detailed statistics by location and topic
- **Interactive Charts**: Professional data visualization with Chart.js

### 📄 **Reports System**
- **Automated Reports**: Weekly, monthly, and quarterly civic intelligence briefs
- **Custom Reports**: Build reports with specific data sources and timeframes
- **Report Templates**: Pre-built templates for common civic analysis needs
- **Export Options**: PDF, Excel, PowerPoint, and web dashboard formats
- **Scheduling**: Automatic report generation and delivery

### ⚙️ **Settings & Configuration**
- **AI Configuration**: Adjust analysis accuracy, speed, and language settings
- **Notification Preferences**: Email, push, and Slack integration
- **Data Sources**: Connect to multiple city council websites and feeds
- **Account Management**: User profiles, subscription, and billing
- **Security Settings**: Two-factor authentication, API keys, and privacy controls

## 🛠️ Technology Stack

### Frontend
- **HTML5/CSS3**: Modern, responsive design with CSS Grid and Flexbox
- **JavaScript**: Vanilla JS for performance and compatibility
- **Font Awesome**: Professional iconography
- **Google Fonts**: Inter font family for modern typography
- **Chart.js**: Interactive data visualization
- **GitHub Pages**: Static site hosting and deployment

### Backend
- **Python 3.9+**: Core programming language
- **Flask**: Lightweight web framework for APIs
- **SQLAlchemy**: Database ORM and management
- **SQLite**: Default database (PostgreSQL/MySQL for production)
- **BeautifulSoup**: Web content parsing and extraction
- **Requests**: HTTP client for URL fetching
- **Flask-CORS**: Cross-origin resource sharing

### AI & Analysis
- **Natural Language Processing**: Topic extraction and classification
- **Content Analysis**: Priority assessment and engagement prediction
- **Quote Extraction**: Speaker identification and statement parsing
- **Sentiment Analysis**: Emotional tone and public sentiment detection
- **Summary Generation**: Automatic meeting overview creation

## 🚀 Quick Start

### 1. Frontend (GitHub Pages)
The frontend is already deployed and ready to use:

```bash
# Simply visit the live site
https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Dashboard.html
```

### 2. Backend (Local Development)

#### Windows
```bash
# Navigate to backend folder
cd backend

# Double-click to run
run.bat
```

#### Mac/Linux
```bash
# Navigate to backend folder
cd backend

# Make executable and run
chmod +x run.sh
./run.sh
```

#### Manual Setup
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run the application
python backend/app.py

# Access at http://localhost:5000
```

### 3. Streamlit Version
```bash
# Install streamlit dependencies
pip install -r requirements.txt

# Run the streamlit app
streamlit run streamlit_app.py

# Access at http://localhost:8501
```

## 📖 Usage Guide

### 🔗 **Analyzing Meeting URLs**

1. **Visit the Dashboard**: https://ranjith1717-cpu.github.io/Civicscoop/CivicScoop_Dashboard.html
2. **Enter Meeting URL**: Paste any city council meeting URL in the analysis section
3. **Click "Analyze with AI"**: Wait for AI processing (2-5 seconds)
4. **Review Results**: See extracted topics, priority, engagement, and quotes
5. **Add to Dashboard**: Click "Add to Dashboard" to save the analysis

### 📊 **Using the Analytics**

1. **View Meeting Trends**: See analysis volume over time
2. **Explore Topic Distribution**: Understand which civic topics are most discussed
3. **Analyze Engagement**: Track citizen participation and interest patterns
4. **Export Data**: Download charts and metrics for reports

### 📄 **Generating Reports**

1. **Choose Report Type**: Select from automated, custom, or template-based reports
2. **Configure Parameters**: Set date ranges, data sources, and output formats
3. **Schedule Reports**: Set up automatic generation and delivery
4. **Download Results**: Export as PDF, Excel, or PowerPoint

## 🔧 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### Analyze Meeting URL
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

## 🔐 Configuration

### Environment Variables
```bash
# Backend Configuration
DATABASE_URL=sqlite:///civicscoop.db
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# Optional AI Integration
OPENAI_API_KEY=your-openai-key
HUGGINGFACE_TOKEN=your-token

# Email Configuration (for notifications)
SMTP_SERVER=smtp.gmail.com
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

### Frontend Configuration
The frontend works entirely with static files and requires no configuration. All settings can be managed through the Settings page interface.

## 🚀 Deployment

### GitHub Pages (Frontend)
1. **Upload Files**: Copy all HTML files to your GitHub repository
2. **Enable Pages**: Go to repository Settings > Pages
3. **Configure Source**: Select "Deploy from a branch" and choose "main"
4. **Access Site**: Your platform will be live at `https://username.github.io/repository`

### Backend Deployment

#### Heroku
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy to Heroku
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

#### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

#### VPS/Cloud Server
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip nginx

# Clone repository
git clone https://github.com/yourusername/civicscoop.git
cd civicscoop/backend

# Install requirements
pip3 install -r requirements.txt

# Configure Nginx (reverse proxy to Flask)
# Set up systemd service for auto-restart
```

### Streamlit Cloud
1. **Connect Repository**: Link your GitHub repository to Streamlit Cloud
2. **Set Main File**: Point to `streamlit_app.py`
3. **Deploy**: Your app will be live at `https://appname.streamlit.app`

## 👥 Team Collaboration

### For Development Teams
1. **Clone Repository**: `git clone https://github.com/Ranjith1717-CPU/CivicScoop.git`
2. **Frontend Development**: Work with HTML/CSS/JS files directly
3. **Backend Development**: Use the Flask API in the `backend/` folder
4. **Database Sharing**: Use PostgreSQL or MySQL for team collaboration
5. **API Integration**: Connect frontend to backend for live data

### Sharing the Project
- **Complete Package**: Share the entire repository folder
- **Frontend Only**: Share just the HTML files for static deployment
- **Backend Only**: Share the `backend/` folder for API development
- **Documentation**: Full README and API documentation included

## 🔍 Troubleshooting

### Common Issues

#### Frontend Issues
- **Navigation Errors**: Ensure all HTML files are in the same directory
- **GitHub Pages 404**: Check that files are uploaded and Pages is enabled
- **Styling Issues**: Verify Font Awesome and Google Fonts are loading

#### Backend Issues
- **Port Conflicts**: Change port in `app.py` if 5000 is occupied
- **Database Errors**: Ensure SQLite file permissions are correct
- **Module Import Errors**: Verify all dependencies are installed

#### Analysis Issues
- **URL Fetching Failures**: Some websites block automated access
- **Slow Analysis**: Content parsing can take time for large pages
- **Accuracy Concerns**: AI analysis is simulated for demonstration

### Debug Mode
```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Run Flask in debug mode
app.run(debug=True)
```

## 📈 Performance & Scale

### Frontend Performance
- **Static Files**: Lightning-fast loading with GitHub Pages CDN
- **Optimized CSS**: Efficient styling with minimal external dependencies
- **Lazy Loading**: Meeting cards load progressively for better performance
- **Mobile Optimized**: Responsive design works on all devices

### Backend Performance
- **SQLite Database**: Perfect for development and moderate traffic
- **PostgreSQL/MySQL**: Recommended for production and high traffic
- **Caching**: Implement Redis for API response caching
- **Background Tasks**: Use Celery for heavy AI processing

### Scaling Recommendations
- **Frontend**: Use CDN for global distribution
- **Backend**: Deploy with load balancers and multiple instances
- **Database**: Implement read replicas for high query volumes
- **AI Processing**: Offload to dedicated AI services or GPUs

## 🤝 Contributing

### Development Setup
1. **Fork the Repository**: Create your own copy on GitHub
2. **Create Branch**: `git checkout -b feature/your-feature-name`
3. **Make Changes**: Implement your improvements
4. **Test Thoroughly**: Ensure all functionality works
5. **Submit PR**: Create a pull request with detailed description

### Code Standards
- **Frontend**: Use consistent indentation and comments
- **Backend**: Follow PEP 8 Python style guidelines
- **Documentation**: Update README for any new features
- **Testing**: Add tests for new functionality

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- **AI Analysis**: Powered by advanced natural language processing
- **Design Inspiration**: Modern civic technology platforms
- **Icons**: Font Awesome icon library
- **Typography**: Google Fonts (Inter font family)
- **Charts**: Chart.js for data visualization

## 📞 Support

### Getting Help
- **Documentation**: Check this README and backend documentation
- **Issues**: Create GitHub issues for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the development team for urgent issues

### Feature Requests
We welcome suggestions for new features! Please create a GitHub issue with:
- **Description**: What feature you'd like to see
- **Use Case**: How it would benefit users
- **Examples**: Any examples from other platforms
- **Priority**: How important this is to your workflow

---

**Built with ❤️ for civic transparency and community engagement**

🏛️ **CivicScoop** - Empowering democracy through AI-powered civic intelligence