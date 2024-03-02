#tipe data
#di python terdapat berbagai macam tipe data kali ini kita akan belajar tipe data yang paling sering digunakan

# 1. String
# tipe data ini ditandai dengan adanya tanda kutip bisa '' atau "" tipe data ini biasanya digunakan untuk huruf abjad
# contoh tipe data string

nama = "Fauzan"
#tipe data string ini bisa digunakan untuk semua karakter bisa juga untuk int tetapi jika ditambahkan maka hasilnya kana seperti ini
nilai1 , nilai2 = "90" , "90"
print(nilai1 + nilai2)
print(nilai1)
#jika string ditambahkan maka hasilnya akan menggabungkan 2 variabel itu bukan menjumlahkannya makanya ada tipe data yang kedua yaitu

# 2. Int
# tipe data ini hanya bisa digunakan oleh angka dan nilai angka itu harus bulat
# contoh penggunaan tipe data Int
# pendeklarasiannya untuk tipe data Int tanpa menggunakan tanda kutip jika menggunakan tanda kutip maka tipe data tersebut akan berubah menjadi Int
x , y = 10 , 20
print(x + y)
#jika tipe data int ditambhakan maka hasilnya akan menghitung jumlah dari variabel x dan variabel y

# 3. Double
# sama seperti dengan Int tetapi tipe data double ini digunakan untuk angka yang nilainya bersifat desimal
# contoh penggunaakn tipe data Double
phi = 3.14

# 4. Boolean
# tipe data ini hanya memiliki 2 nilai yaitu true dan false tipe data ini biasnaya digunakan untuk looping
# atau semisal kita mau memunculkan pesan terimakasih ketika nilai dari variabel a berilai true juga bisa daripada kita
# menggunakan string kita bisa menggunakan Boolean
#
paymentCheck = True
paymentCheck = False
print(paymentCheck)

#kita bisa cek variabel ini memiliki tipe data apa dengan menggunakan Type
#contoh kita akan mengecek tipe data dari variabel phi
print(type(phi))
print(type(x))
print(type(nilai1))
print(type(paymentCheck))
#dengan cara print dilanjukan dengan Type dan dilanjutkan dengan variabel yang ingin kita cek tipe datanya
