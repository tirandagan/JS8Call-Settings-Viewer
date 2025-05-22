# JS8Call Settings in js8call.ini

JS8Call uses QSettings to store configuration in an .ini file named after the application, which would be js8call.ini.

# JS8Call.ini File Locations

The js8call.ini file is stored in different standard locations depending on your operating system:

## Windows

```text
%APPDATA%\JS8Call\js8call.ini
```
This typically resolves to:

```text
C:\Users\<username>\AppData\Roaming\JS8Call\js8call.ini
```
## Linux

```text
~/.config/JS8Call/js8call.ini
```
This expands to:

```text
/home/<username>/.config/JS8Call/js8call.ini
```
## macOS

```text
~/Library/Preferences/JS8Call/js8call.ini
```
This expands to:

```text
/Users/<username>/Library/Preferences/JS8Call/js8call.ini
```
Note: On all platforms, the directory and file will be created automatically when you first run JS8Call. If you need to edit the file manually, ensure JS8Call is completely closed before making changes.


# JS8Call Settings: Comprehensive Reference Table
Here's a comprehensive list of settings organized by category:


# JS8Call Settings: Comprehensive Reference Table with Formats

## User Information Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **MyCall** | Text String | Your amateur radio callsign | Used in all communications; key identifier for your station | Must be valid callsign format; changing mid-operation can confuse stations in QSO with you |
| **MyGrid** | Text String (4-6 chars) | Your Maidenhead grid locator | Used for distance calculations and location reporting | Should be accurate for proper distance calculations; 4-6 character format |
| **MyGroups** | Comma-separated List | Groups you belong to for directed messages | Controls which group messages you'll receive | Comma-separated list; limited to valid group names |
| **MyInfo** | Text String | Your station information (equipment, etc.) | Shared when stations query your info | Limited to reasonable text length for transmission |
| **MyStatus** | Text String | Status message shown to others | Automatically shared in heartbeats and responses | Supports macros like `<MYIDLE>`, `<MYVERSION>`; length affects transmission time |
| **EOTCharacter** | Single Character | End of transmission character | Visual indicator for message completion | Default is "♢"; changing may confuse operators familiar with standard |
| **MFICharacter** | Character(s) | Message fragment indicator | Shows when message continuation follows | Default is "……"; changing may confuse operators familiar with standard |

## Message Templates

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **CQMessage** | Text String | Template used for CQ calls | Sets your standard CQ message format | Supports macros like `<MYGRID4>`; keep reasonably short for better responses |
| **HBMessage** | Text String | Template for heartbeat messages | Format for automatic heartbeats | Should generally include your grid for location awareness |
| **Reply** | Text String | Default reply text | Pre-populated when using quick reply | Keep short and standardized (default "HW CPY?" is widely understood) |

## Display Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **Font** | "Family,Size,Weight,Italic,Strikeout,Underline,StyleHint,Spacing,FixedPitch,Kerning" | Controls text display throughout app | Affects readability and UI layout | Very large fonts may cause UI display issues |
| **TableFont** | Same as Font format | Font for activity tables | Affects readability of call tables | Should balance between readability and information density |
| **RXTextFont** | Same as Font format | Font for received text | Affects readability of messages | Monospace fonts often work best for signal reports and alignment |
| **TXTextFont** | Same as Font format | Font for transmitted text | Affects readability of sent messages | Typically matches RX font for consistency |
| **ComposeTextFont** | Same as Font format | Font for message composition area | Affects typing experience | Choose based on personal preference for typing comfort |

