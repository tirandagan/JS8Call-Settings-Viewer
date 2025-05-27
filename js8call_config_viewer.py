#!/usr/bin/env python3

import os
import sys
import argparse
import configparser
import platform
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.screen import Screen, ModalScreen
from textual.widgets import Header, Footer, Static, Button, DataTable, Label, ListView, ListItem
from textual.reactive import reactive
from textual import events
from rich.text import Text
from rich.panel import Panel
from rich.console import Console

# Define key settings to highlight (based on js8call_ini_file_structure.md)
KEY_SETTINGS = {
    "User Information": [
        "MyCall", "MyGrid", "MyGroups", "MyInfo", "MyStatus", "EOTCharacter", "MFICharacter"
    ],
    "Message Templates": [
        "CQMessage", "HBMessage", "Reply"
    ],
    "Display Settings": [
        "Font", "TableFont", "RXTextFont", "TXTextFont", "ComposeTextFont", 
        "ShowMenus", "ShowStatusbar", "ShowTooltips", "DisplayDecodeAttempts"
    ],
    "Color Settings": [
        "colorCQ", "colorPrimary", "colorSecondary", "colorMyCall", 
        "color_rx_background", "color_rx_foreground", "color_compose_background", 
        "color_compose_foreground", "color_tx_foreground", "colorDXCC", 
        "colorNewCall", "colorTableBackground", "colorTableHighlight", "colorTableForeground"
    ],
    "Audio Settings": [
        "SoundInName", "SoundOutName", "NotificationSoundOutName", "OutAttenuation"
    ],
    "Waterfall Settings": [
        "PlotZero", "PlotGain", "Plot2dGain", "Plot2dZero", "PlotWidth", "BinsPerPixel",
        "SmoothYellow", "Percent2D", "WaterfallAvg", "WaterfallPalette", "WaterfallFPS"
    ],
    "Radio Settings": [
        "PTTMethod", "PTTCommand", "RigName", "SplitMode", "FreqTxOffset", "VHFUHF"
    ],
    "Network Settings": [
        "SpotToAPRS", "SpotToReportingNetworks", "AprsServerName", "AprsServerPort",
        "UDPEnabled", "TCPEnabled", "TCPMaxConnections"
    ],
    "Behavior Settings": [
        "AutoSwitchBands", "BeaconAnywhere", "HeartbeatQSOPause", "WriteLogs", 
        "ResetActivity", "CheckForUpdates", "dBtoComments"
    ],
    "Automation Settings": [
        "AutoWhitelist", "AutoBlacklist", "HBBlacklist", "SpotBlacklist",
        "AutoreplyConfirmation", "TransmitDirected"
    ],
    "Decode Settings": [
        "Decode52", "SingleDecode", "TwoPass", "StopAutoSyncOnDecode", 
        "StopAutoSyncAfter", "QuickDecode", "DeepDecode"
    ],
    "Heartbeat Settings": [
        "HeartbeatInterval", "HeartbeatAcknowledgements", "AutoreplyOnAtStartup",
        "ID_interval", "CallsignAging", "ActivityAging"
    ],
    "Special Modes": [
        "Fox", "Hound", "x2ToneSpacing", "x4ToneSpacing"
    ]
}

