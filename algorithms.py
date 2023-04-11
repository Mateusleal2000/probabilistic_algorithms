import random
import math
from networkx import random_graphs as rg
from networkx import maximal_independent_set
import matplotlib.pyplot as plt


def findbipartiteset(graph):
    set_A = []
    set_B = []
    for vertex in graph.nodes():
        if (random.randint(0, 1) == 1):
            set_A.append(vertex)
        else:
            set_B.append(vertex)
    new_edge_set = []

    for edge in graph.edges():
        if edge[0] in set_A and edge[1] in set_B:
            new_edge_set.append(edge)
        elif edge[0] in set_B and edge[1] in set_A:
            new_edge_set.append(edge)
    return len(new_edge_set)


def algorithm1(erdos_renyi_graphs):
    cont = 1
    subgraph_list = []
    for graph in erdos_renyi_graphs:
        total_weight = len(graph.edges())
        bipartite_weight = 0
        limit = 0
        while (limit != 5):
            bipartite_weight = findbipartiteset(graph)
            limit += 1

            if (bipartite_weight >= math.floor(total_weight/2)):
                subgraph_list.append(bipartite_weight)
                limit = 5
                print(f"Graph {cont} has a heavy bipartite subgraph")
        cont += 1
    return subgraph_list


def algorithm2(gnm_graphs):
    cont = 1
    independent_set_size = []
    for graph in gnm_graphs:
        attempt = 0
        d = 20
        while attempt != 25:
            copied_graph = graph.copy()
            attempt += 1
            for vertex in graph.nodes():
                if (random.random() <= (1 - 1/d)):
                    copied_graph.remove_node(vertex)
            copied_graph_node_set = 0
            copied_graph_node_set = len(copied_graph.nodes())
            real_max_set = 0
            real_max_set = len(maximal_independent_set(copied_graph))
            if (copied_graph_node_set == real_max_set):
                attempt = 25
                independent_set_size.append(len(copied_graph.nodes()))
                print(f"Graph {cont} has a large independent set")

        cont += 1
    return independent_set_size


nodes_number1 = 1000
nodes_number2 = 1200
nodes_number3 = 1600
nodes_number4 = 1800
nodes_number5 = 2000
nodes_number6 = 2200
erdos_renyi_graphs = []
gnm_graphs = []

erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number1, 0.1, None, False))
erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number2, 0.1, None, False))
erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number3, 0.1, None, False))
erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number4, 0.1, None, False))
erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number5, 0.1, None, False))
erdos_renyi_graphs.append(rg.gnp_random_graph(nodes_number6, 0.1, None, False))

gnm_graphs.append(rg.gnm_random_graph(nodes_number1, 500, None, False))
gnm_graphs.append(rg.gnm_random_graph(nodes_number2, 600, None, False))
gnm_graphs.append(rg.gnm_random_graph(nodes_number3, 800, None, False))
gnm_graphs.append(rg.gnm_random_graph(nodes_number4, 900, None, False))
gnm_graphs.append(rg.gnm_random_graph(nodes_number5, 1000, None, False))
gnm_graphs.append(rg.gnm_random_graph(nodes_number6, 1000, None, False))


x = [1000, 1200, 1600, 1800, 2000, 2200]


# y_1 = algorithm1(erdos_renyi_graphs)

# plt.plot(x, y_1)
# plt.xlabel('Number of nodes')
# plt.ylabel('Bipartite graph weight')
# plt.title('Algorithm 1 graph')
# plt.show()


y_2 = algorithm2(gnm_graphs)

plt.plot(x, y_2)
plt.xlabel('Number of nodes')
plt.ylabel('Independent set size')
plt.title('Algorithm 2 graph')
plt.show()
