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

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .meeting-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .priority-high {
        border-left: 4px solid #ef4444;
    }
    .priority-medium {
        border-left: 4px solid #f59e0b;
    }
    .priority-low {
        border-left: 4px solid #10b981;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sample data
@st.cache_data
def load_meeting_data():
    meetings = [
        {
            "id": 1,
            "title": "Austin Housing Crisis Response",
            "location": "Austin City Council",
            "date": "2024-01-15",
            "priority": "High",
            "status": "Analyzed",
            "engagement": 847,
            "topics": ["Housing", "Crisis Response", "Public Policy"],
            "ai_accuracy": 98.7
        },
        {
            "id": 2,
            "title": "Seattle Budget Allocation 2025",
            "location": "Seattle City Council",
            "date": "2024-01-12",
            "priority": "High",
            "status": "In Progress",
            "engagement": 623,
            "topics": ["Budget", "Finance", "Public Services"],
            "ai_accuracy": 97.2
        },
        {
            "id": 3,
            "title": "Miami Climate Action Plan",
            "location": "Miami-Dade Commission",
            "date": "2024-01-10",
            "priority": "Medium",
            "status": "Analyzed",
            "engagement": 534,
            "topics": ["Climate", "Environment", "Sustainability"],
            "ai_accuracy": 96.8
        },
        {
            "id": 4,
            "title": "Denver Transit Expansion",
            "location": "Denver City Council",
            "date": "2024-01-08",
            "priority": "Medium",
            "status": "Scheduled",
            "engagement": 412,
            "topics": ["Transit", "Infrastructure", "Urban Planning"],
            "ai_accuracy": 95.3
        },
        {
            "id": 5,
            "title": "Portland Education Funding",
            "location": "Portland School Board",
            "date": "2024-01-05",
            "priority": "Low",
            "status": "Analyzed",
            "engagement": 298,
            "topics": ["Education", "Funding", "Schools"],
            "ai_accuracy": 97.9
        }
    ]
    return meetings

# Sidebar navigation
def sidebar():
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h2 style='color: #3b82f6;'>🏛️ CivicScoop</h2>
        <p style='color: #64748b;'>AI-Powered Civic Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    page = st.sidebar.selectbox(
        "Navigate to:",
        ["Dashboard", "Meeting Analysis", "Analytics", "Reports", "Settings"]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Quick Actions")
    if st.sidebar.button("🔍 Search Meetings"):
        st.sidebar.info("Search functionality activated!")
    if st.sidebar.button("📊 Generate Report"):
        st.sidebar.success("Report generation started!")
    if st.sidebar.button("⚙️ AI Settings"):
        st.sidebar.info("Opening AI configuration...")

    return page

# Dashboard page
def dashboard_page():
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.markdown("# 🏛️ CivicScoop Dashboard")
    st.markdown("### AI-Powered Civic Intelligence Platform")
    st.markdown('</div>', unsafe_allow_html=True)

    # Metrics row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Meetings",
            value="247",
            delta="12 this week"
        )

    with col2:
        st.metric(
            label="AI Accuracy",
            value="98.7%",
            delta="0.3%"
        )

    with col3:
        st.metric(
            label="Active Stories",
            value="156",
            delta="23 new"
        )

    with col4:
        st.metric(
            label="Citizen Engagement",
            value="89.2K",
            delta="15.7K this week"
        )

    st.markdown("---")

    # Search and filter
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        search_term = st.text_input("🔍 Search meetings, topics, or locations", placeholder="e.g., housing, budget, climate...")

    with col2:
        priority_filter = st.selectbox("Priority", ["All", "High", "Medium", "Low"])

    with col3:
        status_filter = st.selectbox("Status", ["All", "Analyzed", "In Progress", "Scheduled"])

    # Load and filter meetings
    meetings = load_meeting_data()

    # Apply filters
    if priority_filter != "All":
        meetings = [m for m in meetings if m["priority"] == priority_filter]

    if status_filter != "All":
        meetings = [m for m in meetings if m["status"] == status_filter]

    if search_term:
        meetings = [
            m for m in meetings
            if search_term.lower() in m["title"].lower()
            or search_term.lower() in m["location"].lower()
            or any(search_term.lower() in topic.lower() for topic in m["topics"])
        ]

    st.markdown("### Recent Meetings")

    # Display meetings
    for meeting in meetings:
        with st.container():
            priority_class = f"priority-{meeting['priority'].lower()}"

            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

            with col1:
                st.markdown(f"""
                <div class="meeting-card {priority_class}">
                    <h4>{meeting['title']}</h4>
                    <p><strong>📍 {meeting['location']}</strong> • {meeting['date']}</p>
                    <p>Topics: {', '.join(meeting['topics'][:3])}</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"**Priority:** {meeting['priority']}")
                st.markdown(f"**Status:** {meeting['status']}")

            with col3:
                st.markdown(f"**Engagement:** {meeting['engagement']:,}")
                st.markdown(f"**AI Accuracy:** {meeting['ai_accuracy']}%")

            with col4:
                if st.button("Analyze", key=f"analyze_{meeting['id']}"):
                    st.session_state['selected_meeting'] = meeting
                    st.experimental_rerun()

                if st.button("Share", key=f"share_{meeting['id']}"):
                    st.success("Share link copied!")

# Meeting Analysis page
def meeting_analysis_page():
    st.markdown("# 📊 Meeting Analysis")

    # Check if a meeting is selected
    if 'selected_meeting' in st.session_state:
        meeting = st.session_state['selected_meeting']

        st.markdown(f"## {meeting['title']}")
        st.markdown(f"**Location:** {meeting['location']} | **Date:** {meeting['date']}")

        # Tabs for different analysis views
        tab1, tab2, tab3, tab4 = st.tabs(["Video Analysis", "AI Quotes", "Story Builder", "Citizen Engagement"])

        with tab1:
            st.markdown("### Video Analysis")
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Placeholder

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Key Moments:**")
                st.markdown("• 00:05:30 - Housing crisis discussion")
                st.markdown("• 00:12:45 - Budget allocation debate")
                st.markdown("• 00:18:20 - Public comment period")

            with col2:
                st.markdown("**AI Insights:**")
                st.markdown(f"• Accuracy Score: {meeting['ai_accuracy']}%")
                st.markdown(f"• Engagement Level: {meeting['engagement']:,} interactions")
                st.markdown("• Sentiment: Mixed (65% positive)")

        with tab2:
            st.markdown("### AI-Generated Quotes")
            quotes = [
                "Housing affordability remains our top priority for 2024 budget allocation",
                "We need data-driven solutions to address the current crisis",
                "Public input is crucial for making informed policy decisions"
            ]

            for i, quote in enumerate(quotes):
                st.markdown(f"**Quote {i+1}:** *\"{quote}\"*")
                col1, col2 = st.columns([3, 1])
                with col2:
                    if st.button(f"Use Quote", key=f"quote_{i}"):
                        st.success("Quote added to story!")

        with tab3:
            st.markdown("### Story Builder")
            story_template = st.selectbox(
                "Choose story template:",
                ["Breaking News", "Policy Analysis", "Community Impact", "Budget Report"]
            )

            st.text_area(
                "Generated Story:",
                value=f"City Council addresses {meeting['title']} in comprehensive session...",
                height=200
            )

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Generate Story"):
                    st.success("Story generated successfully!")
            with col2:
                if st.button("Publish"):
                    st.success("Story published to newsroom!")

        with tab4:
            st.markdown("### Citizen Engagement")

            # Engagement metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Views", f"{meeting['engagement']:,}")
            with col2:
                st.metric("Comments", "127")
            with col3:
                st.metric("Shares", "89")

            # Comment feed
            st.markdown("**Recent Comments:**")
            comments = [
                {"user": "CitizenJohn", "comment": "Great discussion on housing policy!", "time": "2 hours ago"},
                {"user": "PolicyWatcher", "comment": "More transparency needed in budget process", "time": "3 hours ago"},
                {"user": "LocalResident", "comment": "When will we see action on these issues?", "time": "4 hours ago"}
            ]

            for comment in comments:
                st.markdown(f"**{comment['user']}** ({comment['time']}): {comment['comment']}")

    else:
        st.info("Select a meeting from the Dashboard to view detailed analysis.")
        if st.button("← Back to Dashboard"):
            del st.session_state['selected_meeting']
            st.experimental_rerun()

# Analytics page
def analytics_page():
    st.markdown("# 📈 Analytics Dashboard")

    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Meetings", "247", "↑ 12%")
    with col2:
        st.metric("AI Accuracy", "98.7%", "↑ 0.3%")
    with col3:
        st.metric("Stories Generated", "1,247", "↑ 23%")
    with col4:
        st.metric("Citizen Engagement", "89.2K", "↑ 18%")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Meeting Trends (Last 30 Days)")
        dates = pd.date_range(start='2024-01-01', end='2024-01-30', freq='D')
        meeting_counts = [5 + i % 8 for i in range(len(dates))]

        fig = px.line(x=dates, y=meeting_counts, title="Daily Meeting Analysis")
        fig.update_layout(xaxis_title="Date", yaxis_title="Meetings Analyzed")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### Topic Distribution")
        topics = ["Housing", "Budget", "Climate", "Transit", "Education", "Public Safety"]
        counts = [45, 38, 32, 28, 24, 18]

        fig = px.pie(values=counts, names=topics, title="Meeting Topics")
        st.plotly_chart(fig, use_container_width=True)

    # Engagement analysis
    st.markdown("### Engagement Analysis")

    col1, col2 = st.columns(2)

    with col1:
        meetings_df = pd.DataFrame(load_meeting_data())
        fig = px.scatter(
            meetings_df,
            x='ai_accuracy',
            y='engagement',
            size='engagement',
            color='priority',
            title="AI Accuracy vs Citizen Engagement",
            hover_data=['title']
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Heatmap of activity
        hours = list(range(24))
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        activity_data = [[j + i*3 for i in range(24)] for j in range(7)]

        fig = go.Figure(data=go.Heatmap(
            z=activity_data,
            x=hours,
            y=days,
            colorscale='Blues'
        ))
        fig.update_layout(
            title="Meeting Activity Heatmap",
            xaxis_title="Hour of Day",
            yaxis_title="Day of Week"
        )
        st.plotly_chart(fig, use_container_width=True)

# Reports page
def reports_page():
    st.markdown("# 📄 Reports")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Available Reports")

        reports = [
            {"name": "Weekly Intelligence Brief", "type": "Automated", "last_run": "Today", "status": "Ready"},
            {"name": "Monthly Civic Engagement", "type": "Scheduled", "last_run": "Dec 1", "status": "Processing"},
            {"name": "Housing Crisis Deep Dive", "type": "Custom", "last_run": "Nov 28", "status": "Ready"},
            {"name": "Budget Analysis Q4", "type": "Quarterly", "last_run": "Nov 25", "status": "Ready"},
            {"name": "Climate Action Summary", "type": "Custom", "last_run": "Nov 20", "status": "Ready"}
        ]

        for report in reports:
            with st.container():
                col_a, col_b, col_c, col_d = st.columns([3, 1, 1, 1])

                with col_a:
                    st.markdown(f"**{report['name']}**")
                    st.markdown(f"Type: {report['type']}")

                with col_b:
                    st.markdown(f"**Last Run:** {report['last_run']}")

                with col_c:
                    status_color = "green" if report['status'] == "Ready" else "orange"
                    st.markdown(f"**Status:** :{status_color}[{report['status']}]")

                with col_d:
                    if st.button("Download", key=f"download_{report['name']}"):
                        st.success(f"Downloading {report['name']}...")

                st.markdown("---")

    with col2:
        st.markdown("### Create New Report")

        report_name = st.text_input("Report Name")
        report_type = st.selectbox("Type", ["Custom", "Automated", "Scheduled"])
        date_range = st.date_input("Date Range", value=[datetime.now().date() - timedelta(days=30), datetime.now().date()])

        data_sources = st.multiselect(
            "Data Sources",
            ["Meeting Transcripts", "Citizen Comments", "Social Media", "News Articles", "Government Data"]
        )

        if st.button("Generate Report"):
            st.success(f"Report '{report_name}' generation started!")

        st.markdown("### Report Builder")
        st.markdown("Drag and drop components:")

        components = ["Executive Summary", "Key Metrics", "Charts", "Meeting Highlights", "Recommendations"]
        selected_components = st.multiselect("Report Sections", components)

        if selected_components:
            st.markdown("**Preview:**")
            for component in selected_components:
                st.markdown(f"• {component}")

# Settings page
def settings_page():
    st.markdown("# ⚙️ Settings")

    tab1, tab2, tab3, tab4 = st.tabs(["AI Configuration", "Notifications", "Data Sources", "Account"])

    with tab1:
        st.markdown("### AI Analysis Settings")

        accuracy_threshold = st.slider("Accuracy Threshold", 90, 100, 95)
        st.markdown(f"Current setting: {accuracy_threshold}%")

        analysis_speed = st.selectbox("Analysis Speed", ["Fast", "Balanced", "Thorough"])

        auto_transcription = st.checkbox("Auto-transcription", value=True)
        real_time_analysis = st.checkbox("Real-time Analysis", value=False)

        st.markdown("### Language Settings")
        primary_language = st.selectbox("Primary Language", ["English", "Spanish", "French"])
        detect_language = st.checkbox("Auto-detect Language", value=True)

        if st.button("Save AI Settings"):
            st.success("AI settings saved successfully!")

    with tab2:
        st.markdown("### Notification Preferences")

        email_notifications = st.checkbox("Email Notifications", value=True)
        push_notifications = st.checkbox("Push Notifications", value=False)
        slack_integration = st.checkbox("Slack Integration", value=False)

        st.markdown("### Notification Types")
        new_meetings = st.checkbox("New Meeting Analysis", value=True)
        high_engagement = st.checkbox("High Engagement Alerts", value=True)
        system_updates = st.checkbox("System Updates", value=False)

        notification_frequency = st.selectbox("Frequency", ["Immediate", "Hourly", "Daily", "Weekly"])

        if st.button("Save Notification Settings"):
            st.success("Notification settings saved!")

    with tab3:
        st.markdown("### Data Source Configuration")

        st.markdown("**Connected Sources:**")
        sources = [
            {"name": "Austin City Council", "status": "Connected", "last_sync": "2 hours ago"},
            {"name": "Seattle City Council", "status": "Connected", "last_sync": "1 hour ago"},
            {"name": "Miami-Dade Commission", "status": "Error", "last_sync": "1 day ago"}
        ]

        for source in sources:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

            with col1:
                st.markdown(f"**{source['name']}**")

            with col2:
                status_color = "green" if source['status'] == "Connected" else "red"
                st.markdown(f":{status_color}[{source['status']}]")

            with col3:
                st.markdown(f"*{source['last_sync']}*")

            with col4:
                if st.button("Configure", key=f"config_{source['name']}"):
                    st.info(f"Configuring {source['name']}...")

        if st.button("Add New Source"):
            st.info("Opening data source configuration...")

    with tab4:
        st.markdown("### Account Settings")

        col1, col2 = st.columns(2)

        with col1:
            st.text_input("Full Name", value="City Administrator")
            st.text_input("Email", value="admin@civicscoop.com")
            st.text_input("Organization", value="City Government")

        with col2:
            st.selectbox("Time Zone", ["UTC-8", "UTC-7", "UTC-6", "UTC-5"])
            st.selectbox("Date Format", ["MM/DD/YYYY", "DD/MM/YYYY", "YYYY-MM-DD"])
            st.selectbox("Theme", ["Light", "Dark", "Auto"])

        st.markdown("### Subscription")
        st.markdown("**Current Plan:** Professional")
        st.markdown("**Next Billing:** January 15, 2024")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Upgrade Plan"):
                st.info("Redirecting to billing...")
        with col2:
            if st.button("Billing History"):
                st.info("Loading billing history...")

# Main app
def main():
    page = sidebar()

    if page == "Dashboard":
        dashboard_page()
    elif page == "Meeting Analysis":
        meeting_analysis_page()
    elif page == "Analytics":
        analytics_page()
    elif page == "Reports":
        reports_page()
    elif page == "Settings":
        settings_page()

if __name__ == "__main__":
    main()