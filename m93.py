# from datetime import date
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# print(c.convert(1,"USD","INR" ))
# atm = float(input("\nEnter the amount in USD :>>"))
# new_atm = c.convert(atm,"EUR","INR",date=date(2026, 9, 3))
# print(new_atm)
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://www.python.org/")
qr.make(fit=True)
img = qr.make_image(fill_color="yellow", back_color="black")
img.save("m93.png")


