<p align="center">
  <a name="top" href="#octocat-hi-there-thanks-for-visiting-">
     <img alt="lordacil/Tugas-pemrograman_GUI" height="60%" width="100%" src="https://i.ibb.co/NYv0DCR/gui.png"/>
  </a>
  <br><br><br><br>
</p>

## :star: Tampilan Program Qt-Designer

![](images/program_qt.png)

## :cyclone: Widget yang digunakan
### Komponen 1

![](images/Komponen1.png)

- **Vertical Layout** berguna untuk mengatur tata letak/layout secara vertical ditandai dengan kotak warna merah,<br/>
- **Label** berguna untuk menampilkan sebuah teks, pada gambar disamping nama labelnya adalah Data Mahasiswa,<br/>
- **Plain Text Edit** berguna untuk menulis text dgn jumlah karakter yg banyak.

### Komponen 2

![](images/Komponen2.png)

- **Form Layout** berguna untuk menggabungkan layout-layout lainnya contohnya disini layout vertical dan horizontal,<br/>
- **Vertical Layout** berguna untuk mengatur tata letak/layout secara vertical ditandai dengan kotak warna merah,<br/>
- **Horizontal Layout** berguna untuk mengatur tata letak/layout secara horizontal ditandai dengan kotak warna merah,<br/>
- **Label** berguna untuk menampilkan sebuah teks, pada gambar disamping nama labelnya adalah Nim, Nama, Jurusan, dan NoTelp dengan menggunakan layout Vertical,<br/>
- **Line Edit** berguna untuk mengedit teks dalam satu baris, pada gambar disamping line edit yaitu yang sebelah kanan label dan menggunakan layout Vertical,<br/>
- **Push Button** berguna untuk tombol yang bisa digunakan untuk konfirmasi atau cancel, pada gambar disamping nama buttonnya yaitu yang tambah, edit ,clear, dan hapus dengan menggunakan layout Horizontal.<br/>

## :rice_scene: Convert File Ui Qt-Designer ke Python

  1. Save program yang sudah dibuat di Qt-Designer yang berformat .ui
  2. Buka CMD/Terminal (disini saya memakai terminal)
  3. Lalu ketik command berikut pada CMD/Terminal :
  ``` bash
      $ pyuic5 -x 'nama-program-format-.ui' -o 'nama-untuk-file-pythonnya.py
  ```
  4. Selesai, jika terdapat file python yg sudah diconvert berarti sudah berhasil diconvert

### GIF Convert .ui ke python

![](images/gif_convert.gif)

<p align="center">
  <a name="top" href="#octocat-hi-there-thanks-for-visiting-">
     <img alt="lordacil/Tugas-pemrograman_GUI" height="30%" width="30%" src="https://i.ibb.co/RYWKHnz/ui-prog.png"/>
  </a>
</p>

## :star2: Tampilan Output Program
