# TODO: Hangyu Lin (John), hl2357
# TODO: Guanchen Zhang (James), gz256

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError

def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    # 
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.txt for additional information about the
    # return value of this method.
    
    # List to keep seen closest distance node, and the node that reached it
    node_dist_values = {}
    # Initialize list of visitied nodes with source node in it
    visited = [source]
    # Set the node value of the source to 0
    node_dist_values[source] = (0, source)

    while target not in visited:
        # Find the min distance node out of all visited nodes' neighbors
        min_dist_node = ""
        min_dist = float('inf')
        for current_node in visited:
            # A list to keep all possible neighbors and their distance
            temp_neighbors = graph.get_neighbors(current_node)
            
            # Run a loop to find the cloested neighbor which is unvisited
            for temp_neighbor in temp_neighbors:
                temp_node, direct_dist = temp_neighbor
                temp_dist = node_dist_values[current_node][0] + direct_dist
                
                # Update the node_dist_values list
                if temp_node not in node_dist_values:
                    node_dist_values[temp_node] = (temp_dist, current_node)
                elif temp_dist < node_dist_values[temp_node][0]:
                    node_dist_values[temp_node] = (temp_dist, current_node)
                    
                # If this node is the closest one, update the min node and distance
                if temp_node not in visited:
                    if temp_dist < min_dist:
                        min_dist_node, min_dist = temp_node, temp_dist
        visited.append(min_dist_node)
    # Now we have the shortest distance, we find the shortest path by going backwards until source
    shortest_length = node_dist_values[target][0]
    shortest_path = [target]
    backwards_node = target
    while backwards_node != source:
        backwards_node = node_dist_values[backwards_node][1]
        shortest_path.insert(0, backwards_node)
    return (shortest_path, shortest_length)