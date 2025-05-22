#!/bin/bash

echo "Installing JS8Call Configuration Viewer..."
echo "This tool provides a comprehensive view of your JS8Call.ini settings with explanations"
echo "It automatically finds your JS8Call.ini file on any operating system: Windows, macOS, or Linux"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Display Python version
PYTHON_VERSION=$(python3 --version)
echo "Found ${PYTHON_VERSION}"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Attempting to install pip..."
    python3 -m ensurepip --default-pip || {
        echo "Failed to install pip. Please install pip manually and try again."
        exit 1
    }
fi

# Detect operating system
OS="$(uname -s)"
case "${OS}" in
    Linux*)     SYSTEM="Linux";;
    Darwin*)    SYSTEM="macOS";;
    CYGWIN*)    SYSTEM="Windows";;
    MINGW*)     SYSTEM="Windows";;
    MSYS*)      SYSTEM="Windows";;
    *)          SYSTEM="Unknown";;
esac

echo "Detected operating system: ${SYSTEM}"

# Show expected JS8Call.ini location based on OS
case "${SYSTEM}" in
    Linux)
        echo "JS8Call.ini expected location: ~/.config/JS8Call/js8call.ini"
        ;;
    macOS)
        echo "JS8Call.ini expected location: ~/Library/Preferences/JS8Call/js8call.ini"
        ;;
    Windows)
        echo "JS8Call.ini expected location: %APPDATA%\\JS8Call\\js8call.ini"
        ;;
    *)
        echo "JS8Call.ini location will be auto-detected"
        ;;
esac
echo

# Install options
echo "=== Installation Options ==="
echo "1) Install for current user only (recommended)"
echo "2) Install system-wide (requires sudo)"
echo "3) Install in development mode (for contributors)"
echo "4) Just install dependencies (no installation)"
echo "q) Quit installation"
echo
read -p "Choose an option [1-4 or q]: " OPTION

case $OPTION in
    1)
        echo "Installing for current user..."
        # Install required packages
        echo "Installing dependencies..."
        pip3 install --user rich textual>=0.27.0
        
        # Install the package
        echo "Installing JS8Call Configuration Viewer..."
        pip3 install --user .
        
        # Make the script executable
        chmod +x js8call_config_viewer.py
        
        # Add to PATH if needed
        USER_BIN="$HOME/.local/bin"
        if [[ ":$PATH:" != *":$USER_BIN:"* ]]; then
            echo
            echo "NOTE: You may need to add $USER_BIN to your PATH."
            echo "You can do this by adding the following to your ~/.bashrc or ~/.bash_profile:"
            echo "  export PATH=\$PATH:$USER_BIN"
            echo
        fi
        ;;
    2)
        echo "Installing system-wide (requires sudo)..."
        # Install required packages
        echo "Installing dependencies..."
        sudo pip3 install rich textual>=0.27.0
        
        # Install the package
        echo "Installing JS8Call Configuration Viewer..."
        sudo pip3 install .
        
        # Make the script executable
        chmod +x js8call_config_viewer.py
        ;;
    3)
        echo "Installing in development mode..."
        # Install required packages
        echo "Installing dependencies..."
        pip3 install --user rich textual>=0.27.0
        
        # Install the package in development mode
        echo "Installing JS8Call Configuration Viewer in development mode..."
        pip3 install --user -e .
        
        # Make the script executable
        chmod +x js8call_config_viewer.py
        ;;
    4)
        echo "Installing dependencies only..."
        pip3 install --user rich textual>=0.27.0
        chmod +x js8call_config_viewer.py
        ;;
    q|Q)
        echo "Installation cancelled."
        exit 0
        ;;
    *)
        echo "Invalid option. Installation cancelled."
        exit 1
        ;;
esac

# Check for the JS8Call.ini file - platform specific
JS8CALL_INI=""
case "${SYSTEM}" in
    Linux)
        JS8CALL_INI="$HOME/.config/JS8Call/js8call.ini"
        ;;
    macOS)
        JS8CALL_INI="$HOME/Library/Preferences/JS8Call/js8call.ini"
        ;;
    Windows)
        # This is approximate in MSYS/Cygwin/Git Bash environments
        JS8CALL_INI="$APPDATA/JS8Call/js8call.ini"
        ;;
    *)
        # Default to Linux-style path
        JS8CALL_INI="$HOME/.config/JS8Call/js8call.ini"
        ;;
esac

if [ -f "$JS8CALL_INI" ]; then
    echo
    echo "JS8Call.ini file found at $JS8CALL_INI"
else
    echo
    echo "Note: JS8Call.ini file not found at the expected location ($JS8CALL_INI)"
    echo "Don't worry! The tool will automatically search for it in standard locations."
    echo "You can also specify the path manually when running the tool:"
    echo "  js8call-config-viewer -f /path/to/your/JS8Call.ini"
fi

echo
echo "Installation complete!"
echo
echo "You can now run the tool using either:"
echo "  js8call-config-viewer"
echo "  python3 js8call_config_viewer.py"
echo
echo "To view a custom JS8Call.ini file, use:"
echo "  js8call-config-viewer -f /path/to/your/JS8Call.ini"
echo
echo "To view all settings (including undocumented ones), use:"
echo "  js8call-config-viewer --all"
echo
echo "Enjoy exploring your JS8Call configuration!" 