from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Meeting(db.Model):
    """Meeting model for storing council meeting data"""
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(500), nullable=False, unique=True)
    priority = db.Column(db.String(20), default='medium')
    priority_score = db.Column(db.String(10), default='50%')
    segments = db.Column(db.String(50), default='0:0 high segments')
    engagement = db.Column(db.String(50), default='0% high engagement')
    ai_accuracy = db.Column(db.Float, default=95.0)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # JSON fields for complex data
    topics = db.Column(db.Text, default='[]')
    quotes = db.Column(db.Text, default='[]')
    analysis = db.Column(db.Text, default='{}')
    metadata = db.Column(db.Text, default='{}')

    def get_topics(self):
        """Get topics as Python list"""
        try:
            return json.loads(self.topics) if self.topics else []
        except json.JSONDecodeError:
            return []

    def set_topics(self, topics_list):
        """Set topics from Python list"""
        self.topics = json.dumps(topics_list)

    def get_quotes(self):
        """Get quotes as Python list"""
        try:
            return json.loads(self.quotes) if self.quotes else []
        except json.JSONDecodeError:
            return []

    def set_quotes(self, quotes_list):
        """Set quotes from Python list"""
        self.quotes = json.dumps(quotes_list)

    def get_analysis(self):
        """Get analysis as Python dict"""
        try:
            return json.loads(self.analysis) if self.analysis else {}
        except json.JSONDecodeError:
            return {}

    def set_analysis(self, analysis_dict):
        """Set analysis from Python dict"""
        self.analysis = json.dumps(analysis_dict)

    def get_metadata(self):
        """Get metadata as Python dict"""
        try:
            return json.loads(self.metadata) if self.metadata else {}
        except json.JSONDecodeError:
            return {}

    def set_metadata(self, metadata_dict):
        """Set metadata from Python dict"""
        self.metadata = json.dumps(metadata_dict)

    def to_dict(self):
        """Convert meeting to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'date': self.date.isoformat() if self.date else None,
            'url': self.url,
            'priority': self.priority,
            'priority_score': self.priority_score,
            'segments': self.segments,
            'engagement': self.engagement,
            'ai_accuracy': self.ai_accuracy,
            'status': self.status,
            'topics': self.get_topics(),
            'quotes': self.get_quotes(),
            'analysis': self.get_analysis(),
            'metadata': self.get_metadata(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Meeting {self.title}>'

class User(db.Model):
    """User model for authentication"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User {self.username}>'

class Report(db.Model):
    """Report model for generated reports"""
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='pending')
    file_path = db.Column(db.String(500))
    file_size = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

    # JSON field for report configuration
    config = db.Column(db.Text, default='{}')

    def get_config(self):
        """Get config as Python dict"""
        try:
            return json.loads(self.config) if self.config else {}
        except json.JSONDecodeError:
            return {}

    def set_config(self, config_dict):
        """Set config from Python dict"""
        self.config = json.dumps(config_dict)

    def to_dict(self):
        """Convert report to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'status': self.status,
            'file_path': self.file_path,
            'file_size': self.file_size,
            'config': self.get_config(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

    def __repr__(self):
        return f'<Report {self.name}>'

class Analytics(db.Model):
    """Analytics model for tracking usage statistics"""
    __tablename__ = 'analytics'

    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    event_data = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), nullable=True)
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref=db.backref('analytics', lazy=True))
    meeting = db.relationship('Meeting', backref=db.backref('analytics', lazy=True))

    def get_event_data(self):
        """Get event data as Python dict"""
        try:
            return json.loads(self.event_data) if self.event_data else {}
        except json.JSONDecodeError:
            return {}

    def set_event_data(self, data_dict):
        """Set event data from Python dict"""
        self.event_data = json.dumps(data_dict)

    def __repr__(self):
        return f'<Analytics {self.event_type}>'