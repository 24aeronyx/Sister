# Komunikasi Request-Response

# Arsitektur client-server
# Klien mengirimkan permintaan ke server dan menunggu respons
# Cocok untuk aplikasi di mana klien perlu mendapatkan informasi spesifik dari server
# Memungkinkan pengguna untuk melihat respons secara langsung setelah mengirimkan permintaan
# Memperlihatkan bagaimana data dikirim dan diterima secara langsung, yang berguna dalam memahami interaksi antara komponen dalam sistem terdistribusi

from flask import Flask, request, jsonify #Import library flask untuk web interaksi, request untuk mengirim permintaan, dan jsonify untuk menerima data

app = Flask(__name__)

@app.route('/request', methods=['POST']) # Membuat route pada app dengan metode POST terhadap route '/request', sehingga jika app berjalan di port 5000, maka route nya menjadi 5000/request dengan method post.

def request_response(): # Fungsi komunikasi request-response
    data = request.json # Membuat variabel data dengan menerima request dalam bentuk json
    response_data = {'message': f"Hello {data['name']}!"} # Mendeklarasikan response_data dengan message Hello 'name', jika user memberikan input 'name' = 'lol' dengan method post ke route /request, maka response nya akan menjadi Hello lol
    return jsonify(response_data) # Return nilai dari response_data

if __name__ == '__main__':
    app.run(port=5000) # Set PORT di PORT 5000


# Test
## 127.0.0.1 - - [05/Oct/2024 06:31:57] "POST /request HTTP/1.1" 200 -
## 127.0.0.1 - - [05/Oct/2024 06:38:31] "POST /request HTTP/1.1" 200 -

# Skenario Pengiriman Notifikasi Real-Time untuk Publish-Subscribe
## Pengguna berlangganan ke layanan notifikasi penawaran terbaru dari beberapa kategori produk di aplikasi berita. Saat ada berita baru yang relevan diterbitkan, pelanggan akan langsung menerima pemberitahuan real-time.
## Penanganan skenario di mana pelanggan tidak aktif saat pesan dikirim, memastikan pesan tetap sampai ketika pelanggan kembali aktif.