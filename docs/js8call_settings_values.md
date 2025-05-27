
# JS8Call Settings: Valid Values and Formats

## User Information Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **MyCall** | Valid amateur callsign (e.g., "W1AW", "G4ABC", "VK3XYZ") | Must follow international callsign standards; typically 3-6 characters with prefix and suffix |
| **MyGrid** | 4-6 character Maidenhead grid (e.g., "FN20", "IO91wm") | First 2 characters are letters A-R, second 2 are numbers 0-9, optional 5-6 are letters a-x |
| **MyGroups** | Comma-separated list (e.g., "ARES,RACES,SKCC") | Group names generally 1-10 alphanumeric characters; commas separate multiple groups |
| **MyInfo** | Free text string (e.g., "FT-991A 100W DIPOLE") | Limited by transmission constraints; typically keep under 50 characters |
| **MyStatus** | Free text with optional macros | Supports macros like `<MYIDLE>` (idle time), `<MYVERSION>` (JS8Call version); keep under 50 chars |
| **EOTCharacter** | Single Unicode character (e.g., "♢", "▣", "♥") | Any printable Unicode character; typically special symbols to indicate EOT |
| **MFICharacter** | Single or multiple Unicode characters (e.g., "……", ">>>") | Any printable Unicode character(s); typically indicates message continuation |

## Message Templates

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **CQMessage** | Text with optional macros (e.g., "CQ CQ CQ <MYGRID4>") | Supports macros like `<MYCALL>`, `<MYGRID>`, `<MYGRID4>`; typical length 5-30 chars |
| **HBMessage** | Text with optional macros (e.g., "HB <MYGRID4>") | Same macro support as CQ message; keep concise for efficient transmissions |
| **Reply** | Text with optional macros (e.g., "HW CPY?") | Same macro support; typically short phrases common in radio communications |

## Display Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **Font** | "Family,Size,Weight,Italic,Strikeout,Underline,StyleHint,Spacing,FixedPitch,Kerning" | Family: font name (e.g., "Arial")<br>Size: integer point size (8-14 typical)<br>Weight: integer 0-99 (50=normal, 75=bold)<br>Italic: boolean (0/1)<br>Strikeout: boolean (0/1)<br>Underline: boolean (0/1)<br>StyleHint: integer 0-5<br>Spacing: integer 0-3<br>FixedPitch: boolean (0/1)<br>Kerning: boolean (0/1) |
| **TableFont** | Same as Font format | Same parameters as main Font setting |
| **RXTextFont** | Same as Font format | Same parameters as main Font setting |
| **TXTextFont** | Same as Font format | Same parameters as main Font setting |
| **ComposeTextFont** | Same as Font format | Same parameters as main Font setting |

## Color Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **colorCQ** | Hex color code "#RRGGBB" (e.g., "#66ff66") | Web color format; R,G,B values in hex (00-FF) |
| **colorPrimary** | Hex color code "#RRGGBB" (e.g., "#f1c40f") | Web color format |
| **colorSecondary** | Hex color code "#RRGGBB" (e.g., "#ffff66") | Web color format |
| **colorMyCall** | Hex color code "#RRGGBB" (e.g., "#ff6666") | Web color format |
| **color_rx_background** | Hex color code "#RRGGBB" (e.g., "#ffeaa7") | Web color format |
| **color_rx_foreground** | Hex color code "#RRGGBB" (e.g., "#000000") | Web color format |
| **color_compose_background** | Hex color code "#RRGGBB" (e.g., "#ffffff") | Web color format |
| **color_compose_foreground** | Hex color code "#RRGGBB" (e.g., "#000000") | Web color format |
| **color_tx_foreground** | Hex color code "#RRGGBB" (e.g., "#ff0000") | Web color format |
| **colorDXCC** | Hex color code "#RRGGBB" (e.g., "#ff00ff") | Web color format |
| **colorNewCall** | Hex color code "#RRGGBB" (e.g., "#ffaaff") | Web color format |
| **colorTableBackground** | Hex color code "#RRGGBB" (e.g., "#ffffff") | Web color format |
| **colorTableHighlight** | Hex color code "#RRGGBB" (e.g., "#3498db") | Web color format |
| **colorTableForeground** | Hex color code "#RRGGBB" (e.g., "#000000") | Web color format |