# Define comprehensive descriptions for settings based on js8call_ini_file_structure.md
SETTING_DESCRIPTIONS = {
    # User Information
    "MyCall": "Your amateur radio callsign used in all communications. This is your station's primary identifier. Changing mid-operation can confuse stations in QSO with you and disrupt message routing through the JS8Call network.",
    "MyGrid": "Your Maidenhead grid locator used for distance calculations and location reporting. Should be accurate (4-6 character format) for proper distance calculations and to help others know your geographic location for signal path analysis.",
    "MyGroups": "Groups you belong to for directed messages (comma-separated list). Controls which group messages you'll receive. Joining common groups like ARES or RACES can connect you with emergency communications networks.",
    "MyInfo": "Your station information shared when stations query you. Typically includes radio model, antenna, and power output. Limited to reasonable text length for efficient transmission over the air.",
    "MyStatus": "Status message shown to others in heartbeats and automated responses. Supports macros like <MYIDLE> (idle time) and <MYVERSION> (JS8Call version). Status messages are visible to all stations receiving your transmissions.",
    "EOTCharacter": "End of transmission character (default: '♢'). Visual indicator that marks the end of your message. Changing this may confuse operators familiar with the standard character used by most JS8Call operators.",
    "MFICharacter": "Message fragment indicator (default: '……'). Shows when a message continuation follows in a multi-part transmission. The character appears at the end of fragmented messages to indicate more is coming.",
    
    # Message Templates
    "CQMessage": "Template used for CQ calls. The standard template includes your grid locator. Supports macros like <MYGRID4> for inserting your 4-character grid. Keep reasonably short for better responses and efficient use of airtime.",
    "HBMessage": "Template for heartbeat messages automatically transmitted at regular intervals. Should include your grid for location awareness. Heartbeats help maintain your presence on the JS8Call network and update your status.",
    "Reply": "Default reply text when responding to calls. Standard 'HW CPY?' (How copy?) is widely understood and the conventional first response. This text is pre-populated when you click 'Reply' to another station.",
    
    # Display Settings
    "Font": "Controls text display throughout the application. Specified as 'Family,Size,Weight,Italic,Strikeout,Underline,StyleHint,Spacing,FixedPitch,Kerning'. Very large fonts may cause UI display issues or text overlap in constrained areas.",
    "color": "Color settings for various UI elements stored in hexadecimal format (#RRGGBB). Choose high-contrast colors for visibility, especially for important interface elements. Colors affect the overall readability of the application.",
    "ShowMenus": "Whether to display menu bars in the user interface. Hiding menus saves vertical screen space but limits access to some features. Consider keeping enabled until you're familiar with keyboard shortcuts and operation.",
    "ShowStatusbar": "Whether to display the status bar at the bottom of the window. The status bar provides important information about program state, frequencies, and operating conditions. Hiding saves space but removes status information.",
    "ShowTooltips": "Whether to show helpful tooltips when hovering over controls. Useful for learning the program's features; experienced users may disable for a cleaner interface. Tooltips provide contextual help for various controls and settings.",
    "DisplayDecodeAttempts": "Show decode attempts visually in the waterfall display. Can be distracting but useful for debugging reception issues. When enabled, shows where the decoder is attempting to find signals, even unsuccessful attempts.",
    
    # Audio Settings
    "SoundInName": "Audio input device for receiving signals. Must match a functioning audio input device connected to your radio's audio output. Incorrect settings will prevent JS8Call from decoding incoming signals completely.",
    "SoundOutName": "Audio output device for transmitting signals. Must match a functioning audio output device connected to your radio's audio input. Incorrect settings will prevent JS8Call from generating transmit audio completely.",
    "NotificationSoundOutName": "Device for playing notification sounds when messages are received. Can be the same as or different from your main audio output. Setting to a different device allows alerts without interfering with radio audio.",
    "OutAttenuation": "Output audio level adjustment in decibels. Setting too high may cause overmodulation, distortion, and excessive signal bandwidth. Too low may result in weak transmissions that others cannot decode. Adjust with your radio's ALC meter.",
    
    # Waterfall Settings
    "PlotZero": "Zero reference baseline for waterfall display in dB. Adjust for optimal signal visibility based on your noise floor. Lower values (more negative) make weaker signals more visible but increase background noise display.",
    "PlotGain": "Gain multiplier for waterfall display. Higher values amplify signal visualization, making weaker signals more visible. Excessive gain will make noise more prominent and may obscure signal details in high noise environments.",
    "Plot2dGain": "Gain for 2D spectrum display shown above the waterfall. Balance between seeing weak signals and excessive noise. Higher values make weak signals visible but also amplify noise, potentially making signal identification harder.",
    "Plot2dZero": "Zero reference for 2D plot in dB. Adjusts where the baseline appears in the 2D spectrum display. Set to position typical noise floor appropriately for your receiver and band conditions.",
    "PlotWidth": "Width of waterfall in pixels. Wider displays show more frequency range, narrower shows more detail in a smaller range. The optimum value depends on your screen resolution and how much frequency span you want to monitor.",
    "BinsPerPixel": "Frequency bins per screen pixel in the waterfall display. Lower values show more spectral detail but narrow the total visible frequency range. Higher values show more bandwidth but with less resolution per Hz.",
    "SmoothYellow": "Smoothing factor for the yellow trace (current sweep) in the waterfall. Higher values smooth the display but may hide fast signal changes or brief transmissions. Lower values show more detail but appear more jittery.",
    "Percent2D": "Screen percentage allocated to the 2D spectrum display (0-100). Balance between waterfall and 2D display height. Many operators prefer a small 2D display (10-20%) with more space for the waterfall and message area.",
    "WaterfallAvg": "Waterfall averaging factor. Higher values smooth noise but slow response to signal changes. Lower values show signals immediately but with more noise artifacts. Adjust based on your preference for signal visibility versus noise reduction.",
    "WaterfallPalette": "Color scheme for waterfall signal intensity display. Choose based on personal preference and visibility. Different palettes enhance different aspects of signals; some are better for weak signal detection, others for strong signal clarity.",
    "WaterfallFPS": "Frames per second for waterfall updates. Higher values give smoother animation but increase CPU usage. Lower values reduce processor load but make the waterfall appear more jerky. Typical values range from 15-30 FPS.",
    
    # Radio Interface Settings
    "PTTMethod": "Method used for transmit control (CAT, DTR, RTS, VOX, etc.). Must match your radio interface setup and capabilities. Incorrect settings will prevent proper transmit switching or cause the radio to be constantly keyed.",
    "PTTCommand": "External command used for PTT if command-based keying is selected. Requires proper command syntax for your system. Used for specialized interfaces like those controlling amplifiers or custom hardware.",
    "UDPEnabled": "Enable UDP server for external radio control applications. Creates potential security risk if exposed to the internet. Allows other software to control JS8Call, which can be useful for station automation.",
    "TCPEnabled": "Enable TCP server for external radio control. Creates potential security risk if exposed to the internet. More reliable than UDP for remote control but requires proper firewall configuration for security.",
    "TCPMaxConnections": "Maximum simultaneous TCP connections allowed to JS8Call. Higher values allow more clients but consume more resources. Setting too high could allow excess connections that impact performance.",
    "VHFUHF": "Enable VHF/UHF specific features and timing. Use only when operating on VHF/UHF bands. Affects timing parameters and other mode-specific behaviors to optimize for typical VHF/UHF propagation characteristics.",
    "RigName": "Selected radio model for CAT control. Must match your actual radio for proper frequency control and PTT operation. Each radio uses specific commands; selecting the wrong model will cause communication failures.",
    "SplitMode": "Controls TX/RX frequency relationship for split operation. Affects how JS8Call determines transmit frequency relative to receive. Essential for DX operation where transmit and receive frequencies differ.",
    "FreqTxOffset": "TX offset from RX frequency in Hz. Used for working DX stations operating split or compensating for radio frequency offset errors. Positive values transmit above receive frequency; negative values transmit below.",
    
    # Behavior Settings
    "AutoSwitchBands": "Automatically switches bands based on configuration. May interfere with manual frequency control if enabled. When enabled, JS8Call will automatically QSY to configured frequencies when changing bands.",
    "BeaconAnywhere": "Allow heartbeat transmission anywhere in the band, not just on standard JS8Call frequencies. Enabling may cause interference to other digital modes if you transmit outside standard JS8Call segments.",
    "HeartbeatQSOPause": "Pause automatic heartbeat transmissions during active QSOs. Disabling may cause your heartbeat to transmit during conversations, potentially interrupting ongoing message exchanges with other stations.",
    "HeartbeatAckSNR": "Include signal strength reports (SNR) in heartbeat acknowledgments. Slightly increases message length but provides useful signal information to the originating station. Report helps others assess propagation quality.",
    "SpotToAPRS": "Send reception reports to APRS network. Requires properly configured APRS settings and credentials. Contributes to the wider amateur radio community by providing propagation data visible on services like aprs.fi.",
    "WriteLogs": "Save detailed log files of contacts and activity. Disabling means activity is not saved permanently and history will be lost between sessions. Logs are valuable for troubleshooting and documenting contacts.",
    "ResetActivity": "Clear activity display when starting JS8Call. Historical information is lost if enabled, giving a clean interface at startup. Disabling preserves message history between program restarts.",
    "CheckForUpdates": "Check for JS8Call software updates at startup. Disabling may leave you on older versions with bugs or missing features. Recommended to leave enabled to ensure you're using the latest version with security fixes.",
    "dBtoComments": "Include signal reports in ADIF log comments. Makes logs more detailed but longer. Provides valuable signal strength history when reviewing past contacts or analyzing propagation patterns.",
    
    # Automation Settings
    "AutoWhitelist": "Callsigns allowed for automatic responses and features. Too many entries might cause unwanted automatic behavior. Use for trusted stations you want to allow automatic interaction with your station.",
    "AutoBlacklist": "Callsigns blocked from automated features and responses. Prevents automatic interaction with problematic stations or interference sources. Useful for blocking stations causing issues with your automated functions.",
    "HBBlacklist": "Calls excluded from heartbeat features and processing. Use for stations sending excessive heartbeats that may congest your activity display. Stations on this list won't trigger notifications or automatic responses.",
    "SpotBlacklist": "Calls excluded from spotting to reporting networks. Won't report these stations to PSKReporter, APRS, or other networks. Useful if certain stations request privacy or generate false spots due to unique configurations.",
    "AutoreplyConfirmation": "Prompt before sending automatic replies. Disabling removes safeguard against unwanted transmissions but increases automation. The confirmation dialog helps prevent accidental transmissions in response to received messages.",
    "TransmitDirected": "Enables auto-replies to directed messages addressed to your callsign. Disabling requires manual replies to all messages, even those specifically sent to you. Key setting for station automation versus manual operation.",
    
    # Network Settings
    "SpotToReportingNetworks": "Send reception reports to PSKReporter and other networks. Increases internet traffic; may reveal your operation to public spotting sites. Contributes valuable propagation data to the amateur community.",
    "AprsServerName": "APRS server hostname for reporting station spots. Must be valid APRS-IS server (typically rotate.aprs2.net). The server receives your reception reports for distribution to the APRS network.",
    "AprsServerPort": "APRS server port for connections. Typically 14580 for standard APRS-IS access. Must be correct and accessible through your firewall for successful APRS reporting of spots and location information.",
    
    # Decode Settings
    "Decode52": "Decode at 52-second timing used by some JS8Call operators. Enabling allows reception of both standard (15 sec) and extended (52 sec) messages. Useful for challenging propagation conditions where longer transmissions may be more reliable.",
    "SingleDecode": "Use single pass decoding algorithm. Faster but may miss some signals, especially in difficult conditions. Uses less CPU but potentially reduces decoding success rate compared to multi-pass decoding.",
    "TwoPass": "Use two-pass decoding for better weak signal performance. More thorough but uses significantly more CPU resources. Recommended for marginal conditions where signals are near the noise floor.",
    "StopAutoSyncOnDecode": "Stop automatic sync adjustments after successful decodes. Balances between timing stability and adapting to changing drift. Enabling may improve decode reliability for signals with stable timing.",
    "StopAutoSyncAfter": "Number of successful decodes before stopping automatic sync adjustments. Higher values track drift longer before stabilizing. Setting depends on the frequency stability of stations you commonly work.",
    "QuickDecode": "Use fast decode algorithm optimized for speed over sensitivity. Faster decoding but less sensitive to weak signals. Useful on faster computers or when working predominantly with strong signals.",
    "DeepDecode": "Use thorough decoding algorithms for maximum sensitivity. Slower but can find weaker signals buried in noise. Requires more CPU power but improves reception in difficult conditions or when working weak signal stations.",
    
    # Heartbeat/Auto Settings
    "HeartbeatInterval": "Time between automatic heartbeats in minutes. More frequent uses more airtime; less frequent reduces your visibility on the network. Finding the right balance avoids both excessive transmissions and appearing inactive.",
    "HeartbeatAcknowledgements": "Enable automatic responses to received heartbeats. Increases transmissions but improves network functionality by confirming reception. Helps others know their signals are being received and improves network mapping.",
    "AutoreplyOnAtStartup": "Start the application with autoreply feature active. May cause immediate transmissions after startup if messages are waiting. Consider disabling if you need to check frequencies before transmitting.",
    "ID_interval": "Station identification frequency in minutes. Must comply with your regulatory requirements for station identification. In the US, FCC rules require identification every 10 minutes during active communication.",
    "CallsignAging": "Time in minutes before calls age out of the active stations list. Shorter times keep list current; longer remembers more stations. Affects how long stations appear in your active station display after their last transmission.",
    "ActivityAging": "Time in minutes before activity messages age out. Balances between maintaining conversation history and preventing clutter. Affects how long messages remain in your activity panel before being removed.",
    
    # Special Mode Settings
    "Fox": "Fox mode for contesting or special event operations. Not for normal everyday operation. Creates special transmission sequencing for efficient contest exchanges when many stations are calling you.",
    "Hound": "Hound mode for contesting or working special event stations. Not for normal operation. Optimizes your station to efficiently call and work contest stations (Foxes) in a competitive pileup environment.",
    "x2ToneSpacing": "Use 2x tone spacing for improved decoding in moderate noise. Uses more bandwidth but can improve decoding in poor conditions. Doubles the normal tone spacing, making signals more resistant to selective fading and QRM.",
    "x4ToneSpacing": "Use 4x tone spacing. Uses much more bandwidth but most resistant to interference. Four times normal tone spacing makes signals extremely robust but uses excessive bandwidth that may cause interference to others."
}

