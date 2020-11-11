# 1. Pick any node visit the adjacent unvisted vertex, mark it as visited,
# display it and insert it in a queue.

# 2. If there are no remaining adjacent vertices left remove the first vertex from the queue.

# 3. Repeat step 1 and 2 until queue is empty or the desired node is found.

            # Consider Graph
            #      A
            #    |   |
            #    B    C
            #   |  |   |
            #   D   E-->F

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited = [] #list to keep track of visited nodes
queue = [] #initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

#Driver code
bfs(visited, graph, 'A')