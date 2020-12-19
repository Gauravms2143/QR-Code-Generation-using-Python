import pyqrcode as qrcode 
import png
def generate_qr_code():
  q=qrcode.create(input("Enter Your Link"))
  q.png('QR Code.png',scale=12)
  
  
if __name__ == '__main__':
  generate_qr_code()
