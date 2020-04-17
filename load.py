#Imports
import csv
import Obfuscator

def load():
    sizeus = 201 # ukuran maksimal array user
    sizeelse = 1001 # ukuran maksimal array lain
    Auser = [None for i in range (sizeus)] # template array user dengan ukuran sizeus
    Aelse = [None for i in range (sizeelse)] # template array lain dengan ukuran else
    Filename = [Auser,Aelse,Aelse,Aelse,Aelse,Aelse,Aelse]
    File = ['' for i in range(7)]
    File[0] = input('Masukkan nama File User: ')
    File[1] = input('Masukkan nama File Daftar Wahana: ')
    File[2] = input('Masukkan nama File Pembelian Tiket: ')
    File[3] = input('Masukkan nama File Penggunaan Tiket: ')
    File[4] = input('Masukkan nama File Kepemilikan Tiket: ')
    File[5] = input('Masukkan nama File Refund Tiket: ')
    File[6] = input('Masukkan nama File Kritik dan Saran: ')
    Error = [False for i in range(7)]
    for i in range(7):
        try:
            with open(File[i], 'r') as csv_file:
                read = csv.reader(csv_file, delimiter=',')
                j = 0
                for row in read:
                    Filename[i][j]=row
                    j += 1
        except:
            print('Error! File',File[i],'not found!')
            Error[i] = True
    if (Error.count(True) == 0):
        print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return Filename

Filename = load()