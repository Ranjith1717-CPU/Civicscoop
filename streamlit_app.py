import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Set page config
st.set_page_config(
    page_title="CivicScoop - AI-Powered Civic Intelligence",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Exact CSS styling from HTML version
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

    .main > div {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    .stApp {
        background: #0a0f1c;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Header styling */
    .main-header {
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px 30px;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0;
    }

    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }

    .main-title {
        color: #60a5fa;
        font-size: 28px;
        font-weight: 700;
        margin: 0;
    }

    .pro-badge {
        background: linear-gradient(135deg, #dc2626, #ea580c);
        color: white;
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Hero section styling */
    .hero-section {
        background: linear-gradient(135deg, #0a0f1c 0%, #1e293b 50%, #0a0f1c 100%);
        padding: 80px 30px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin: -2rem -1rem 2rem -1rem;
        border-radius: 0;
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(168, 85, 247, 0.1) 0%, transparent 50%);
        pointer-events: none;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 20px;
        background: linear-gradient(135deg, #60a5fa, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
        z-index: 1;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #94a3b8;
        margin-bottom: 40px;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }

    /* Meeting cards */
    .meeting-card {
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin: 20px 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .meeting-card:hover {
        background: rgba(30, 41, 59, 0.8);
        border-color: rgba(96, 165, 250, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    }

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }

    .priority-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
    }

    .priority-critical {
        background: rgba(239, 68, 68, 0.2);
        color: #ef4444;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    .priority-high {
        background: rgba(245, 158, 11, 0.2);
        color: #f59e0b;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .priority-medium {
        background: rgba(59, 130, 246, 0.2);
        color: #3b82f6;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }

    .segments-count {
        color: #94a3b8;
        font-size: 12px;
    }

    .meeting-title {
        color: #e2e8f0;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 12px;
        line-height: 1.3;
    }

    .meeting-meta {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
        color: #94a3b8;
        font-size: 14px;
    }

    .meta-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .engagement-score {
        color: #22c55e;
        font-weight: 600;
    }

    .topic-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 20px;
    }

    .topic-tag {
        background: rgba(96, 165, 250, 0.1);
        color: #60a5fa;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
    }

    /* Stats banner */
    .stats-banner {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 30px;
        margin: 40px 0;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 30px;
    }

    .stat-item {
        text-align: center;
    }

    .stat-value {
        color: #60a5fa;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .stat-label {
        color: #94a3b8;
        font-size: 14px;
        font-weight: 500;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1e293b;
    }

    .css-1544g2n {
        color: #e2e8f0;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af);
        transform: translateY(-1px);
    }

    /* Text input styling */
    .stTextInput > div > div > input {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #e2e8f0;
        border-radius: 12px;
    }

    .stTextInput > div > div > input:focus {
        border-color: #60a5fa;
        box-shadow: 0 0 0 4px rgba(96, 165, 250, 0.1);
    }

    /* Selectbox styling */
    .stSelectbox > div > div > div {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #e2e8f0;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #1e293b;
    }

    ::-webkit-scrollbar-thumb {
        background: #60a5fa;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

# Exact meeting data from HTML version
@st.cache_data
def load_meeting_data():
    meetings = [
        {
            "id": "austin-housing",
            "title": "Austin City Council Meeting: Housing Crisis Response",
            "date": "August 15, 2025",
            "location": "Austin",
            "priority": "critical",
            "priorityScore": "95%",
            "segments": "14:7 high segments",
            "engagement": "85.3% high engagement",
            "topics": ["Housing", "Crisis Response", "Public Policy"],
            "filename": "austin-housing-crisis.html"
        },
        {
            "id": "seattle-budget",
            "title": "Seattle City Council Session: 2025 Budget Allocation",
            "date": "July 22, 2025",
            "location": "Seattle",
            "priority": "high",
            "priorityScore": "73%",
            "segments": "22:15 high segments",
            "engagement": "73.2% high engagement",
            "topics": ["Budget", "Finance", "Public Services"],
            "filename": "seattle-budget-2025.html"
        },
        {
            "id": "miami-climate",
            "title": "Miami-Dade Commission: Climate Action Implementation",
            "date": "June 18, 2025",
            "location": "Miami-Dade",
            "priority": "high",
            "priorityScore": "68%",
            "segments": "18:12 high segments",
            "engagement": "68.4% high engagement",
            "topics": ["Climate", "Environment", "Sustainability"],
            "filename": "miami-climate-action.html"
        },
        {
            "id": "denver-transit",
            "title": "Denver City Council: Public Transit Expansion",
            "date": "September 3, 2025",
            "location": "Denver",
            "priority": "medium",
            "priorityScore": "45%",
            "segments": "11:23 high segments",
            "engagement": "45.1% high engagement",
            "topics": ["Transit", "Infrastructure", "Urban Planning"],
            "filename": "denver-transit.html"
        },
        {
            "id": "waste-management",
            "title": "City Council Meeting: Waste Management Solutions",
            "date": "July 15, 2025",
            "location": "Regional",
            "priority": "medium",
            "priorityScore": "65%",
            "segments": "9:14 high segments",
            "engagement": "65.1% high engagement",
            "topics": ["Landfill", "Transportation", "Dumping"]
        },
        {
            "id": "hickory",
            "title": "Hickory City Council Meeting: Economic Development",
            "date": "August 5, 2025",
            "location": "Hickory",
            "priority": "critical",
            "priorityScore": "86%",
            "segments": "6:7 high segments",
            "engagement": "85.7% high engagement",
            "topics": ["Economic Development", "Tourism", "Infrastructure"]
        },
        {
            "id": "fort-worth",
            "title": "Fort Worth City Council Discussion: Road Infrastructure",
            "date": "August 5, 2025",
            "location": "Fort Worth",
            "priority": "medium",
            "priorityScore": "30%",
            "segments": "15:50 high segments",
            "engagement": "30.0% high engagement",
            "topics": ["Roads", "Infrastructure", "Budget"]
        },
        {
            "id": "palmetto-bay",
            "title": "Palmetto Bay Council Meeting: Environmental Protection",
            "date": "September 15, 2025",
            "location": "Palmetto Bay",
            "priority": "medium",
            "priorityScore": "22%",
            "segments": "8:28 high segments",
            "engagement": "22.2% high engagement",
            "topics": ["Environment", "Protection", "Sustainability"]
        },
        {
            "id": "south-san-francisco",
            "title": "City of South San Francisco Council: Development Review",
            "date": "May 28, 2025",
            "location": "South San Francisco",
            "priority": "high",
            "priorityScore": "7%",
            "segments": "2:31 high segments",
            "engagement": "6.5% high engagement",
            "topics": ["Development", "Planning", "Zoning"]
        },
        {
            "id": "richmond",
            "title": "Richmond City Council: Community Safety Initiative",
            "date": "October 10, 2025",
            "location": "Richmond",
            "priority": "critical",
            "priorityScore": "78%",
            "segments": "22:15 high segments",
            "engagement": "68.3% high engagement",
            "topics": ["Public Safety", "Community", "Crime Prevention"]
        }
    ]
    return meetings

# Sidebar navigation with exact styling
def create_sidebar():
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem; background: rgba(30, 41, 59, 0.8); border-radius: 12px; margin-bottom: 1rem;'>
        <h2 style='color: #60a5fa; margin: 0; font-size: 24px; font-weight: 700;'>🏛️ CivicScoop</h2>
        <div style='background: linear-gradient(135deg, #dc2626, #ea580c); color: white; padding: 4px 10px; border-radius: 8px; font-size: 10px; font-weight: 600; text-transform: uppercase; margin-top: 8px; display: inline-block;'>Pro Platform</div>
        <p style='color: #94a3b8; margin-top: 10px; font-size: 14px;'>AI-Powered Civic Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.sidebar.selectbox(
        "📊 Navigate to:",
        ["🏛️ Dashboard", "📊 Meeting Analysis", "📈 Analytics", "📄 Reports", "⚙️ Settings"],
        index=0
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("### 🚀 Quick Actions")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.sidebar.button("🔍 Search", use_container_width=True):
            st.sidebar.info("🔍 Search activated!")

    with col2:
        if st.sidebar.button("📊 Report", use_container_width=True):
            st.sidebar.success("📊 Generating report...")

    if st.sidebar.button("⚙️ AI Config", use_container_width=True):
        st.sidebar.info("⚙️ Opening AI settings...")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Live Stats")
    st.sidebar.metric("Active Meetings", "247", "+12")
    st.sidebar.metric("AI Accuracy", "98.7%", "+0.3%")
    st.sidebar.metric("Engagement", "89.2K", "+15.7K")

    return page

# Dashboard page with exact HTML layout
def dashboard_page():
    # Header section
    st.markdown("""
    <div class="main-header">
        <div class="logo-container">
            <h1 class="main-title">🏛️ CivicScoop</h1>
            <span class="pro-badge">Pro Platform</span>
        </div>
        <div style="display: flex; gap: 20px; align-items: center;">
            <a href="#" style="color: #60a5fa; text-decoration: none; font-weight: 500;">Dashboard</a>
            <a href="#" style="color: #94a3b8; text-decoration: none; font-weight: 500;">Analytics</a>
            <a href="#" style="color: #94a3b8; text-decoration: none; font-weight: 500;">Reports</a>
            <a href="#" style="color: #94a3b8; text-decoration: none; font-weight: 500;">Settings</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero section
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">AI-Powered Civic Intelligence</h1>
        <p class="hero-subtitle">Real-time analysis of city council meetings with advanced AI insights</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats banner
    st.markdown("""
    <div class="stats-banner">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-value">247</div>
                <div class="stat-label">Total Meetings Analyzed</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">98.7%</div>
                <div class="stat-label">AI Accuracy Score</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">156</div>
                <div class="stat-label">Active Stories</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">89.2K</div>
                <div class="stat-label">Citizen Engagement</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Search and filter section
    col1, col2, col3 = st.columns([6, 2, 2])

    with col1:
        search_term = st.text_input(
            "🔍 Search meetings, topics, or locations",
            placeholder="e.g., housing, budget, climate...",
            label_visibility="collapsed"
        )

    with col2:
        priority_filter = st.selectbox(
            "Priority Filter",
            ["All Priorities", "Critical", "High", "Medium"],
            label_visibility="collapsed"
        )

    with col3:
        location_filter = st.selectbox(
            "Location Filter",
            ["All Locations", "Austin", "Seattle", "Miami-Dade", "Denver", "Other"],
            label_visibility="collapsed"
        )

    # Load and filter meetings
    meetings = load_meeting_data()

    # Apply filters
    if priority_filter != "All Priorities":
        meetings = [m for m in meetings if m["priority"].title() == priority_filter]

    if location_filter != "All Locations":
        meetings = [m for m in meetings if location_filter.lower() in m["location"].lower()]

    if search_term:
        meetings = [
            m for m in meetings
            if search_term.lower() in m["title"].lower()
            or search_term.lower() in m["location"].lower()
            or any(search_term.lower() in topic.lower() for topic in m["topics"])
        ]

    st.markdown(f"### 🏛️ Recent Meetings ({len(meetings)} found)")

    # Display meetings in exact format
    for meeting in meetings:
        priority_class = f"priority-{meeting['priority']}"
        priority_text = (
            "Critical Priority" if meeting['priority'] == 'critical'
            else "High Priority" if meeting['priority'] == 'high'
            else "Medium Priority"
        )

        # Create meeting card with exact styling
        st.markdown(f"""
        <div class="meeting-card" onclick="document.querySelector('[data-testid=\\"meeting-{meeting['id']}\\"]').click()">
            <div class="card-header">
                <div class="priority-badge {priority_class}">
                    <i class="fas fa-exclamation-triangle"></i>
                    {priority_text} {meeting['priorityScore']}
                </div>
                <div class="segments-count">{meeting['segments']}</div>
            </div>
            <h3 class="meeting-title">{meeting['title']}</h3>
            <div class="meeting-meta">
                <div class="meta-item">
                    <i class="fas fa-calendar"></i>
                    {meeting['date']}
                </div>
                <div class="meta-item">
                    <i class="fas fa-map-marker-alt"></i>
                    {meeting['location']}
                </div>
                <div class="meta-item">
                    <i class="fas fa-users"></i>
                    <span class="engagement-score">{meeting['engagement']}</span>
                </div>
            </div>
            <div class="topic-tags">
                {' '.join([f'<span class="topic-tag">{topic}</span>' for topic in meeting['topics'][:3]])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Hidden button for navigation
        col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
        with col2:
            if st.button("📊 Analyze", key=f"analyze_{meeting['id']}", help="Analyze this meeting"):
                st.session_state['selected_meeting'] = meeting
                st.session_state['page'] = '📊 Meeting Analysis'
                st.experimental_rerun()

        with col3:
            if st.button("📤 Share", key=f"share_{meeting['id']}", help="Share this meeting"):
                st.success("📤 Share link copied!")

        with col4:
            if st.button("💾 Save", key=f"save_{meeting['id']}", help="Save to bookmarks"):
                st.success("💾 Meeting bookmarked!")

# Meeting Analysis page
def meeting_analysis_page():
    if 'selected_meeting' not in st.session_state:
        st.warning("⚠️ No meeting selected. Please go back to Dashboard and select a meeting to analyze.")
        if st.button("← Back to Dashboard"):
            st.session_state['page'] = '🏛️ Dashboard'
            st.experimental_rerun()
        return

    meeting = st.session_state['selected_meeting']

    # Header
    st.markdown(f"""
    <div class="main-header">
        <div class="logo-container">
            <h1 class="main-title">📊 Meeting Analysis</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Meeting title and details
    st.markdown(f"""
    <div class="meeting-card" style="margin-bottom: 30px;">
        <h2 class="meeting-title">{meeting['title']}</h2>
        <div class="meeting-meta">
            <div class="meta-item">
                <i class="fas fa-calendar"></i> {meeting['date']}
            </div>
            <div class="meta-item">
                <i class="fas fa-map-marker-alt"></i> {meeting['location']}
            </div>
            <div class="meta-item">
                <i class="fas fa-users"></i> <span class="engagement-score">{meeting['engagement']}</span>
            </div>
        </div>
        <div class="topic-tags">
            {' '.join([f'<span class="topic-tag">{topic}</span>' for topic in meeting['topics']])}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs for analysis
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎥 Video Analysis",
        "💬 AI Quotes",
        "📝 Story Builder",
        "👥 Citizen Engagement",
        "🔍 Deep Insights"
    ])

    with tab1:
        st.markdown("### 🎥 Video Analysis")

        # Video placeholder
        st.video("https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📍 Key Moments")
            moments = [
                "00:05:30 - Housing crisis discussion begins",
                "00:12:45 - Budget allocation debate",
                "00:18:20 - Public comment period",
                "00:25:15 - Council deliberation",
                "00:32:40 - Final voting session"
            ]
            for moment in moments:
                st.markdown(f"• {moment}")

        with col2:
            st.markdown("#### 🤖 AI Insights")
            st.metric("Accuracy Score", meeting['priorityScore'])
            st.metric("Engagement Level", meeting['engagement'])
            st.metric("Sentiment Score", "68% Positive")
            st.metric("Key Topics", f"{len(meeting['topics'])} identified")

    with tab2:
        st.markdown("### 💬 AI-Generated Quotes")

        quotes = [
            {
                "speaker": "Council Member Johnson",
                "quote": "We need immediate action on the housing affordability crisis affecting our most vulnerable residents.",
                "timestamp": "00:07:45",
                "confidence": 98.7
            },
            {
                "speaker": "Mayor Williams",
                "quote": "This budget allocation represents our commitment to data-driven solutions for community challenges.",
                "timestamp": "00:14:22",
                "confidence": 97.3
            },
            {
                "speaker": "Citizen Speaker #3",
                "quote": "The public deserves transparency in how these decisions affect our daily lives and neighborhoods.",
                "timestamp": "00:19:56",
                "confidence": 95.8
            }
        ]

        for i, quote in enumerate(quotes):
            with st.container():
                st.markdown(f"""
                <div class="meeting-card">
                    <h4>{quote['speaker']} <span style="color: #94a3b8;">({quote['timestamp']})</span></h4>
                    <p style="font-style: italic; font-size: 16px; margin: 10px 0;">"{quote['quote']}"</p>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #22c55e; font-size: 14px;">Confidence: {quote['confidence']}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns([4, 1, 1])
                with col2:
                    if st.button("📋 Use Quote", key=f"quote_{i}"):
                        st.success("📋 Quote added to story!")
                with col3:
                    if st.button("🔗 Get Link", key=f"link_{i}"):
                        st.info(f"🔗 Link: meeting.ai/{meeting['id']}#{quote['timestamp']}")

    with tab3:
        st.markdown("### 📝 Story Builder")

        col1, col2 = st.columns([1, 1])

        with col1:
            story_template = st.selectbox(
                "📄 Choose Story Template:",
                ["Breaking News Alert", "Policy Analysis Report", "Community Impact Story", "Budget Analysis", "Action Item Summary"]
            )

        with col2:
            story_tone = st.selectbox(
                "✍️ Writing Tone:",
                ["Professional", "Conversational", "Urgent", "Analytical", "Community-Focused"]
            )

        # Generated story
        story_content = f"""**{meeting['location']} City Council Addresses {meeting['topics'][0]} in Comprehensive Session**

In a {meeting['priority']} priority session on {meeting['date']}, {meeting['location']} city officials convened to address critical {meeting['topics'][0].lower()} challenges facing the community.

The meeting, which generated {meeting['engagement']} from citizens, focused on implementing practical solutions to ongoing municipal concerns. Council members engaged in detailed discussions about budget allocations, policy frameworks, and community impact assessments.

**Key Highlights:**
• Comprehensive review of {meeting['topics'][0].lower()} policies
• Public engagement with {meeting['engagement']} citizen participation
• {meeting['segments']} of high-priority discussion segments
• AI-verified accuracy score of {meeting['priorityScore']}

**Next Steps:**
The council will reconvene next week to finalize implementation details and establish timelines for the proposed initiatives. Community feedback continues to be welcomed through the city's official channels.

*This story was generated using AI analysis with {meeting['priorityScore']} accuracy verification.*"""

        st.text_area(
            "📰 Generated Story:",
            value=story_content,
            height=300,
            help="Edit the generated story as needed before publishing"
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🔄 Regenerate Story", use_container_width=True):
                st.success("🔄 Story regenerated with new insights!")

        with col2:
            if st.button("👀 Preview", use_container_width=True):
                st.info("👀 Opening story preview...")

        with col3:
            if st.button("📤 Publish", use_container_width=True):
                st.success("📤 Story published to newsroom!")

    with tab4:
        st.markdown("### 👥 Citizen Engagement Analysis")

        # Engagement metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("👀 Total Views", "2,847", "+312 today")
        with col2:
            st.metric("💬 Comments", "127", "+18 new")
        with col3:
            st.metric("📤 Shares", "89", "+23 today")
        with col4:
            st.metric("⭐ Average Rating", "4.3/5", "+0.2")

        # Engagement over time chart
        st.markdown("#### 📈 Engagement Timeline")
        dates = pd.date_range(start='2024-12-01', end='2024-12-02', freq='H')
        engagement_data = [45 + i*2 + (i%6)*10 for i in range(len(dates))]

        fig = px.line(
            x=dates,
            y=engagement_data,
            title="Hourly Engagement Activity",
            labels={'x': 'Time', 'y': 'Engagement Count'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#e2e8f0'
        )
        st.plotly_chart(fig, use_container_width=True)

        # Recent comments
        st.markdown("#### 💬 Recent Citizen Comments")

        comments = [
            {
                "user": "CityResident2024",
                "comment": "Finally seeing real action on housing policy! This gives me hope.",
                "time": "2 hours ago",
                "likes": 23
            },
            {
                "user": "ConcernedParent",
                "comment": "More transparency needed in the budget allocation process.",
                "time": "3 hours ago",
                "likes": 15
            },
            {
                "user": "LocalBusiness",
                "comment": "These infrastructure improvements will benefit everyone.",
                "time": "4 hours ago",
                "likes": 31
            },
            {
                "user": "YoungVoter",
                "comment": "Glad to see climate issues being prioritized finally.",
                "time": "5 hours ago",
                "likes": 18
            }
        ]

        for comment in comments:
            st.markdown(f"""
            <div class="meeting-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <strong>{comment['user']}</strong>
                    <span style="color: #94a3b8; font-size: 12px;">{comment['time']}</span>
                </div>
                <p style="margin-bottom: 10px;">{comment['comment']}</p>
                <div style="color: #22c55e; font-size: 14px;">
                    <i class="fas fa-thumbs-up"></i> {comment['likes']} likes
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        st.markdown("### 🔍 Deep AI Insights")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🎯 Key Topics Analysis")

            # Topic sentiment analysis
            topic_data = {
                'Topic': meeting['topics'] + ['Budget Impact', 'Community Response'],
                'Sentiment': [85, 72, 68, 45, 79],
                'Mentions': [23, 18, 15, 12, 9]
            }

            fig = px.scatter(
                x=topic_data['Mentions'],
                y=topic_data['Sentiment'],
                size=[x*2 for x in topic_data['Mentions']],
                hover_name=topic_data['Topic'],
                title="Topic Sentiment vs Frequency",
                labels={'x': 'Mentions', 'y': 'Sentiment Score'}
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#e2e8f0'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("#### 🗣️ Speaker Analysis")

            speakers = ['Council Members', 'Mayor', 'Citizens', 'Staff']
            speaking_time = [35, 25, 30, 10]

            fig = px.pie(
                values=speaking_time,
                names=speakers,
                title="Speaking Time Distribution"
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='#e2e8f0'
            )
            st.plotly_chart(fig, use_container_width=True)

        # Action items and recommendations
        st.markdown("#### 📋 AI-Identified Action Items")

        action_items = [
            {
                "item": "Follow-up budget review scheduled within 2 weeks",
                "priority": "High",
                "deadline": "December 16, 2024"
            },
            {
                "item": "Community stakeholder meeting organization",
                "priority": "Medium",
                "deadline": "December 20, 2024"
            },
            {
                "item": "Policy draft review and public comment period",
                "priority": "High",
                "deadline": "January 5, 2025"
            }
        ]

        for item in action_items:
            priority_color = "#ef4444" if item['priority'] == "High" else "#f59e0b"
            st.markdown(f"""
            <div class="meeting-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>{item['item']}</span>
                    <div>
                        <span style="background: {priority_color}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px; margin-right: 10px;">{item['priority']}</span>
                        <span style="color: #94a3b8; font-size: 14px;">Due: {item['deadline']}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Navigation buttons at bottom
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("← Back to Dashboard", use_container_width=True):
            st.session_state['page'] = '🏛️ Dashboard'
            del st.session_state['selected_meeting']
            st.experimental_rerun()

    with col2:
        if st.button("📊 View Analytics", use_container_width=True):
            st.session_state['page'] = '📈 Analytics'
            st.experimental_rerun()

    with col3:
        if st.button("📄 Generate Report", use_container_width=True):
            st.session_state['page'] = '📄 Reports'
            st.experimental_rerun()

# Analytics page
def analytics_page():
    st.markdown("""
    <div class="main-header">
        <div class="logo-container">
            <h1 class="main-title">📈 Analytics Dashboard</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📊 Total Meetings", "247", "↑ 12%")
    with col2:
        st.metric("🤖 AI Accuracy", "98.7%", "↑ 0.3%")
    with col3:
        st.metric("📰 Stories Generated", "1,247", "↑ 23%")
    with col4:
        st.metric("👥 Citizen Engagement", "89.2K", "↑ 18%")

    st.markdown("---")

    # Charts section
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📈 Meeting Analysis Trends (Last 30 Days)")
        dates = pd.date_range(start='2024-11-02', end='2024-12-02', freq='D')
        meeting_counts = [5 + (i % 8) + (i // 7) for i in range(len(dates))]

        fig = px.line(
            x=dates,
            y=meeting_counts,
            title="Daily Meeting Analysis Volume",
            labels={'x': 'Date', 'y': 'Meetings Analyzed'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#e2e8f0'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 🏷️ Topic Distribution")
        topics = ["Housing", "Budget", "Climate", "Transit", "Education", "Public Safety", "Development"]
        counts = [45, 38, 32, 28, 24, 18, 15]

        fig = px.pie(
            values=counts,
            names=topics,
            title="Meeting Topics Analysis"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#e2e8f0'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Engagement analysis
    st.markdown("### 👥 Detailed Engagement Analysis")

    col1, col2 = st.columns(2)

    with col1:
        # AI Accuracy vs Engagement scatter
        meetings_df = pd.DataFrame(load_meeting_data())

        # Extract numeric values from engagement strings
        meetings_df['engagement_numeric'] = meetings_df['engagement'].str.extract(r'(\d+\.?\d*)').astype(float)
        meetings_df['priority_numeric'] = meetings_df['priorityScore'].str.extract(r'(\d+)').astype(int)

        fig = px.scatter(
            meetings_df,
            x='priority_numeric',
            y='engagement_numeric',
            size='engagement_numeric',
            color='priority',
            title="Priority Score vs Citizen Engagement",
            hover_data=['title', 'location'],
            labels={'priority_numeric': 'Priority Score (%)', 'engagement_numeric': 'Engagement (%)'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#e2e8f0'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Activity heatmap
        st.markdown("#### 🕐 Meeting Activity Heatmap")

        hours = list(range(24))
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        # Generate sample activity data
        activity_data = []
        for day in range(7):
            day_data = []
            for hour in range(24):
                # Simulate meeting activity (higher during business hours)
                if 9 <= hour <= 17:
                    activity = 15 + (hour % 3) * 5 + day * 2
                else:
                    activity = 2 + (hour % 2) + day
                day_data.append(activity)
            activity_data.append(day_data)

        fig = go.Figure(data=go.Heatmap(
            z=activity_data,
            x=hours,
            y=days,
            colorscale='Blues',
            hoverongaps=False
        ))

        fig.update_layout(
            title="Weekly Meeting Activity Pattern",
            xaxis_title="Hour of Day",
            yaxis_title="Day of Week",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#e2e8f0'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Performance metrics table
    st.markdown("### 📊 Detailed Performance Metrics")

    performance_data = {
        'Location': ['Austin', 'Seattle', 'Miami-Dade', 'Denver', 'Richmond'],
        'Meetings': [15, 12, 8, 6, 4],
        'Avg Engagement': ['85.3%', '73.2%', '68.4%', '45.1%', '68.3%'],
        'AI Accuracy': ['98.7%', '97.2%', '96.8%', '95.3%', '97.9%'],
        'Stories Generated': [45, 38, 25, 18, 15],
        'Citizen Comments': [456, 387, 234, 189, 167]
    }

    performance_df = pd.DataFrame(performance_data)
    st.dataframe(performance_df, use_container_width=True)

# Reports page
def reports_page():
    st.markdown("""
    <div class="main-header">
        <div class="logo-container">
            <h1 class="main-title">📄 Reports Dashboard</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📋 Available Reports")

        reports = [
            {
                "name": "Weekly Civic Intelligence Brief",
                "type": "Automated",
                "last_run": "Today, 9:00 AM",
                "status": "Ready",
                "size": "2.3 MB"
            },
            {
                "name": "Monthly Council Engagement Report",
                "type": "Scheduled",
                "last_run": "Dec 1, 2024",
                "status": "Processing",
                "size": "1.8 MB"
            },
            {
                "name": "Housing Crisis Deep Dive Analysis",
                "type": "Custom",
                "last_run": "Nov 28, 2024",
                "status": "Ready",
                "size": "4.2 MB"
            },
            {
                "name": "Budget Analysis Q4 2024",
                "type": "Quarterly",
                "last_run": "Nov 25, 2024",
                "status": "Ready",
                "size": "3.1 MB"
            },
            {
                "name": "Climate Action Policy Summary",
                "type": "Custom",
                "last_run": "Nov 20, 2024",
                "status": "Ready",
                "size": "2.7 MB"
            },
            {
                "name": "Citizen Engagement Trends",
                "type": "Automated",
                "last_run": "Nov 18, 2024",
                "status": "Archived",
                "size": "1.9 MB"
            }
        ]

        for report in reports:
            status_color = {
                "Ready": "#22c55e",
                "Processing": "#f59e0b",
                "Archived": "#94a3b8"
            }.get(report['status'], "#94a3b8")

            st.markdown(f"""
            <div class="meeting-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <div>
                        <h4 style="margin: 0;">{report['name']}</h4>
                        <p style="color: #94a3b8; margin: 5px 0 0 0;">Type: {report['type']} • Size: {report['size']}</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="background: {status_color}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px; margin-bottom: 5px;">{report['status']}</div>
                        <p style="color: #94a3b8; font-size: 12px; margin: 0;">Last: {report['last_run']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b, col_c, col_d = st.columns([6, 1, 1, 1])
            with col_b:
                if st.button("👀 View", key=f"view_{report['name']}", help=f"View {report['name']}"):
                    st.info(f"📄 Opening {report['name']}...")

            with col_c:
                if st.button("⬇️ Download", key=f"download_{report['name']}", help=f"Download {report['name']}"):
                    st.success(f"⬇️ Downloading {report['name']}...")

            with col_d:
                if st.button("📤 Share", key=f"share_{report['name']}", help=f"Share {report['name']}"):
                    st.info(f"📤 Share link for {report['name']} generated!")

    with col2:
        st.markdown("### ➕ Create New Report")

        with st.form("new_report_form"):
            report_name = st.text_input("📝 Report Name", placeholder="e.g., Transit Analysis Q4")

            report_type = st.selectbox(
                "📊 Report Type",
                ["Custom Analysis", "Automated Weekly", "Monthly Summary", "Quarterly Review", "Ad-hoc Investigation"]
            )

            date_range = st.date_input(
                "📅 Date Range",
                value=[datetime.now().date() - timedelta(days=30), datetime.now().date()],
                help="Select the time period for analysis"
            )

            data_sources = st.multiselect(
                "📚 Data Sources",
                [
                    "Meeting Transcripts",
                    "Citizen Comments",
                    "Social Media Mentions",
                    "News Articles",
                    "Government Data",
                    "Budget Documents",
                    "Policy Papers"
                ],
                default=["Meeting Transcripts", "Citizen Comments"]
            )

            locations = st.multiselect(
                "📍 Locations",
                ["Austin", "Seattle", "Miami-Dade", "Denver", "Richmond", "All Locations"],
                default=["All Locations"]
            )

            priority_filter = st.multiselect(
                "⚡ Priority Levels",
                ["Critical", "High", "Medium", "Low"],
                default=["Critical", "High", "Medium"]
            )

            output_format = st.selectbox(
                "📄 Output Format",
                ["PDF Report", "Excel Workbook", "PowerPoint Presentation", "Web Dashboard", "All Formats"]
            )

            schedule_report = st.checkbox("🔄 Schedule recurring generation")

            if schedule_report:
                frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly", "Quarterly"])

            submitted = st.form_submit_button("🚀 Generate Report", use_container_width=True)

            if submitted:
                if report_name and data_sources:
                    st.success(f"🚀 Report '{report_name}' generation started!")
                    st.info(f"📊 Analyzing {len(data_sources)} data source(s) from {date_range[0]} to {date_range[1]}")
                    st.info(f"📄 Report will be delivered as: {output_format}")

                    if schedule_report:
                        st.info(f"🔄 Scheduled for {frequency.lower()} generation")
                else:
                    st.error("⚠️ Please provide a report name and select at least one data source.")

        # Quick report templates
        st.markdown("### ⚡ Quick Templates")

        templates = [
            {"name": "🏠 Housing Analysis", "desc": "Housing policy and crisis response"},
            {"name": "💰 Budget Review", "desc": "Financial allocation analysis"},
            {"name": "🌍 Climate Report", "desc": "Environmental policy tracking"},
            {"name": "🚌 Transit Study", "desc": "Transportation and mobility"},
            {"name": "👥 Engagement Summary", "desc": "Citizen participation metrics"}
        ]

        for template in templates:
            if st.button(f"{template['name']}", key=f"template_{template['name']}", help=template['desc'], use_container_width=True):
                st.success(f"📋 {template['name']} template loaded!")

        # Recent activity
        st.markdown("### 📈 Recent Activity")
        st.metric("Reports This Week", "12", "+3")
        st.metric("Total Downloads", "1,847", "+156")
        st.metric("Active Subscribers", "234", "+12")

# Settings page
def settings_page():
    st.markdown("""
    <div class="main-header">
        <div class="logo-container">
            <h1 class="main-title">⚙️ Settings & Configuration</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🤖 AI Configuration",
        "🔔 Notifications",
        "📚 Data Sources",
        "👤 Account Settings",
        "🔐 Security & Privacy"
    ])

    with tab1:
        st.markdown("### 🤖 AI Analysis Configuration")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🎯 Analysis Settings")

            accuracy_threshold = st.slider(
                "Minimum Accuracy Threshold",
                85, 100, 95,
                help="Minimum AI confidence required for auto-publication"
            )
            st.markdown(f"Current setting: **{accuracy_threshold}%** accuracy required")

            analysis_speed = st.selectbox(
                "Analysis Processing Speed",
                ["🚀 Fast (2-3 minutes)", "⚖️ Balanced (5-7 minutes)", "🔬 Thorough (10-15 minutes)"],
                index=1,
                help="Choose between speed and analysis depth"
            )

            language_detection = st.checkbox("🌐 Auto-detect Language", value=True)
            real_time_analysis = st.checkbox("⚡ Real-time Analysis", value=False)
            auto_transcription = st.checkbox("🎤 Auto-transcription", value=True)

        with col2:
            st.markdown("#### 🗣️ Language & Regional Settings")

            primary_language = st.selectbox(
                "Primary Language",
                ["🇺🇸 English (US)", "🇪🇸 Spanish", "🇫🇷 French", "🇨🇳 Mandarin"]
            )

            regional_context = st.selectbox(
                "Regional Context",
                ["United States", "Canada", "United Kingdom", "Australia", "Global"]
            )

            terminology_mode = st.selectbox(
                "Terminology Mode",
                ["Government/Legal", "Community-Friendly", "Technical/Academic", "Journalistic"]
            )

        st.markdown("#### 🎛️ Advanced AI Settings")

        col1, col2 = st.columns(2)
        with col1:
            topic_sensitivity = st.slider("Topic Detection Sensitivity", 1, 10, 7)
            quote_extraction = st.slider("Quote Extraction Threshold", 1, 10, 8)

        with col2:
            sentiment_analysis = st.checkbox("Enable Sentiment Analysis", value=True)
            emotion_detection = st.checkbox("Enable Emotion Detection", value=False)

        if st.button("💾 Save AI Configuration", use_container_width=True):
            st.success("🤖 AI settings saved successfully!")

    with tab2:
        st.markdown("### 🔔 Notification Preferences")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📧 Delivery Methods")
            email_notifications = st.checkbox("📧 Email Notifications", value=True)
            if email_notifications:
                email_address = st.text_input("Email Address", value="admin@civicscoop.com")

            push_notifications = st.checkbox("📱 Push Notifications", value=False)
            slack_integration = st.checkbox("💬 Slack Integration", value=False)
            if slack_integration:
                slack_webhook = st.text_input("Slack Webhook URL", placeholder="https://hooks.slack.com/...")

            sms_alerts = st.checkbox("📱 SMS Alerts (Critical Only)", value=False)

        with col2:
            st.markdown("#### 🚨 Alert Types")
            new_meetings = st.checkbox("🏛️ New Meeting Analysis", value=True)
            high_engagement = st.checkbox("👥 High Engagement Alerts", value=True)
            critical_issues = st.checkbox("⚡ Critical Priority Issues", value=True)
            system_updates = st.checkbox("🔄 System Updates", value=False)
            weekly_summary = st.checkbox("📊 Weekly Summary", value=True)
            error_alerts = st.checkbox("🚨 Error Alerts", value=True)

        st.markdown("#### ⏰ Notification Timing")

        col1, col2 = st.columns(2)
        with col1:
            notification_frequency = st.selectbox(
                "Default Frequency",
                ["Immediate", "Every 15 minutes", "Hourly", "Twice Daily", "Daily", "Weekly"]
            )

        with col2:
            quiet_hours = st.checkbox("🌙 Enable Quiet Hours", value=True)
            if quiet_hours:
                quiet_start = st.time_input("Quiet Hours Start", value=datetime.strptime("22:00", "%H:%M").time())
                quiet_end = st.time_input("Quiet Hours End", value=datetime.strptime("07:00", "%H:%M").time())

        if st.button("🔔 Save Notification Settings", use_container_width=True):
            st.success("🔔 Notification preferences saved!")

    with tab3:
        st.markdown("### 📚 Data Source Configuration")

        st.markdown("#### 🔗 Connected Data Sources")

        sources = [
            {
                "name": "Austin City Council",
                "type": "Municipal API",
                "status": "Connected",
                "last_sync": "2 hours ago",
                "meetings": 45,
                "url": "https://austin.gov/meetings"
            },
            {
                "name": "Seattle City Council",
                "type": "RSS Feed",
                "status": "Connected",
                "last_sync": "1 hour ago",
                "meetings": 38,
                "url": "https://seattle.gov/council/meetings"
            },
            {
                "name": "Miami-Dade Commission",
                "type": "Web Scraper",
                "status": "Error",
                "last_sync": "1 day ago",
                "meetings": 25,
                "url": "https://miami-dade.gov/meetings"
            },
            {
                "name": "Denver City Council",
                "type": "Municipal API",
                "status": "Connected",
                "last_sync": "3 hours ago",
                "meetings": 28,
                "url": "https://denver.gov/meetings"
            }
        ]

        for source in sources:
            status_color = {
                "Connected": "#22c55e",
                "Error": "#ef4444",
                "Pending": "#f59e0b"
            }.get(source['status'], "#94a3b8")

            st.markdown(f"""
            <div class="meeting-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">{source['name']}</h4>
                        <p style="color: #94a3b8; margin: 5px 0;">
                            {source['type']} • {source['meetings']} meetings • Last sync: {source['last_sync']}
                        </p>
                        <p style="color: #60a5fa; font-size: 12px; margin: 0;">{source['url']}</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="background: {status_color}; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px;">
                            {source['status']}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns([5, 1, 1, 1])
            with col2:
                if st.button("⚙️ Config", key=f"config_{source['name']}", help=f"Configure {source['name']}"):
                    st.info(f"⚙️ Configuring {source['name']}...")

            with col3:
                if st.button("🔄 Sync", key=f"sync_{source['name']}", help=f"Force sync {source['name']}"):
                    st.success(f"🔄 Syncing {source['name']}...")

            with col4:
                if source['status'] == "Error":
                    if st.button("🔧 Fix", key=f"fix_{source['name']}", help=f"Troubleshoot {source['name']}"):
                        st.info(f"🔧 Diagnosing {source['name']} connection...")

        st.markdown("#### ➕ Add New Data Source")

        with st.form("new_source_form"):
            source_name = st.text_input("Source Name", placeholder="e.g., Portland City Council")
            source_url = st.text_input("Source URL", placeholder="https://...")
            source_type = st.selectbox("Source Type", [
                "Municipal API",
                "RSS/Atom Feed",
                "Web Scraper",
                "Manual Upload",
                "Email Integration"
            ])

            update_frequency = st.selectbox("Update Frequency", [
                "Real-time", "Every 15 minutes", "Hourly", "Daily", "Weekly"
            ])

            if st.form_submit_button("➕ Add Data Source"):
                st.success(f"✅ {source_name} added successfully!")

    with tab4:
        st.markdown("### 👤 Account & Organization Settings")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 👤 Personal Information")

            full_name = st.text_input("Full Name", value="City Administrator")
            email = st.text_input("Email Address", value="admin@civicscoop.com")
            title = st.text_input("Job Title", value="Municipal Technology Director")
            organization = st.text_input("Organization", value="City Government")
            department = st.text_input("Department", value="Information Technology")

        with col2:
            st.markdown("#### 🌍 Localization")

            timezone = st.selectbox("Time Zone", [
                "UTC-8 (Pacific)", "UTC-7 (Mountain)", "UTC-6 (Central)",
                "UTC-5 (Eastern)", "UTC+0 (GMT)", "Other"
            ])

            date_format = st.selectbox("Date Format", [
                "MM/DD/YYYY (US)", "DD/MM/YYYY (EU)", "YYYY-MM-DD (ISO)"
            ])

            time_format = st.selectbox("Time Format", ["12-hour (AM/PM)", "24-hour"])

            theme = st.selectbox("Interface Theme", ["🌙 Dark", "☀️ Light", "🔄 Auto"])

        st.markdown("#### 💳 Subscription & Billing")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            **Current Plan:** Professional
            **Status:** Active
            **Next Billing:** January 15, 2025
            **Price:** $299/month
            """)

        with col2:
            if st.button("📈 Upgrade Plan", use_container_width=True):
                st.info("📈 Redirecting to upgrade options...")

            if st.button("📄 Billing History", use_container_width=True):
                st.info("📄 Loading billing history...")

        with col3:
            st.markdown("""
            **Features:**
            ✅ Unlimited Meetings
            ✅ Real-time Analysis
            ✅ Custom Reports
            ✅ API Access
            ✅ Priority Support
            """)

        if st.button("💾 Save Account Settings", use_container_width=True):
            st.success("👤 Account settings updated!")

    with tab5:
        st.markdown("### 🔐 Security & Privacy Settings")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 🔐 Security Settings")

            two_factor = st.checkbox("🔒 Two-Factor Authentication", value=True)
            if two_factor:
                st.success("🔒 2FA is enabled and active")
                if st.button("🔄 Reset 2FA"):
                    st.info("🔄 2FA reset instructions sent to email")

            session_timeout = st.selectbox(
                "Session Timeout",
                ["15 minutes", "30 minutes", "1 hour", "4 hours", "Never"]
            )

            login_notifications = st.checkbox("🚨 Login Notifications", value=True)
            api_access = st.checkbox("🔌 API Access Enabled", value=False)

            if api_access:
                st.text_input("API Key", value="sk-1234567890abcdef", type="password")
                if st.button("🔄 Regenerate API Key"):
                    st.warning("⚠️ This will invalidate the current API key!")

        with col2:
            st.markdown("#### 🛡️ Privacy Controls")

            data_sharing = st.selectbox(
                "Data Sharing",
                ["None", "Anonymized Analytics Only", "Research Participation", "Full Sharing"]
            )

            retention_period = st.selectbox(
                "Data Retention Period",
                ["30 days", "90 days", "1 year", "2 years", "Indefinite"]
            )

            analytics_tracking = st.checkbox("📊 Usage Analytics", value=True)
            error_reporting = st.checkbox("🐛 Automatic Error Reporting", value=True)

            marketing_emails = st.checkbox("📧 Marketing Communications", value=False)

        st.markdown("#### 🗂️ Data Management")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📤 Export My Data", use_container_width=True):
                st.success("📤 Data export initiated. Download link will be emailed.")

        with col2:
            if st.button("🗑️ Delete Account", use_container_width=True):
                st.error("⚠️ This action cannot be undone!")

        with col3:
            if st.button("🔄 Data Audit", use_container_width=True):
                st.info("🔄 Generating data usage report...")

        # Privacy compliance
        st.markdown("#### ⚖️ Privacy Compliance")
        st.markdown("""
        **🛡️ GDPR Compliance:** Fully compliant with European data protection regulations
        **🇺🇸 CCPA Compliance:** Meets California Consumer Privacy Act requirements
        **🔒 SOC 2 Certified:** Annual security audits and compliance verification
        **📋 Data Processing Agreement:** Available for enterprise customers
        """)

        if st.button("🔐 Save Security Settings", use_container_width=True):
            st.success("🔐 Security and privacy settings updated!")

# Main application
def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state['page'] = '🏛️ Dashboard'

    # Create sidebar and get selected page
    selected_page = create_sidebar()

    # Update session state if page changed
    if selected_page != st.session_state['page']:
        st.session_state['page'] = selected_page

    # Route to appropriate page
    if st.session_state['page'] == '🏛️ Dashboard':
        dashboard_page()
    elif st.session_state['page'] == '📊 Meeting Analysis':
        meeting_analysis_page()
    elif st.session_state['page'] == '📈 Analytics':
        analytics_page()
    elif st.session_state['page'] == '📄 Reports':
        reports_page()
    elif st.session_state['page'] == '⚙️ Settings':
        settings_page()

if __name__ == "__main__":
    main()