# Define standard category names that match the markdown document
STANDARD_CATEGORIES = [
    "User Information",
    "Message Templates",
    "Display Settings",
    "Color Settings",
    "Audio Settings",
    "Waterfall Settings",
    "Radio Settings",
    "Network Settings",
    "Behavior Settings",
    "Automation Settings", 
    "Decode Settings",
    "Heartbeat Settings",
    "Special Modes"
]

# Create a mapping from JS8Call.ini section names to our standard categories
SECTION_TO_CATEGORY = {
    "Configuration": "User Information",
    "Settings": "Behavior Settings",
    "Audio": "Audio Settings",
    "AudioInput": "Audio Settings",
    "AudioOutput": "Audio Settings",
    "Colors": "Color Settings",
    "Waterfall": "Waterfall Settings",
    "Radio": "Radio Settings",
    "Rig": "Radio Settings",
    "Band": "Radio Settings",
    "Network": "Network Settings",
    "Reporting": "Network Settings",
    "Notifications": "Behavior Settings",
    "Specials": "Special Modes",
    "Fonts": "Display Settings",
    "Decode": "Decode Settings",
    "AutoReply": "Automation Settings",
    "Heartbeat": "Heartbeat Settings",
    "Display": "Display Settings"
}

# Dictionary to store valid values and formats for settings
SETTING_VALUES = {}

