#!/bin/bash

# 1. Initial message
echo "Starting initial configuration..."

# 2. Verifying virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
else 
    echo "Virtual environment already created."
fi

# 3. Install dependencies (if execute)
echo "Installing dependencies..."
./venv/bin/pip install -r requirements.txt

# 4. Final message with instructions
echo "Setup completed successfully!"
echo "To activate the virtual environment, run:"
echo "source venv/bin/activate"