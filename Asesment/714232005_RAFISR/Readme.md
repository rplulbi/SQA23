ASSESMENT – SOFTWARE QUALITY


Nama 		: Rafi Saumi Rustian
NPM		: 714232005
Studi Kasus	: Perusahaan B sedang mengembangkan platform e-commerce baru.


1.	Bagaimana QA dapat memverifikasi keamanan platform e-commerce ini untuk melindungi data sensitif pelanggan, seperti informasi pembayaran dan data pribadi?

Quality assurance adalah proses mengevaluasi dan mendokumentasikan yang telah dibuat selama siklus pengembangan perangkat lunak (SDLC). Tujuan utama dilakukan quality assurance untuk memastikan produk yang telah dibuat telah sesuai dengan persyaratan yang telah ditetapkan. Software testing dan quality assurance merupakan bagian yang tidak terpisah dari siklus pengembangan perangkat lunak (SDLC) seperti halnya desain, code dan analisis. Software testing sendiri merupakan elemen kritis dari software quality assurance. Quality assurance adalah pendekatan manajemen secara keseluruhan untuk memastikan keberhasilan penerapan tujuan kualitas perusahaan. 
Sebuah situs e-commerce harus terus menjaga keamanan website. Keamanan situs e-commerce sangat penting untuk kelancaran bisnis dan kenyamanan pelanggan.
setiap hari, jutaan transaksi terjadi pada situs e-commerce. Kemudahan dalam berbelanja online menjadikan situs e-commerce sebagai pilihan utama dalam belanja. Disisi lain, serangan cyber terus mengintai situs e-commerce. Mulai dari serangan DDoS hingga Phisihing dan pencurian data kartu kredit sering terjadi pada situs e-commerce.
Untuk melindungi informasi sensitif pelanggan bisa dilakukan beberapa pengujian diantaranya :
-	Pengujian Password atau Kata Sandi
Pengujian enkripsi katasandi di uji dengan memecahkan kata sandi yangsudah di enkripsi dengan cara dictionaryattackmelalui tools password cracked yaituhashcat. Dictionary attack dilakukan dengan menyediakansekumpulan password yang paling memungkinkandigunakan, dengan daftar password yangtelahdisiapkan, selanjutnya mengeliminasi setiapdaftaryang telah dicoba dan gagal.
-	Pengujian OTP
pengujian test case OTP dengan beberapa kategori seperti kode OTP terkirim ke email akun pengguna yang sudah terdaftar, kode OTP akan kadaluarsa pada waktu tertentu, kode OTP hanya dikirimkan ke email pengguna, kode OTP yang kadaluarsa tidak dapat digunakan, pengiriman ulang kode OTP berfungsi dengan baik, kode OTP lama tidak akan valid jika pengguna meminta ulang kode OTP yang baru, kode OTP yang diberikan terbatas yaitu 3 kali pengiriman, akun pengguna akan di ban untuk beberapa waktu, saat sudah melebihi batas mengirim ulang kata sandi, dll.


2.	Bagaimana QA dapat menguji performa platform e-commerce ini dalam skenario beban tinggi, seperti saat ada peningkatan lalu lintas selama periode penjualan besar-besaran?

Untuk menguji platform selama pengingkatan beban kerja termasuk kedalam tipe Load Testing, Load Testing merupakan jenis Performance Testing yang dilakukan untuk memastikan kemampuan sistem dalam menghadapi beban tertentu serta memastikan sebuah sistem dapat berada pada kondisi terbaik pada kondisi penggunaan yang diharapkan. Load Testing akan melakukan pengujian dengan memberikan beban pengguna dengan jumlah yang bervariasi atau dengan jumlah yang cukup besar agar bisa melakukan evaluasi terhadap responsivitas terhadap perangkat lunak yang sedang diuji. Untuk pengujian dapat dilakukan dengan performance testing tool yang sudah ada. 
Beberapa hal yang dapat diajdikan acuan dalam load testing adalah total waktu rata-rata untuk melakukan keseluruhan threads dalam waktu milisekon, waktu terlama yang digunakan oleh satu user untuk mengeksekusi test scenario yang dijalankan, waktu tercepat yang digunakan oleh satu user untuk mengeksekusi test scenario yang dijalankan, jumlah error dalam satuan persen yang terjadi pada skenario yang dijalankan, penyebaran kumpulan data relatif terhadap rata-ratanya. Semakin kecil nilai dari std.dev menunjukkan bahwa data yang dijalankan pada masing-masing label semakin konsisten. Nilai dari std.dev sebaiknya lebih kecil atau sama dengan setengah dari nilai average dari setiap label, dsb.


