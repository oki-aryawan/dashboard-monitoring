"""

Aplikasi utama

"""


def extrac_data():
    """
    Date: 7 Januari 2022
    Time: 04:26:12 WIB
    Magnitude: 4.1
    Range: 10 km
    Location: 2.73 LS - 121.99 BT
    Epicentrum: Pusat gempa berada di darat 6 km selatan Kab.Morowali
    Impact: Dirasakan (Skala MMI): II-III Bahodopi
    :return:
    """
    extract_result = dict()
    extract_result['date'] = '7 Januari 2022'
    extract_result['time'] = '04:26:12 WIB'
    extract_result['magnitude'] = 4.1
    extract_result['depth'] = 10
    extract_result['loct'] = {'ls': 2.73, 'bt': 121.99}
    extract_result['epicentrum'] = 'Pusat gempa berada di darat 6 km selatan Kab.Morowali'
    extract_result['impact'] = 'Dirasakan (Skala MMI): II-III Bahodopi'

    return extract_result


def data_display(result: object):
    print('Recent earthquake data from BMKG')
    print(f"Lokasi: {result['date']}")
    print(f"Waktu: {result['time']}")
    print(f"Magnitudo: {result['magnitude']}")
    print(f"Kedalaman: {result['depth']}")
    print(f"Lokasi: LS = {result['loct']['ls']} dan BT = {result['loct']['bt']}")
    print(f"Episentrum: {result['epicentrum']}")
    print(f"Dampak: {result['impact']}")


if __name__ == "__main__":
    print('Aplikasi Utama')

    result = extrac_data()
    data_display(result)
