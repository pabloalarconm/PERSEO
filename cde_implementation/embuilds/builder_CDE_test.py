from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "https://sio.semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [


["this:$(pid)_$(uniqid)_Process","sio:SIO_000139","$(agent_id)","iri", "this:$(uniqid)_Context"],


["$(agent_id)","rdf:type","sio:SIO_000015","iri", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","rdf:type","sio:SIO_000006","iri", "this:$(uniqid)_Context"],


["$(agent_id)","sio:SIO_000300","$(value)","xsd:string", "this:$(uniqid)_Context"],

]

config = dict(
  source_name = "source_cde_test",
  configuration = "ejp",   
  csv_name = "source_1",
  basicURI = "this"
)

builder = EMB(config, prefixes, triplets)
test = builder.transform_YARRRML()
# test = builder.transform_OBDA()
# test = builder.transform_ShEx()
# test = builder.transform_SPARQL()
print(test)
