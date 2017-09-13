import socket
from threading import Thread
from şifreleme import şifrele, çöz

host = input("Bağlanacağınız sunucunun IP adresini giriniz:")
port = 1234

veri_boyutu = 4096

calistir = (host, port)
istemci = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
istemci.connect(calistir)
print("Program başlatılıyor...")

belirlenen_anahtar = istemci.recv(veri_boyutu)

print("Bu programla gönderdiğiniz tüm veriler güvenliğinizi sağlamak amacıyla şifrelenmektedir.")
def yolla():
    girdi = input()
    istemci.send(şifrele(girdi, belirlenen_anahtar))
def girdi_al():
    while True:
        veri = istemci.recv(veri_boyutu)
        print("Sunucu" + " : " + str(çöz(veri, belirlenen_anahtar)))
print("Sunucuya bağlanıldı.")
Thread(target=girdi_al).start()
while True:
    yolla()