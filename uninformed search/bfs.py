graph={
    'P':['Q','R','S'],
    'Q':['P','R'],
    'R':['P','Q','T'],
    'T':['R'],
    'S':['P']
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("following is the breadth first search")
bfs(visited,graph,'P')