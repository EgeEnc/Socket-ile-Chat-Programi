from cryptography.fernet import Fernet

def şifrele(karakter_dizisi, anahtar):
    return Fernet(anahtar).encrypt(karakter_dizisi.encode("UTF-8"))
def çöz(şifre, anahtar):
    return Fernet(anahtar).decrypt(şifre).decode("UTF-8")

