![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-whatsapi

Ini adalah node komunitas n8n. Node ini memungkinkan Anda menggunakan WhatsApp API dalam alur kerja n8n Anda.

WhatsApp API adalah layanan yang memungkinkan integrasi fungsionalitas WhatsApp ke dalam aplikasi dan sistem pihak ketiga.

[n8n](https://n8n.io/) adalah platform otomasi alur kerja yang [berlisensi fair-code](https://docs.n8n.io/reference/license/).

[Instalasi](#instalasi)  
[Operasi](#operasi)  
[Kredensial](#kredensial)  
[Kompatibilitas](#kompatibilitas)  
[Penggunaan](#penggunaan)  
[Sumber Daya](#sumber-daya)  

## Instalasi

Ikuti [panduan instalasi](https://docs.n8n.io/integrations/community-nodes/installation/) dalam dokumentasi node komunitas n8n.

## Operasi

Node WhatsApi mendukung operasi berikut:
- Mengirim pesan
- Mengirim file media
- Menerima pesan
- Memeriksa status pesan

## Kredensial

Untuk menggunakan node WhatsApi, Anda perlu memiliki akun WhatsApp yang sudah dihubungkan dengan WhatsApi. Setelah mendaftar, Anda akan menerima token akses yang diperlukan untuk otentikasi.

Untuk mengatur kredensial:
1. Buka pengaturan kredensial n8n
2. Pilih 'WhatsApi'
3. Masukkan token akses Anda, url WhatsApi dan nomor yang akan digunakan.

## Kompatibilitas

Node ini kompatibel dengan n8n versi 0.187.0 ke atas. Pengujian dilakukan terhadap versi terbaru n8n.

## Penggunaan

Untuk menggunakan node WhatsApi:
1. Tambahkan node WhatsApi ke alur kerja Anda
2. Pilih operasi yang diinginkan
3. Konfigurasikan parameter yang diperlukan (misalnya, nomor tujuan, isi pesan)
4. Hubungkan node dengan elemen alur kerja lainnya sesuai kebutuhan

Untuk informasi lebih lanjut tentang penggunaan dasar n8n, lihat [dokumentasi Try it out](https://docs.n8n.io/try-it-out/).

## Sumber Daya

* [Dokumentasi node komunitas n8n](https://docs.n8n.io/integrations/community-nodes/)
* [Dokumentasi WhatsApp Business API](https://github.com/tanivision/whatsapi)