3.	Apa strategi yang tepat untuk menguji ketersediaan dan keandalan platform e-commerce ini, terutama saat menghadapi serangan DDoS atau serangan lainnya?

DDoS adalah singkatan dari Distributed Denial of Service, salah satu ancaman siber yang dapat mengguncang fondasi keamanan digital website Anda dalam sekejap.
Jenis serangan ddos :
-	Serangan Aplikasi (Application Attacks)
Serangan ini menyebabkan lapisan server bertanggung jawab merespons dan menerima permintaan HTTP serta memuat halaman-halaman situs web. Kategori serangan ini bertujuan menguras seluruh sumber daya yang dimiliki oleh target. 
-	Serangan Protokol (Protocol Attacks)
protocol Attacks pada DDoS adalah serangan yang umumnya memaksa perangkat jaringan dan sumber daya server, seperti load balancer dan firewall, hingga melebihi kapasitas awal mereka.
-	Serangan Volumetrik (Volumetric Attacks)
Serangan Volumetrik bertujuan membanjiri seluruh bandwith server antara target dan jaringan internet. dengan jumlah traffic yang relatif besar.

Ciri terkena ddos :
-	Bandwidth melonjak drastis secara tiba-tiba dan berlangsung terus-menerus selama serangan
-	Beban CPU meningkat yang mengakibatkan penurunan kinerja server sehingga situs web atau layanan tidak dapat diakses.
-	menerima peringatan mencurigakan pada server. 
-	Adanya kesalahan HTTP di mana pengguna mungkin sering melihat pesan kesalahan seperti "502 Bad Gateway" atau "504 Gateway Timeout."

Cara mengantisipasi :
-	Memaksimalkan Kapasitas pada Sumber Daya Server
memastikan bahwa server Anda memiliki kapasitas yang cukup untuk menangani beban traffic yang datang selama serangan.
-	Memantau Traffic Secara Berkala (Monitoring Traffic)
melakukan pemantauan traffic secara berkala. Sebagai upaya mengatasi serangan DDoS, Anda perlu mendeteksi adanya anomali atau peningkatan lalu lintas yang mencurigakan sedini mungkin.  memantau jaringan, mengidentifikasi pola-pola yang tidak wajar, serta bertindak cepat dalam merespons serangan tersebut
-	Menggunakan Layanan Proteksi DDoS
mendeteksi serangan DDoS secara otomatis dan mengarahkan traffic mencurigakan ke luar jaringan Anda guna menjaga sumber daya tetap aman.
-	Menggunakan Content Delivery Network (CDN)
CDN akan mengakses konten dari server di berbagai wilayah geografis. Langkah ini membantu mempersempit dampak serangan DDoS dengan mendistribusikan traffic ke sejumlah server berbeda dan menjauhkan server utama Anda dari serangan berbahaya.
-	Membatasi Akses IP
mengatur firewall agar membatasi akses halaman IP Anda hanya kepada alamat yang sah dan terkonfigurasi resmi.
-	Berhenti Menggunakan Proteksi Koneksi Terbuka
menggantinya dengan koneksi yang lebih aman seperti TCP (Transmission Control Protocol)
-	Menggunakan Firewall
mengidentifikasi dan memblokir traffic mencurigakan sesegera mungkin

4.	Bagaimana QA dapat memastikan kesesuaian platform e-commerce ini dengan standar kepatuhan industri yang relevan, seperti PCI-DSS (Payment Card Industry Data Security Standard)?

