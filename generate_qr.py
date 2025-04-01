import qrcode

url = "https://segiitu.github.io/gift-email/"
qr = qrcode.make(url)
qr.save("wedding_email_qr.png")
