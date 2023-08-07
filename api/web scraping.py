# from bs4 import BeautifulSoup
# import requests
# import csv


# def web_scrap():
#     Url = ["" for i in range(15)]

#     Url[0] = 'https://news.detik.com/berita/d-5248482/sambut-habib-rizieq-begini-suasana-kawasan-petamburan-pagi-ini'
#     Url[1] = 'https://news.detik.com/berita/d-5248648/massa-penjemput-habib-rizieq-menyemut-putihkan-terminal-3-bandara-soetta?_ga=2.222972508.694954718.1604973538-1470613650.1604973538'
#     Url[2] = 'https://news.detik.com/foto-news/d-5248702/penampakan-habib-rizieq-saat-keluar-di-terminal-3-bandara-soekarno-hatta?_ga=2.190417388.694954718.1604973538-1470613650.1604973538'
#     Url[3] = 'https://news.detik.com/berita/d-5248797/ramai-massa-penjemput-hrs-kerusakan-di-terminal-3-soetta-tak-terhindarkan?_ga=2.47466976.694954718.1604973538-1470613650.1604973538'
#     Url[4] = 'https://news.detik.com/berita/d-5248569/pesawat-habib-rizieq-mendarat-di-bandara-soekarno-hatta?_ga=2.260744522.694954718.1604973538-1470613650.1604973538'
#     Url[5] = 'https://news.detik.com/berita/d-5248683/dki-serahkan-urusan-kepulangan-karantina-mandiri-habib-rizieq-ke-pusat?_ga=2.152807806.694954718.1604973538-1470613650.1604973538'
#     Url[6] = 'https://news.detik.com/berita/d-5248595/pesawat-habib-rizieq-mendarat-pendukung-di-soetta-serukan-ahlan-wa-sahlan?_ga=2.51736046.694954718.1604973538-1470613650.1604973538'
#     Url[7] = 'https://news.detik.com/berita/d-5248822/pulang-jemput-habib-rizieq-massa-naik-motor-masuk-tol-bandara?_ga=2.193768938.694954718.1604973538-1470613650.1604973538'
#     Url[8] = 'https://news.detik.com/berita/d-5248870/pkb-sayangkan-kerumunan-massa-habib-rizieq-potensi-corona-delaynya-pesawat?tag_from=wp_nhl_1'
#     Url[9] = 'https://news.detik.com/berita/d-5248733/jokowi-resmi-anugerahkan-gelar-pahlawan-nasional-ke-6-tokoh-ini?_ga=2.160596346.694954718.1604973538-1470613650.1604973538'
#     Url[10] = 'https://news.detik.com/berita-jawa-barat/d-5248799/polisi-tangkap-sindikat-pembuat-madu-palsu-khas-lebak-beromzet-miliaran?_ga=2.228421082.694954718.1604973538-1470613650.1604973538'
#     Url[11] = 'https://news.detik.com/berita/d-5248927/polri-bangga-kapolri-pertama-jenderal-rs-soekanto-jadi-pahlawan-nasional?tag_from=wp_hl_judul'
#     Url[12] = 'https://news.detik.com/berita-jawa-timur/d-5248926/cuaca-kembali-panas-bmkg-sebut-suhu-di-surabaya-mulai-normal?tag_from=wp_nhl_5'
#     Url[13] = 'https://news.detik.com/berita/d-5248610/peringati-hari-pahlawan-jokowi-pimpin-ziarah-nasional-di-tmp-kalibata'
#     Url[14] = 'https://news.detik.com/berita/d-5248943/tilap-dana-desa-rp-232-juta-mantan-kades-sekdes-di-aceh-ditangkap?tag_from=wp_nhl_1'

#     for i in range(15):

#         src = requests.get(Url[i]).text

#         soup = BeautifulSoup(src,'lxml')

#         filename_data = "data" + str(i+1) + ".csv"

#         csv_fie = open("test/"+filename_data,'w')
#         csv_writer = csv.writer(csv_fie)
#         csv_writer.writerow([])

#         title = soup.title.text
#         print(title)

#         content = soup.find('div',class_ = 'detail__body-text itp_bodycontent')

#         paragraf = ""

#         for isi in soup.find_all('p'):
#             paragraf = paragraf + isi.text

#         print(paragraf)

#         csv_writer.writerow([title])
#         csv_writer.writerow([paragraf])

#         csv_fie.close()



