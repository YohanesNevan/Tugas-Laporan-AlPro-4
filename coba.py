nama = input("Masukan nama anda = ")

print("Hallo aku", nama, "selamat pagi")

def tambah(a,b):
    hasil = a + b
    return hasil

tambah =lambda a, b: a + b

c = tambah(10,5)
print (c)

def print_twice(message):
    print(message)
    print(message)
    
print_twice("Hello World")

def hitung_belanja(belanja, diskon=0):
    bayar = belanja- (belanja * diskon)/100
    return bayar

print(hitung_belanja(100000))
print(hitung_belanja(100000, 10))
print(hitung_belanja(100000, 50))

def abc(a, b, c):
    a = b + c
    b = c + a
    c = a + b
    
nilai1 = 20
nilai2 = 30
nilai3 = 40

abc(nilai1, nilai2, nilai3)
print(nilai1)
print(nilai2)
print(nilai3)

def kelipatan_sembilan(angka):
    if angka % 9 == 0:
        return True
    else:
        return False
    
print(kelipatan_sembilan(81))
print(kelipatan_sembilan(2000))
    
kelipatan_sembilan = lambda angka: angka % 9 == 0

print(kelipatan_sembilan(81))
print(kelipatan_sembilan(2000))