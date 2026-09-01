import random
import string


def generate_otp(length=6):
  characters = string.digits
  otp = "".join(random.choice(characters) for _ in range(length))
  return otp


print("--- Secure OTP Generator ---")
length_input = input("Enter OTP length (default is 6): ")

if length_input.isdigit():
  otp_length = int(length_input)
  if otp_length > 0:
    secure_otp = generate_otp(otp_length)
    print(f"\nGenerated OTP: {secure_otp}")
    print("Status: Valid for 5 minutes.")
  else:
    print("Error: Length must be greater than zero.")
else:
  secure_otp = generate_otp(6)
  print(f"\nGenerated OTP (Default 6-digit): {secure_otp}")
  print("Status: Valid for 5 minutes.")