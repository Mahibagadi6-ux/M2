import qrcode
while True:
    link = input("Enter the link: ")

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("custom_qrcode.png")
    print("Custom QR Code saved as custom_qrcode.png")
