import qrcode
from qrcode import constants
# The above line imports the constants module from the qrcode library. 
# It's used to specify error correction levels for the QR code.

qr = qrcode.QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    # Sets the error correction level to "L," which stands for low. 
    # This level is suitable for QR codes with a relatively low chance of being damaged.
    box_size=10,
    border=4,
)
data = "https://www.linkedin.com/in/frasirfan"
qr.add_data(data)  # Use the 'data' variable containing the URL
qr.make(fit=True)
# The fit=True argument ensures that the QR code adjusts its size to fit the data properly.

img = qr.make_image(fill_color="black", back_color="white")
img.save('qr-code-linkedin.png')
