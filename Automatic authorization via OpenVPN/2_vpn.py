import pyotp
from subprocess import Popen, PIPE
from time import sleep

USERNAME = 'Here is your login'
STH_PASS = 'Here is your password'
sth_otp = pyotp.TOTP('Here is your QR in string')
args = ["C:/Program Files/OpenVPN/bin/openvpn.exe", "--config", "D:/MailruSRE/sth55.ovpn"]
openvpn = Popen(args, stdin=PIPE)
sleep(2)
openvpn.stdin.write(b"Here is your login")
openvpn.stdin.flush()
openvpn.stdin.write((STH_PASS + sth_otp.now()).encode('ascii'))
openvpn.stdin.flush()
