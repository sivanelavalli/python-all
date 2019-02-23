import pyotp
import time
totp = pyotp.TOTP('base32secret3232')
tempotp = totp.now()
print(tempotp)

