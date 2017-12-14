# Algorithmic Methods of Data Mining Homework 4
### Valerio Guarrasi, Eleonora Grassucci, Shamrun Karimov

The repository has three files:

The file Modules.py contains the functions we used;

The file Report.pdf contains the results we obtained.

As soon as we load the file on Python we created a dictionary with the ids of the author as keys in order to create a graph where each author id was a node and each edge was a publication the two nodes shared.
In the graph G, each node has as attributes the name of the author, the list of the publications he/she has done, the conferences where he/she has taken part.
Instead, each edge has one attribute, the weight evaluated as 1 - Jaccard distance between the two authors.

The function Jaccard calulates the Jaccard distance where the numerator is the intersection between the two authors and the denominator is the union between them.

### 2 a.

In this point, given in input a conference, we return the induced subgraph with the authors who published in that event.
To do it, we copied the graph G and then removed the nodes that did not published at the input conference.

Once we created the graph, we evaluated some centrality measures using the networkx functions:
Degree Centrality, Closeness Centrality, Betweenness Centrality.
Check the .pdf file to see the results and the plots.

### 2 b.

Here, we wrote a function named neighbors to evaluate the hop distance from Aris.
This function saves into a list "to_visit" the neighbors of the nodes it visits and then it takes the node to visit into account.
It repeats this steps until the d-distance set from the input.

In particular, as you can see in the pdf file, this function is faster than the newtorkx one.


