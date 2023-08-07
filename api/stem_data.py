# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary

# def stemmer():
#     # create stemmer
#     factory = StemmerFactory()
#     stemmer = factory.create_stemmer()

#     # create factory
#     stop_factory = StopWordRemoverFactory().get_stop_words()
#     dict_stop = ArrayDictionary(stop_factory)
#     delete = StopWordRemover(dict_stop)

#     for i in range(1,16):

#         filename_data = "data" + str(i) + ".csv"
#         filename_stem = "data" + str(i) + ".txt"

#         file1 = open("test/"+filename_data)
#         line = file1.read()

#         sentence = stemmer.stem(line)
#         print(sentence)

#         final_sentence = delete.remove(sentence)
#         print(final_sentence)

#         appendFile = open("test/"+filename_stem,'a')
#         appendFile.write(final_sentence)
#         appendFile.close()
