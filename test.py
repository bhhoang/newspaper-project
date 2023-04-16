import bcrypt

password = "admin"
hashed = "$2b$12$rM0Tj8g5vEb8ITOLLV6Rq.LWeeitvI.JTy3aNMb/wsDFPm10RzIAO"

print(bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')))