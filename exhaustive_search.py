from graph_environment import Graphiest

def has_hamiltonian(Graph,start_node):
    visited = [False] * Graph.vertices_count
    
    # stack for searched node
    stack = []
    
    # condition when there are zero - one vertices in the passed through graph
    if Graph.vertices_count < 2:
        print('no graph')

     # condition when there is > 1 vertices passed through
    if Graph.vertices_count > 1:
        stack.append(start_node)

        while (len(stack)):
            s = stack[-1]
            stack.pop()

            if (not visited[s]):
                print(s, end=' ')
                visited[s] = True

            # for  all verticies adjacent to current
            for vert in Graph.get_neighbors(s):
                if (not visited[vert]):
                    stack.append(vert)

    

    