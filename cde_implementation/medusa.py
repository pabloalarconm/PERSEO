import sys
# from rdflib import Graph, URIRef
import sys
from perseo.main import get_files, nt2ttl, uniqid
# 
# from ..pyperseo.perseo.main import get_files , nt2ttl, uniqid
# from pyperseo.functions import get_files, nt2ttl, uniqid

argv = sys.argv[1:]

if argv[0] == "uniqids":

    all_files = get_files(argv[0],"csv")

    for a in all_files:
        afile = argv[1] + "/" + a
        uniqid(afile)

elif argv[0] == "uniqid":

    file = argv[1] + ".csv"
    uniqid(file)

elif argv[0] == "nt2ttl":

    file = argv[1] + ".nt"
    nt2ttl(file)

else:
    print("You must provide an argument depending on your choosen functionality, like 'uniqid', 'uniqids' or 'nt2ttl'")

