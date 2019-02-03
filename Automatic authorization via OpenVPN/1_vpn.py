import pyotp
from subprocess import Popen, PIPE
from time import sleep

USERNAME = 'Here is your login'
ZZTAP1_PASS = 'Here is your password'
zztap1_otp = pyotp.TOTP('Here is your QR in string')
args = ["C:/Program Files/OpenVPN/bin/openvpn.exe", "--config", "D:/MailruSRE/zztap1.ovpn"]
openvpn = Popen(args, stdin=PIPE)
sleep(2)
openvpn.stdin.write(b"Here is your login")
openvpn.stdin.flush()
openvpn.stdin.write((ZZTAP1_PASS + zztap1_otp.now()).encode('ascii'))
openvpn.stdin.flush()
