#!/usr/bin/env python
# coding: utf-8

# In[41]:


import csv
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS


# In[ ]:


# Set the namespace
namespace = "http://www.semanticweb.org/andreacortes/ontologies/2023/1/pizza-ontology#"
cw = Namespace(namespace)

# Load the ontology
g_onto = Graph()
g_onto.parse("/Users/andreacortes/Desktop/PizzaOntology2Project2023/ontology/pizza-restaurants-ontology_with_data.ttl", format="turtle")

# Create an empty graph
g_data = Graph()

# Load the data
with open("/Users/andreacortes/Desktop/PizzaOntology2Project2023/Data 02/IN3067-INM713_coursework_data_pizza_500.csv") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            # Skip header row
            continue
        # Extract data from row
        restaurant = URIRef(namespace + "restaurant_" + row[0])
        name = Literal(row[1])
        address = Literal(row[2])
        city = Literal(row[3])
        country = Literal(row[4])
        rating = Literal(row[5])
        # Add triples to the graph
        g_data.add((restaurant, RDF.type, cw.Restaurant))
        g_data.add((restaurant, cw.hasName, name))
        g_data.add((restaurant, cw.hasAddress, address))
        g_data.add((restaurant, cw.isLocatedIn, URIRef(namespace + city)))
        g_data.add((URIRef(namespace + city), RDF.type, cw.City))
        g_data.add((URIRef(namespace + city), cw.isLocatedIn, URIRef(namespace + country)))
        g_data.add((URIRef(namespace + country), RDF.type, cw.Country))
        g_data.add((restaurant, cw.hasRating, rating))


# In[43]:


import csv

with open("Data 02/IN3067-INM713_coursework_data_pizza_500.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        print(row)
        ...


# In[10]:


# Save RDF data to turtle format
with open("pizza-restaurants-example-data.ttl", "w") as f:
    f.write(graph.serialize(format="turtle"))
print("RDF data saved to pizza-restaurants-example-data.ttl")


# In[49]:


# Save RDF data to turtle format
with open("output/pizza_restaurants_data.ttl", "w") as f:
    f.write(graph.serialize(format="turtle").decode("utf-8"))
print("RDF data saved to output/pizza_restaurants_data.ttl")


# In[ ]:




