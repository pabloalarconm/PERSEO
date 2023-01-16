
from rdflib import Graph, Dataset, ConjunctiveGraph

g = Dataset()
g.parse("/home/pabloalarconm/Desktop/EJP/PERSEO/cde_implementation/data/triples/unifiedCDE_one.nt", format="nquads")
g.serialize(destination="result.ttl", format="trig")