# ASESSMENT SOFTWARE QUALITY
#### Nama : La Ode Saktika Awaludin Luthfi
#### NPM : 714232009
#### Studi Kasus: Perusahaan C sedang mengembangkan perangkat lunak medis yang kritis
## Link PPT : https://docs.google.com/presentation/d/1hrKWoKmwn_zY-f6vqA-ovZ9REgn8ADtl/edit?usp=drive_link&ouid=116033211074015855013&rtpof=true&sd=true
## Link Youtube :https://youtu.be/dxR8O6m9XxA

## 1. Bagaimana QA dapat memverifikasi bahwa perangkat lunak medis ini memenuhi persyaratan regulasi dan kepatuhan industri yang ketat, seperti ISO 13485 atau FDA (Food and Drug Administration)?

QA dapat memverifikasi bahwa perangkat lunak medis memenuhi persyaratan regulasi dan kepatuhan industri yang ketat, seperti ISO 13485 atau FDA (Food and Drug Administration), dengan mengikuti langkah-langkah berikut:

Memahami persyaratan regulasi dan kepatuhan industri yang berlaku untuk perangkat lunak medis yang sedang dikembangkan. Persyaratan ini dapat ditemukan di berbagai sumber, termasuk peraturan pemerintah, standar industri, dan pedoman dari organisasi profesi.
Salah satu standar yang digunakan adalah Sertifikasi ISO 13485 yang diterbitkan pada tahun 2016 yang merupakan sistem manajemen mutu khusus untuk industri perangkat medis.
ISO 13485 dapat diterapkan oleh organisasi apa pun yang terlibat dalam desain, pengembangan, produksi, instalasi, atau layanan perangkat medis, termasuk produsen perangkat medis, distributor perangkat medis, pemasok komponen perangkat medis, rumah sakit atau organisasi layanan kesehatan

Contoh di rumah sakit dan klinik harus memastikan bahwa perangkat medis yang mereka gunakan aman dan efektif. Dengan demikian setiap tenaga profesional dapat mempergunakan alat medis yang sesuai dengan standar dan aman bagi pasien.


## 2. Apa strategi pengujian yang paling tepat untuk memvalidasi keakuratan dan keandalan hasil yang dihasilkan oleh perangkat lunak medis ini?

Strategi yang digunakan merupakan gabungan dari testing fungsional dan non fungsional
Strategi pengujian perangkat lunak merupakan proses integrasi metode perancangan kasus uji kedalam bentuk urutan langkah pengujian perangkat
lunak.Strategi pengujian perangkat lunak secara berurutan adalah pengujian unit (unit testing), integration testing dan system testing

Pengujian Unit (Unit Testing) adalah pengujian yang difokuskan pada unit terkecil dari program (modul). Pengujian ini didasarkan pada informasi
dari deskripsi perancangan detil perangkat lunak. Pada umumnya pengujian ini dilakukan secara white-box dan source code based testing dengan
melakukan pengecekan jalur khusus pada struktur kendali modul untuk meyakinkan kelengkapan cakupan dan deteksi maksimum kesalahan
Adapun hal-hal yang diuji pada pengujian unit ini adalah sebagai berikut :
1. Antarmuka (interface)
2. Struktur data
3. Kondisi batas
4. Jalur-jalur bebas (independent paths)
5. Jalur penanganan kesalahan

Pengujian Integrasi (Integration Testing) adalah pengujian yang difokuskan pada gabungan unit-unit
atau modul-modul yang membentuk kesatuan fungsional. 
Pengujian ini didasarkan pada informasi dari deskripsi perancangan awal perangkat lunak

Pengujian sistem adalah pengujian yang dilakukan pada sistem komputer (computer-based system) secara keseluruhan. Pengujian ini umumnya dilakukan oleh pengembang bersamaan dengan pengembang lain, karena pengujian yang dilakukan berhubungan dengan elemen lain perangkat lunak. Pengujian ini dilakukan untuk mengantisipasi masalah-masalah antarmuka dan perancangan jalur penanganan kesalahan antar sistem pada perangkat lunak
Pengujian sistem juga meliputi :
1. Pengujian Recovery (Recovery Testing)
2. Pengujian Keamanan (Security Testing)
3. Stress Testing
   
## 3. Bagaimana QA dapat memastikan bahwa perangkat lunak medis ini memiliki antarmuka pengguna yang intuitif dan mudah digunakan oleh para profesional medis?

Langkah langkah untuk memastikan bahwa perangkat lunak medis memiliki antarmuka pengguna yang intuitif dan mudah digunakan oleh para profesional medis sebagai berikut :

