from collections import deque

mota = {}
mota['you'] = ['zxc','qwe','123']
mota['zxc'] = ['cxz','asd']
mota['qwe'] = ['111']
mota['123'] = ['999','000',]
mota['cxz'] = []
mota['asd'] = []
mota['111'] = []
mota['999'] = []
mota['000'] = []

def bfs(what_find,the_graph,the_start):
    search = deque()
    search += the_graph[the_start]
    already_was = []

    if the_start == what_find:
        return True
    else:
        already_was.append(the_start)

    while bool(search):
        node = search.popleft()
        if not node in already_was:
            if node == what_find:
                return True
            else:
                search += the_graph[node]
                already_was.append(node)

    return False
print(bfs('000',mota,'you'))