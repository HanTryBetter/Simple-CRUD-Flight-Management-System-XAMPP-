import datetime
import mysql.connector

def periksaKoneksi():
    connector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="raihan_5230411282"
    )
    if connector.is_connected:
        print("berhasil terkoneksi")
        return connector
    else:
        print("gagal terkoneksi")
        return False

def tambahLokasi(idL, nama, lintang, bujur):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "INSERT INTO lokasi (idL, nama, lintang, bujur) VALUES (%s,%s,%s,%s)"
        data = (idL, nama, lintang, bujur)
        cursor.execute(sql, data)
        connect.commit()
        print("data berhasil ditambahkan")
    except mysql.connector.Error as error:
        print(f"kesalahan : {error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def tambahIzin(idI, kecepatan_angin, jarak_pandang, cuaca, probabilitas):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "INSERT INTO izin (idI, kecepatan_angin, jarak_pandang, cuaca, probabilitas) VALUES (%s,%s,%s,%s,%s)"
        data = (idI, kecepatan_angin, jarak_pandang, cuaca, probabilitas)
        cursor.execute(sql, data)
        connect.commit()
        print("data berhasil ditambahkan")
    except mysql.connector.Error as error:
        print(f"kesalahan : {error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def tambahUtama(idU, lokasi, waktu, suhu, kondisi, kelembapan, izin):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "INSERT INTO utama (idU, lokasi, waktu, suhu, kondisi, kelembapan, izin) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (idU, lokasi, waktu, suhu, kondisi, kelembapan, izin)
        cursor.execute(sql, data)
        connect.commit()
        print("data berhasil ditambahkan")
    except mysql.connector.Error as error:
        print(f"kesalahan : {error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def memilihLokasi(idL):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "SELECT * FROM lokasi WHERE idL= %s"
        data = (idL,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as Error:
        print(f"kesalahan : {Error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def memilihIzin(idI):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "SELECT * FROM izin WHERE idI= %s"
        data = (idI,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as Error:
        print(f"kesalahan : {Error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def memilihUtama(idU):
    try:
        connect = periksaKoneksi()
        cursor = connect.cursor()
        sql = "SELECT * FROM utama WHERE idU= %s"
        data = (idU,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("data tidak ditemukan")
    except mysql.connector.Error as Error:
        print(f"kesalahan : {Error}")
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()

def ubahDataUtama(idU, waktu, suhu, kondisi, kelembapan, idU_lama):
    try:
        conn = periksaKoneksi()
        cursor = conn.cursor()
        sql = "UPDATE  utama SET idU=%s, waktu=%s, suhu=%s, kondisi=%s, kelembapan=%s WHERE idU = %s"
        data = (idU, waktu, suhu, kondisi, kelembapan, idU_lama)
        cursor.execute(sql, data)
        conn.commit()
        print("data berhasil diubah")
    except mysql.connector.Error as Error:
        print(f"kesalahan: {Error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def hapusDataUtama(idU):
    try:
        conn = periksaKoneksi()
        cursor = conn.cursor()
        sql = "DELETE FROM utama WHERE idU = %s"
        data = (idU,)
        cursor.execute(sql, data)
        conn.commit()
        print("data berhasil dihapus")
    except mysql.connector.Error as Error:
        print(f"kesalahan: {Error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

while True:
    print("===========================================================")
    print("=====>>>>>                MENU                   <<<<<=====")
    print("=====              1. Tambah Data Lokasi              =====")
    print("=====              2. Tambah Data Izin                =====")
    print("=====              3. Tambah Data Utama               =====")
    print("=====              4. Pilih Data Lokasi               =====")
    print("=====              5. Pilih Data Izin                 =====")
    print("=====              6. Pilih Data Utama                =====")
    print("=====              7. Update Data Utama               =====")
    print("=====              8. Hapus Data Utama                =====")
    print("=====              0. Exit                            =====")
    print("===========================================================")
    inputUser = input("Masukkan Pilihan [1-8] : ")
    if inputUser == "1":
        idL = input("Masukkan ID Lokasi anda : ")
        nama = input("Masukkan Nama Wilayah : ")
        lintang = input("Masukkan Koordinat Lintang Wilayah : ")
        bujur = input("Masukkan Koordinat Bujur Wilayah : ")
        tambahLokasi(idL, nama, lintang, bujur)
    elif inputUser == "2":
        idI = input("Masukkan ID Izin Penerbangan : ")
        kecepatan_angin = input("Masukkan Kecepatan Angin : ")
        jarak_pandang = input("Masukkan Jarak Pandang Pilot : ")
        cuaca = input("Masukkan Cuaca yg Terjadi [berkabut, cerah, badai, hujan] : ")
        probabilitas = input("Masukkan Probabilitas Terjadinya Kecelakaan : ")
        tambahIzin(idI, kecepatan_angin, jarak_pandang, cuaca, probabilitas)
    elif inputUser == "3":
        idU = input("Masukkan ID Utama : ")
        lokasi = input("Masukkan ID Lokasi : ")
        waktu = input("Masukkan Waktu : ")
        suhu = input("Masukkan Suhu : ")
        kondisi = input("Masukkan Kondisi : ")
        kelembapan = input("Masukkan Kelembapan : ")
        izin = input("Masukkan ID Izin : ")
        tambahUtama(idU, lokasi, waktu, suhu, kondisi, kelembapan, izin)
    elif inputUser == "4":
        idL = input("Masukkan ID Lokasi yang akan dipilih : ")
        memilihLokasi(idL)
    elif inputUser == "5":
        idI = input("Masukkan ID Izin Penerbangan yang akan dipilih : ")
        memilihIzin(idI)
    elif inputUser == "6":
        idU = input("Masukkan ID Utama yang akan dipilih : ")
        memilihUtama(idU)
    elif inputUser == "7":
        idU = input("Masukkan ID yang akan diganti : ")
        idU_baru = input("Masukkan ID BARU : ")
        waktu = input("Masukkan Waktu terbaru : ")
        suhu = input("Masukkan Suhu terkini : ")
        kondisi = input("Masukkan Kondisi Terbaru : ")
        kelembapan = input("Masukkan Kelembapan Terbaru : ")
        ubahDataUtama(idU_baru, waktu, suhu, kondisi, kelembapan, idU)
        print(
            f"===Data dirubah pada: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    elif inputUser == "8":
         while True:
            idU = input("hapus data berdasarkan ID Utama : ")
            hasil = input("anda yakin ingin menghapus data? [y/t]: ")
            if hasil == "y":
                hapusDataUtama(idU)
                print(
                    f"===Data dihapus pada: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
                break
            elif hasil == "t":
                continue
            else:
                print("salah memasukan opsi! coba lagi.")

    else: 
        break 