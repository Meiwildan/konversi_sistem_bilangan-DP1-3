# US DP1 & DP3 Konversi bilangan
# Nama: Meiwildan Muhammad Farrel
# Kelas: XII RPL 4
# Absen: 25

# Import modul tkinter
import tkinter as tk

# Fungsi konversi bilangan
def konversi_awal(num, base):
    if base == 2:
        return bin(num)
    elif base == 8:
        return oct(num)
    elif base == 10:
        return str(num)
    elif base == 16:
        return hex(num)

def basis_konversi(num, basis_awal, basis_akhir):
    if basis_awal == 10:
        nomer_desimal = int(num)
    elif basis_awal == 2:
        nomer_desimal = int(num, 2)
    elif basis_awal == 8:
        nomer_desimal = int(num, 8)
    elif basis_awal == 16:
        nomer_desimal = int(num, 16)

    if basis_akhir == 10:
        return str(nomer_desimal)
    else:
        return konversi_awal(nomer_desimal, basis_akhir)
    
def konversi():
    num = inputan.get()
    basis_awal = int(var_basis_awal.get())
    basis_akhir = int(var_basis_akhir.get())
    var_hasil_konversi = basis_konversi(num, basis_awal, basis_akhir)
    hasil_konversi.config(text="" + var_hasil_konversi, font=("Arial", 14))

# Fungsi konversi ascii
def ascii(string):
    nilai_ascii = []
    for char in string:
        nilai_ascii.append(ord(char))
    return nilai_ascii

def konversi_ascii():
    string = label_input2.get()
    nilai_ascii = ascii(string)
    hasil_ascii.config(text="\n" + ", ".join(str(value) for value in nilai_ascii), font=("Arial", 14))

#Membuat window GUI
root = tk.Tk()
root.title('Konversi Bilangan Farrel')     
root.geometry("900x400")
root.resizable(False, False)
root.configure(bg='#2193b0')


# Bagian konverter sistem bilangan
inputan = tk.Entry(root, width=50)
inputan.pack(pady=10)

label_keterangan = tk.Label(root, text="Konversi ke", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan.pack(pady=10)

var_basis_awal = tk.StringVar(value="bilangan", )
basis_awal_dropdown = tk.OptionMenu(root, var_basis_awal, "2", "8", "10", "16")
basis_awal_dropdown.pack( pady=25,anchor="ne")

var_basis_akhir = tk.StringVar(value=" bilangan")
basis_akhir_dropdown = tk.OptionMenu(root, var_basis_akhir, "2", "8", "10", "16")
basis_akhir_dropdown.pack( pady=25,)

label_keterangan2 = tk.Label(text="Hasil:", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan2.pack(pady=2)

label_keterangan3 = tk.Label(text="Konversi Bilangan", font=("Arial", 20, "bold"), bg='#2193b0')
label_keterangan3.pack(pady=2)

label_keterangan4 = tk.Label(text="Masukkan Bilangan", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan4.pack(pady=2)

label_keterangan6 = tk.Label(text="Hasil:", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan6.pack(pady=2)

tombol_konversi = tk.Button( text="Konversi", font=("Arial", 10, "bold"),fg="#fff", bg="#65C7F7",command=konversi)
tombol_konversi.pack(pady=10)

hasil_konversi = tk.Label(root, text="", font=("Arial", 14, "bold"), bg='#2193b0')
hasil_konversi.pack(pady=10)


#bagian konverter ascii
label_keterangan5 = tk.Label( text="Konversi ASCII", font=("Arial", 20, "bold"), bg='#2193b0')
label_keterangan5.pack(pady=2)

label_input2 = tk.Entry(root, width=40)
label_input2.pack(padx=10)

tombol_konversi_ascii = tk.Button( text="Konversi", fg="#fff", bg="#65C7F7" ,command=konversi_ascii)
tombol_konversi_ascii.pack(pady=10)

hasil_ascii = tk.Label(root, text="", font=("Arial", 14, "bold"), bg='#2193b0')
hasil_ascii.pack(pady=10)

label_keterangan7 = tk.Label( text="Nama: Meiwildan Muhammad Farrel", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan7.pack(pady=2)

label_keterangan8 = tk.Label( text="Kelas: XII RPL 4", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan8.pack(pady=2)

label_keterangan9 = tk.Label( text="Absen: 25", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan9.pack(pady=2)

label_keterangan10 = tk.Label( text="Masukkan String", font=("Arial", 14, "bold"), bg='#2193b0')
label_keterangan10.pack(pady=2)

# Keterangan Author
label_keterangan7.place(relx=0.05, rely=0.7, anchor=tk.W)
label_keterangan8.place(relx=0.05, rely=0.78, anchor=tk.W)
label_keterangan9.place(relx=0.05, rely=0.86, anchor=tk.W)

# Penaruhan Tata Letak Sistem Bilangan
label_keterangan3.place(relx=0.805, rely=0.11, anchor=tk.SE)
label_keterangan4.place(relx=0.74, rely=0.18, anchor=tk.SE)
inputan.place(relx=0.87, rely=0.25, anchor=tk.SE)
basis_awal_dropdown.place(relx=0.635, rely=0.35, anchor=tk.SE)
label_keterangan.place(relx=0.769, rely=0.35, anchor=tk.SE)
basis_akhir_dropdown.place(relx=0.88, rely=0.35, anchor=tk.SE)
tombol_konversi.place(relx=0.61, rely=0.44, anchor=tk.SE)
label_keterangan2.place(relx=0.6, rely=0.53, anchor=tk.SE)
hasil_konversi.place(relx=0.67, rely=0.53, anchor=tk.SE)

# Penaruhan Tata Letak ASCII
label_keterangan5.place(relx=0.1, rely=0.08, anchor=tk.W)
label_keterangan10.place(relx=0.1, rely=0.16, anchor=tk.W)
label_input2.place(relx=0.1, rely=0.25, anchor=tk.W)
tombol_konversi_ascii.place(relx=0.1, rely=0.34, anchor=tk.W)
label_keterangan6.place(relx=0.1, rely=0.43, anchor=tk.W)
hasil_ascii.place(relx=0.17, rely=0.4, anchor=tk.W)

# Menjalankan GUI
root.mainloop()




# label_keterangan = tk.Label(text="2: Binary", font=("Arial", 14, "bold"), bg='#2193b0')
# label_keterangan.pack(pady=2)
# label_keterangan = tk.Label(text="8: Octal", font=("Arial", 14, "bold"), bg='#2193b0')
# label_keterangan.pack(pady=2)
# label_keterangan = tk.Label(text="10: Decimal", font=("Arial", 14, "bold"), bg='#2193b0')
# label_keterangan.pack(pady=2)
# label_keterangan = tk.Label(text="16: Hexadecimal", font=("Arial", 14, "bold"), bg='#2193b0')
# label_keterangan.pack(pady=2)