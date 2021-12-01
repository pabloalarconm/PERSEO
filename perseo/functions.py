
from rdflib import Graph, URIRef
from os import listdir
from os.path import isfile, join
from datetime import datetime
import pandas as pd


def get_files(path,format):
    """
    Obtain all files from current directory with certain format
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    format_files = [ff for ff in files if ff.endswith(str("." + format))]
    if len(format_files) == 0:
        print("No resources are present at {} path with .{} format.".format(path,format))
    else:
        return format_files


def nt2ttl(path_file):
    """
    Data transformation from .nt file to .ttl
    """

    g = Graph()
    g.parse(str(path_file), format="turtle")

    g.namespace_manager.bind('this', URIRef("http://example.org/data/"))
    g.namespace_manager.bind('sio', URIRef("http://semanticscience.org/resource/"))
    g.namespace_manager.bind('obo', URIRef("http://purl.obolibrary.org/obo/"))
    #all_ns = [n for n in g.namespace_manager.namespaces()]
    #print(all_ns)

    splited = path_file.split(sep=".")
    filename = splited[0]
    ttl_path_file = filename + "." + "ttl"

    g.serialize(destination = str(ttl_path_file), format="turtle")


def milisec():
    """
    Creates a milisecond timestamp.
    """
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S%f')
    return now


def uniqid(path_file):
    """
    Creates unique identifier column based on milisecond timestamp.
    """
    data = pd.read_csv(path_file)

    data['uniqid'] = ""
    for i in data.index:
        data.at[i, "uniqid"] = milisec()

    print(data['uniqid'])
    data.to_csv(path_file, sep="," , index=False)



