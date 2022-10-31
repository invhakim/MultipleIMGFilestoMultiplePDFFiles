# Bagaimana Mengkonversi Banyak file Gambar ke banyak file PDF dengan Python?

`img2pdf` adalah paket Python open source untuk mengonversi gambar ke format pdf. Ini termasuk modul `pillow` yang juga dapat digunakan untuk meningkatkan gambar (Kecerahan, kontras dan hal-hal lain)

Gunakan perintah ini untuk menginstal paket

```
pip install img2pdf
```

Di bawah ini adalah implementasinya:
Gambar dapat dikonversi menjadi byte pdf menggunakan fungsi `img2pdf.convert()` yang disediakan oleh modul img2pdf, kemudian file pdf dibuka dalam mode `wb` dan ditulis dengan byte.

Nama Folder
```
KT-PEMKAB-SERUYAN-10
```

Nama File .csv 
```
KT-PEMKAB-SERUYAN-10.csv
```

Isi File .csv
```
2022-10-01-bupati-seruyan-pimpin-upacara-peringatan-hari-kesaktian-pancasila.jpg-kt.png
2022-10-01-bupati-seruyan-apresiasi-upaya-optimalisasi-pad.jpg-kt.png
2022-10-01-pemkab-seruyan-dan-kanwil-kemenkumham-kalteng-matangkan-rencana-pembangunan-lapas.jpg-kt.png
2022-10-03-bupati-harapkan-politeknik-seruyan-jadi-perguruan-tinggi-terdepan.jpg-kt.png
```

Hasil File .PDF
```
2022-10-01-bupati-seruyan-pimpin-upacara-peringatan-hari-kesaktian-pancasila.jpg-kt.pdf
2022-10-01-bupati-seruyan-apresiasi-upaya-optimalisasi-pad.jpg-kt.pdf
2022-10-01-pemkab-seruyan-dan-kanwil-kemenkumham-kalteng-matangkan-rencana-pembangunan-lapas.jpg-kt.pdf
2022-10-03-bupati-harapkan-politeknik-seruyan-jadi-perguruan-tinggi-terdepan.jpg-kt.pdf
```

Ref :  
- https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