## Behavior Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **AutoSwitchBands** | "true" or "false" | Boolean setting |
| **BeaconAnywhere** | "true" or "false" | Boolean setting |
| **HeartbeatQSOPause** | "true" or "false" | Boolean setting |
| **HeartbeatAckSNR** | "true" or "false" | Boolean setting |
| **SpotToAPRS** | "true" or "false" | Boolean setting |
| **WriteLogs** | "true" or "false" | Boolean setting |
| **ResetActivity** | "true" or "false" | Boolean setting |
| **CheckForUpdates** | "true" or "false" | Boolean setting |
| **dBtoComments** | "true" or "false" | Boolean setting |

## Automation Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **AutoWhitelist** | QStringList format (internal Qt storage) | List of valid callsigns, serialized by Qt; edit through UI |
| **AutoBlacklist** | QStringList format (internal Qt storage) | List of valid callsigns, serialized by Qt; edit through UI |
| **HBBlacklist** | QStringList format (internal Qt storage) | List of valid callsigns, serialized by Qt; edit through UI |
| **SpotBlacklist** | QStringList format (internal Qt storage) | List of valid callsigns, serialized by Qt; edit through UI |
| **AutoreplyConfirmation** | "true" or "false" | Boolean setting |
| **TransmitDirected** | "true" or "false" | Boolean setting |

## UI Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **HideControls** | "true" or "false" | Boolean setting |
| **ShowMenus** | "true" or "false" | Boolean setting |
| **ShowStatusbar** | "true" or "false" | Boolean setting |
| **ShowTooltips** | "true" or "false" | Boolean setting |
| **DisplayDecodeAttempts** | "true" or "false" | Boolean setting |
| **BandActivityVisible** | "true" or "false" | Boolean setting |
| **SplitState** | QByteArray (binary data, Base64 encoded) | Qt internal format for splitter positions; edit through UI only |
| **Geometry** | QByteArray (binary data, Base64 encoded) | Qt internal format for window geometry; edit through UI only |
| **GeometryNoControls** | QByteArray (binary data, Base64 encoded) | Qt internal format for window geometry; edit through UI only |
| **State** | QByteArray (binary data, Base64 encoded) | Qt internal format for window state; edit through UI only |

## Audio Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **SoundInName** | Device name string (e.g., "Microphone (USB Audio Device)") | Must match exact name of available audio input device |
| **SoundOutName** | Device name string (e.g., "Speakers (USB Audio Device)") | Must match exact name of available audio output device |
| **NotificationSoundOutName** | Device name string (e.g., "Speakers (Realtek High Definition Audio)") | Must match exact name of available audio output device |
| **AudioInputChannel** | Integer: 0=Mono, 1=Left, 2=Right | Channel selection for input audio |
| **AudioOutputChannel** | Integer: 0=Mono, 1=Left, 2=Right | Channel selection for output audio |
| **NotificationAudioOutputChannel** | Integer: 0=Mono, 1=Left, 2=Right | Channel selection for notifications |
| **OutAttenuation** | Integer: 0-100 (dB) | Attenuation value in decibels |
| **DefaultAudioInputDeviceSelected** | "true" or "false" | Boolean setting |
| **DefaultAudioOutputDeviceSelected** | "true" or "false" | Boolean setting |

## Waterfall Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **PlotZero** | Integer: typically -50 to 50 | Baseline reference level for waterfall |
| **PlotGain** | Integer: typically 0-100 | Gain/brightness control for waterfall |
| **Plot2dGain** | Integer: typically 0-100 | Gain control for 2D spectral plot |
| **Plot2dZero** | Integer: typically -50 to 50 | Baseline reference for 2D plot |
| **PlotWidth** | Integer: 500-5000 (pixels) | Width of waterfall in pixels |
| **BinsPerPixel** | Integer: 1-8 | Number of FFT bins per display pixel; lower = higher resolution |
| **SmoothYellow** | Integer: 0-10 | Smoothing factor for yellow trace line |
| **Percent2D** | Integer: 0-100 | Percentage of screen height for 2D display |
| **WaterfallAvg** | Integer: 1-10 | Number of frames to average in waterfall |
| **Current** | "true" or "false" | Boolean setting |
| **Cumulative** | "true" or "false" | Boolean setting |
| **LinearAvg** | "true" or "false" | Boolean setting |
| **Reference** | "true" or "false" | Boolean setting |
| **StartFreq** | Integer: 0-5000 (Hz) | Starting frequency for waterfall display |
| **CenterOffset** | Integer: 500-2500 (Hz) | Center frequency offset (typically ~1500Hz) |
| **WaterfallPalette** | String: "Default", "Fldigi", "Blue", "Digipan", "Gray", "Gray2", "Scope", "User" | Name of predefined palette or "User" for custom |
| **WaterfallFPS** | Integer: 1-100 | Frames per second for waterfall updates; typical 2-25 |
| **FilterEnabled** | "true" or "false" | Boolean setting |
| **FilterMinimum** | Integer: 0-5000 (Hz) | Lower boundary for filter in Hz |
| **FilterMaximum** | Integer: 0-5000 (Hz) | Upper boundary for filter in Hz |
| **FilterOpacityPercent** | Integer: 0-100 | Opacity percentage for filter visualization |
| **UserPalette** | QVariant (complex serialized object) | Custom palette colors; edit through UI only |

