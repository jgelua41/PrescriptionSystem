#!/bin/bash

# Prescription Automation System - Shell Script

echo "Starting Prescription Automation System..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the Flask application
echo ""
echo "========================================"
echo "Prescription Automation System Starting"
echo "========================================"
echo ""
echo "Open your browser and go to: http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python app.py