1. Lakukan riset pengguna. Pahami kebutuhan dan harapan pengguna perangkat lunak medis. Ini dapat dilakukan dengan melakukan wawancara, survei, atau observasi.
2. Menggunakan prinsip desain yang baik. Prinsip desain yang baik, seperti usability heuristics dan design thinking, dapat membantu memastikan antarmuka pengguna yang intuitif.
3. Mendapatkan feedback dari pengguna. Tes perangkat lunak medis dengan pengguna nyata dan dapatkan umpan balik mereka tentang antarmuka pengguna.
   
## 4. Apa langkah-langkah yang harus diambil oleh QA untuk menguji kehandalan perangkat lunak medis ini dalam kondisi darurat, seperti pemadaman listrik atau kegagalan perangkat keras?


Berikut adalah langkah-langkah yang dapat diambil oleh QA untuk menguji kehandalan perangkat lunak medis dalam kondisi darurat:

1. Melakukan identifikan skenario darurat yang mungkin terjadi.
Langkah pertama adalah mengidentifikasi skenario darurat yang mungkin terjadi, seperti pemadaman listrik, kegagalan perangkat keras, atau serangan cyber. Skenario-skenario ini dapat diidentifikasi dengan berkonsultasi dengan pakar medis, pengguna, dan pihak berwenang.

2. Kembangkan kasus uji untuk setiap skenario.
Untuk setiap skenario darurat, kasus uji harus dikembangkan untuk memverifikasi bahwa perangkat lunak dapat beroperasi dengan andal dalam kondisi tersebut. Contoh :
Perangkat lunak harus dapat terus beroperasi dalam kondisi darurat.
Perangkat lunak harus dapat memberikan peringatan yang tepat kepada pengguna tentang kondisi darurat.
Perangkat lunak harus dapat memulihkan operasi normal setelah kondisi darurat berlalu.

3. Analisis hasil pengujian.
Hasil pengujian harus dianalisis untuk mengidentifikasi area yang perlu ditingkatkan. Jika perangkat lunak tidak dapat beroperasi dengan andal dalam kondisi darurat, perbaikan harus dilakukan.
Contoh adalah penggunaan server cloud untuk meminimalisir resiko kehilangan data apabila terjadi pemadaman listrik atau bencana alam.


## 5. Bagaimana QA dapat memverifikasi bahwa perangkat lunak medis ini memiliki tingkat kesalahan yang minimal dalam memproses data pasien dan memberikan rekomendasi yang akurat?

Berikut adalah beberapa contoh spesifik dari langkah-langkah QA yang dapat dilakukan untuk memverifikasi tingkat kesalahan dan akurasi perangkat lunak medis:

1. Untuk memverifikasi bahwa perangkat lunak dapat membaca dan memproses data pasien dengan benar, tim QA dapat menggunakan data pasien yang nyata atau data yang dibuat secara sintetis. Data pasien dapat mencakup informasi medis seperti riwayat kesehatan, hasil tes, dan resep obat. Tim QA dapat menggunakan data ini untuk menguji apakah perangkat lunak dapat membaca data dengan benar dan menghasilkan output yang akurat.

2. Untuk memverifikasi bahwa perangkat lunak dapat menghasilkan rekomendasi yang akurat, tim QA dapat menggunakan data pasien yang telah didiagnosis dengan kondisi medis tertentu. Data ini dapat digunakan untuk menguji apakah perangkat lunak dapat menghasilkan rekomendasi yang tepat untuk kondisi medis tersebut.

3. Untuk memverifikasi bahwa perangkat lunak dapat berkomunikasi dengan sistem lain dengan baik, tim QA dapat menggunakan data dari sistem lain untuk menguji perangkat lunak. Misalnya, tim QA dapat menggunakan data dari sistem EMR untuk menguji apakah perangkat lunak dapat mengakses dan memproses data tersebut dengan benar.

4. Untuk memverifikasi bahwa perangkat lunak mudah digunakan dan dimengerti oleh pengguna, tim QA dapat melakukan survei atau wawancara dengan pengguna akhir. Survei atau wawancara dapat digunakan untuk mengumpulkan umpan balik dari pengguna tentang perangkat lunak.

5. Untuk memverifikasi bahwa perangkat lunak dapat menangani volume data pasien yang besar, tim QA dapat menggunakan data pasien dalam jumlah besar untuk menguji perangkat lunak.

6. Untuk memverifikasi bahwa perangkat lunak dapat bekerja dengan lancar dan tidak mengalami gangguan, tim QA dapat menguji perangkat lunak secara terus menerus selama periode waktu tertentu.


