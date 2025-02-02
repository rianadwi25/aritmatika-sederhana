import tkinter as tk
from tkinter import messagebox

# fungsi untuk melakukan penjumlahan
def hitung():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        
        hasil_jumlah = angka1 + angka2
        hasil_kali = angka1 * angka2
        hasil_kurang = angka1 - angka2

        label_hasil.config(text=f"Jumlah: {hasil_jumlah}\nKali: {hasil_kali}\nKurang: {hasil_kurang}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")
    
# fungsi untuk membersihkan semua input dan hasil
def bersihkan():
    entry_angka1.delete(0, tk.END)
    entry_angka2.delete(0, tk.END)
    label_hasil.config(text="Hasil: ")

# fungsi untuk menutup aplikasi
def tutup_aplikasi():
    window.quit()

# membuat jendela utama
window = tk.Tk()
window.title("Menjumlahkan Dua Angka")

# mengatur latar belakang jendela menjadi biru
window.configure(bg="blue")

# menyelaraskan label dan entry
label_width = 25 # menentukan lebar label yang sama untuk menyelaraskan

# label dan entry angka pertama
label_angka1 = tk.Label(window, text="Masukkan Angka Pertama:", width=label_width, anchor="w", bg="blue", fg="white")
label_angka1.grid(row=0, column=0, padx=10, pady=5)

entry_angka1 = tk.Entry(window)
entry_angka1.grid(row=0, column=1, padx=10, pady=5)

# label dan entry angka kedua
label_angka2 = tk.Label(window, text="Masukkan Angka Kedua:", width=label_width, anchor="w", bg="blue", fg="white")
label_angka2.grid(row=1, column=0, padx=10, pady=5)

entry_angka2 = tk.Entry(window)
entry_angka2.grid(row=1, column=1, padx=10, pady=5)

# lebar tombol yang sama
button_width = 10

# tombol untuk menghitung penjumlahan
tombol_hitung = tk.Button(window, text="Hitung", command=hitung, width=button_width, bg="blue", fg="white")
tombol_hitung.grid(row=4, column=0, columnspan=2, pady=5)

# tombol untuk membersihkan input dan hasil
tombol_bersih = tk.Button(window, text="Bersih", command=bersihkan, width=button_width, bg="blue", fg="white")
tombol_bersih.grid(row=4, column=1, columnspan=2, pady=5)

# tombol untuk menutup aplikasi
tombol_tutup = tk.Button(window, text="Tutup", command=tutup_aplikasi, width=button_width, bg="blue", fg="white")
tombol_tutup.grid(row=4, column=2, columnspan=5, pady=5, padx=50)

# label untuk menanmpilkan hasil
label_hasil = tk.Label(window, bg="blue", fg="white")
label_hasil.grid(row=5, column=0, columnspan=2, pady=10)

# menjalankan jendela utama
window.mainloop()
                          