Ada tiga  cakupan penilaian PCI DSS
a.	Data
lingkungan data pemegang kartu (CDE), sistem yang terhubung ke sistem dan sistem yang berdampak pada keamanan berada di dalam batas cakupan penilaian, sementara sistem yang tidak tepercaya dan di luar ruang lingkup berada di luar batas ruang lingkup penilaian singkat ini.
b.	Koneksi, 
Untuk tujuan mengevaluasi cakupan PCI, koneksi ditentukan oleh hal berikut:
Transportasi informasi aktif yang menghubungkan dua komputer atau
System manakah dari dua pihak yang memulai panggilan
c.	Sistem
cakupan sistem ditentukan sebagai berikut:
a.	Komponen sistem yang tercakup dalam PCI DSS:
-	Sistem yang berada dalam CDE memiliki salah satu hal berikut:
•	Komponen sistem menyimpan, memproses, atau mengirimkan CHD atau SAD.
•	Komponen sistem berada pada segmen jaringan yang sama, misalnya pada subnet atau VLAN yang sama dengan sistem yang menyimpan, memproses, atau mengirimkan CHD.
-	Sistem yang terhubung ke sistem yang berdampak pada keamanan atau yang mengalami salah satu hal berikut:
•	Komponen sistem terhubung langsung ke CDE.
Komponen sistem berdampak pada konfigurasi atau keamanan CDE.
•	Komponen sistem mengelompokkan sistem CDE dari sistem dan jaringan di luar cakupan.
•	Komponen sistem secara tidak langsung terhubung ke CDE.
•	Komponen sistem menyediakan layanan keamanan ke CDE.
•	Komponen sistem mendukung persyaratan PCI DSS.
b.	Komponen sistem dapat dianggap tidak tepercaya dan berada di luar cakupan PCI DSS jika semua hal berikut berlaku:
-	Komponen sistem tidak menyimpan, memproses, atau mengirimkan CHD atau SAD.
-	Komponen sistem bukan merupakan segmen jaringan yang sama, misalnya pada subnet atau VLAN yang sama, dengan sistem yang menyimpan, memproses, atau mengirimkan CHD atau SAD.
-	Komponen sistem tidak dapat terhubung ke sistem apa pun di CDE.
-	Komponen sistem tidak memenuhi kriteria apa pun untuk sistem yang terhubung ke atau yang berdampak pada keamanan.
Sistem di luar cakupan dapat mencakup sistem yang terhubung ke komponen sistem yang terhubung atau berdampak pada keamanan, di mana kontrol yang ada digunakan untuk mencegah sistem di luar ruang lingkup untuk mendapatkan akses ke CDE dengan menggunakan komponen sistem dalam ruang lingkup.

5.	Bagaimana QA dapat menguji integrasi platform e-commerce ini dengan sistem backend, seperti sistem manajemen inventaris atau sistem keuangan perusahaan?

Backend atau sering di sebut server side pada dasarnya adalah tempat dimana proses suatu aplikasi atau sistem berjalan di back end ini data di proses ditambahkan, diubah atau dihapus.Back end mengurusi segala sesuatu yang biasanya tidak dilihat atau berinteraksi langsung kepada user, seperti database dan server. Biasanya orang yang bekerja sebagai back end developer adalah programmer atau developer yang fokus pekerjaannya pada keamanan, desain sistem , dan managemen data pada system.

Metode yang digunakan dalam perancangan REST API pada penelitian adalah System Development Life Cycle (SDLC), yang mempunyai tahapan sebagai berikut:
a.	Identifikasi: identifikasi dilakukan untuk mendapatkan kebutuhan informasi terkait transaksi jual beli khususnya untuk . 
b.	Analisis: pada tahapan ini dilakukan pengumpulan data dan informasi yang berhubungan dengan data apa saja yang harus ditampilkan oleh Backend.
c.	Perancangan: pada tahapan ini peneliti merancang arsitektur sistem dan merancang REST API. Selain itu juga merancang database yang akan digunakan.
d.	Implementasi: pada tahapan ini dikembangkan REST API dengan framework Spring Boot dan frontend dengan menggunakan bahasa pemrograman Java. Dilakukan pengujian dengan data dummy untuk pengiriman data API berbentuk JSON ke pihak frontend. Skema basis data dibuat menggunakan Dewa.io Visual Studio Code dengan ekstensi Live Server. GIT sebagai Version Control System, web browser menggunakan Chrome dan postman untuk mempermudah testing REST API. Tipe database PostgreSQL serta Sequelize untuk mempermudah lalu lintas data ke dalam database.
e.	Uji Coba/Testing: tahap terakhir melaksanakan uji coba terhadap masingmasing REST API yang telah dibuat pada situs URL (Uniform Resource Locator) website menggunakan bantuan postman. Tujuan dilakukan uji coba adalah agar API dapat berjalan menghantar-kan data secara optimal