## 6. jelaskan langkah-langkah yang akan Anda ambil untuk memverifikasi bahwa perangkat lunak medis memenuhi persyaratan regulasi dan kepatuhan industri yang berlaku

1. Identifikasi persyaratan regulasi dan kepatuhan industri yang berlaku

Persyaratan regulasi dan kepatuhan industri untuk perangkat lunak medis dapat ditemukan dalam berbagai sumber, termasuk:

Peraturan pemerintah: Peraturan pemerintah yang mengatur perangkat lunak medis dapat ditemukan di berbagai negara, termasuk Indonesia. Di Indonesia, peraturan pemerintah yang mengatur perangkat lunak medis adalah Peraturan Menteri Kesehatan Republik Indonesia Nomor 1697/Menkes/Per/VIII/2016 tentang Keamanan, Mutu, dan Kinerja Alat Kesehatan.

Standar industri: Standar industri yang mengatur perangkat lunak medis dapat ditemukan di berbagai organisasi, termasuk International Organization for Standardization (ISO) dan International Medical Device Regulators Forum (IMDRF).

Pedoman dari organisasi profesional: Organisasi profesional yang terkait dengan perangkat lunak medis dapat menerbitkan pedoman yang mengatur aspek-aspek tertentu dari perangkat lunak medis. Misalnya, American Society for Testing and Materials (ASTM) menerbitkan pedoman untuk perangkat lunak medis yang digunakan dalam sistem kesehatan.

2. Lakukan analisis risiko

Analisis risiko adalah proses untuk mengidentifikasi potensi risiko yang dapat timbul dari penggunaan perangkat lunak medis. Analisis risiko ini dapat membantu untuk mengidentifikasi area yang perlu diprioritaskan untuk pemeriksaan.

3. Lakukan pemeriksaan dan pengujian

Pemeriksaan dan pengujian adalah proses untuk memastikan bahwa perangkat lunak medis memenuhi persyaratan regulasi dan kepatuhan industri. Pemeriksaan dan pengujian ini dapat mencakup pemeriksaan dokumentasi, pengujian fungsional, dan pengujian kinerja.

Pemeriksaan dokumentasi: Pemeriksaan dokumentasi dilakukan untuk memastikan bahwa perangkat lunak medis memiliki dokumentasi yang memadai, seperti spesifikasi, desain, dan manual.
Pengujian fungsional: Pengujian fungsional dilakukan untuk memastikan bahwa perangkat lunak medis berfungsi sebagaimana mestinya.
Pengujian kinerja: Pengujian kinerja dilakukan untuk memastikan bahwa perangkat lunak medis memenuhi persyaratan kinerja, seperti akurasi, keandalan, dan keamanan.


## 7. Buatlah serangkaian kasus uji yang melibatkan input data yang berbeda untuk memverifikasi keakuratan dan keandalan perangkat lunak medis

Berikut contoh input data untuk memverifikasi keakuratan dan keandalan perangkat lunak
1. Pengujian data pasien.
Contoh data pasien yang tidak valid, seperti nama yang kosong, tanggal lahir yang tidak valid, alamat yang tidak lengkap, atau jenis kelamin yang tidak valid

2. Pengujian Hasil tes laboratorium yang tidak valid, seperti nilai hemoglobin yang tidak masuk akal, glukosa darah yang negatif, atau tekanan darah yang tinggi secara tidak wajar

3. Pengujian Resep obat yang tidak valid, seperti nama obat yang tidak dikenal, dosis yang tidak masuk akal, atau frekuensi yang tidak benar

## 8. Jelaskan bagaimana Anda akan melibatkan pengguna akhir, seperti dokter atau petugas medis, dalam pengujian perangkat lunak medis ini untuk mendapatkan umpan balik dan validasi dari perspektif pengguna

Untuk melibatkan pengguna akhir, seperti dokter atau petugas medis, dalam pengujian perangkat lunak medis, saya akan mengikuti langkah-langkah berikut:

