# WS2812B controller
- You can control your WS2812B (RGB LED) color from the web using this code.
- **[click here for connect to author](https://t.me/Soltan_Python)**

# connections
![help](https://doc-0o-c8-docs.googleusercontent.com/docs/securesc/8ens8iqutentttr8mp9gnpq5d3rd0gft/5i91cmqggq6ggnsbbcvjvommh1g8q7n8/1662120900000/13322951042871938865/13322951042871938865/1zYSaaRT1F2sORlTHgwQRrMb_SGLPwc8h?e=download&ax=AI9vYm7x1NYBmAI1-RJVvSOB1_uJPqwJxXatcDBCi2BIMacimwLZw4TqTEQAhgkSrP6B4tMpBtCVV0MCAlAPApnoTcLu2CEHwSZGChCplMU83V2ar542nQCocfm3_4zAMvacEMycPo9JmNZVDUKq8qLx8kTBfnP41Wlsf6JsS7VnqeJF0HVe5iWS-Spd8DeZgFbexGbngTQgFbgkq71ItWt6KqujvLVdUzNrxlxWDnKMx-4WRqDOjad1x2e5zovGLV9JMDggv-YhPtj5tJufzjVPnV-NnhI19AduqFYu5hnAcLP3fiEQywGjlApBC63t2EpbGCd9e19sEnpQrxrkn7iN-zr60qPtMBMQUlzZq_OnA4Rvpy9FKlFqSS2zfXjlJODZrZI9kV1bPBPkJRQwqClfaa1HJZztj_MyVUC1d7nAUNmp7cUb7WGiMrR5xk0o-m4_8M3VqdBgbG8dD6u8QjeNkFN0NnwZC3tgICOR8260N8HKVfayYKtzo8_8UCxHZ4YyMezHmXqoVAF3r_O5I9SzLdF_FQjQproqfXSsvBGbLKklXz2CrmCt-Czeu5c7dW8WBuGRJ31izYXrmY5HC_rOkWjv1YZdkDZ4GRWKt0Mzs7nMblB3fuDkfeSsCMuyCvj2ekZPLIfJy0On2O5EdX5UK8h71R7C57qMV5xS_ZgAVQnmsGDps_oOEyyDJCMsm8M0kaAs3pCKO5bPCRG1&uuid=1c9861f0-c991-4aa0-9cfd-09d8699aab4c&authuser=0&nonce=iolilruacppnc&user=13322951042871938865&hash=0s1neb31p0jfb235j6544jstae0hch0p)

|ESP8266        |WS2812B    |
|---            | ---       |
|GPIO14(D5)     |IN         |
|3v3            |VCC        |
|GND            |GND        |

- connect the Pin 14 to input pin of WS2812B and 3v3 to VCC and GND to GND

# settings
- open the `config.py` file and fill out of all variables
- for example : line 4 `matrix` value is 16 , if my WS2812B have 8 LED's i'll put 8 instead of 16
- and your SSID of wifi is your wifi name

Good Luck ;)