## Color Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **colorCQ** | Hex Color "#RRGGBB" | Color for CQ messages | Makes CQ calls visually distinct | Choose high-contrast colors for visibility |
| **colorPrimary** | Hex Color "#RRGGBB" | Primary highlight color | Used for key highlighting | Should be distinct from normal text for visibility |
| **colorSecondary** | Hex Color "#RRGGBB" | Secondary highlight color | Used for less important highlights | Should contrast with background but not compete with primary |
| **colorMyCall** | Hex Color "#RRGGBB" | Color for your callsign | Makes references to your call stand out | Choose a bright, attention-grabbing color |
| **color_rx_background** | Hex Color "#RRGGBB" | RX window background color | Affects message readability | Light colors typically work best for readability |
| **color_rx_foreground** | Hex Color "#RRGGBB" | RX text color | Core readability factor | Should have strong contrast with background |
| **color_compose_background** | Hex Color "#RRGGBB" | Compose window background | Affects typing comfort | Neutral colors reduce eye strain during long operations |
| **color_compose_foreground** | Hex Color "#RRGGBB" | Compose window text color | Affects typing experience | High contrast with background is important |
| **color_tx_foreground** | Hex Color "#RRGGBB" | TX text color | Visually separates transmitted text | Red is traditional but any high-contrast color works |
| **colorDXCC** | Hex Color "#RRGGBB" | Color for DXCC entities | Highlights rare or needed countries | Distinct color helps identify important DX |
| **colorNewCall** | Hex Color "#RRGGBB" | Color for new calls | Highlights stations not worked before | Choose a noticeable but not distracting color |
| **colorTableBackground** | Hex Color "#RRGGBB" | Table background color | Affects overall UI appearance | Light colors typically work best for readability |
| **colorTableHighlight** | Hex Color "#RRGGBB" | Selected row highlight | Indicates current selection | Should be distinct but not harsh |
| **colorTableForeground** | Hex Color "#RRGGBB" | Table text color | Affects readability of tables | High contrast with table background is essential |

## Behavior Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **AutoSwitchBands** | Boolean ("true"/"false") | Auto-switches bands based on config | Can automate band changes | May interfere with manual frequency control if enabled |
| **BeaconAnywhere** | Boolean ("true"/"false") | Allow heartbeat anywhere in band | Controls where heartbeats are sent | Enabling may cause interference if not careful |
| **HeartbeatQSOPause** | Boolean ("true"/"false") | Pause heartbeat during active QSOs | Prevents interrupting ongoing contacts | Disabling may cause your heartbeat to transmit during conversations |
| **HeartbeatAckSNR** | Boolean ("true"/"false") | Include SNR in heartbeat acknowledgments | Adds signal report to HB responses | Slightly increases message length |
| **SpotToAPRS** | Boolean ("true"/"false") | Send spots to APRS network | Shares station spots via APRS | Requires properly configured APRS settings |
| **WriteLogs** | Boolean ("true"/"false") | Save log files of contacts and activity | Controls record keeping | Disabling means activity not saved permanently |
| **ResetActivity** | Boolean ("true"/"false") | Clear activity display on start | Starts with clean display each launch | Historical information lost if enabled |
| **CheckForUpdates** | Boolean ("true"/"false") | Check for JS8Call updates | Controls auto-update checking | Disabling may leave you on older versions with bugs |
| **dBtoComments** | Boolean ("true"/"false") | Include signal reports in comments | Adds SNR to logged comments | Makes logs more detailed but longer |

## Automation Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **AutoWhitelist** | QStringList (internal format) | Callsigns allowed auto-responses | Controls automatic replies | Too many entries might cause unwanted automatic behavior |
| **AutoBlacklist** | QStringList (internal format) | Callsigns blocked from auto features | Prevents automatic responses | Useful for problematic stations but check entries carefully |
| **HBBlacklist** | QStringList (internal format) | Calls excluded from heartbeat features | Prevents HB interactions with specific stations | Use for stations sending excessive heartbeats |
| **SpotBlacklist** | QStringList (internal format) | Calls excluded from spotting | Won't report these stations to networks | Use for stations you don't want to contribute to spotting |
| **AutoreplyConfirmation** | Boolean ("true"/"false") | Prompt before automatic replies | Controls auto response behavior | Disabling removes safeguard against unwanted transmissions |
| **TransmitDirected** | Boolean ("true"/"false") | Enables auto-replies to directed messages | Controls whether directed messages trigger responses | Disabling requires manual replies to all messages |

