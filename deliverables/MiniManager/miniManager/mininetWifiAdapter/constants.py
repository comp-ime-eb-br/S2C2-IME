class MininetConstants:
    UPDATE = "UPDATE"
    ERROR = "ERROR"
    FINISH = "FINISH"
    START = "START"

    RADIO_FREQUENCY_KEY = "radioFrequency"
    PERFORMANCE_KEY = "performance"
    ERROR_KEY = "error"
    TIME_KEY = "time"
    POSITIONS_KEY = "positions"

    CONFIG_FILE_PATH = 'mininetWifiAdapter/config.json'
    #CONFIG_FILE_PATH = 'config.json'

    RADIO_FREQUENCY_MEASURES = {'name', 'rssi','channel','band','ssid','txpower','ip', 'position', 'associatedto'}
    PERFORMANCE_MEASURES = {'ping', 'Iperf'}

    DELAY = 1
