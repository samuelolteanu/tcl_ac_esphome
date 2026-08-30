ESPHome external component for TCL (and TCL OEM) mini-split air conditioners, 
controlled directly via UART — no Tuya cloud, no IR blaster.

Replaces the stock TYWE1S/Tuya WiFi dongle with an ESP32 (tested on ESP32-S2/S3) 
connected directly to the indoor unit's JST UART port.

Features:
- Full climate entity: heat, cool, dry, fan, auto modes
- ECO and Turbo presets
- Variable fan speed (1-5, Mute, Automatic)
- Horizontal and vertical swing control
- Display on/off and beep control
- External temperature and humidity sensor support (sensor: / humidity_sensor:)
- No cloud dependency — fully local

Based on https://github.com/lNikazzzl/tcl_ac_esphome by lNikazzzl.
Fixes: dry/fan mode swap, eco readback, temperature rate limiter, 
deprecated API calls. Adds: external sensor wiring, display/beep switches,
humidity support.