## UI Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **HideControls** | Boolean ("true"/"false") | Show/hide waterfall controls | Affects UI space utilization | Hiding increases waterfall size but restricts easy adjustments |
| **ShowMenus** | Boolean ("true"/"false") | Display menu bars | Controls access to menu functions | Hiding saves space but limits feature access |
| **ShowStatusbar** | Boolean ("true"/"false") | Show status bar | Controls visibility of status information | Hiding saves space but limits status visibility |
| **ShowTooltips** | Boolean ("true"/"false") | Display tooltips | Controls help pop-ups | Useful for learning program; experienced users may disable |
| **DisplayDecodeAttempts** | Boolean ("true"/"false") | Show decode attempts in waterfall | Shows where decoder is working | Can be distracting but useful for debugging |
| **BandActivityVisible** | Boolean ("true"/"false") | Show band activity panel | Controls primary activity display | Essential panel for normal operation |
| **SplitState** | QByteArray (binary) | Window splitter positions | Controls panel sizing | Affects screen space allocation between components |
| **Geometry** | QByteArray (binary) | Window size and position | Controls application window | May need adjustment after display changes |
| **GeometryNoControls** | QByteArray (binary) | Window layout without controls | Alternative layout setting | Used when controls are hidden |
| **State** | QByteArray (binary) | Window state information | Controls window maximized/normal state | May affect visibility on different screens |

## Audio Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **SoundInName** | Text String | Audio input device | Controls which device captures audio | Must match functioning audio input device |
| **SoundOutName** | Text String | Audio output device | Controls which device outputs audio | Must match functioning audio output device |
| **NotificationSoundOutName** | Text String | Device for notifications | Controls alert sounds | Can be same as or different from main audio output |
| **AudioInputChannel** | Integer (0=Mono, 1=Left, 2=Right) | Input audio channel selection | Controls which channel is used for input | Must match your interface setup |
| **AudioOutputChannel** | Integer (0=Mono, 1=Left, 2=Right) | Output audio channel selection | Controls which channel is used for output | Must match your interface configuration |
| **NotificationAudioOutputChannel** | Integer (0=Mono, 1=Left, 2=Right) | Channel for notification sounds | Controls which channel notification sounds use | Independent from main audio output channel |
| **OutAttenuation** | Integer (dB) | Output audio level adjustment | Controls transmit audio level | Setting too high may cause overmodulation |
| **DefaultAudioInputDeviceSelected** | Boolean ("true"/"false") | Flag for default input device | Determines if system default is used | System may change default device unexpectedly |
| **DefaultAudioOutputDeviceSelected** | Boolean ("true"/"false") | Flag for default output device | Determines if system default is used | System may change default device unexpectedly |

## Waterfall Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **PlotZero** | Integer | Zero reference for waterfall | Affects display baseline | Adjust for optimal signal visibility |
| **PlotGain** | Integer | Gain for waterfall display | Controls signal visibility/contrast | Higher values show weaker signals but increase noise |
| **Plot2dGain** | Integer | Gain for 2D plot | Controls 2D display sensitivity | Balance between seeing signals and noise |
| **Plot2dZero** | Integer | Zero reference for 2D plot | Affects 2D display baseline | Adjust to center signals in display |
| **PlotWidth** | Integer (pixels) | Width of waterfall plot | Controls frequency range displayed | Wider shows more band, narrower shows more detail |
| **BinsPerPixel** | Integer | Frequency bins per screen pixel | Controls spectral resolution | Lower values show more detail but narrow frequency range |
| **SmoothYellow** | Integer | Smoothing for yellow trace | Affects trace appearance | Higher values smooth display but may hide fast changes |
| **Percent2D** | Integer (0-100) | Screen percentage for 2D display | Controls space allocation | Balance between waterfall and 2D display |
| **WaterfallAvg** | Integer | Waterfall averaging | Controls smoothness of display | Higher values smooth noise but slow response to changes |
| **Current** | Boolean ("true"/"false") | Show current trace | Controls trace visibility | Helps identify immediate signals |
| **Cumulative** | Boolean ("true"/"false") | Use cumulative display | Controls signal persistence | Shows history of signals |
| **LinearAvg** | Boolean ("true"/"false") | Use linear averaging | Changes averaging algorithm | Affects how signals blend over time |
| **Reference** | Boolean ("true"/"false") | Use reference trace | Shows reference for comparison | Useful for comparing signal conditions |
| **StartFreq** | Integer (Hz) | Starting frequency | Controls displayed frequency range | Should match your operating segment |
| **CenterOffset** | Integer (Hz) | Center frequency offset | Controls display centering | Adjust to center your operating frequency |
| **WaterfallPalette** | Text String | Color scheme for waterfall | Affects signal visualization | Choose based on personal preference and visibility |
| **WaterfallFPS** | Integer (1-100) | Frames per second | Controls display update rate | Higher values smoother but more CPU intensive |
| **FilterEnabled** | Boolean ("true"/"false") | Enable frequency filter | Controls filtering of display | Helps focus on specific frequency ranges |
| **FilterMinimum** | Integer (Hz) | Lower filter boundary | Sets low frequency limit | Adjust to match mode bandwidth |
| **FilterMaximum** | Integer (Hz) | Upper filter boundary | Sets high frequency limit | Adjust to match mode bandwidth |
| **FilterOpacityPercent** | Integer (0-100) | Filter visibility | Controls filter visual strength | Higher values make filter more prominent |
| **UserPalette** | QVariant (complex) | Custom waterfall palette colors | Controls waterfall appearance | Personal preference for signal visibility |

