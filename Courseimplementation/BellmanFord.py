
class Edge:

    def __init__(self, weight, start_node, target_node):
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node


class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')


class BellmanFordAlgorithm:

    def __init__(self, node_list, edge_list, start_node):
        self.node_list = node_list
        self.edge_list = edge_list
        self.start_node = start_node
        self.has_cycle = False

    def find_shortest_path(self):

        self.start_node.min_distance = 0

        for _ in range(len(self.node_list)-1):
            # in every iteration we consider all the edges
            for edge in self.edge_list:
                # calculate whether are there shorter paths
                u = edge.start_node
                v = edge.target_node

                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.predecessor = u
                    v.min_distance = dist

        # after make V-1 iterations we have to check negative cycles
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Negative cycle detected...")
                return

    def check_cycle(self, edge):
        # if the total cost (min_distance) of a given node decreases after V-1 iterations
        # it means there is a negative cycle
        if edge.start_node.min_distance + edge.weight < edge.target_node.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, node):

        if not self.has_cycle:
            print("Shortest path exists with value: ", node.min_distance)
            node = node

            while node is not None:
                print(node.name)
                node = node.predecessor
        else:
            print('There is a negative cycle in the G(V,E) graph...')


if __name__ == '__main__':

    # the nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")

    # the edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(-6, node7, node3)

    # handle the adjacency lists
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    # run the algorithm
    nodes = (node1, node2, node3, node4, node5, node6, node7)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)

    algorithm = BellmanFordAlgorithm(nodes, edges, node1)
    algorithm.find_shortest_path()
    algorithm.get_shortest_path(node7)
