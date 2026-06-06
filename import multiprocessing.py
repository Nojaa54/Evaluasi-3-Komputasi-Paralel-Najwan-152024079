import multiprocessing
import time

def proses_paralel(data):
    return data * data

if __name__ == "__main__":
    kumpulan_data = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        hasil = pool.map(proses_paralel, kumpulan_data)
    print("Hasil eksekusi paralel:", hasil)