## Radio Interface Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **PTTMethod** | Integer (0-5) | Method used for transmit control | Controls how radio keying works | Must match your radio interface setup |
| **PTTCommand** | Text String | Command used for PTT | Used for custom PTT scripts | Requires proper command syntax for your system |
| **RigName** | Text String | Selected radio model | Sets parameters for CAT control | Must match actual radio for proper control |
| **SplitMode** | Integer (0-2) | TX/RX frequency relationship | Controls split operation | Affects how TX frequency is determined |
| **FreqTxOffset** | Integer (Hz) | TX offset from RX frequency | Sets split operation parameters | Used for working DX split operations |
| **PTT_PORT** | Text String | PTT serial port designation | Controls which port is used for PTT | Must match hardware configuration |
| **CAT_PORT** | Text String | CAT serial port designation | Controls which port is used for rig control | Must match radio control port |
| **CAT_SERIAL_BAUD** | Integer | CAT port baud rate | Sets communication speed with radio | Must match radio's baud rate setting |
| **CAT_DATA_BITS** | Integer (7-8) | Number of data bits for CAT | Sets data format for radio communication | Typically 8; must match radio setting |
| **CAT_STOP_BITS** | Integer (1-2) | Number of stop bits for CAT | Sets data format for radio communication | Usually 1 or 2; must match radio setting |
| **CAT_HANDSHAKE** | Integer (0-2) | CAT handshaking method | Controls flow control for radio interface | Must match radio configuration |
| **CAT_POLL_INTERVAL** | Integer (milliseconds) | Time between CAT polling | Controls how often radio is polled | Lower values more responsive but increase traffic |
| **FORCE_DTR** | Integer (0-2) | DTR line control | Forces DTR line state | May be needed for some interfaces |
| **FORCE_RTS** | Integer (0-2) | RTS line control | Forces RTS line state | May be needed for some interfaces |

