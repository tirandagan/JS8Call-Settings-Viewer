#!/bin/bash

echo "JS8Call Configuration Viewer - Installation Test"
echo "==============================================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version)
echo "✓ Found ${PYTHON_VERSION}"

# Check if Rich library is installed
if python3 -c "import rich" &> /dev/null; then
    echo "✓ Rich library is installed"
else
    echo "✗ Rich library is not installed"
    echo "  Please run: pip3 install rich"
    exit 1
fi

# Check if Textual library is installed
if python3 -c "import textual" &> /dev/null; then
    echo "✓ Textual library is installed"
else
    echo "✗ Textual library is not installed"
    echo "  Please run: pip3 install textual>=0.27.0"
    exit 1
fi

# Check if script exists and is executable
if [ -f "js8call_config_viewer.py" ]; then
    echo "✓ Found js8call_config_viewer.py script"
    if [ -x "js8call_config_viewer.py" ]; then
        echo "✓ Script is executable"
    else
        echo "✗ Script is not executable"
        echo "  Please run: chmod +x js8call_config_viewer.py"
    fi
else
    echo "✗ js8call_config_viewer.py script not found in current directory"
    echo "  Please make sure you're in the correct directory"
    exit 1
fi

# Check if the command is available in PATH
if command -v js8call-config-viewer &> /dev/null; then
    echo "✓ js8call-config-viewer is available in PATH"
else
    echo "ℹ js8call-config-viewer is not available in PATH"
    echo "  The script can be run directly with: ./js8call_config_viewer.py"
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

echo "✓ Detected operating system: ${SYSTEM}"

# Check for JS8Call.ini file based on platform
JS8CALL_INI_FOUND=false
case "${SYSTEM}" in
    Linux)
        DEFAULT_PATH="$HOME/.config/JS8Call/js8call.ini"
        if [ -f "$DEFAULT_PATH" ]; then
            echo "✓ JS8Call.ini found at: $DEFAULT_PATH"
            JS8CALL_INI_FOUND=true
        else
            echo "ℹ JS8Call.ini not found at default Linux location"
        fi
        ;;
    macOS)
        DEFAULT_PATH="$HOME/Library/Preferences/JS8Call/js8call.ini"
        if [ -f "$DEFAULT_PATH" ]; then
            echo "✓ JS8Call.ini found at: $DEFAULT_PATH"
            JS8CALL_INI_FOUND=true
        else
            echo "ℹ JS8Call.ini not found at default macOS location"
        fi
        ;;
    Windows)
        # This is approximate in MSYS/Cygwin/Git Bash environments
        if [ -n "$APPDATA" ] && [ -f "$APPDATA/JS8Call/js8call.ini" ]; then
            echo "✓ JS8Call.ini found at: $APPDATA/JS8Call/js8call.ini"
            JS8CALL_INI_FOUND=true
        else
            echo "ℹ JS8Call.ini not found at default Windows location"
        fi
        ;;
    *)
        echo "ℹ Unknown OS, will rely on auto-detection"
        ;;
esac

if [ "$JS8CALL_INI_FOUND" = false ]; then
    echo "ℹ JS8Call.ini not found in default location for your OS"
    echo "  The script will try to auto-detect the file in various locations"
    echo "  Or you can specify the path when running the tool"
fi

echo
echo "Test Completed"
echo
echo "To test the viewer, run one of the following:"
echo "  ./js8call_config_viewer.py"
echo "  python3 js8call_config_viewer.py"
if command -v js8call-config-viewer &> /dev/null; then
    echo "  js8call-config-viewer"
fi
echo
echo "If you need to specify an INI file path, use:"
echo "  ./js8call_config_viewer.py -f /path/to/your/JS8Call.ini"
echo
echo "To show all settings including undocumented ones:"
echo "  ./js8call_config_viewer.py --all" 