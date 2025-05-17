# import qrcode


# data = "taha is a good boy"
# img = qrcode.make(data)
# img.save("C:/my_qrcode.png")

import qrcode
import os

data = "what is artificial intelligence"
# output_path = "C:/Users/TECHNOSELLERS/Desktop/qr_code_project"
output_path = "C:/Users/TECHNOSELLERS/Desktop/python_25/08_qr_code_project"
filename = "my_qrcode.png"
full_path = os.path.join(output_path, filename)

img = qrcode.make(data)
img.save(full_path)

print(f"QR code saved at {full_path}")