## Network and Reporting Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **UDP_SERVER_NAME** | Text String | UDP server address | Controls where UDP data is sent | Must be valid hostname or IP |
| **UDP_SERVER_PORT** | Integer | UDP server port | Controls UDP connection port | Should be available and not blocked by firewall |
| **TCP_SERVER_NAME** | Text String | TCP server address | Controls where TCP data is sent | Must be valid hostname or IP |
| **TCP_SERVER_PORT** | Integer | TCP server port | Controls TCP connection port | Should be available and not blocked by firewall |
| **N3FJP_SERVER_NAME** | Text String | N3FJP logger address | Controls connection to N3FJP logging software | Must match N3FJP configuration |
| **N3FJP_SERVER_PORT** | Integer | N3FJP logger port | Sets port for N3FJP connection | Must match N3FJP port setting |
| **BroadcastToN3FJP** | Boolean ("true"/"false") | Enable N3FJP logging | Controls if contacts are sent to N3FJP | Requires running N3FJP software |
| **N1MM_SERVER_NAME** | Text String | N1MM logger address | Controls connection to N1MM logging software | Must match N1MM configuration |
| **N1MM_SERVER_PORT** | Integer | N1MM logger port | Sets port for N1MM connection | Must match N1MM port setting |
| **BroadcastToN1MM** | Boolean ("true"/"false") | Enable N1MM logging | Controls if contacts are sent to N1MM | Requires running N1MM software |
| **AcceptUDPRequests** | Boolean ("true"/"false") | Allow incoming UDP | Controls if external UDP commands are accepted | Security risk if exposed to internet |
| **AcceptTCPRequests** | Boolean ("true"/"false") | Allow incoming TCP | Controls if external TCP commands are accepted | Security risk if exposed to internet |
| **UDPEnabled** | Boolean ("true"/"false") | Enable UDP server | Allows external UDP control | Security risk if exposed to internet |
| **TCPEnabled** | Boolean ("true"/"false") | Enable TCP server | Allows external TCP control | Security risk if exposed to internet |
| **TCPMaxConnections** | Integer | Maximum TCP connections | Controls multiple connections | Higher values allow more clients but use resources |
| **SpotToReportingNetworks** | Boolean ("true"/"false") | Send spots to networks | Controls automatic reporting | Increases internet traffic; may reveal operation |
| **AprsServerName** | Text String | APRS server hostname | Controls APRS reporting | Must be valid APRS-IS server |
| **AprsServerPort** | Integer | APRS server port | Sets connection port | Typically 14580 for standard APRS-IS |

## Decode Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **Decode52** | Boolean ("true"/"false") | Decode at 52s timing | Controls decode timing | Useful for some propagation conditions |
| **SingleDecode** | Boolean ("true"/"false") | Use single decode pass | Controls decode thoroughness | Faster but may miss signals |
| **TwoPass** | Boolean ("true"/"false") | Use two-pass decoding | Controls decode algorithm | More thorough but uses more CPU |
| **StopAutoSyncOnDecode** | Boolean ("true"/"false") | Stop auto sync after success | Controls drift correction behavior | Balances between stability and adapting to changing drift |
| **StopAutoSyncAfter** | Integer | Decodes before stopping sync | Controls auto-sync duration | Higher values track drift longer |
| **QuickDecode** | Boolean ("true"/"false") | Use fast decode algorithm | Controls decode thoroughness | Faster but less sensitive |
| **DeepDecode** | Boolean ("true"/"false") | Use thorough decoding | Controls decode sensitivity | Slower but can find weaker signals |
| **DecodingDrift** | Integer (Hz) | Amount of drift compensation | Controls how much drift is automatically corrected | Higher values track more drift but may cause false decodes |
| **Aggressive** | Integer (0-10) | Aggressive decoding level | Controls decode sensitivity | Higher values may produce false decodes |
| **Ntrials** | Integer | Number of decode attempts | Controls decode thoroughness | Higher values more thorough but slower |

## Heartbeat/Auto Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **HeartbeatInterval** | Integer (minutes) | Time between automatic heartbeats | Controls HB frequency | More frequent uses more airtime; less frequent reduces visibility |
| **HeartbeatAcknowledgements** | Boolean ("true"/"false") | Enable automatic HB responses | Controls automatic replies | Enabling increases transmissions but improves network functionality |
| **AutoreplyOnAtStartup** | Boolean ("true"/"false") | Start with autoreply active | Controls initial autoreply state | May cause immediate transmissions after startup |
| **ID_interval** | Integer (minutes) | Station identification frequency | Controls automatic ID | Must comply with regulatory requirements |
| **CallsignAging** | Integer (minutes) | Time before calls age out | Controls station list management | Shorter times keep list current; longer remembers more stations |
| **ActivityAging** | Integer (minutes) | Time before activity ages out | Controls message aging | Balances between history and clutter |

## Special Mode Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **Fox** | Boolean ("true"/"false") | Fox mode for contesting | Special contesting mode | Not for normal operation; special purpose only |
| **Hound** | Boolean ("true"/"false") | Hound mode for contesting | Special contesting mode | Not for normal operation; special purpose only |
| **x2ToneSpacing** | Boolean ("true"/"false") | Use 2x tone spacing | Changes signal bandwidth | Uses more bandwidth but can improve decoding in poor conditions |
| **x4ToneSpacing** | Boolean ("true"/"false") | Use 4x tone spacing | Changes signal bandwidth | Uses much more bandwidth but most resistant to interference |

