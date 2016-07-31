from stop_words import get_stop_words

import jaccard
import jellyfish
import MySQLdb
import IDF

DB = "database"
DB_HOST = "localhost"
DB_PORT = 8888
DB_NAME = "linked_reverb"
DB_USER = "root"
DB_PWD = "12345"

cachedStopWords = get_stop_words("en")

def get_corpus():
    db_conn = MySQLdb.connect(host="localhost", port=8889, db="linked_reverb", user="root", passwd="root")
    cursor = db_conn.cursor()
    cursor.execute("select argument1, argument2 from linked_entity80_a")

    ls_result = []
    ls_corpus = []

    row_count = int(cursor.rowcount)
    for i in range(0, row_count):
        row = cursor.fetchone()
        ls_result.append(row)

    stop_words = get_stop_words('en')

    for i in range(len(ls_result)):
        for item in ls_result[i][0].split(" "):
            if item in stop_words:
                pass
            else:
                ls_corpus.append(item)
        for item in ls_result[i][1].split(" "):
            if item in stop_words:
                pass
            else:
                ls_corpus.append(item)

                #
                # ls_corpus.append(ls_result[i][0].split(" "))
                # ls_corpus.append(ls_result[i][1].split(" "))

    db_conn.close()
    return ls_corpus

def get_subject():
    db_conn = MySQLdb.connect(host="localhost", port=8889, db="linked_reverb", user="root", passwd="root")
    cursor = db_conn.cursor()
    cursor.execute("select argument1 from linked_entity80_a")

    ls_result = []
    ls_subject = []

    row_count = int(cursor.rowcount)
    for i in range(0, row_count):
        row = cursor.fetchone()
        ls_result.append(row)

    for i in range(0, len(ls_result)):
        print ls_result[i][0].split()
        subj = ' '.join([word for word in str(ls_result[i][0]).split() if word not in cachedStopWords])
        #ls_result[i][0] = ' '.join([word for word in str(ls_result[i][0]).split() if word not in cachedStopWords])
        ls_subject.append(subj)

    print ls_subject
                #
                # ls_corpus.append(ls_result[i][0].split(" "))
                # ls_corpus.append(ls_result[i][1].split(" "))

    db_conn.close()
    return ls_subject


# # Jaron distance
# jarowinker = jellyfish.jaro_winkler(u'MARTHA tmp', u'MARTHA tmp')
# jaro = jellyfish.jaro_distance(u'MARTHA', u'MARTHA')
# # Jaccard distance
# jaccard = jaccard.Jaccard("will be a common year starting on Thursday of the Gregorian calendar", "is a common year starting on Thursday of the Gregorian calendar")
# similarity = jaccard.similarity()
# distance = jaccard.distance()
# # IDF
# list_corpus = get_corpus()
#
# idf = IDF.IDF("Sushi Mutzig", "Sushi marinara Mutzig", list_corpus)
#
# #print idf.cal_overlap()
