# Algorithmic Methods of Data Mining Homework 4
### Valerio Guarrasi, Eleonora Grassucci, Shamrun Karimov

The repository has three files:

The file Modules.py contains the functions we used;

The file Report.pdf contains the results we obtained.

As soon as we load the file on Python, with the createDict function, we created a 4 dictionaries with all the informations that we are going to use. Maybe some of them are useless, but we prefered to have them for versatility. First we created a dictionary, authors_dict, with the ids of the authors as keys in order to create a graph where each author's id is a node and each edge is a publication that two nodes shared. The structure is: {author_id: [author_name,[list of tuples(publication_id,publication_id_int)],[list of tuples(conference_id,conference_id_int)]]}. The second dictionary is authors_dict_reference witch associates to each author_name his author id. The third dictionary is publications_dict that associates to each pubblication a list of the author_id 's that participated t that pubblication. The last dictionary is conferences_dict that associates to each conference_id a list of the publication_id that were part of it. We prefered using dictionaries because they are fast and usefull to retrive a desired information.
To create the graph we used the function createGraph where each node has as attributes the name of the author, the list of the publications he/she has done, the conferences where he/she has taken part. 
Instead, each edge has one attribute, the weight evaluated as 1 - Jaccard distance between the two authors.

The function Jaccard calulates the Jaccard distance where the numerator is the intersection between the two authors and the denominator is the union between them.
While we are createting the graph, we create a dictionary similar that, if a node has distance 0 from another, it means that they are identical, so we associate for each group of similar nodes, one of them that will rappressent the group. We will use this for the third part. 

### 2 a.

In this point, given in input a conference, we return the induced subgraph with the authors who published in that event.
To do it, we copied the graph G and then removed the nodes that did not published at the input conference.

Once we created the graph, we evaluated some centrality measures using the networkx functions:
Degree Centrality, Closeness Centrality, Betweenness Centrality.
Check the .pdf file to see the results and the plots.

### 2 b.

Here, we wrote a function named neighbors to evaluate the hop distance from Aris.
This function saves into a list "to_visit" the neighbors of the nodes it visits and then it takes the node to visit into account.
It repeats these steps until the d-distance set from the input.

In particular, as you can see in the pdf file, this function is faster than the newtorkx one.

### 3

To make everything faster, we want to make a smaller graph without loosing any information. First we removed the isolated nodes, beacouse, since we have to work on the distance between two nodes, we already know that the distance between any node and a isolated one doesn't exixt (since the nodes can't be connected). Then, by using the similar dictionary, we removed every node, except for one, from every group of identical nodes. We did this beacouse the distance between any node and two identical node is the same. So if you have one distance, you automatically have even the second distance. This procedure reduces the complexity of the graph.

To calculate the shortest distance between any couple of nodes, we used Dijkstra algorithm, that gives in output a dictionary of the shortest path lenghts between one node and all the other ones. To make everyhting really fast we used the heapq library with the heap structure.

### 3.a

Here we used the function distances_aris, that by recalling the Dijkstra's algorithm, we find the shortest path length from Aris to every other node that is connected to him. We give as output the distance between the node given in input and Aris. Since we took out a few nodes, we always have to check if the node that we ask in input doesn't exixt or was removed. If it was removed, then we look at it as if it is the node that we kept from it's identical group.