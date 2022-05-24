import matplotlib.pyplot as plt
import numpy as np
import os

def przyklad_z_czatu():
    path = "C:\\Windows"
    total_files = 0
    total_size = 0
    for dir_path, _, file_name_array in os.walk(path):
        for file_name in file_name_array:
            if not file_name.endswith(".xml"):
                continue
            total_files += 1
            full_file_path = os.path.join(dir_path, file_name)
            total_size += os.path.getsize(full_file_path)

    print(F"Liczba plików .xml to {total_files}")
    print(F"Rozmiar plików to {total_size} bajtów.")
    print(F"Rozmiar plików to {round(total_size * (10 ** -6))} megabajtów.")


if __name__ == '__main__':
    print(f"Poczatek")

    # y = np.array([35,25,25,15])
    #
    # plt.pie(y)
    # plt.show()

    przyklad_z_czatu()

    print(f"Koniec")