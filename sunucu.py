import socket
from threading import Thread
from cryptography.fernet import Fernet
from şifreleme import şifrele, çöz

belirlenen_anahtar = Fernet.generate_key()

host = socket.gethostbyname(socket.gethostname())
print("Sunucu oluşturuldu.Sunucunun IP adresi : ", host)
port = 1234

baglanti_sayisi = 10

veri_boyutu = 4096

calistir = (host, port)

bagla = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bagla.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bagla.bind(calistir)
bagla.listen(baglanti_sayisi)

sunucu, adres = bagla.accept(
)
print(sunucu.getpeername()[0] + str("IP adresli kullanıcı sunucuya bağlandı."))
sunucu.send(belirlenen_anahtar)

def yolla():
    girdi = input()
    sunucu.send(şifrele(girdi, belirlenen_anahtar))
def girdi_al():
    while True:
        veri = sunucu.recv(veri_boyutu)
        print(str(sunucu.getpeername()[0]) + " : " + str(çöz(veri, belirlenen_anahtar)))
Thread(target=girdi_al).start()
while True:
    yolla()