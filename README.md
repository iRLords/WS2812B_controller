# WS2812B controller

https://user-images.githubusercontent.com/98465015/188142102-1b7b7e8c-dafe-4060-b73c-ec3a2519e3c3.mov

- You can control your WS2812B (RGB LED) color from the web using this code.
- **[click here for connect to author](https://t.me/Soltan_Python)**

# connections

![WS2812B_breadboard](https://user-images.githubusercontent.com/98465015/188141833-36c2cad2-ee91-4da7-b39d-b791c5c6f51c.png)


|ESP8266        |WS2812B    |
|---            | ---       |
|GPIO14(D5)     |IN         |
|3v3            |VCC        |
|GND            |GND        |

- connect the Pin 14 to input pin of WS2812B and 3v3 to VCC and GND to GND

# settings
- open the `config.py` file and fill out of all variables
- For example: line _4_ `matrix` value is `16`, if my WS2812B has 8 LEDs, I put `8` instead of `16`.
- and your SSID of wifi is your wifi name

Good Luck ;)
