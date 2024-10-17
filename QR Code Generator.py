import qrcode
qr = qrcode.QRCode(version=3, box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_H)
data =input("Enter the data: ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("name.png")