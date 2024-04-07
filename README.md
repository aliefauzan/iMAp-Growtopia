# iMAp-Growtopia

Skrip Python ini dirancang untuk mengekstrak tautan permainan Growtopia dari email yang diterima di akun email, dan kemudian membuka tautan terakhir yang diekstraksi ke dalam website

## Instruksi
**Persyaratan:** Pastikan Anda telah menginstal Python di sistem Anda bersama dengan libraries yang diperlukan (imaplib, email, re, webbrowser).
**Konfigurasi:** Modifikasi skrip untuk menyertakan detail server IMAP Anda (misalnya, alamat server, port). Saat ini, skrip dikonfigurasi untuk berfungsi dengan server IMAP Outlook.

## Penggunaan:
1. Jalankan skrip.
2. Masukkan email dan kata sandi Anda dalam format yang diminta (email:katasandi). Anda dapat memasukkan beberapa akun email yang dipisahkan dengan tanda ',' seperti email:katasandi,email2:katasandi
Skrip akan terhubung ke akun email(s), mencari email dari "Growtopia Game", mengekstrak tautan yang terkandung dalam email tersebut, dan membuka tautan terakhir yang diekstraksi dalam web.
Keluar: Untuk keluar dari skrip, ketik 'purani' saat diminta untuk kredensial email. atau anda dapat memmodifikasinya dengan mengganti pada bagian     if credentials_input.lower() == 'purani':

## Catatan
1. Skrip ini saat ini mendukung ekstraksi tautan secara khusus dari email yang diterima dari "Growtopia Game".
2. Jika terjadi kesalahan selama eksekusi (misalnya, kredensial yang salah, masalah koneksi), pesan kesalahan yang sesuai akan ditampilkan.
