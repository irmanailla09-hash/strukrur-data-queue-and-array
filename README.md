# strukrur-data-queue-and-array
## 1. Komponen Utama (Struktur Data)

Untuk menjalankan simulasi, kode menggunakan dua struktur data dasar:

* [cite_start]**`Array`**: Digunakan untuk menyimpan daftar agen loket (`TicketAgent`) dengan ukuran tetap[cite: 38].
* [cite_start]**`Queue`**: Menggunakan prinsip **FIFO (First-In, First-Out)**[cite: 94]. [cite_start]Penumpang yang datang pertama akan dilayani lebih dulu[cite: 97].
    * [cite_start]`enqueue`: Menambah penumpang ke belakang barisan[cite: 97].
    * [cite_start]`dequeue`: Mengambil penumpang dari depan barisan untuk dilayani[cite: 104].


---

## 2. Logika Simulasi (`TicketCounterSimulation`)

[cite_start]Kelas ini adalah "otak" dari program yang mengatur jalannya waktu menit demi menit[cite: 29].

### A. Inisialisasi (`__init__`)
* [cite_start]**Probabilitas Kedatangan**: Dihitung dari $1.0 / \text{betweenTime}$[cite: 33]. Jika rata-rata waktu antar kedatangan adalah 2 menit, maka peluang munculnya penumpang di setiap menit adalah 50%.
* [cite_start]**Komponen**: Membuat antrean kosong (`passengerQ`) dan daftar agen loket (`theAgents`) sesuai jumlah yang diminta[cite: 37, 38].

### B. Siklus Utama (`run`)
[cite_start]Setiap menit (`curTime`), sistem melakukan tiga hal[cite: 45]:
1.  **`_handleArrival`**: Menentukan secara acak apakah ada penumpang baru yang datang. [cite_start]Jika ada, masukkan ke `Queue`[cite: 46].
2.  [cite_start]**`_handleBeginService`**: Jika ada agen yang menganggur (`isFree`) dan ada orang di antrean, ambil orang tersebut dan mulailah pelayanan[cite: 47]. [cite_start]Di sini waktu tunggu dihitung[cite: 42].
3.  [cite_start]**`_handleEndService`**: Mengecek apakah ada agen yang sudah selesai melayani penumpang berdasarkan waktu layanan (`serviceTime`)[cite: 49].

---

## 3. Analisis Eksekusi Manual (Nomor 2 & 3)

Bagian ini menguji pemahaman Anda tentang cara kerja antrean dalam perulangan:

* [cite_start]**Nomor 2**: Memasukkan angka kelipatan 3 dari 0 hingga 15[cite: 95, 96].
    * [cite_start]Hasil: `[3, 6, 9, 12, 15]`.
* [cite_start]**Nomor 3**: Ada logika tambahan; jika angka kelipatan 4, maka lakukan `dequeue` (hapus data paling depan)[cite: 103, 104].
    * [cite_start]Saat $i=0$: Masuk ke antrean (karena $0 \% 3 == 0$)[cite: 96, 97].
    * [cite_start]Saat $i=4$: Kondisi `if` gagal, masuk ke `elif` ($4 \% 4 == 0$), maka angka `0` dihapus dari depan[cite: 103, 104].
    * [cite_start]Hasil Akhir: `[3, 6, 9, 12, 15]`.

---

## 4. Membalik Urutan Antrean (Nomor 6)

[cite_start]Fungsi `reverseQueue` menunjukkan cara memanipulasi data menggunakan struktur data tambahan[cite: 107]:
1.  [cite_start]Semua isi antrean dikeluarkan (`dequeue`) dan dimasukkan ke dalam **Stack** (Tumpukan)[cite: 108].
2.  Karena Stack bersifat **LIFO (Last-In, First-Out)**, saat data dikeluarkan dari Stack dan dimasukkan kembali ke antrean, urutannya otomatis terbalik.

---

## 5. Ringkasan Hasil Simulasi
[cite_start]Setelah fungsi `run()` selesai, `printResults()` akan menampilkan statistik penting[cite: 54]:
* [cite_start]**Jumlah penumpang terlayani**: Total penumpang yang masuk dikurangi yang masih tersisa di antrean[cite: 56, 57].
* [cite_start]**Rata-rata waktu tunggu**: Total akumulasi waktu tunggu dibagi jumlah penumpang yang dilayani[cite: 59, 69].

> [cite_start]**Catatan Implementasi**: Kode ini menunjukkan bahwa efisiensi loket sangat bergantung pada perbandingan antara `betweenTime` (kedatangan) dan `serviceTime` (kecepatan layanan)[cite: 33, 34]. [cite_start]Jika waktu layanan jauh lebih lama dari kedatangan, antrean akan terus menumpuk[cite: 67].
