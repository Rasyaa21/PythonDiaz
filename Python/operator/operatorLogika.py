#Operator Logika
#Operator logika memiliki fungsi untuk melakukan pemeriksaan kesamaan nilai dari dua data atau lebih.
#Operator logika juga memiliki fungsi sebagai ekspresi yang dapat mengembalikan nilai dengan tipe boolean.
#Contoh dari operator logika

# and (&&)
# bahasa pemrograman lain melambangkan operator logika sebagai (&&) tetapi berbeda dengan bahasa pemrograman python python sendiri menggunakan
# "and" untuk melambangkan operator logika and, inilah mengapa bahasa pemorograman python termasuk bahasa pemrograman yang beginner friendly
# kondisi and ini akan bernilai true jika kedua dari kedua nilai dari true jika salah satunya true dan satunya lagi false maka output dari
# program itu sendiri akan menjadi false karena salah satunya tidak
#contoh
check1 = True
check2 = False

if check1 and check2:
    print(True)
else:
    print(False)
#hasil output dari program tersebut akan menjadi false karena salah satu kondisinya tidak terpenuhi

# Or (||)
# sama seperti and operator logika or dalam python dilambangkan dengan "or" biasanya dibahasa pemrograman lain dilambangkan sebagai (||)
# operator logika or akan bernilai true jika salah satu dari nilai tersebut bernilai true
# contoh penggunaannya
nomor1 = 21
nomor2 = 22

if nomor1 == 22 or nomor2 == 22:
    print(True)
else:
    print(False)

# Not (!)
#operator not ini digunakan ketika kita mau mengecek bahwa nilai tersebut bukan nilai yang kita inginkan semisal kita ingin cek bahwa
#pembayarannya sudah dibayar bisa juga menggunakan if payment is not false maka bisa juga diartika jika payment == true maka outputnya akan true
payment = True
if payment is not False:
    print(True)
else:
    print(False)
