# HW4

The repository has three files:

The file Modules.py contains the function we used;

The file Report.pdf contains the results we obtained.

As soon as we load the file on Python we created a dictionary with the ids of the author as keys in order to create a graph where each author id was a node and each edge was a publication the two nodes shared.
In the graph G, each node has as attributes the name of the author, the list of the publications he/she has done, the conferences where he/she has taken part.
Instead, each edge has one attribute, the weight evaluated as 1 - Jaccard distance between the two authors.

The function Jaccard calulates the Jaccard distance where the numerator is the intersection between the two authors and the denominator is the union between them.

### 2 a.

In this point, given in input a conference, we return the induced subgraph with the authors who published in that event.
To do it, we copied the graph G and then removed the nodes that did not published at the input conference.

On the created graph, we evaluated some centrality measures:

Degree Centrality, Closeness Centrality, Betweenness Centrality.