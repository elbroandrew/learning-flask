from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)

# print(hashed_password)

# check password
check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
print(check) # False, wrongpassword != supersecretpassword