6.	Jelaskan langkah-langkah yang akan Anda ambil untuk menguji keandalan dan ketersediaan platform e-commerce selama periode lonjakan lalu lintas atau peningkatan beban kerja!

Langkah yang ambil adalah melakukan Non-Functional testing. Non-Functional testing  adalah jenis pengujian perangkat lunak untuk menguji parameter non-fungsional seperti reliability atau keandalan, load atau beban, performance atau kinerja, dan security atau keamanan. Non-Functional testing dilakukan setelah functional testing selesai. Pengujian ini juga sangat penting karena digunakan untuk memastikan kepuasan pelanggan atau user. Tipe-tipe testing yang termasuk dalam non-functional testing antara lain :
-	Performance Testing
-	Load Testing
-	Security Testing
-	Portability Testing
-	Accountability Testing
-	Reliability Testing
-	Efficiency Testing
-	Usability Testing
-	Stress Testing
-	Scalability Testing

Untuk menguji platform selama pengingkatan beban kerja termasuk kedalam tipe Load Testing, Load Testing merupakan jenis Performance Testing yang dilakukan untuk memastikan kemampuan sistem dalam menghadapi beban tertentu serta memastikan sebuah sistem dapat berada pada kondisi terbaik pada kondisi penggunaan yang diharapkan. Load Testing akan melakukan pengujian dengan memberikan beban pengguna dengan jumlah yang bervariasi atau dengan jumlah yang cukup besar agar bisa melakukan evaluasi terhadap responsivitas terhadap perangkat lunak yang sedang diuji. Untuk pengujian dapat dilakukan dengan performance testing tool yang sudah ada. 
Beberapa hal yang dapat diajdikan acuan dalam load testing adalah total waktu rata-rata untuk melakukan keseluruhan threads dalam waktu milisekon, waktu terlama yang digunakan oleh satu user untuk mengeksekusi test scenario yang dijalankan, waktu tercepat yang digunakan oleh satu user untuk mengeksekusi test scenario yang dijalankan, jumlah error dalam satuan persen yang terjadi pada skenario yang dijalankan, penyebaran kumpulan data relatif terhadap rata-ratanya. Semakin kecil nilai dari std.dev menunjukkan bahwa data yang dijalankan pada masing-masing label semakin konsisten. Nilai dari std.dev sebaiknya lebih kecil atau sama dengan setengah dari nilai average dari setiap label, dsb.

7.	Buatlah serangkaian skenario pengujian untuk memverifikasi integrasi platform e-commerce dengan sistem backend yang relevan, seperti sistem manajemen inventaris atau sistem keuangan!

