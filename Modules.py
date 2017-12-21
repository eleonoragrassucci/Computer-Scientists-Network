
# coding: utf-8

# In[1]:

import networkx as nx


# In[2]:

def createDict(dataset):
    authors_dict = {}
    authors_dict_reference = {}
    publications_dict = {}
    conferences_dict = {}
    for publication in dataset:
        publications_dict[publication["id_publication"]] = []
        if publication["id_conference"] not in conferences_dict:
            conferences_dict[publication["id_conference"]] = [publication["id_publication"]]
        else:
            conferences_dict[publication["id_conference"]].append(publication["id_publication"])
        conferences_dict["id_conference"] = []
        for aut in publication["authors"]:
            #clean ugly names
            if "&" not in aut["author"]:
                publications_dict[publication["id_publication"]].append(aut["author_id"])
                if aut["author_id"] not in authors_dict:
                    authors_dict[aut["author_id"]] = [aut["author"],[(publication["id_publication"],publication["id_publication_int"])],
                                                      [(publication["id_conference"],publication["id_conference_int"])]]
                    authors_dict_reference[aut["author"]] = aut["author_id"]
                else:
                    authors_dict[aut["author_id"]][1].append((publication["id_publication"],publication["id_publication_int"]))
                    if (publication["id_conference"],publication["id_conference_int"]) not in authors_dict[aut["author_id"]][2]:
                        authors_dict[aut["author_id"]][2].append((publication["id_conference"],publication["id_conference_int"]))
                        
    return authors_dict, authors_dict_reference, publications_dict, conferences_dict


# In[3]:

def Jaccard(id1,id2, authors_dict):
    a = authors_dict[id1][1]
    b = authors_dict[id2][1]
    intersection = len(list(set(a) & set(b)))
    union = len(set(a + b))
    return intersection/union


# In[11]:

def createGraph(authors_dict, publications_dict):
    import networkx as nx
    import itertools
    from Modules import Jaccard
    similar={}
    G = nx.Graph()
    for k,v in authors_dict.items():
        G.add_node(k, id = k, author_name = v[0], pubblications = v[1], conferences = v[2])
    for publication, authors in publications_dict.items():
        try:
            for couple in itertools.combinations(authors, 2):
                author_1 = couple[0]
                author_2 = couple[1]
                w = 1 - Jaccard(author_1, author_2,authors_dict)
                if w == 0:
                    if author_1 not in similar:
                        similar[author_2] = author_1
                    else:
                        similar[author_2] = similar[author_1]       
                G.add_edge(author_1, author_2, weight= w)
        except:
            pass
    return G, similar


# In[5]:

#function that returns the nodes at hop distance d
def neighbors(G, start, d):
    visit = []
    to_visit = [start]
    for i in range(d):
        temp = []
        for n in to_visit:
            if n not in visit:
                temp += G.neighbors(n)
        visit = list(set(visit).union(to_visit))
        to_visit = temp
    visit = list(set(visit).union(to_visit))
    return visit


# In[6]:

#remove isolated nodes and identical nodes
def removeNodes(G, similar):
    import networkx as nx
    Gcon = G.copy()
    #remove isolated nodes
    for node in nx.nodes(Gcon):
        if Gcon.degree(node)==0:
            Gcon.remove_node(node)
    #remove identical nodes (nodes whose distance is 0.0)
    for node in similar.keys():
        Gcon.remove_node(node)
    return Gcon


# In[7]:

def Dijkstra(graph, start):
    import networkx as nx
    from heapq import heappush, heappop
    #A = [None] * len(graph)
    A={}
    for node in graph.nodes():
        A[node]=None
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len["weight"], w))

    # to give same result as original, assign zero distance to unreachable vertices             
    return A
    #return [0 if x is None else x for x in A]


# In[8]:

def aris_subgraph(Gcon, similar):
    aris = 256176
    if aris in similar:
        aris = similar[aris]
    p = Dijkstra(Gcon, 256176)
    return p


# In[9]:

def distances_aris(p, similar):
    authorid = int(input("Enter Author id: "))
    if authorid in similar:
        authorid = similar[authorid]
    try:
        output = p[authorid]
        if output == None:
            print("The nodes are not connected")
        else:
            print(output)
    except:
        print("The node does not exist")


# In[10]:

def groupNumber(G, Gcon, similar):
    inp = list(map(int,input("Insert author id or enter to stop: ").split()))
    #inp = [234889, 523286, 523285, 256177, 114821] 
    if len(inp)>21:
        print("Too many nodes!")
    else:
        GROUP_NUMBER = {} 
        dijkstra_list = [] #list of dikstra dictionaries for each author in the input list
        for author in inp:
            if author in similar:
                author = similar[author]
            dijkstra_list.append(Dijkstra(Gcon, author))
        for nodeG in G.nodes():
            groups = []
            if nodeG in similar:
                node = similar[nodeG]
            else:
                node = nodeG
            try: 
                for i in range(len(dijkstra_list)):
                #for tree in dijkstra_list:
                    shortest_path = dijkstra_list[i][node]
                    if shortest_path != None:
                        groups.append((shortest_path,inp[i]))
            except: #for the isolated nodes
                pass
            if len(groups) == 0:
                GROUP_NUMBER[nodeG] = "This node is not connected to any of these nodes."
                #print("node "+str(nodeG)+" isn't connected to any of these nodes")
            else:
                result = min(groups)
                GROUP_NUMBER[nodeG] =(result[1],result[0])
                #print("the groupnumber for node "+str(nodeG)+" is "+str(result[1])+" with distance "+ str(result[0]))
    return GROUP_NUMBER


# In[ ]:




# In[ ]:



