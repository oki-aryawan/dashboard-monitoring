import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        date_time = soup.find('span', {'class': 'waktu'})
        date_time = date_time.text.split(', ')
        date = date_time[0]
        time = date_time[1]

        data_pack = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        data_pack = data_pack.findChildren('li')
        i = 0
        loct = None
        ls = None
        bt = None
        depth = 0
        epi = None
        impact = None

        for data in data_pack:
            if i == 1:
                magni = data.text
            elif i == 2:
                depth = data.text
            elif i == 3:
                loct = data.text.split(' - ')
                ls = loct[0][:4]
                bt = loct[1][:5]
            elif i == 4:
                epi = data.text
            elif i == 5:
                impact = data.text
            i = i + 1

        extract_result = dict()
        extract_result['date'] = date
        extract_result['time'] = time
        extract_result['magnitude'] = magni
        extract_result['depth'] = depth
        extract_result['loct'] = {'ls': ls, 'bt': bt}
        extract_result['epicentrum'] = epi
        extract_result['impact'] = impact

        return extract_result
    else:
        return None


def data_display(result):
    if result is None:
        print('Data tidak ditemukan')
        return
    print('Data gempa bumi terkini dari BMKG')
    print(f"Tanggal: {result['date']}")
    print(f"Waktu: {result['time']}")
    print(f"Magnitudo: {result['magnitude']}")
    print(f"Kedalaman: {result['depth']}")
    print(f"Lokasi: LS = {result['loct']['ls']} dan BT = {result['loct']['bt']}")
    print(f"Episentrum: {result['epicentrum']}")
    print(f"Dampak: {result['impact']}")
