from __future__ import division
from stop_words import get_stop_words

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.spatial.distance as ssd
import numpy as np
import jaccard
import MySQLdb
import utils

def get_corpus():
    db_conn = MySQLdb.connect(host="localhost", port=8889, db="linked_reverb", user="root", passwd="root")
    cursor = db_conn.cursor()
    cursor.execute("select relation, argument2 from linked_entity80_a order by id")

    ls_result = []
    ls_corpus = []

    row_count = int(cursor.rowcount)
    for i in range(0, row_count):
        row = cursor.fetchone()
        ls_result.append(row[0]+' '+row[1])
    print ls_result


def cal_attr_overlap():
    list_att = utils.list_attr

    ls_distance_final = []
    ls_distance_row = []
    print len(list_att)
    length = len(list_att)

    for i in range(0, length):
        if i == 500 or i == 1000 or i == 1500:
            print i
        for j in range(0, length):
            print i,j
            jaccard_instance = jaccard.Jaccard(list_att[i],list_att[j])
            distance = jaccard_instance.distance()
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
cal_attr_overlap()
