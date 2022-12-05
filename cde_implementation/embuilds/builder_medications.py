from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [

# Nodes
["this:$(pid)_ID","sio:SIO_000020","this:$(pid)_$(uniqid)_Role","iri", "this:$(context_id)_Context"],
["this:$(pid)_Entity","sio:SIO_000228","this:$(pid)_$(uniqid)_Role","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Process","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000362","this:$(pid)_$(uniqid)_Route","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000139","this:$(pid)_$(uniqid)_Drug","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Drug","sio:SIO_000008","this:$(pid)_$(uniqid)_Dose","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","sio:SIO_000221","this:$(pid)_$(uniqid)_Unit","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","sio:SIO_000900","this:$(pid)_$(uniqid)_Frequency","iri", "this:$(context_id)_Context"],
["$(atcURI)","sio:SIO_000313","this:$(pid)_$(uniqid)_Drug","iri", "this:$(context_id)_Context"],

# Types
["this:$(pid)_ID","rdf:type","sio:SIO_000115","iri", "this:$(context_id)_Context"],
["this:$(pid)_Entity","rdf:type","sio:SIO_000498","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Role","rdf:type","sio:SIO_000016","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Role","rdf:type","obo:OBI_0000093","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","rdf:type","sio:SIO_000006","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","rdf:type","$(processURI)","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Route","rdf:type","$sio:SIO_000015","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Route","rdf:type","$(inputURI)","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","rdf:type","sio:SIO_000614","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","rdf:type","obo:NCIT_C25488","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Drug","rdf:type","sio:SIO_010038","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdf:type","sio:SIO_001367","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdf:type","$(frequencyURI)","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Unit","rdf:type","sio:SIO_000074","iri", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Unit","rdf:type","$(unitURI)","iri", "this:$(context_id)_Context"],
["$(atcURI)","rdf:type","obo:NCIT_C177929","iri", "this:$(context_id)_Context"],

# Labels
["this:$(pid)_ID","rdfs:label","Identifier","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_Entity","rdfs:label","Person","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Role","rdfs:label","Patient role","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","rdfs:label","$(model) measurement process","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Process","rdfs:comment","$(comments)","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Route","rdfs:label","$(inputLabel)","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","rdfs:label","Dose","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Drug","rdfs:label","Drug","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Drug","rdfs:label","Drug","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdfs:label","$(frequencyLabel)","xsd:string", "this:$(context_id)_Context"],
["$(atcURI)","rdfs:label","Drug component","xsd:string", "this:$(context_id)_Context"],

# Values
["this:$(pid)_ID","sio:SIO_000300","$(pid)","xsd:string", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Dose","sio:SIO_000300","$(value)","$(datatype)", "this:$(context_id)_Context"],
["this:$(pid)_$(uniqid)_Frequency","sio:SIO_000300","$(valueFrequency)","xsd:integer", "this:$(context_id)_Context"],

# Metadata:
["this:$(context_id)_Context","sio:SIO_000680","this:$(context_id)_Startdate","iri"],
["this:$(context_id)_Context","sio:SIO_000681","this:$(context_id)_Enddate", "iri"],
["this:$(context_id)_Context","sio:SIO_000068","this:$(pid)_Timeline","iri"],
["this:$(pid)_Timeline","sio:SIO_000332","this:$(pid)_Person","iri"],
["this:$(pid)_Person","sio:SIO_000671","this:$(pid)_Identifier","iri"],

["this:$(context_id)_Context","rdf:type","obo:NCIT_C25616","iri"],
["this:$(context_id)_Startdate","rdf:type","sio:SIO_000031","iri"],
["this:$(context_id)_Enddate","rdf:type","sio:SIO_000032","iri"],
["this:$(pid)_Timeline","rdf:type","sio:SIO_000417","iri"],
["this:$(pid)_Timeline","rdf:type","obo:NCIT_C54576","iri"],
["this:$(pid)_Person","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_Identifier","rdf:type","sio:SIO_000115","iri"],

["this:$(context_id)_Startdate","rdfs:label","$(model) startdate: $(startdate)","xsd:string"],
["this:$(context_id)_Enddate","rdfs:label","$(model) enddate: $(enddate)","xsd:string"],

["this:$(context_id)_Startdate","sio:SIO_000300","$(startdate)","xsd:date"],
["this:$(context_id)_Enddate","sio:SIO_000300","$(enddate)","xsd:date"],
["this:$(pid)_Identifier","sio:SIO_000300","$(pid)","xsd:string"]
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