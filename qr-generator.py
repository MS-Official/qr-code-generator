import qrcode

# Data you want to encode in the QR code
data = "https://www.google.com"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

# Add data to the QRCode object
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QRCode object
img = qr.make_image(fill='black', back_color='white')

# Save the QR code as an image file
img.save("qr_code.png")

# Optionally, show the image (this will open the image in the default viewer)
img.show()
