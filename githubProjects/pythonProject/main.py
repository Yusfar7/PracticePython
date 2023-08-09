import qrcode

ssid="rewrwerwerk"
password= "qwertttqewt"
encryptionType = "WPA2"

wifiData = f"WIFI:S:{ssid};T:{encryptionType};P:{password};;"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(wifiData)
qr.make(True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("WifiQr.png")