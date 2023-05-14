#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from rdflib import Graph


# #The rdflib library is used to create the first two Graph objects in the code, graph_rdf and graph_ttL,graph ttl. These code are used to load and store RDF information from different files. The parse method takes the file paths and the relevant file formats (XML for RDF and Turtle for TTL) as parameters. The code uses the + operator to combine the RDF data after it has been loaded into the Graph objects. The merged_graph variable contains the merged graph. The code invokes the serialise method on the merged graph to serialise it.

# In[36]:


# Load the file RDF
rdf_file = "/Users/andreacortes/Desktop/CW2---/SWCW2./task 2/pizzat.rdf"
graph_rdf = Graph()
graph_rdf.parse(rdf_file, format="xml")

# Load the file TTL
ttl_file = "/Users/andreacortes/Desktop/CW2---/SWCW2./task 2/pizzat.ttl"
graph_ttl = Graph()
graph_ttl.parse(ttl_file, format="turtle")

# Load the file TTL
ttl_file = "/Users/andreacortes/Desktop/CW2---/SWCW2./task 4/pizzat4.ttl"
graph_ttl = Graph()
graph_ttl.parse(ttl_file, format="turtle")

# Merge the RDF and TTL graphs
merged_graph = graph_rdf + graph_ttl + graph_ttl

# Print the merged graph
print(merged_graph.serialize(format="turtle"))
print(merged_graph.serialize(format="xml"))
print(merged_graph.serialize(format="xml"))


# In[ ]:




