"""

Aplikasi utama

"""
import recent_eartquake

if __name__ == "__main__":
    print('Main Programm')

    result = recent_eartquake.extrac_data()
    recent_eartquake.data_display(result)