1. Identifikasi pengguna akhir yang tepat. Perangkat lunak medis dapat digunakan oleh berbagai jenis pengguna akhir, termasuk dokter, perawat, teknisi medis, dan pasien. Penting untuk mengidentifikasi pengguna akhir yang tepat untuk pengujian, karena mereka akan dapat memberikan umpan balik yang paling relevan.
2. Mengembangkan  rencana pengujian. Rencana pengujian harus mencakup tujuan pengujian, kriteria penerimaan, dan metode pengujian. Tujuan pengujian harus spesifik, terukur, dapat dicapai, relevan, dan berbatas waktu. Kriteria penerimaan harus menentukan apakah pengujian telah berhasil. Metode pengujian harus menjelaskan bagaimana pengujian akan dilakukan.
3. Mengumpulkan feedback dari end user. Umpan balik dari pengguna akhir dapat dikumpulkan melalui berbagai metode, termasuk wawancara, kuesioner, dan observasi. Wawancara memungkinkan pengumpulan umpan balik yang mendalam, tetapi membutuhkan waktu dan sumber daya yang lebih banyak. Kuesioner adalah metode yang lebih efisien untuk mengumpulkan umpan balik dari sejumlah besar pengguna akhir. Observasi memungkinkan pengumpulan umpan balik tentang bagaimana pengguna akhir sebenarnya menggunakan perangkat lunak.
4. Analisis umpan balik dari pengguna akhir. Umpan balik dari pengguna akhir harus dianalisis untuk mengidentifikasi area yang perlu ditingkatkan. Analisis dapat dilakukan secara kualitatif atau kuantitatif. Analisis kualitatif melibatkan interpretasi umpan balik secara tertulis. Analisis kuantitatif melibatkan penghitungan frekuensi dan tingkat keparahan masalah.
5. Lakukan iterasi berdasarkan umpan balik dari pengguna akhir. Umpan balik dari pengguna akhir harus digunakan untuk meningkatkan perangkat lunak. Proses ini dapat dilakukan secara iteratif, dengan perangkat lunak diuji dan ditingkatkan secara berkala.

## 9. Jelaskan bagaimana Anda akan memverifikasi bahwa perangkat lunak medis memiliki tingkat kesalahan yang minimal dalam memproses data pasien dan memberikan rekomendasi yang akurat


Ada beberapa cara untuk memverifikasi bahwa perangkat lunak medis memiliki tingkat kesalahan yang minimal dalam memproses data pasien dan memberikan rekomendasi yang akurat. Berikut adalah beberapa metode yang umum digunakan:

1. Pengujian perangkat lunak
Pengujian perangkat lunak adalah proses yang dilakukan untuk memeriksa apakah perangkat lunak berfungsi sesuai dengan spesifikasinya. Pengujian perangkat lunak medis biasanya dilakukan menggunakan data uji yang mewakili berbagai kondisi klinis yang mungkin dihadapi pasien. Data uji ini dapat berasal dari berbagai sumber, seperti database pasien, penelitian klinis, atau simulasi komputer.

2. Validasi perangkat lunak
Validasi perangkat lunak adalah proses yang dilakukan untuk menentukan apakah perangkat lunak memenuhi kebutuhan penggunanya. Validasi perangkat lunak medis biasanya dilakukan dengan melibatkan pengguna akhir, seperti dokter atau perawat, dalam proses pengujian. Pengguna akhir dapat memberikan umpan balik tentang bagaimana perangkat lunak bekerja dalam praktik dan membantu mengidentifikasi kesalahan atau area yang dapat ditingkatkan.

3. Uji klinis
Uji klinis adalah penelitian yang dilakukan untuk menentukan apakah suatu obat, prosedur, atau perangkat medis aman dan efektif. Uji klinis perangkat lunak medis biasanya dilakukan dengan menggunakan data pasien yang sebenarnya. Data ini dikumpulkan dari berbagai sumber, seperti rumah sakit, klinik, atau praktik dokter.

## 10. Jelaskan langkah-langkah yang akan Anda ambil untuk memverifikasi bahwa antarmuka pengguna perangkat lunak medis intuitif dan mudah digunakan oleh para profesional medis.

Untuk memverifikasi bahwa antarmuka pengguna perangkat lunak medis intuitif dan mudah digunakan oleh para profesional medis, saya akan mengambil langkah-langkah berikut:

1. Melakukan penelitian pengguna
Langkah pertama adalah melakukan penelitian pengguna untuk memahami kebutuhan dan harapan profesional medis. Penelitian ini dapat dilakukan dengan wawancara, survei, atau observasi.

2. Merancang antarmuka pengguna yang sesuai
Berdasarkan hasil penelitian pengguna, saya akan merancang antarmuka pengguna yang sesuai dengan kebutuhan dan harapan profesional medis. Antarmuka pengguna ini harus:

Intuitif, artinya mudah dipahami dan digunakan tanpa harus membaca instruksi.
Fungsional, artinya dapat memenuhi kebutuhan profesional medis untuk melakukan tugas-tugas mereka.
Aman, artinya melindungi pasien dari risiko kesalahan.