Backend merupakan proses sistem yang berjalan di belakang layar sebuah website atau aplikasi. Pada penelitian ini backend dikembangkan dengan menggunakan bahasa pemograman Java. Backend membantu mengkomunikasikan informasi atau data yang terdapat pada basis data kepada user melalui tampian User Interface (UI) dari frontend. Aplikasi client dalam versi android dan website pada penelitian ini menggunakan métode REST untuk melakukan integrasi Application Programming Interface. 
System Integration Testing (SIT) adalah salah satu proses dalam software development lifecycle, berupa pengujian yang dilakukan untuk memastikan setiap komponen dari suatu software dapat berfungsi secara menyeluruh dan bekerja dengan baik.
Pengujian ini memastikan bahwa seluruh fungsi sesuai dengan konfigurasi dan fungsionalitasnya berdasarkan:
-	Functional Design Specifications,
-	Technical Specifications,
-	Business Requirements, dan
-	dokumen-dokumen pembangun sistem lainnya.
Hal ini dilakukan untuk memastikan bahwa sistem dibangun sudah terintegrasi dan sesuai dengan spesifikasi yang diharapkan. Sekalipun setiap unit diuji secara individual, masih ada kemungkinan gagal ketika terintegrasi secara keseluruhan, karena biasanya banyak masalah yang muncul ketika subsistem berinteraksi satu sama lain. Hal ini dapat diselesaikan dengan menjalankan system integration testing. Pedekatan yang dapat dilakukan dalamSIT adalah :
a.	Top-Down
Pendekatan ini direkomendasikan jika ada program yang tidak lengkap di level bawah.
Dalam pendekatan ini, integration testing akan dilakukan dari atas ke bawah.
Program yang tidak selesai di level bawah akan diganti dengan stub (program simulasi yang menggantikan program yang disebut).
Pertama, akan ditest Main.Prg dan Sub 1, lalu Sub 1 dan Procedure 1.
Selanjutnya Main.Prg dan Sub 2, dilanjutkan ke Sub 2 dan Function 2, kemudian Sub 2 dan Procedure 2.
b.	Bottom-Up
Pendekatan ini direkomendasikan ketika ada program yang belum selesai di level atas.
Dalam pendekatan ini, integration testing akan dilakukan dari bawah ke atas.
Program yang tidak selesai di atas akan diganti dengan driver (program simulasi yang menggantikan program yang disebut).
c.	Sandwich
Pendekatan ini menggabungkan pendekatan Top-down dan Bottom-up dari integration testing.
Di level tengah ini, modul diuji menggunakan driver dan stub.
d.	Big bang
Pendekatan ini direkomendasikan ketika semua unit source code tersedia dan telah dilakukan unit testing.
Dalam pendekatan ini, semua unit source code akan digabungkan bersama sebagai sistem yang besar, kemudian integrasi di antara semua unit ini akan divalidasi.

8.	Jelaskan bagaimana Anda akan menguji kemampuan platform e-commerce untuk melindungi informasi sensitif pelanggan, seperti data pembayaran!

Untuk melindungi informasi sensitif pelanggan bisa dilakukan beberapa pengujian diantaranya :
-	Pengujian Password atau Kata Sandi
Pengujian enkripsi katasandi di uji dengan memecahkan kata sandi yangsudah di enkripsi dengan cara dictionaryattackmelalui tools password cracked yaituhashcat. Dictionary attack dilakukan dengan menyediakansekumpulan password yang paling memungkinkandigunakan, dengan daftar password yangtelahdisiapkan, selanjutnya mengeliminasi setiapdaftaryang telah dicoba dan gagal.
-	Pengujian OTP
pengujian test case OTP dengan beberapa kategori seperti kode OTP terkirim ke email akun pengguna yang sudah terdaftar, kode OTP akan kadaluarsa pada waktu tertentu, kode OTP hanya dikirimkan ke email pengguna, kode OTP yang kadaluarsa tidak dapat digunakan, pengiriman ulang kode OTP berfungsi dengan baik, kode OTP lama tidak akan valid jika pengguna meminta ulang kode OTP yang baru, kode OTP yang diberikan terbatas yaitu 3 kali pengiriman, akun pengguna akan di ban untuk beberapa waktu, saat sudah melebihi batas mengirim ulang kata sandi, dll.

9.	Identifikasi beberapa metode pengujian yang dapat digunakan untuk memverifikasi keamanan platform e-commerce terhadap serangan potensial, seperti serangan injeksi SQL atau cross-site scripting (XSS)!

