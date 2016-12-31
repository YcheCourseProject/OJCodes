import networkx as nx


def get_graph(edge_list_filename):
    graph = nx.Graph()
    with open(edge_list_filename) as ifs:
        edge_list = [line.rstrip().split(" ") for line in ifs.readlines()]
        print 'all edge list num:', len(edge_list)
        for src_vertex, dst_vertex in edge_list:
            graph.add_edge(src_vertex, dst_vertex)
    return graph


def demo_connected_components0():
    print 'demo0'
    graph = get_graph('dataset/edge_list0.txt')
    components = list(nx.connected_component_subgraphs(graph))
    print 'undirected edges num:', len(graph.edges())
    print 'connected components num:', len(components)


def demo_connected_components1():
    print '\ndemo1'
    g = get_graph('dataset/edge_list1.txt')
    components = list(nx.connected_component_subgraphs(g))
    print 'graph nodes num:', g.number_of_nodes()
    print 'components num:', len(components)
    print 100000 - g.number_of_nodes() + len(components)


if __name__ == '__main__':
    demo_connected_components0()
    demo_connected_components1()
