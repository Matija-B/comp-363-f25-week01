def reachability_of(s:int, G: list[list[int]]) -> list[int]:
    local_infinity = G[0][0]
    reach: list[int] = [] # return object
    visit_next: list[int] = [s] # place to store which vertex to process next 
    while visit_next: # shortcut to while len(bag) > 0, ie bag is not empty
        v: int = visit_next.pop()
        if v not in reach:
            reach.append(v)
            for u in range (len(G)):
                if G[v][u] != local_infinity:
                    visit_next.append(u)
    return reach

#COUNTING COMPONENTS IN A GRAPH
def count_and_label(graph): 
    # count : int
    # number of components in the graph
    # comp : list[int]
    # Component label for each vertex such that 
    # comp[v] = component that vertex v belongs to


    # Shortcut to number of vertices
    n = len(graph)
    # List to remember vertices I've been to
    visited = []
    # Return item: count of components 
    count = 0
    # Return time
    comp_labels = [None] * n    

    # Consider every vertex in the graph 
    # len(array) -> #rows
    # len(array) * len(array[0])
    for u in range(n):
        #Have we seen you before
        if u not in visited:
            #New component: updates component count
            count += 1
            # find all verticies reachable
            # B/C they are in the same component !!!!!!
            reachable_from_u = reachability_of(u, graph)
            # Label these vertecies reachable from u with 
            # current component number
            for vertex in reachable_from_u:
                comp_labels[vertex] = count
            #mark all these visitied 
            visited.extend(reachable_from_u)


    return count, comp_labels


def min_span_tree(G):
    # Empty adjacency matrix
    T = [[float('inf')] * len(G) for _ in range (len(G))]
    # Then we initalize count and label 
    count, label = count_and_label(T)
    # While there is more then component
    while count > 1:
        #list of empty values
        safe = [None] * len(G)
        for u in range(len(G)):
            for v in range(len(G)):
                #Then we want to check if there are no edge cases. 
                if G[u][v] != G[0][0] and label[u] != label[v]:
                        # We check if the label is None or we check if the weight of the edge is then less then the current edge.
                        if safe[label[u]] == None or G[u][v] < G[safe[label[u]][0]][safe[label[u]][1]]:
                            #We update the edge 
                            safe[label[u]] = (u,v)
                            # Same thing for v
                        if safe[label[v]] == None or G[u][v] < G[safe[label[v]][0]][safe[label[v]][1]]:
                            #We update the edge
                            safe[label[v]] = (u,v)
        
        count, label = count_and_label(T)
    return T
   

def testMethod() -> None:
    _ = float('inf') 

    G = [
        [_, 1, _, 1, _, _],  # vertex 0's neighbors
        [1, _, _, 1, _, 1],  # vertex 1's neighbors
        [_, _, _, _, _, _],  # vertex 2's neighbors
        [1, 1, _, _, _, 1],  # vertex 3's neighbors
        [_, _, _, _, _, 1],  # vertex 4's neighbors
        [_, 1, _, 1, 1, _]  # vertex 5's neighbors
    ]

   
    T = min_span_tree(G)
    print(T)
    
   


testMethod()


            