## Radio Interface Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **PTTMethod** | Integer: 0=VOX, 1=CAT, 2=DTR, 3=RTS, 4=GPIO, 5=Command | Method used for transmit control |
| **PTTCommand** | Text string: system command | Command line to execute for PTT; format depends on OS |
| **RigName** | Text string (e.g., "Hamlib NET rigctl", "Kenwood TS-2000") | Must match a supported transceiver in program |
| **SplitMode** | Integer: 0=None, 1=Rig, 2=Fake | Method for handling split operation |
| **FreqTxOffset** | Integer: Hz offset (e.g., -1500 to +1500) | TX offset from RX frequency in Hz |
| **PTT_PORT** | Text string: port name (e.g., "COM3", "/dev/ttyS0") | Valid system COM/serial port name |
| **CAT_PORT** | Text string: port name (e.g., "COM4", "/dev/ttyS1") | Valid system COM/serial port name |
| **CAT_SERIAL_BAUD** | Integer: standard baud rate (e.g., 4800, 9600, 19200, 38400, 57600, 115200) | Must match radio's supported baud rate |
| **CAT_DATA_BITS** | Integer: 7 or 8 | Data bits for serial communication |
| **CAT_STOP_BITS** | Integer: 1 or 2 | Stop bits for serial communication |
| **CAT_HANDSHAKE** | Integer: 0=None, 1=XON/XOFF, 2=Hardware | Handshaking method for serial port |
| **CAT_POLL_INTERVAL** | Integer: milliseconds (typically 500-2000) | Time between CAT polling commands |
| **FORCE_DTR** | Integer: 0=None, 1=On, 2=Off | Force DTR line state |
| **FORCE_RTS** | Integer: 0=None, 1=On, 2=Off | Force RTS line state |

## Network and Reporting Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **UDP_SERVER_NAME** | Text string: hostname or IP (e.g., "localhost", "192.168.1.5") | Valid hostname or IPv4 address |
| **UDP_SERVER_PORT** | Integer: 1-65535 | Valid network port number |
| **TCP_SERVER_NAME** | Text string: hostname or IP (e.g., "localhost", "192.168.1.5") | Valid hostname or IPv4 address |
| **TCP_SERVER_PORT** | Integer: 1-65535 | Valid network port number |
| **N3FJP_SERVER_NAME** | Text string: hostname or IP (e.g., "localhost") | Valid hostname or IPv4 address |
| **N3FJP_SERVER_PORT** | Integer: 1-65535 | Valid network port number |
| **BroadcastToN3FJP** | "true" or "false" | Boolean setting |
| **N1MM_SERVER_NAME** | Text string: hostname or IP (e.g., "localhost") | Valid hostname or IPv4 address |
| **N1MM_SERVER_PORT** | Integer: 1-65535 | Valid network port number |
| **BroadcastToN1MM** | "true" or "false" | Boolean setting |
| **AcceptUDPRequests** | "true" or "false" | Boolean setting |
| **AcceptTCPRequests** | "true" or "false" | Boolean setting |
| **UDPEnabled** | "true" or "false" | Boolean setting |
| **TCPEnabled** | "true" or "false" | Boolean setting |
| **TCPMaxConnections** | Integer: 1-20 | Maximum number of simultaneous TCP connections |
| **SpotToReportingNetworks** | "true" or "false" | Boolean setting |
| **AprsServerName** | Text string (e.g., "rotate.aprs2.net") | Valid APRS-IS server hostname |
| **AprsServerPort** | Integer: typically 14580 | APRS-IS port number |

