#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : graph.py
# @Author: Jeff Liu
# @Date  : 2019/3/30
# @Desc  : drawing graph

import networkx as nx
import matplotlib.pyplot as plt
import sys
import numpy as np



def trk_graph(trk):
    g = nx.MultiDiGraph()
    g.add_node(trk[0])
    for pos in range(len(trk[1:])):
        g.add_node(trk[pos+1])
        g.add_edge(trk[pos],trk[pos+1])
    return g

def tran_graph(data):
    g_list = []
    for trk in data:
        g_list.append(trk_graph(trk))
        print('trk done')
    return g_list

# defining grid size
g_width = 72
g_height = 48


data = np.load('Transformed_DATA/after_label_arr'+'('+ str(g_width) + 'X' + str(g_height)+')' + '.npy', encoding="latin1")
data = data[:10]


graph_list = tran_graph(data)

options = {
     'node_color': 'red',
     'node_size': 4,
 }
g0 = graph_list[0]
g1 = graph_list[1]
print(list(g1.edges()))

plt.subplot(221)
nx.draw(g0, with_labels=True, font_weight='bold',**options)
plt.subplot(222)
nx.draw(g1, with_labels=True, font_weight='bold',**options)

plt.subplot(223)
gg = nx.compose(g0,g1)

nx.draw(gg, with_labels=True, font_weight='bold',**options)


