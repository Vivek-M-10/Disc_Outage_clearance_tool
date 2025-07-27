#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Print helpful info
echo "🚀 Starting Flask app at: http://127.0.0.1:5000/clean"

# Run Flask on port 5000
flask run --port=5000 --host=127.0.0.1
