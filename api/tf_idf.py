# import math #for computeIDF
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# import re
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
# import csv

# def computeTF(wordDict, bagOfWords):
#     tfDict = {}
#     bagOfWordsCount = len(bagOfWords)
#     for word, count in wordDict.items():
#         tfDict[word] = count/float(bagOfWordsCount)
#     return tfDict

# def computeIDF(documents):
#     import math
#     N = len(documents)

#     idfDict = dict.fromkeys(documents[0].keys(),0)
#     for document in documents:
#         for word, val in document.items():
#             if val > 0:
#                 idfDict[word] += 1

#     for word, val in idfDict.items():
#         idfDict[word] = math.log(N/float(val))
#     return idfDict

# def computeTFIDF(tfBagOfWords, idfs):
#     tfidf = {}
#     for word, val in tfBagOfWords.items():
#         tfidf[word] = val * idfs[word]
#     return tfidf

# def cosine_sim(vektor1, vektor2):    #example v = [1,2,4,0,0,0]
#     count = 0
#     lenv2 = 0
#     lenv1 = 0
#     for word in vektor2:
#         if word in vektor1:
#             count += vektor1[word]*vektor2[word]
#     for word in vektor1:
#         lenv1 += vektor1[word]*vektor1[word]
#     for word in vektor2:
#         lenv2 += vektor2[word]*vektor2[word]
#     return(count/math.sqrt(lenv1*lenv2))

# def fill_csv(og_table, tf_idf_table):
#     term_table_og = [[0 for j in range(17)] for i in range(len(og_table[0])+1)]
#     term_table_tfidf = [[0 for j in range(17)] for i in range(len(tf_idf_table[0])+1)]

#     for i in range(17):
#         if(i == 0):
#             term_table_og[0][i] = "Term"
#             term_table_tfidf[0][i] = "Term"
#         elif(i == 1):
#             term_table_og[0][i] = "Query"
#             term_table_tfidf[0][i] = "Query"
#         else:
#             term_table_og[0][i] = "D"+str(i-1)
#             term_table_tfidf[0][i] = "D"+str(i-1)

#     i = 1
#     for word, val in og_table[0].items():
#         term_table_og[i][0] = word
#         for j in range(1, 17):
#             if(j == 1):
#                 term_table_og[i][j] = og_table[15][word]
#             else:
#                 term_table_og[i][j] = og_table[j-2][word]

#         term_table_tfidf[i][0] = word
#         for j in range(1, 17):
#             if(j == 1):
#                 term_table_tfidf[i][j] = tf_idf_table[15][word]
#             else:
#                 term_table_tfidf[i][j] = tf_idf_table[j-2][word]

#         i += 1

#     with open('original_table.csv','w+',newline="") as file_og:
#         csv.writer(file_og).writerows(term_table_og)
#     with open('tfidf_table.csv','w+',newline="") as file_tf:
#         csv.writer(file_tf).writerows(term_table_tfidf)
#     return

# def search_result(query):   #data type of query is string
#     BagOfWords = [[] for i in range(16)]
#     BagOfWords_og = [[] for i in range(15)]

#     # create stemmer
#     factory = StemmerFactory()
#     stemmer = factory.create_stemmer()

#     # create factory
#     stop_factory = StopWordRemoverFactory().get_stop_words()
#     dict_stop = ArrayDictionary(stop_factory)
#     delete = StopWordRemover(dict_stop)

#     ##stemming query
#     stem_query = stemmer.stem(query)
#     computed_query = delete.remove(stem_query)

#     #Filling array BagOfWords with all words from each document
#     #idx 0-14 filled from data1,data2,etc respectively, idx 15 will be filled with query
#     for i in range(15):
#         data_file_og = open("test/data" + str(i + 1) + ".csv")
#         data_file = open("test/data" + str(i+1) + ".txt")
#         content_og = data_file_og.read()
#         content = data_file.readlines()[0]
#         BagOfWords_og[i] = re.split(',|\:|\[|\]|\-|\.| |\n|"', content_og)  # Split word
#         BagOfWords_og[i] = [j for j in BagOfWords_og[i] if j]  # Remove empty string
#         BagOfWords[i] = content.split(' ')
#     BagOfWords[15] = computed_query.split(' ')

#     #UniqueWords contain query
#     UniqueWords = set(BagOfWords[15])

#     #Filling Unique Words with number of the same word in 1 file
#     for i in range(15):
#         UniqueWords = set(UniqueWords).union(set(BagOfWords[i]))

#     #Filling query table for vektor computing(Not normalized)
#     numOfWords = []
#     for i in range(16):
#         new_dict = dict.fromkeys(UniqueWords, 0)
#         for word in BagOfWords[i]:
#             new_dict[word] += 1
#         numOfWords.append(new_dict)

#     #For result
#     result_key = ['sim', 'url','description','title','id','wordcount']
#     result = []

#     #computing TF-IDS
#     tf = [{} for i in range(16)]
#     idfs = computeIDF(numOfWords)
#     for i in range(16):
#         tf[i] = computeTF(numOfWords[i], BagOfWords[i])

#     tfids = [{} for i in range(16)]
#     for i in range(16):
#         tfids[i] = computeTFIDF(tf[i], idfs)

#     #each document url based on id
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

#     #formatting and ranking the final search result
#     for i in range(15):
#         new_el = dict.fromkeys(result_key, 0)
#         new_el['id'] = i+1
#         new_el['sim'] = cosine_sim(tfids[i], tfids[15])
#         dir_file = "test/data" + str(i+1) + ".csv"
#         csv_file = open(dir_file, 'r')
#         content = csv_file.readlines()
#         new_el['title'] = content[2]

#         #get the first sentence from description in document
#         desc = ""
#         for j in content[4]:
#             if "." not in j:
#                 if desc == "":
#                     desc = j
#                 else:
#                     desc += j
#             else:
#                 desc += j
#                 break

#         new_el['description'] = desc
#         new_el['url'] = Url[i]
#         new_el['wordcount'] = len(BagOfWords_og[i])
#         result.append(new_el)

#     #linear search for ranking
#     for i in range(15):
#         for j in range(i, 15):
#             if(result[i]['sim'] < result[j]['sim']):
#                 temp = result[i]
#                 result[i] = result[j]
#                 result[j] = temp

#     fill_csv(numOfWords, tfids)
#     # for testing the result
#     # for i in result:
#     #    print(i)
#     #    print()

#     return result

# #for testing if the function is running
# # search_result("Sambut Habib Rizieq pulang adalah Indonesia di kediaman penghapusan")