## Notification Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **EnableNotifications** | Boolean ("true"/"false") | Master toggle for notifications | Controls all alerts | Disabling silences all notifications |
| **NotificationsEnabled/[type]** | Boolean ("true"/"false") | Per-event notification toggle | Controls specific notification | Configure to alert for important events only |
| **NotificationsPath/[type]** | Text String (file path) | Sound file for notification | Sets sound for specific notification | Must be valid audio file path |

## Advanced Settings

| Setting | Format | Explanation | Impact of Changes | Limits & Warnings |
|---------|--------|-------------|-------------------|-------------------|
| **CalibrationIntercept** | Double (Hz) | Frequency calibration offset | Corrects for radio frequency error | Must be accurately set for proper frequency alignment |
| **CalibrationSlopePPM** | Double (parts per million) | Frequency calibration slope | Corrects frequency error across spectrum | Must be accurately calculated for proper operation |
| **TXLockAllowed** | Boolean ("true"/"false") | Allow TX frequency changes | Controls if TX frequency can be changed during operation | Disabling prevents accidental frequency changes |
| **DataMode** | Integer | Digital mode variant | Controls modulation specifics | Should match operating practice |
| **FminPerBand** | QHash (complex) | Minimum frequencies per band | Controls band edge limits | Should comply with license privileges |
| **FrequenciesForRegionModes** | QHash (complex) | Stored frequencies by region/mode | Controls band memories | Used for frequency management |
| **HoldPTT** | Boolean ("true"/"false") | Keep PTT active between transmissions | Controls PTT behavior | Can reduce wear on PTT relay but keeps radio in transmit mode |
| **MultiSettingsCurrentConfiguration** | Text String | Active settings profile | Controls which settings profile is used | Changing manually may cause unexpected behavior |
| **FFTSize** | Integer (power of 2) | FFT size for signal processing | Controls spectral resolution | Larger values provide better frequency resolution but use more CPU |
| **RxBandwidth** | Integer (Hz) | Receiver bandwidth | Controls receive filtering | Must match mode and conditions |
| **Degrade** | Double (0.0-1.0) | Audio quality degradation for testing | Simulates poor conditions | For testing only; don't enable for normal operation |
| **TxDelay** | Double (seconds) | Delay before transmit starts | Allows radio to fully key up | Too short may clip transmissions; too long wastes time |
| **SaveDirectory** | Text String (directory path) | Location for audio recordings | Controls where recordings are saved | Should be a valid, writable directory path |
| **TimeDrift** | Double (seconds) | System clock drift compensation | Adjusts for computer clock error | Critical for accurate timing |
| **VHFUHF** | Boolean ("true"/"false") | Enable VHF/UHF features | Optimizes for VHF/UHF propagation | Use only when operating on VHF/UHF bands |
| **ModeMultiDecoder** | Boolean ("true"/"false") | Run multiple decoders simultaneously | Controls decoding approach | Uses more CPU but can decode different speeds simultaneously |
| **ModeAutoreply** | Boolean ("true"/"false") | Controls automatic reply behavior | Sets reply automation | Can cause transmissions without user action |
| **ModeJS8HB** | Boolean ("true"/"false") | Heartbeat mode | Controls heartbeat behavior | Enables/disables automatic heartbeats |
| **PrimaryHighlightWords** | QStringList (internal format) | Words to highlight with primary color | Controls highlighting of key terms | Use for important terms you want to stand out |
| **SecondaryHighlightWords** | QStringList (internal format) | Words to highlight with secondary color | Controls secondary term highlighting | Use for moderately important terms |
| **Type2MsgGen** | Integer | Type 2 message generation method | Controls message encoding | Technical setting affecting JS8 protocol behavior |

The format descriptions clarify how each setting is stored in the js8call.ini file. For complex types like QVariant, QByteArray, QHash, and QStringList, these are stored in Qt's internal serialization format and are best modified through the JS8Call interface rather than direct file editing.
