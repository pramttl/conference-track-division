TAK = 6   # Talks per Track
TOTAK = 18 # Total number of talks to be scheduled.
N = 30    # Number of people attending the conf.

import networkx as nx
G = nx.Graph()

# Assuiming TAK workshops per track in a day.
# N people attending the confenrence in total.
# Each conference attende is told to choose "TAK" number of talks from a total of "TOTAK" talks which they would like to attend.


# So the graph has TOTAK number of nodes.
G.add_nodes_from(range(TOTAK))

f = open("sample_data.txt","r")

# Number of people maing choices is N.
for k in range(N):
    choices = f.readline()[:-1]
    choices = map(int,list(choices))
    print choices
    assert len(choices) == TOTAK
    for i in range(TOTAK-1):
        for j in range(i+1,TOTAK):
            if (choices[i] == 1 and choices[j] == 1):
                # print i,j
                try:
                    G[i][j]['weight'] += 1
                except KeyError:
                    G.add_edge(i,j,weight=1)


# The graph is now ready for use.
'''
# TODO: Here come the main graph algorithms which should deal with the graph. A few maybe's in the logic-
* Graph Coloring
* Graph partitioning
* Block Modelling
'''

# Visualizing the graph with mathplotlib.
import matplotlib.pyplot as plt
nx.draw(G)
plt.show()
