# Publish-Subscribe
# Arsitektur decoupled (terpisah) antara penerbit dan pelanggan.
# Penerbit mengirimkan pesan ke saluran, dan semua pelanggan yang berlangganan saluran tersebut menerima pesan.
# Cocok untuk aplikasi yang membutuhkan pembaruan data secara real-time, seperti aplikasi berita atau notifikasi.
# Model ini memungkinkan penerbit dan pelanggan untuk beroperasi secara independen, mengurangi ketergantungan.
# Mudah untuk menambah lebih banyak pelanggan tanpa mengubah penerbit, menjadikannya ideal untuk aplikasi besar.
# Menunjukkan bagaimana komunikasi asinkron dapat dilakukan di antara komponen, yang penting dalam sistem terdistribusi di mana banyak entitas mungkin berinteraksi secara bersamaan.

import paho.mqtt.client as mqtt #Import library komunikasi mqtt

def on_message(client, userdata, message): # Buat fungsi untuk menerima message
    print(f"Message received: {message.payload.decode()}") # Tampilkan message pada terminal

client = mqtt.Client() # Set client menggunakan komunikasi MQTT
client.on_message = on_message # Mengaitkan fungsi on_message yang telah didefinisikan sebelumnya dengan event on_message dari klien. Artinya, setiap kali klien menerima pesan dari broker, fungsi ini akan dipanggil.
client.connect("test.mosquitto.org", 1883, 60) # Klien mencoba terhubung ke broker MQTT di alamat test.mosquitto.org menggunakan port 1883 (default port untuk komunikasi MQTT tanpa enkripsi). Timeout maksimum untuk koneksi ditetapkan ke 60 detik.
client.subscribe("test/topic") # Klien berlangganan ke topik "test/topic". Ini berarti setiap kali ada pesan yang diterbitkan ke topik ini, klien akan menerima pesan tersebut.
client.loop_start() # Memulai loop komunikasi asinkron dari klien, yang akan terus-menerus memantau pesan yang masuk dan event lain tanpa memblokir eksekusi kode lainnya.

# Publisher
def publish_message(message):
    client.publish("test/topic", message) # Fungsi publish_message didefinisikan untuk menerbitkan pesan ke topik "test/topic". Pesan yang diterima oleh fungsi ini akan dikirimkan ke broker, dan semua pelanggan yang berlangganan ke topik ini akan menerima pesan tersebut.

# Example usage
publish_message("Hello Subscribers!") # Contoh pemanggilan fungsi publish_message untuk mengirimkan pesan "Hello Subscribers!" ke topik "test/topic". Pesan ini akan diterima oleh semua klien yang telah berlangganan topik tersebut.

# Buat loop yang terus berjalan hingga program dihentikan secara manual
try:
    while True:
        # Program akan terus berjalan di sini.
        pass  # Anda bisa memasukkan logika tambahan di sini jika diperlukan.
except KeyboardInterrupt:
    print("\nProgram stopped by user (Ctrl + C).")
    client.loop_stop()  # Hentikan loop MQTT saat keluar
    client.disconnect()  # Putuskan koneksi dengan broker

# Test
## Message received: waiting ...
## Message received: Hello Subscribers!
## Message received: Rucne: keren

# Skenario E-Commerce untuk Request-Response
## Seorang pengguna melakukan pencarian produk di platform e-commerce, kemudian mengajukan permintaan untuk menambahkan produk tersebut ke dalam keranjang. Server kemudian merespons dengan memvalidasi stok dan menambahkannya ke keranjang pengguna.

# Tantangan
## Penanganan waktu respons yang cepat serta penanganan skenario seperti produk habis atau gagal menambahkan produk ke keranjang.

# Program stopped by user (Ctrl + C).   