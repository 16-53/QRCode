from datetime import date

import qrcode


def getqr():
    url = input("Give me the link: ")
    today = str(date.today())
    qr = qrcode.make(url)
    qr.save("1653-" + today + ".png")
    return "Completed ✔ \nYour QRCode is saved"

print(getqr())