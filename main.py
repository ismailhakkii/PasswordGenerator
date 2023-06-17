import random
import string
import hashlib

def generate_salt(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt

def hash_password(password, salt):
    # Şifre + salt'ın birleştirilmesi
    salted_password = password + salt

    # SHA256 algoritmasını kullanarak şifrenin hash değerini hesaplama
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    return hashed_password

def generate_password(length):
    if length < 8:  # 8 is a common minimum length for passwords
        return "Error: Password length must be at least 8."

    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

while True:
    try:
        password_length = int(input("Şifre uzunluğunu girin: "))
        generated_password = generate_password(password_length)
        if "Error" in generated_password:
            print(generated_password)
        else:
            salt = generate_salt(16)  # Salt'ı rastgele oluşturun
            print("Oluşturulan şifre:", generated_password)
            print("Oluşturulan şifrenin Hash değeri:", hash_password(generated_password, salt))
            break
    except ValueError:
        print("Geçerli bir sayı girin.")
