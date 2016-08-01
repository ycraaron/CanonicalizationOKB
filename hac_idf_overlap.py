from __future__ import division
from stop_words import get_stop_words

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.spatial.distance as ssd
import numpy as np
import IDF
import MySQLdb
import utils

def get_corpus():
    db_conn = MySQLdb.connect(host="localhost", port=8889, db="linked_reverb", user="root", passwd="root")
    cursor = db_conn.cursor()
    cursor.execute("select argument1 from linked_entity80_a order by id")

    ls_result = []
    ls_corpus = []

    row_count = int(cursor.rowcount)
    for i in range(0, row_count):
        row = cursor.fetchone()
        ls_result.append(row[0])
    print len(ls_result)

def cal_idf_overlap():
    list_subj = utils.list_subject

    ls_distance_final = []
    ls_distance_row = []
    #print len(list_att)
    stop_words = get_stop_words('en')
    tmp_corpus = []
    for i in range(len(list_subj)):
        item = str(list_subj[i]).split(" ")
        for token in item:
            if token in stop_words:
                pass
            else:
                tmp_corpus.append(token)
    #print "corpus", corpus

    length = len(list_subj)
    for i in range(0, length):
        if i == 500 or i == 1000 or i == 1500:
            print i
        for j in range(0, length):
            print i, j
            idf_instance = IDF.IDF(str(list_subj[i]),str(list_subj[j]), tmp_corpus)
            distance = idf_instance.cal_overlap()
            ls_distance_row.append(distance)
        ls_distance_final.append(ls_distance_row)
        ls_distance_row = []

    myarray = np.asarray(ls_distance_final)
    print myarray
    Z = linkage(myarray, "ward")
    thefile = open('/Users/Aaron/test.txt', 'w')
    for item in Z:
        thefile.write("%s\n" % item)

    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
         Z,
         leaf_rotation=90.,  # rotates the x axis labels
         leaf_font_size=8.,  # font size for the x axis labels
     )
    plt.show()

    plt.title('Hierarchical Clustering Dendrogram (truncated)')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z,
        truncate_mode='lastp',  # show only the last p merged clusters
        p=30,  # show only the last p merged clusters
        show_leaf_counts=True,  # otherwise numbers in brackets are counts
        leaf_rotation=90.,
        leaf_font_size=12.,
        show_contracted=True,  # to get a distribution impression in truncated branches
    )
    plt.show()
#get_corpus()

cal_idf_overlap()