def load_setting_values():
    """Parse the JS8Call settings values markdown file to extract valid values and formats."""
    # Find the markdown file relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, "docs", "js8call_settings_values.md")
    
    if not os.path.exists(md_path):
        # Try with parent directory
        md_path = os.path.join(script_dir, "..", "docs", "js8call_settings_values.md")
        if not os.path.exists(md_path):
            # If file is still not found, we can't load values
            console = Console()
            console.print("[bold yellow]Warning: js8call_settings_values.md not found, valid values information will not be available[/bold yellow]")
            return
    
    # Parse the markdown file to extract settings and their valid values
    current_category = None
    in_table = False
    
    with open(md_path, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        
        # Check for category headers
        if line.startswith("## "):
            current_category = line[3:].strip()
            in_table = False
        # Check for table header separator
        elif "|---" in line:
            in_table = True
            continue
        # Process table rows
        elif in_table and line.startswith("|") and line.endswith("|"):
            # Split by pipe character and strip spaces
            parts = [part.strip() for part in line.split("|")[1:-1]]
            
            if len(parts) >= 3:  # Ensure we have setting, values, and description
                # Extract setting name and remove formatting
                setting = parts[0].replace("**", "").strip()
                values = parts[1].strip()
                description = parts[2].strip()
                
                # Store in our dictionary
                SETTING_VALUES[setting] = {
                    "category": current_category,
                    "values": values,
                    "description": description
                }

def get_setting_values(key):
    """Get the valid values/format for a setting."""
    # Try to find an exact match first
    if key in SETTING_VALUES:
        return SETTING_VALUES[key]
    
    # Try case-insensitive match
    key_lower = key.lower()
    for setting_key, values in SETTING_VALUES.items():
        if setting_key.lower() == key_lower:
            return values
    
    # Return None if no match found
    return None

def is_documented_setting(key):
    """Check if a setting is documented in js8call_ini_file_structure.md."""
    # Check for exact match
    if key in SETTING_DESCRIPTIONS:
        return True
    
    # Check for case-insensitive match
    key_lower = key.lower()
    for setting_key in SETTING_DESCRIPTIONS.keys():
        if setting_key.lower() == key_lower:
            return True
    
    # Check for partial match in documented settings
    for setting_key in SETTING_DESCRIPTIONS.keys():
        if setting_key.lower() in key_lower or key_lower in setting_key.lower():
            return True
    
    # Not documented
    return False

def get_setting_description(key):
    """Get a comprehensive description for a setting."""
    # Try to find an exact match first
    if key in SETTING_DESCRIPTIONS:
        return SETTING_DESCRIPTIONS[key]
    
    # Try case-insensitive match
    key_lower = key.lower()
    for setting_key, description in SETTING_DESCRIPTIONS.items():
        if setting_key.lower() == key_lower:
            return description
    
    # Try to find a partial match
    for setting_key, description in SETTING_DESCRIPTIONS.items():
        if setting_key.lower() in key_lower or key_lower in setting_key.lower():
            return description
    
    # Default description if nothing matches
    return "Configuration setting for JS8Call"

def get_default_ini_path():
    """Get the default path to JS8Call.ini based on the operating system."""
    system = platform.system()
    
    if system == "Windows":
        # Windows path: %APPDATA%\JS8Call\js8call.ini
        return Path(os.path.expandvars("%APPDATA%\\JS8Call\\js8call.ini"))
    elif system == "Darwin":  # macOS
        # macOS path: ~/Library/Preferences/JS8Call/js8call.ini
        return Path(os.path.expanduser("~/Library/Preferences/JS8Call/js8call.ini"))
    else:  # Linux and others
        # Linux path: ~/.config/JS8Call/js8call.ini
        return Path(os.path.expanduser("~/.config/JS8Call/js8call.ini"))

def find_js8call_ini_file():
    """Attempt to find the JS8Call.ini file in standard locations."""
    # Get the default path based on OS
    default_path = get_default_ini_path()
    
    if default_path.exists():
        return default_path
    
    # If not found in default location, try alternative locations
    alternative_paths = [
        Path(os.path.expanduser("~/.config/JS8Call.ini")),  # Legacy Linux path
        Path(os.path.expanduser("~/JS8Call/js8call.ini")),  # Alternative user directory
        Path(os.path.expanduser("~/js8call.ini")),          # Home directory
        Path("/usr/local/share/JS8Call/js8call.ini"),       # System-wide installation (Unix-like systems)
        Path("/opt/JS8Call/js8call.ini"),                   # Alternative system-wide (Unix-like systems)
    ]
    
    # For Windows, add a few alternative paths
    if platform.system() == "Windows":
        program_files = os.path.expandvars("%ProgramFiles%")
        program_files_x86 = os.path.expandvars("%ProgramFiles(x86)%")
        
        alternative_paths.extend([
            Path(f"{program_files}\\JS8Call\\js8call.ini"),
            Path(f"{program_files_x86}\\JS8Call\\js8call.ini"),
            Path("C:\\JS8Call\\js8call.ini")
        ])
    
    # Try each alternative path
    for path in alternative_paths:
        if path.exists():
            return path
    
    # If we got here, no file was found
    return None

def read_js8call_ini(file_path=None):
    """Read the JS8Call.ini file from the specified location or default."""
    if file_path:
        ini_path = Path(file_path)
    else:
        # Try to find the ini file
        ini_path = find_js8call_ini_file()
        
        if ini_path is None:
            console = Console()
            console.print("[bold red]Error: JS8Call.ini file not found in any standard location[/bold red]")
            console.print("[bold yellow]Please specify the path manually with the -f option[/bold yellow]")
            return None, None
    
    if not ini_path.exists():
        console = Console()
        console.print(f"[bold red]Error: JS8Call.ini file not found at {ini_path}[/bold red]")
        return None, None
    
    config = configparser.ConfigParser()
    try:
        config.read(ini_path)
        return config, str(ini_path)
    except Exception as e:
        console = Console()
        console.print(f"[bold red]Error reading config file: {e}[/bold red]")
        return None, None

def is_key_setting(key):
    """Check if a key is in our list of key settings."""
    for category in KEY_SETTINGS.values():
        if any(setting in key for setting in category):
            return True
    return False

def get_category_for_key(key):
    """Get the category a key belongs to."""
    for category, settings in KEY_SETTINGS.items():
        if any(setting in key for setting in category):
            return category
    return "Other"

def get_setting_category(key):
    """Determine which category a setting belongs to."""
    # Check if it's in one of our defined categories
    for category, settings in KEY_SETTINGS.items():
        # Try exact match first
        if key in settings:
            return category
        
        # Try case-insensitive match
        key_lower = key.lower()
        if any(s.lower() == key_lower for s in settings):
            return category
    
    # If not found, try to guess based on name patterns
    key_lower = key.lower()
    if "color" in key_lower:
        return "Color Settings"
    elif "font" in key_lower:
        return "Display Settings"
    elif "sound" in key_lower or "audio" in key_lower:
        return "Audio Settings"
    elif "waterfall" in key_lower or "plot" in key_lower:
        return "Waterfall Settings"
    elif "ptt" in key_lower or "rig" in key_lower or "cat" in key_lower or "radio" in key_lower:
        return "Radio Settings"
    elif "udp" in key_lower or "tcp" in key_lower or "server" in key_lower or "aprs" in key_lower:
        return "Network Settings"
    elif "heartbeat" in key_lower or "hb" in key_lower:
        return "Heartbeat Settings"
    elif "decode" in key_lower:
        return "Decode Settings"
    elif "auto" in key_lower or "whitelist" in key_lower or "blacklist" in key_lower:
        return "Automation Settings"
    
    # Default
    return "Other Settings"

def organize_settings_by_category(config):
    """Organize all settings from the config into our standard categories."""
    categorized_settings = {category: {} for category in STANDARD_CATEGORIES}
    categorized_settings["Other Settings"] = {}  # For anything not categorized
    
    # Go through each section and setting, assigning to the appropriate category
    for section in config.sections():
        for key, value in config[section].items():
            category = get_setting_category(key)
            categorized_settings[category][key] = value
    
    # Remove empty categories
    return {k: v for k, v in categorized_settings.items() if v}

class SettingValuesScreen(ModalScreen):
    """Modal screen to display valid values and format for a setting."""
    
    BINDINGS = [
        # Any key will dismiss this screen
        Binding("escape", "dismiss", "Back"),
        Binding("q", "dismiss", "Back"),
    ]
    
    def __init__(self, setting_key, setting_value, setting_values):
        super().__init__()
        self.setting_key = setting_key
        self.setting_value = setting_value
        self.setting_values = setting_values
        
    def compose(self) -> ComposeResult:
        """Create child widgets for the values screen."""
        # Create a simple modal dialog with the setting information
        with Vertical(id="values-dialog"):
            yield Static(f"Valid Values for: [bold]{self.setting_key}[/bold]", id="values-title")
            
            with ScrollableContainer(id="values-content"):
                if self.setting_values:
                    # Format the values information nicely
                    values_text = f"[bold underline]Valid Values/Format:[/bold underline]\n{self.setting_values['values']}\n\n"
                    values_text += f"[bold underline]Description:[/bold underline]\n{self.setting_values['description']}\n\n"
                    values_text += f"[bold underline]Current Value:[/bold underline]\n{self.setting_value}"
                    
                    yield Static(values_text)
                else:
                    yield Static("No valid values information available for this setting.")
            
            yield Static("Press any key to close", id="values-footer")
    
    def on_key(self, event: events.Key) -> None:
        """Handle key press events - any key dismisses this screen."""
        # Dismiss the screen
        self.dismiss()
        
        # We still want to allow navigation keys to be processed after dismissal
        # So we don't prevent default
        event.prevent_default = False

class SettingTable(DataTable):
    """A data table for displaying configuration settings."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_column("Setting", width=30)  # Slightly reduce setting column width
        self.add_column("Value")  # Remove fixed width to let it expand to fill available space
        self.cursor_type = "row"  # Ensure entire row is highlighted

    def update_category_settings(self, category_settings, category_name, show_all=False):
        """Update the table with settings from the given category."""
        self.clear()
        
        if not category_settings:
            return
            
        # Sort the keys for better display
        for key, value in sorted(category_settings.items()):
            # Skip undocumented settings if show_all is False
            if not show_all and not is_documented_setting(key):
                continue
            
            # Format value for better display
            if len(value) > 100:
                # For very long values, use rich text that can wrap nicely
                display_value = Text(value)
                display_value.no_wrap = False
            else:
                display_value = value
                
            # Highlight key settings
            key_style = "bold" if is_key_setting(key) else ""
            
            # Add the row with styling
            self.add_row(
                Text(key, style=key_style), 
                display_value
            )
    
    # Keep the original update_settings method for backward compatibility
    def update_settings(self, config_section, section_name, show_all=False):
        """Update the table with settings from the given section (kept for backward compatibility)."""
        self.clear()
        
        if not config_section:
            return
            
        # Sort the keys for better display
        for key, value in sorted(config_section.items()):
            # Skip undocumented settings if show_all is False
            if not show_all and not is_documented_setting(key):
                continue
            
            # Format value for better display
            if len(value) > 100:
                # For very long values, use rich text that can wrap nicely
                display_value = Text(value)
                display_value.no_wrap = False
            else:
                display_value = value
                
            # Highlight key settings
            key_style = "bold" if is_key_setting(key) else ""
            
            # Add the row with styling
            self.add_row(
                Text(key, style=key_style), 
                display_value
            )

class DescriptionArea(Static):
    """Multiline area for displaying setting descriptions."""
    
    def update_description(self, key="", value="", description=""):
        """Update the description area with information about a setting."""
        if not key:
            self.update("")
            return
        
        # Get description if not provided
        if not description:
            description = get_setting_description(key)
        
        # Create multiline display focusing on description
        if description:
            # Fix for safer text splitting - always use integers for slicing
            description_length = len(description)
            
            # For short descriptions, just display as-is
            if description_length <= 100:
                formatted_text = f"[bold]{description}[/bold]"
            else:
                # For longer descriptions, split into 3 lines with proper sentence/word breaks
                # Calculate approximately how many chars per line (aiming for 3 lines)
                chars_per_line = description_length // 3
                
                # Find first break point at a sentence or word boundary
                first_break = description.find(". ", 0, int(chars_per_line * 1.5))
                if first_break == -1:
                    # No sentence break found, try word break
                    first_break = description.rfind(" ", int(chars_per_line * 0.8), int(chars_per_line * 1.2))
                    if first_break == -1:
                        # Still no good break, just use the calculated position
                        first_break = chars_per_line
                
                # Find second break point
                second_break = description.find(". ", first_break + 1, int(first_break + chars_per_line * 1.5))
                if second_break == -1:
                    # No sentence break found, try word break
                    second_break = description.rfind(" ", int(first_break + chars_per_line * 0.8), 
                                                  int(first_break + chars_per_line * 1.2))
                    if second_break == -1:
                        # Still no good break, just use first_break + chars_per_line
                        second_break = first_break + chars_per_line
                
                # Make sure our break points are good integers
                first_break = max(0, int(first_break))
                second_break = max(first_break + 1, int(second_break))
                
                # Extract our 3 lines, handling punctuation at the break points
                line1 = description[:first_break + (2 if first_break < len(description)-2 and 
                                                 description[first_break:first_break+2] == ". " else 1)]
                line2 = description[first_break + (2 if first_break < len(description)-2 and 
                                                 description[first_break:first_break+2] == ". " else 1):second_break + 
                                  (2 if second_break < len(description)-2 and 
                                   description[second_break:second_break+2] == ". " else 1)]
                line3 = description[second_break + (2 if second_break < len(description)-2 and 
                                                 description[second_break:second_break+2] == ". " else 1):]
                
                # Format the text
                formatted_text = f"[bold]{line1}[/bold]\n{line2}\n{line3}"
            
            self.update(formatted_text)
        else:
            # Fallback if no description
            self.update("No detailed information available for this setting.")

class SettingsView(Screen):
    """Main screen for the JS8Call Configuration Viewer."""
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("h", "focus_categories", "Categories"),
        Binding("l", "focus_settings", "Settings"),
        Binding("j", "next_setting", "Next"),
        Binding("k", "prev_setting", "Previous"),
        Binding("tab", "toggle_focus", "Toggle Focus"),
        Binding("f1", "help", "Help"),
        Binding("v", "show_values", "Values"),
    ]
    
    def __init__(self, config, config_path, show_all=False):
        super().__init__()
        self.config = config
        self.config_path = config_path
        self.show_all = show_all
        self.current_category = None
        self.categories = []
        self.categorized_settings = organize_settings_by_category(config)
        
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        
        with Horizontal():
            # Category sidebar (20% of width)
            with Vertical(id="sidebar", classes="sidebar"):
                yield Static("Categories", id="sidebar-header", classes="sidebar-header")
                yield ListView(*[], id="categories-list")
            
            # Settings display (80% of width)
            with Vertical(id="settings-area"):
                yield Static("", id="section-title", classes="section-title")
                with ScrollableContainer(id="table-container"):
                    yield SettingTable(id="settings-table")
        
        # Description area above the status bar
        yield DescriptionArea("", id="description-area", classes="description-area")
        
        # Status bar and footer - status bar acts as the separator
        yield Static("", id="status-bar", classes="status-bar")
        yield Footer()
    
    def on_mount(self) -> None:
        """Set up the application when it first starts."""
        # Populate the categories list
        categories_list = self.query_one("#categories-list", ListView)
        
        # Create list items for each non-empty category in our standard order
        items = []
        for category in STANDARD_CATEGORIES:
            if category in self.categorized_settings and self.categorized_settings[category]:
                self.categories.append(category)
                items.append(ListItem(Label(category)))
        
        # Add "Other Settings" at the end if it has any items
        if "Other Settings" in self.categorized_settings and self.categorized_settings["Other Settings"]:
            self.categories.append("Other Settings")
            items.append(ListItem(Label("Other Settings")))
        
        # Add items one by one
        for item in items:
            categories_list.append(item)
        
        # Select the first category by default
        if self.categories:
            self.current_category = self.categories[0]
            self.update_table()
            
            # First select and focus the categories list to ensure proper highlighting
            categories_list.focus()
            if len(categories_list.children) > 0:
                # This will highlight the first item when we have focus
                categories_list.index = 0  # Set index to first item
            
            # Then move focus to the table, leaving the category highlighted
            table = self.query_one("#settings-table")
            table.focus()
            
            # Make sure the first row is highlighted in the table
            if table.row_count > 0:
                # Move cursor to first row
                table.move_cursor(row=0, column=0)
                # Trigger description update for the first row
                self.update_selected_row_description()
    
    def update_selected_row_description(self):
        """Update the description area based on the currently selected row in the table."""
        table = self.query_one("#settings-table")
        # Safety check - make sure we have rows and a valid cursor position
        if table.row_count > 0 and 0 <= table.cursor_row < table.row_count:
            # Get the actual row key at the current cursor position
            try:
                # Try to get row key from cursor position
                row_key = list(table.rows.keys())[table.cursor_row]
                row = table.get_row(row_key)
                
                # Update description area with the full description
                if row:
                    setting_key = str(row[0])
                    setting_value = str(row[1])
                    description = get_setting_description(setting_key)
                    
                    # Update description area
                    description_area = self.query_one("#description-area", DescriptionArea)
                    description_area.update_description(setting_key, setting_value, description)
            except (IndexError, KeyError):
                # Handle any issues gracefully
                pass
    
    def update_table(self):
        """Update the settings table with data from the current category."""
        if not self.current_category or self.current_category not in self.categorized_settings:
            return
        
        # Update section title
        section_title = self.query_one("#section-title", Static)
        section_title.update(f"Category: {self.current_category}")
        
        # Update table data
        table = self.query_one("#settings-table", SettingTable)
        category_settings = self.categorized_settings[self.current_category]
        table.update_category_settings(category_settings, self.current_category, self.show_all)
        
        # Update status bar with compact file path and author credit
        setting_count = len(table.rows)
        status_bar = self.query_one("#status-bar", Static)
        
        # Compact info with file path and subtle author credit
        status_msg = f" File: {self.config_path} [dim]• By Tiran Dagan[/dim]"
        status_bar.update(status_msg)
        
        # Clear description area
        description_area = self.query_one("#description-area", DescriptionArea)
        description_area.update_description()
        
        # Show description of first setting if available
        if table.row_count > 0:
            try:
                # Get the first row key
                first_row_key = list(table.rows.keys())[0]
                row = table.get_row(first_row_key)
                
                if row:
                    setting_key = str(row[0])
                    setting_value = str(row[1])
                    description = get_setting_description(setting_key)
                    description_area.update_description(setting_key, setting_value, description)
            except (IndexError, KeyError):
                # Handle case where row access fails
                pass
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle selection of a category in the list."""
        if isinstance(event.item, ListItem):
            # Find the index of the selected item
            list_view = self.query_one("#categories-list")
            items = list(list_view.children)
            if event.item in items:
                index = items.index(event.item)
                if 0 <= index < len(self.categories):
                    self.current_category = self.categories[index]
                    self.update_table()
                    
                    # Focus on the table after selecting a category
                    self.query_one("#settings-table").focus()
    
    def on_key(self, event: events.Key) -> None:
        """Handle key press events."""
        # Check if we're focused on the table and it's a navigation key
        if self.focused and self.focused.id == "settings-table":
            if event.key in ("up", "down", "j", "k", "home", "end", "page_up", "page_down"):
                # Let the key be processed normally
                event.prevent_default = False
                # Update the description area after a short delay to allow the cursor to move
                self.set_timer(0.05, self.update_selected_row_description)
            else:
                # Allow other keys to be processed normally
                event.prevent_default = False
    
    def action_focus_categories(self) -> None:
        """Focus on the categories list."""
        self.query_one("#categories-list").focus()
    
    def action_focus_settings(self) -> None:
        """Focus on the settings table."""
        self.query_one("#settings-table").focus()
    
    def action_next_setting(self) -> None:
        """Move to the next setting."""
        table = self.query_one("#settings-table")
        if table.cursor_row < len(table.rows) - 1:
            table.move_cursor(row_offset=1)
            self.update_selected_row_description()
    
    def action_prev_setting(self) -> None:
        """Move to the previous setting."""
        table = self.query_one("#settings-table")
        if table.cursor_row > 0:
            table.move_cursor(row_offset=-1)
            self.update_selected_row_description()
    
    def action_toggle_focus(self) -> None:
        """Toggle focus between categories and settings."""
        if self.focused.id == "categories-list":
            self.query_one("#settings-table").focus()
        else:
            self.query_one("#categories-list").focus()

    def action_show_values(self) -> None:
        """Show the valid values screen for the current setting."""
        # Get the current setting from the table
        table = self.query_one("#settings-table")
        
        # Make sure the table has focus and there are rows
        if table.row_count > 0 and 0 <= table.cursor_row < table.row_count:
            try:
                # Get the current row at cursor position
                row_key = list(table.rows.keys())[table.cursor_row]
                row = table.get_row(row_key)
                
                if row:
                    setting_key = str(row[0])
                    setting_value = str(row[1])
                    setting_values = get_setting_values(setting_key)
                    
                    # Show the values screen as a modal dialog
                    values_screen = SettingValuesScreen(setting_key, setting_value, setting_values)
                    self.app.push_screen(values_screen)
            except (IndexError, KeyError):
                # Handle any issues gracefully
                pass

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle selection of a setting in the table."""
        if event.row_key is None:
            return
            
        table = self.query_one("#settings-table")
        row = table.get_row(event.row_key)
        
        # Update description area with the full description
        if row:
            setting_key = str(row[0])
            setting_value = str(row[1])
            description = get_setting_description(setting_key)
            
            # Update description area
            description_area = self.query_one("#description-area", DescriptionArea)
            description_area.update_description(setting_key, setting_value, description)

class HelpScreen(Screen):
    """Help screen for the application."""
    
    BINDINGS = [
        Binding("escape", "app.pop_screen", "Back"),
        Binding("q", "app.pop_screen", "Back")
    ]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the help screen."""
        yield Static("JS8Call Configuration Viewer - Help", id="help-title")
        
        with ScrollableContainer():
            yield Static("""
Keyboard Shortcuts:
-----------------
[Tab]    - Toggle focus between categories and settings
[h]      - Focus on categories
[l]      - Focus on settings
[j]      - Move to next setting
[k]      - Move to previous setting
[Enter]  - Select item
[F1]     - Show/hide this help
[v]      - Show valid values for current setting
[q]      - Quit application

About this application:
---------------------
This tool displays JS8Call settings from your js8call.ini file with descriptions 
of what each setting does and how it affects JS8Call's behavior.

The left sidebar shows configuration categories, and the right panel displays 
the settings in the selected category.

By default, only documented settings are shown. If you launched with --all, 
all settings including undocumented ones will be shown.

The description area at the bottom shows detailed information about the 
currently selected setting.

Navigate with arrow keys or hjkl keys and select items with Enter.

Copyright and Attribution:
------------------------
© 2023-2024 Tiran Dagan (tiran@tirandagan.com)
All rights reserved.

This software is provided for educational and personal use only.
Redistribution requires written permission from the author.
            """, id="help-content")
        
        yield Button("Close", id="close-help")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "close-help":
            self.app.pop_screen()

class JS8CallConfigViewer(App):
    """Main application class."""
    
    CSS = """
    Screen {
        background: $surface;
    }
    
    #sidebar {
        width: 20%;
        border-right: solid $primary;
    }
    
    .sidebar-header {
        background: $accent;
        color: $text;
        text-align: center;
        text-style: bold;
        padding: 1;
    }
    
    #settings-area {
        width: 80%;
    }
    
    .section-title {
        background: $accent;
        color: $text;
        text-align: center;
        text-style: bold;
        padding: 1;
    }
    
    #settings-table {
        height: 100%;
        border: solid $primary;
    }
    
    /* Make the second column (Value) expand to fill space */
    .datatable--header-cell.column-1,
    .datatable--cell.column-1 {
        width: 1fr;
    }
    
    #table-container {
        height: 1fr;
    }
    
    #categories-list {
        border: none;
        padding: 0 1;
        background: $surface;
        height: 1fr;
    }
    
    .description-area {
        padding: 0 1;
        height: 3;
        background: $boost;
        color: $text;
        border-top: none;
    }
    
    .status-bar {
        padding: 0;
        background: $surface-lighten-1;
        color: $text;
        height: 1;
        border-top: solid $primary;
    }
    
    #help-title {
        background: $accent;
        color: $text;
        text-align: center;
        text-style: bold;
        padding: 1;
    }
    
    #help-content {
        padding: 1 2;
    }
    
    #close-help {
        margin: 1 0;
        dock: bottom;
        width: 20;
        align: center middle;
    }
    
    #values-dialog {
        width: 70%;
        height: 70%;
        border: solid $primary;
        background: $surface;
    }
    
    #values-title {
        background: $accent;
        color: $text;
        text-align: center;
        text-style: bold;
        padding: 1;
    }
    
    #values-content {
        padding: 1 2;
        height: 1fr;
        overflow-y: auto;
    }
    
    #values-footer {
        background: $surface-lighten-1;
        color: $text;
        text-align: center;
        padding: 1;
        border-top: solid $primary;
    }
    
    Header {
        height: 1;
        padding: 0;
    }
    
    Footer {
        height: 1;
        padding: 0;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("f1", "show_help", "Help"),
    ]
    
    def __init__(self, config_path=None, show_all=False):
        super().__init__()
        self.config_path = config_path
        self.show_all = show_all
    
    def on_mount(self) -> None:
        """Set up the application after it has been mounted."""
        # Load valid values for settings
        load_setting_values()
        
        # Read the config file
        result = read_js8call_ini(self.config_path)
        if result:
            config, config_path = result
            if config:
                self.push_screen(SettingsView(config, config_path, self.show_all))
            else:
                self.exit()
        else:
            self.exit()
    
    def action_show_help(self) -> None:
        """Show the help screen."""
        self.push_screen(HelpScreen())

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="JS8Call Configuration Viewer")
    parser.add_argument("-f", "--file", help="Path to JS8Call.ini file (auto-detected if not specified)")
    parser.add_argument("-a", "--all", action="store_true", help="Show all settings, including undocumented ones")
    args = parser.parse_args()
    
    # Run the app
    app = JS8CallConfigViewer(config_path=args.file, show_all=args.all)
    app.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting by user request.")
        sys.exit(0) 