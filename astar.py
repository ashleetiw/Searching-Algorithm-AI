from expand import expand

def list_to_dict(list):
	new_dict=dict()
	for i,j in list:
		new_dict[i]=j
	
	return new_dict


def a_star_search (dis_map, time_map, start, end):
	h=[[val for d,val in v.items() if d==end] for k,v in dis_map.items() if k==start]  # calculate h value for start node
	g=0
	f=g+h[0][0]
	g_prev={start:g}
	open={start:f}
	closed=[]
	visited=[]
	prev_vertex=dict()
	while open:
		# print(open)
		if len(open.values()) != len(set(open.values())):  # checks if 2 or more keys hold same value
				list = [(k, open[k]) for k in sorted(open)]  # this gives the output as list
				open=list_to_dict(list)  # convert list to dictionary
		node=min(open,key=open.get)  
		
		if node==end:
			# print('all nodes in line',visited)
			# print(prev_vertex)
			path=[]
			p=end
			while(p!=start):
				path.append(p)
				p=prev_vertex[p]
			path.append(start)
			return path[::-1]   # returns path in reverse order 
			# break
		

		child=expand(node,time_map)        
		for n in child:
			# calculate cost
			if n not in closed:
				visited.append(n)
				h=[[val for d,val in v.items() if d==end] for k,v in dis_map.items() if k==n]
				g=[[val for d,val in v.items() if d==n] for k,v in time_map.items() if k==node]

				g_cost=g_prev[node]+g[0][0]   #  start to node + node to chile n
				h_cost=h[0][0]
				# print(n,g_cost,h_cost)
				f=g_cost+h_cost
				if n in g_prev.keys():  # check if child n has been previously visited 
					# print('check if new cost is less than the prev_assigned cost')
					if f<(g_prev[n]+h_cost):  # if new value is less than the previous value then update its f value
						g_prev[n]=g_cost	
						open[n]=f
						prev_vertex[n]=node

				else:
					g_prev[n]=g_cost	
					open[n]=f
					prev_vertex[n]=node


		if node not in closed:
			closed.append(node)

		open.pop(node)        	





# //////////////////////////////////////////////////////////////////////////////////////////
def find_key_dfs(map,node):
	m=[]
	for k,v in map.items():
		for n,val in v.items():
			if n==node and val!=None: 
				m.append(k)
	return m

def dfs(map,start,end,path_dfs,stack,visited):
    if start==end:
            p=end
            while(p!=visited[0]):
                path_dfs.append(p)
                lis=find_key_dfs(map,p)
                for l in lis:
                    if l in visited:
                        p=l
                        break
            path_dfs.append(visited[0])
            return path_dfs[::-1]

    if start not in stack and start not in visited : # previously visited 
        stack.append(start)
    node=stack.pop()
    # print('going to node',node)
    child=expand(node,map)
    if len(child)==0 :  #leaf node 
        return dfs(map,stack.pop(),end,path_dfs,stack,visited)
    else:
        visited.append(node)
        for n in child:
            stack.append(n)
        return dfs(map,stack.pop(),end,path_dfs,stack,visited)

def depth_first_search(time_map, start, end):

	stack=[]
	visited=[]
	path_dfs= []
	path=dfs(time_map,start,end,path_dfs,stack,visited)
	return path


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def find_key_bfs(map,node,visited):
	for k,v in map.items():
		for n,val in v.items():
			if n==node and val!=None and k in visited : 
				return k  


def bfs(map,start,end,path_bfs,queue,visited):
    if start==end:
        p=end
        while(p!=visited[0]):
                path_bfs.append(p)
                p=find_key_bfs(map,p,visited)
                # print('p',p)
        path_bfs.append(visited[0])
        return path_bfs[::-1]


    if start not in queue and start not in visited : # previously visited 
        queue.append(start)

    node=queue.pop(0)
    # print('going to node',node)
    child=expand(node,map)
    # print(child)
    visited.append(node)
    for n in child:
        if n not in visited and n not in queue:
            queue.append(n)
    
    # print( queu0])
    return bfs(map,queue[0],end,path_bfs,queue,visited)


def breadth_first_search(time_map, start, end):
	path_bfs= []
	queue=[]
	visited=[]
	path=bfs(time_map,start,end,path_bfs,queue,visited)
	return path


	
