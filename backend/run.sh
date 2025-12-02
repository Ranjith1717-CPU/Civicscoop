#!/bin/bash

echo "Starting CivicScoop Backend Server..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed"
        echo "Please install Python 3.7+ from https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    if ! command -v pip &> /dev/null; then
        echo "ERROR: pip is not installed"
        echo "Please install pip or reinstall Python"
        exit 1
    else
        PIP_CMD="pip"
    fi
else
    PIP_CMD="pip3"
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing/updating dependencies..."
$PIP_CMD install -r requirements.txt

# Initialize database if it doesn't exist
if [ ! -f "civicscoop.db" ]; then
    echo "Initializing database..."
    $PYTHON_CMD -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created successfully!')"
fi

echo ""
echo "================================================"
echo "CivicScoop Backend Server Starting..."
echo "================================================"
echo ""
echo "Dashboard: http://localhost:5000"
echo "Add Meeting: http://localhost:5000/add_meeting"
echo "Analytics: http://localhost:5000/analytics"
echo "API Docs: Check README.md for API endpoints"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================================"
echo ""

# Start the Flask application
$PYTHON_CMD app.py