SQL Injection adalah kerentanan yang terjadi ketika penyerang memiliki kemampuan untuk mempengaruhi Structured Query Language (SQL) Query yang melewati suatu aplikasi ke database back-end.dengan mampu mempengaruhi apa yang akan diteruskan ke database, penyerang dapat memanfaatkan sintaks dan kemampuan dari SQL, serta kekuatan dan fleksibilitas untuk mendukung operasi dan fungsionalitas sistem yang tersedia ke database. serangan SQL Injection sangat berbahaya karena penyerangan yang telah berhasil memasuki database sistem dapat melakukan manipulasi data yang ada pada database sistem. Proses manipulasi data yang tidak semestinya oleh penyerang dapat menimbulkan kerugian bagi pemilik website yang terinjeksi kebocoran data dan informasi merupakan hal yang fatal. Data-data tersebut dapat disalahgunakan oleh pihak yang tidak bertanggung jawab.
Untuk skenarion pengujian injeksi SQL dilakukan dengan memasukkan string-string di tempat input yang nantinya akan memodifikasi source code dari aplikasi berbasis web yang akan menjadi target. Berikut adalah tahapan-tahapan yang dilakukan dalam skenario pengujian ini
a.	Injeksi URL Aplikasi berbasis web yang menjadi target adalah web aplikasi bwapp yang sudah terinstall di laptop. Hal yang pertama dilakukan adalah membuka alamat web aplikasi bwapp dari browser. Setelah terbuka maka disinilah proses injeksi dijalankan. Proses yang dilakukan adalah menambahkan string-string yang dapat mengganggu jalannya web aplikasi bwapp. String-string tersebut antara lain dapat berupa tanda petik satu („) tanda minus (-), dsb. 
b.	Injeksi di form search Pada saat membuka web aplikasi bwapp localhost/bwapp, maka alamat tersebut akan menampilkan login form. Login dan memilih SQL Injection Get/Search. Disinilah proses SQL Injection dapat dilakukan. Input form pada search bar dapat ditambahkan string-string yang bukan input seharusnya seperti tanda petik satu („), dsb. String ini yang akan memanipulasi query yang ada dalam source code web aplikasi bwapp.
c.	Memberi pencegahan Setelah web aplikasi bwapp diuji keamanannya, maka baru source code dari web ini diberi pencegahan. Pencegahan ini dimaksudkan agar proses SQL Injection ini tidak berhasil dijalankan. Pencegahan yang diberikan tergantung dari pengujian yang sudah dilakukan, seperti apakah SQL Injection yang berhasil dilakukan. Bentuk pencegahan ini bisa berupa pembatalan atau pelarangan perintah masukan input yang seharusnya tidak boleh dimasukkan, seperti string-string atau integer-integer yang dapat mengganggu source code web.

10.	Bagaimana Anda akan melakukan pengujian fungsional untuk memverifikasi bahwa platform e-commerce beroperasi dengan benar dan memenuhi persyaratan bisnis yang ditetapkan?

Untuk pengujian ini termasuk kedalam tipe Acceptance Testing. Testin gyang dilakukan pad atahap terakhir untuk memastikan keselutuhan system beroperasi dengan baik dan benar. Seperti integration testing, acceptance testing juga meliputi testing pada keseluruhan aplikasi. Perbedaannya terletak pada siapa yang melakukan testing. Pada tahap ini, end-user yang terpilih melakukan testing terhadap fungsi-fungsi aplikasi. Testing yang dilakukan merupakan simulasi penggunaan nyata dari aplikasi pada lingkungan yang sebenarnya. Acceptance testing dilakukan untuk menemukan apakah persyaratan spesifikasi atau kontrak sudah terpenuhi sesuai dengan requirement di awal. 
Langkah-langkah dalam menjalankan User Acceptance Test, yaitu sebagai berikut: 
a.	Rencana UAT 
Hal pertama yang dilakukan adalah menyiapkan perencanaan. Rencana uji ini adalah dokumen yang menguraikan kasus uji yang akan digunakan untuk memvalidasi hasil kerja.
b.	Kasus Uji
Setelah melakukan rencana tersebut, kita membuat kasus uji. Pada tahap kasus uji memberikan instruksi tentang cara menguji perangkat lunak. Dengan ini, untuk melakukan proses sesuai serta efektif, sangat penting untuk menulis test case yang sesuai.
c.	Testing
Menjalankan test setelah melakukan perencanaan demi menentukan apakah perangkat lunak memenuhi spesifikasi yang diperlukan, Di sini maka akan diuji menggunakan data sampel pada server UAT klien.
d.	Input pada Matriks 
Hasil harus dimasukkan ke dalam matriks ketertelusuran, dimana juga akan menunjukkan bagaimana kemajuan pengujian. Jika pengujian berhasil dan user telah memberikan persetujuannya, BA mencatatnya dalam matriks ketertelusuran dan beralih ke fase penerapan.
e.	Proses Verifikasi 
Verifikasi bahwa tujuan bisnis tercapai. Jika persyaratan tidak terpenuhi, masalah akan didokumentasikan dalam kolom cacat matriks ketertelusuran di sebelah kasus uji, dan perangkat lunak akan dikirim ke tim pengembangan untuk diperbaiki.

