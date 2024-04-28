import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

#Ukuran layar
Window.size = (1280, 720)
Window.fullscreen = True

#Layar awal
class Started(Screen):
    pass

#Layar amenu
class Menu(Screen,Widget):
    pass

#Layar aboutme
class About_me(Screen,Widget):
    pass

#Layar about hardwares
class Pilih(Screen,Widget):
    pass

#Layar hasil diagnosa
class Problem(Screen, Widget):
    pass

#Screen manager
class WindowManager(ScreenManager):
    pass

#Layar wiki hardware
class Wiki(Screen):
    hardware = ''
    component= ''
    def type_hardware(self, instance, number):
        self.hardware = f'{number}'
        if self.hardware == "1":
            self.component = "               CPU (Central Processing Unit) \nDalam bahasa Indonesia disebut sebagai Unit\nPemrosesan Pusat. CPU adalah bagian utama dari\nkomputer yang bertanggung jawab untuk mengeksekusi\ninstruksi-instruksi program dan melakukan operasi \npemrosesan data. Ini adalah otak dari sistem komputer\ndan berperan penting dalam menjalankan berbagai tugas\ndan program."
        elif self.hardware == "2":
            self.component = "                 Random Access Memory (RAM)\n\nRAM adalah tempat penyimpanan sementara untuk\ndata dan instruksi yang sedang digunakan oleh CPU.\nData dalam RAM dapat diakses lebih cepat daripada dari\npenyimpanan jangka panjang (seperti hard drive atau SSD)."
        elif self.hardware == "3":
            self.component = "                     HDD (Hard Disk Drive)\n\nHDD adalah jenis penyimpanan mekanis menggunakan\npiringan magnetik yang berputar untuk menyimpan data.\nData dibaca atau ditulis menggunakan kepala pembaca\nyang bergerak secara fisik di atas piringan.\n\nKecepatan: HDD cenderung lebih lambat dalam\nmembaca dan menulis data dibandingkan SSD.\nKecepatannya diukur dalam RPM (rotasi per menit)."
        elif self.hardware == "4":
            self.component = "SSD adalah jenis penyimpanan tanpa bagian bergerak.\nIa menggunakan chip memori flash (sering NAND-based)\nuntuk menyimpan data. Karena tidak ada komponen\nmekanis yang berputar, SSD memiliki kecepatan\nakses yang lebih cepat\n\nKecepatan: SSD jauh lebih cepat dalam membaca dan\nmenulis data dibandingkan HDD. Ini dapat menyebabkan\nwaktu booting yang lebih cepat, pembukaan aplikasi\nyang lebih cepat dan responsif."
        elif self.hardware == "5":
            self.component = "                                 Motherboard\n\nadalah papan sirkuit utama yang menghubungkan berbagai \nkomponen komputer,termasuk CPU, RAM, kartu grafis,\ndan perangkat lainnya.\n\nMotherboard juga menyediakan koneksi untuk port I/O,\nseperti USB, HDMI, dan Ethernet."
        elif self.hardware == "6":
            self.component = "                 POWER SUPPLY UNIT (PSU)\n\nPSU menyediakan daya listrik yang diperlukan\noleh semua komponen dalam komputer.\nPSU mengonversi daya listrik dari sumber listrik\neksternal menjadi bentuk yang dapat digunakan\noleh komponen-komponen dalam komputer."
        elif self.hardware == "7":
            self.component = "                 Graphics Processing Unit (GPU)\n\nGPU mengelola tugas-tugas grafis dan memproses data\nyang berkaitan dengan tampilan visual pada layar\nGPU sangat penting untuk permainan video,\npemrosesan grafis, dan tugas-tugas yang\nmemerlukan pemrosesan paralel."
        elif self.hardware == "8":
            self.component = "                 BIOS (Basic Input/Output System)\n\nadalah suatu jenis perangkat lunak firmware\nyang disematkan pada motherboard komputer.\n\nBIOS berfungsi sebagai antarmuka antara sistem operasi\ndan perangkat keras komputer, memungkinkan komunikasi\ndasar antara keduanya"
        elif self.hardware == "9":
            self.component = "                                       Wi-Fi\n\nadalah teknologi nirkabel yang memungkinkan perangkat\nelektronik, seperti komputer, smartphone, tablet, dan\nperangkat lainnya, untuk terhubung ke jaringan internet\natau jaringan lokal tanpa menggunakan kabel fisik."
        elif self.hardware == "10":
            self.component = "                                      Monitor\n\nadalah perangkat output atau tampilan yang digunakan\nuntuk menampilkan informasi grafis dan visual\ndari komputer atau perangkat lainnya.\n\nFungsinya adalah untuk menyajikan data dalam\nbentuk visual kepada pengguna, sehingga pengguna\ndapat melihat dan berinteraksi dengan informasi tersebut."
        elif self.hardware == "11":
            self.component = "                         Kabel SATA (Serial ATA)\n\nadalah kabel yang digunakan untuk menghubungkan\nperangkat penyimpanan, seperti hard drive (HDD),\nsolid-state drive (SSD),atau perangkat optik, ke motherboard\ndalam sebuah komputer.Kabel ini membawa data antara\nperangkat penyimpanan dan motherboard, serta menyediakan\ndaya listrik jika diperlukan."
        elif self.hardware == "x":
            self.component = " "
        else:
            self.component = "error"

         #Output Hardware
        self.ids.hardware.text = f'{self.component}'
        Clock.schedule_once(self.shapes, 0)
        Clock.schedule_once(self.picture_hardware, 0)

    def shapes(self,dt):
        hardware = self.hardware
        if hardware == "1" or hardware == "2" or hardware == "3" or hardware == "4" or hardware == "5" or hardware == "6" or hardware == "7" or hardware == "8" or hardware == "9" or hardware == "10" or hardware == "11":
            self.ids.shapes.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Rectangle_Menu2.png')
            self.ids.button_close.background_normal=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Close.png')
        elif hardware == "x":
            self.ids.button_close.background_normal=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png')
            self.ids.shapes.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png')

    def picture_hardware(self, dt):
        hardware = self.hardware
        if hardware == "1":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/CPU2.png')
        elif hardware == "2":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/RAM.png')
        elif hardware == "3":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/HDD.png')
        elif hardware == "4":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/SSD.png')
        elif hardware == "5":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Motherboard.png')
        elif hardware == "6":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/PSU.png')
        elif hardware == "7":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GPU.png')
        elif hardware == "8":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BIOS.png')
        elif hardware == "9":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/WIFI.png')
        elif hardware == "10":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/MONITOR.png')
        elif hardware == "11":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/KABELSATA.png')
        elif hardware == "x":
            self.ids.picture_hardware.source=str('C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png')
        