## Decode Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **Decode52** | "true" or "false" | Boolean setting |
| **SingleDecode** | "true" or "false" | Boolean setting |
| **TwoPass** | "true" or "false" | Boolean setting |
| **StopAutoSyncOnDecode** | "true" or "false" | Boolean setting |
| **StopAutoSyncAfter** | Integer: 1-10 | Number of successful decodes before stopping auto-sync |
| **QuickDecode** | "true" or "false" | Boolean setting |
| **DeepDecode** | "true" or "false" | Boolean setting |
| **DecodingDrift** | Integer: 0-100 (Hz) | Maximum drift to compensate for in Hz |
| **Aggressive** | Integer: 0-10 | Aggressive decoding level; higher = more aggressive |
| **Ntrials** | Integer: 1-10000 | Number of decode attempts; typically 100-1000 |

## Heartbeat/Auto Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **HeartbeatInterval** | Integer: minutes (typically 10-60) | Time between automatic heartbeats |
| **HeartbeatAcknowledgements** | "true" or "false" | Boolean setting |
| **AutoreplyOnAtStartup** | "true" or "false" | Boolean setting |
| **ID_interval** | Integer: minutes (typically 5-30) | Time between automatic identifications |
| **CallsignAging** | Integer: minutes (typically 30-1440) | Time before calls age out of display |
| **ActivityAging** | Integer: minutes (typically 10-1440) | Time before activity ages out of display |

## Special Mode Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **Fox** | "true" or "false" | Boolean setting |
| **Hound** | "true" or "false" | Boolean setting |
| **x2ToneSpacing** | "true" or "false" | Boolean setting |
| **x4ToneSpacing** | "true" or "false" | Boolean setting |

## Notification Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **EnableNotifications** | "true" or "false" | Boolean setting |
| **NotificationsEnabled/[type]** | "true" or "false" | Boolean setting for specific notification type |
| **NotificationsPath/[type]** | Text string: file path (e.g., "C:\\Sounds\\alert.wav") | Valid path to .wav sound file |

## Advanced Settings

| Setting | Valid Values/Format | Description |
|---------|-------------------|-------------|
| **CalibrationIntercept** | Double: Hz offset (e.g., -125.0 to +125.0) | Frequency calibration offset in Hz |
| **CalibrationSlopePPM** | Double: PPM value (e.g., -100.0 to +100.0) | Frequency calibration slope in parts per million |
| **TXLockAllowed** | "true" or "false" | Boolean setting |
| **DataMode** | Integer: mode identifier | Mode variant identifier; best set through UI |
| **FminPerBand** | QHash (complex serialized object) | Qt serialized hash of minimum frequencies; edit through UI |
| **FrequenciesForRegionModes** | QHash (complex serialized object) | Qt serialized hash of frequencies; edit through UI |
| **HoldPTT** | "true" or "false" | Boolean setting |
| **MultiSettingsCurrentConfiguration** | Text string (profile name) | Name of currently active settings profile |
| **FFTSize** | Integer: power of 2 (e.g., 512, 1024, 2048, 4096, 8192, 16384) | FFT size for signal processing |
| **RxBandwidth** | Integer: Hz (typically 500-2500) | Receiver bandwidth in Hz |
| **Degrade** | Double: 0.0-1.0 | Audio quality degradation factor for testing |
| **TxDelay** | Double: seconds (e.g., 0.0-2.0) | Delay before transmit starts |
| **SaveDirectory** | Text string: directory path | Valid system directory path |
| **TimeDrift** | Double: seconds | System clock drift compensation in seconds |
| **VHFUHF** | "true" or "false" | Boolean setting |
| **ModeMultiDecoder** | "true" or "false" | Boolean setting |
| **ModeAutoreply** | "true" or "false" | Boolean setting |
| **ModeJS8HB** | "true" or "false" | Boolean setting |
| **PrimaryHighlightWords** | QStringList format (internal Qt storage) | List of words to highlight; edit through UI |
| **SecondaryHighlightWords** | QStringList format (internal Qt storage) | List of words to highlight; edit through UI |
| **Type2MsgGen** | Integer: 0-2 | Type 2 message generation method; best set through UI |

These valid values should help when manually editing the js8call.ini file. For complex data types (QByteArray, QStringList, QHash, QVariant), it's strongly recommended to use the JS8Call interface rather than directly editing these values, as they use Qt's internal serialization format which can be difficult to edit correctly by hand.