#Layar utama
class Main_Screen(Screen, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    checks = []

    #Menampilkan checkbox dan rule
    def checkbox_click(self, instance, value, rules):
        if value == True:
            Main_Screen.checks.append(rules)
        else:
            Main_Screen.checks.remove(rules)
    
    #Mendiagnosa kerusakan berdasar rule yang ada
    def problem_diagnose(self):
        cheks = Main_Screen.checks
        rules = ''
        for x in Main_Screen.checks:
            rules = f'{rules} {x}'

        #LOGIKA PAKAR
        if rules == " R1 R2":
            problem = "Monitor Rusak, Solusi: Periksa kabel monitor, pastikan monitor dan kabelnya berfungsi dengan baik."
        elif rules == " R3 R11":
            problem = "Memori Rusak, Solusi: Periksa dan bersihkan RAM, pastikan koneksi dan slot RAM baik."
        elif rules == " R6 R7 R8 R10 R21 R22":
            problem = "HDD Rusak, Solusi: Periksa HDD, lakukan scanning disk, dan periksa koneksi pada device manager dan BIOS. "
        elif rules == " R1 R3 R5 R9 R10 R12 R13":
            problem = "VGA Rusak, Solusi: Periksa driver VGA, pastikan setting device sesuai, dan periksa koneksi audio."
        elif rules == " R10 R13":
            problem = "Sound Card Rusak, Solusi: Periksa driver sound card, pastikan setting device sesuai, dan periksa koneksi audio."
        elif rules == " R11 R15":
            problem = "OS Bermasalah, Solusi: Periksa pesan error saat OS loading, lakukan troubleshooting pada OS."
        elif rules == " R7 R12":
            problem = "Aplikasi Crash/Rusak, Solusi: Periksa aplikasi yang menyebabkan crash, lakukan troubleshooting pada aplikasi."
        elif rules == " R16 R17":
            problem = "Power Supply Rusak, Solusi: Periksa kipas pendingin, pastikan tidak ada tanda-tanda kerusakan, dan periksa daya listrik."
        elif rules == " R1 R3 R4 R5":
            problem = "Prosesor Rusak, Solusi: Periksa kondisi prosesor, pastikan tidak ada pesan error pada BIOS. "
        elif rules == " R18 R19":
            problem = "Memory Kurang, Solusi: Tambahkan RAM atau atasi kekurangan virtual memory pada Windows."
        elif rules == " R20":
            problem = "Memory VGA Kurang, Solusi: Tambahkan kartu grafis yang lebih kuat atau perbarui driver grafis."
        elif rules == " R9 R19":
            problem = "Clock Prosesor Kurang Tinggi, Solusi: Periksa konfigurasi BIOS untuk meningkatkan clock prosesor jika memungkinkan. Perbarui atau tingkatkan prosesor jika diperlukan."
        elif rules == " R21 ":
            problem = "Kabel IDE/SATA/ATA Rusak, Solusi: Ganti kabel yang rusak dengan kabel yang baru dan pastikan koneksi ke perangkat keras benar."
        elif rules == " R5 R23 ":
            problem = "Kurang Daya pada PSU, Solusi: Gantilah Power Supply Unit (PSU) dengan unit yang memiliki daya yang cukup untuk mendukung semua perangkat keras. "
        elif rules == " R10 ":
            problem = "Perangkat USB Rusak, Solusi: Coba ganti port USB atau hub USB. Jika perangkat USB masih tidak terdeteksi, coba ganti kabel atau perangkat USB itu sendiri."
        elif rules == " R10 R24 ":
            problem = "Keyboard Rusak, Solusi: Ganti keyboard dengan yang baru. Pastikan kabel atau konektornya tidak rusak."
        elif rules == " R10 R25":
            problem = "Mouse Rusak, Solusi: Solusi: Ganti mouse dengan yang baru. Pastikan kabel atau konektornya tidak rusak. Jika menggunakan mouse nirkabel, pastikan baterai atau daya sudah mencukupi."
        else:
            problem = "Sistem Tidak Dapat Mendeteksi"

        #Output Problem
        test_problem = self.manager.get_screen("problem")
        test_problem.ids.output_problem.text = f'{problem}'

KV = '''
#:kivy 2.1.0
#:import utils kivy.utils
#: import WipeTransition kivy.uix.screenmanager.FadeTransition

WindowManager:
    Started:
        name: "started"
    Menu:
        name: "menu"
    Wiki:
        name: "wiki"
    Main_Screen:
        name: "main"
    Pilih:
        name: "pilih"
    About_me:
        name: "aboutme"
    Problem:
        name: "problem"

<Started>:
    FloatLayout:
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Logo.png'
                size: (200, 130)
                pos: (540,380)
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Rectangle_Start.png'
                size: root.width, root.height
                pos: self.pos
        Button:
            text: "GET STARTED"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/button.png'
            font_size:40
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GothamBold.ttf'
            color:0,0,0,1
            width: 400
            height: 100
            size_hint: (None, None)
            pos:(440,250)
            on_release:
                app.root.current = "menu"
                root.manager.transition.direction = "up"

<Menu>:
    FloatLayout:
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Rectangle_Menu.png'
                size: root.width, root.height
                pos: self.pos
        Label:
            text:'MAIN MENU'
            color:0,0,0,1
            font_size: 50
            pos: (10,200)
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica-Bold.ttf'
        Button:
            text: "Diagnosa\\n Kerusakan Komputer"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Button.png'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GothamMedium.ttf'
            color:0,0,0,1
            font_size:25
            width: 400
            height: 100
            size_hint: (None, None)
            halign:'center'
            pos:(440,400)
            on_release:
                app.root.current = "pilih"
                root.manager.transition.direction = "up"
        Button:
            text: "Wiki Hardware"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Button.png'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GothamMedium.ttf'
            color:0,0,0,1
            font_size:30
            width: 400
            height: 100
            size_hint: (None, None)
            pos:(440,275)
            on_release:
                app.root.current = "wiki"
                root.manager.transition.direction = "up"
        Button:
            text: "About Me"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Button.png'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GothamMedium.ttf'
            color:0,0,0,1
            font_size:30
            width: 400
            height: 100
            size_hint: (None, None)
            pos:(440,150)
            on_release:
                app.root.current = "aboutme"
                root.manager.transition.direction = "up"

<About_me>:
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
        Image:
            source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Aboutme.png'
            size_hint: (None, None)
            size: (150, 80)
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
        GridLayout:
            cols: 1
            Label:
                text: 'TENTANG KAMI'
                color: 0, 0, 0, 1
                font_size: 30
                size_hint: (None, None)
                width: 1280
                height: 70
                halign: 'center'
                font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica-Bold.ttf'
            BoxLayout:
                orientation: 'horizontal'
                Image:
                    source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Fauzi.png'
                    size_hint: (None, None)
                    size: (250, 250)
                    width: 400  # Sesuaikan dengan lebar yang diinginkan
                    height: 200
                    pos_hint: {'center_x': 0.55, 'center_y': 0.55}
                Label:
                    text: 'Fauzi Rakhman Dwi Wiyana. \\nLahir di Lampung, pada tanggal 22 April 2003.\\nBerasal dari Kotabumi, Lampung Utara.\\nDia merupakan mahasiswa Jurusan Fisika Fakultas MIPA Universitas Lampung.\\nMengambil konsentrasi Fisika Instrumentasi.\\nHe says,"Kalau Orang lain bisa, kenapa harus aku."\\nYou can find Fauzi at:\\nEmail: fauzi.rakhmandwi2001@students.unila.ac.id\\nInstagram : @Fauzirakhmannn'
                    color: 0, 0, 0, 1
                    font_size: 18
                    size_hint: (None, None)
                    width: 700 # Sesuaikan dengan lebar yang diinginkan
                    height: 30
                    halign: 'left'
                    font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica-Bold.ttf'
                    pos_hint: {'center_y': 0.55}  # Geser ke atas
            BoxLayout:
                orientation: 'horizontal'
                Image:
                    source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Agriffa.png'
                    size_hint: (None, None)
                    size: (250, 250)
                    width: 400  # Sesuaikan dengan lebar yang diinginkan
                    height: 200
                    pos_hint: {'center_x': 0.55, 'center_y': 0.5}
                Label:
                    text: 'Agriffa Nuzra Djolanda. \\nLahir di Jakarta, pada tanggal 5 Maret 2002.\\nBerasal dari Kota Bekasi, Jawa Barat.\\nDia merupakan mahasiswi Jurusan Fisika Fakultas MIPA Universitas Lampung.\\nMengambil konsentrasi Fisika Instrumentasi.\\nShe says,"Start with what you have, no matter how small it is."\\nYou can find Agriffa at:\\nEmail: agriffa.nuzradjolanda2003@students.unila.ac.id \\nInstagram : @agriffanzr'
                    color: 0, 0, 0, 1
                    font_size: 18
                    size_hint: (None, None)
                    width: 700 # Sesuaikan dengan lebar yang diinginkan
                    height: 30
                    halign: 'left'
                    font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica-Bold.ttf'
                    pos_hint: {'center_y': 0.5}  # Geser ke atas
    FloatLayout:
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Arrow.png'
                size: (40,40)
                pos: (20,650)
        Button:
            text: " "
            background_color:0,0,0,0
            font_size: 1
            width: 70
            height: 70
            size_hint: (None, None)
            pos:(20,650)
            on_release:
                app.root.current = "menu"
                root.manager.transition.direction = "down"
<Wiki>:
    Image:
        source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
    Image:
        source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Rectangle_Menu.png'
        size: root.width, root.height
        pos: (-310, 0)
    Image:
        id: shapes
        source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png'
        size: root.width, root.height
        pos: (465, 0)
    Image:
        id: picture_hardware
        source: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png'
        size: root.width, root.height
        pos: (300,150)

    Button:
        id:button_close
        text: ""
        background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Transparent.png'
        font_size: 20
        width: 60
        height: 60
        size_hint: (None, None)
        pos: (1180, 625)
        on_press:
            root.type_hardware(self, "x")
    Label:
        id: hardware
        color:0,0,0,1
        font_size: 20
        pos : (700,200)
        text_size: self.size
        halign: 'left'
        font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

    GridLayout:
        cols:1
        padding : 90
        Button:
            text: "CPU"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "1")
        Button:
            text: "RAM"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "2")
        Button:
            text: "HDD"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "3")
        Button:
            text: "SSD"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "4")
        Button:
            text: "MOTHERBOARD"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "5")
        Button:
            text: "PSU"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "6")
        Button:
            text: "GPU"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "7")
        Button:
            text: "BIOS"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "8")
        Button:
            text: "WIFI"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "9")
        Button:
            text: "MONITOR"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "10")
        Button:
            text: "KABEL SATA"
            background_color: 1,1,1,1
            font_size: 20
            width: 480
            height: 50
            size_hint: (None, None)
            on_press:
                root.type_hardware(self, "11")
    FloatLayout:
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Arrow.png'
                size: (30,30)
                pos: (50,640)
        Button:
            text: " "
            background_color: 0,0,0,0
            font_size: 1
            width: 30
            height: 30
            size_hint: (None, None)
            pos:(50,640)
            on_release:
                app.root.current = "menu"
                root.manager.transition.direction = "down"

<Pilih>:
    FloatLayout:
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Rectangle_Start.png'
                size: root.width, root.height
                pos: self.pos
        Label:
            text:'SILAHKAN PILIH\\n PERMASALAHAN KOMPUTER ANDA'
            color:0,0,0,1
            font_size: 30
            pos: (0,90)
            halign:'center'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica-Bold.ttf'
        Button:
            text:''
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Arrow.png'
            font_size:2
            width: 60
            height: 60
            size_hint: (None, None)
            pos: (350,490)
            on_release:
                app.root.current = "menu"
                root.manager.transition.direction = "down"
        Button:
            text: "Pilih Kerusakan"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/button.png'
            font_size:40
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/GothamBold.ttf'
            color:0,0,0,1
            width: 400
            height: 100
            size_hint: (None, None)
            pos:(440,250)
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "left"
        
<Main_Screen>:
    FloatLayout:
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
        Button:
            text:''
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Arrow.png'
            font_size:2
            width: 60
            height: 60
            size_hint: (None, None)
            pos: (0,660)
            on_release:
                app.root.current = "pilih"
                root.manager.transition.direction = "right"
        Button:
            text:"Submit"
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Submit.png'
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            size: (200,70)
            pos_hint: {'center_x': 0.9, 'center_y': 0.08}  # Ganti nilai 'center_y' sesuai kebutuhan
            halign: 'center'
            on_press:
                root.problem_diagnose()
            on_release:
                app.root.current = "problem"
                root.manager.transition.direction = "left"
        
    GridLayout:
        cols: 2
        row_force_default: False
        col_force_default: True
        padding : 50
        #Rules 1
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R1")
        Label:
            text:"Tidak ada gambar tampil pada monitor"
            width: 500
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 2
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R2")
        Label:
            text:"  Terdapat garis horizontal/vertikal di tengah monitor"
            width: 590
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 3
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R3")
        Label:
            text:"Tidak terdapat tampilan awal bios"
            width: 460
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 4
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R4")
        Label:
            text:"  Muncul pesan error pada bios"
            width: 410
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 5
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R5")
        Label:
            text:"Alarm bios berbunyi"
            width: 330
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 6
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R6")
        Label:
            text:"Terdengar suara aneh pada HDD"
            width: 450
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 7
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R7")
        Label:
            text:"Sering terjadi hang/crash saat menjalankan aplikasi"
            width: 610
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 8
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R8")
        Label:
            text:"Selalu scandisk ketika booting"
            width: 420
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 9
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R9")
        Label:
            text:"Muncul pesan error saatmenjalankan game atau aplikasi"
            width: 653
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 10
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R10")
        Label:
            text:"Device driver informasi tidak terdeteksi dalam device manager, meski driver telah di install"
            width: 950
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 11
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R11")
        Label:
            text:"Tiba-tiba bios melakukan restart otomatis"
            width: 520
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 12
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R12")
        Label:
            text:"Keluarnya blue screen pada OS Windows (isi pesan selalu berbeda tergantung pada kondisi tertentu)"
            width: 1050
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 13
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R13")
        Label:
            text:"Suara tetap tidak keluar meskipun driver dan setting device telah dilakukan sesuai petunjuk"
            width: 960
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 14
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R14")
        Label:
            text:"Muncul pesan error saat menjalankan aplikasi audio"
            width: 620
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 15
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R15")
        Label:
            text:"Muncul pesan error saat pertama OS di load dari HDD"
            width: 640
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 16
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R16")
        Label:
            text:"Tidak ada tanda tanda dari bagian/seluruh perangkat bekerja (semua kipas pendingin tidak berputar)"
            width: 1050
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 17
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R17")
        Label:
            text:"Sering tiba-tiba mati tanpa sebab"
            width: 450
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 18
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R18")
        Label:
            text:"Muncul pesan pada windows, bahwa windows kekurangan virtual memori"
            width: 805
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 19
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R19")
        Label:
            text:"Aplikasi berjalan dengan lambat, respon yang lambat terhadap inputan"
            width: 780
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
        
        #Rules 20
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R20")
        Label:
            text:"Kinerja grafis terasa sangat berat (biasanya dalam game dan manipulasi gambar)"
            width: 880
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 21
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R21")
        Label:
            text:"Device tidak terdeteksi dalam bios"
            width: 460
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 22
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R22")
        Label:
            text:"Informasi terdeteksi yang salah dalam bios"
            width: 530
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 23
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R23")
        Label:
            text:"Hanya sebagian perangkat yang bekerja"
            width: 505
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 24
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R24")
        Label:
            text:"Sebagian/seluruh karakter inputan mati"
            width: 490
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

        #Rules 25
        CheckBox:
            color:0,0,0,1
            width: 50
            height: 25
            size_hint: (None, None)
            on_active: root.checkbox_click(self, self.active, "R25")
        Label:
            text:"Pointer mouse tidak merespon gerakan mouse"
            width: 560
            height: 25
            color:0,0,0,1
            font_size: 20
            size_hint: (None, None)
            halign: 'left'
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'

<Problem>:
    GridLayout:
        cols: 1
        size: root.width, root.height
        canvas.before:
            Rectangle:
                source:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/BG.png'
                size: root.width, root.height
                pos: self.pos
        Button:
            text:''
            background_normal:'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Arrow.png'
            font_size:2
            width: 60
            height: 60
            size_hint: (None, None)
            pos: (0,660)
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
        Label:
            id: output_problem
            color:0,0,0,1
            font_size: 40
            text_size: self.size
            halign: 'center'
            valign: 'middle'  # Tambahkan properti valign agar teks berada di tengah secara vertikal
            font_name: 'C:/Users/Agriffa Nuzra/Documents/SEMESTER 7/Pakar EXE/Assets/Helvetica.ttf'
'''
kv = Builder.load_string(KV)

#Class app
class MainApp(App):
    global sm
    sm = ScreenManager()

   #Deklarasi layar
    def build(self):
        sm.add_widget(Started(name="started"))
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(About_me(name="aboutme"))
        sm.add_widget(Wiki(name="wiki"))
        sm.add_widget(Pilih(name="pilih"))
        sm.add_widget(Main_Screen(name="main"))
        sm.add_widget(Problem(name="problem"))
        return sm
        
#Menjalankan App pada main function
if __name__ == '__main__':
    MainApp().run()