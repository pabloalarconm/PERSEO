from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "https://sio.semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [

# Nodes
["this:$(pid)_ID","sio:SIO_000020","this:$(pid)_$(uniqid)_Role","iri","this:$(uniqid)_Context"],
["this:$(pid)_Entity","sio:SIO_000228","this:$(pid)_$(uniqid)_Role","iri","this:$(uniqid)_Context"],
["this:$(pid)_Entity","sio:SIO_000008","this:$(pid)_$(uniqid)_Attribute","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Process","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000291","$(target_id)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000139","$(agent_id)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000230","this:$(pid)_$(uniqid)_Input","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000229","$(output_id)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","sio:SIO_000339","$(protocol_id)","iri","this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000628","this:$(pid)_$(uniqid)_Attribute","iri","this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000221","this:$(pid)_$(uniqid)_Unit","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","$(substance_id)","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","this:$(pid)_$(uniqid)_Route","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","this:$(pid)_$(uniqid)_Activity","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","this:$(pid)_$(uniqid)_Intensity","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","this:$(pid)_$(uniqid)_Concentration","iri","this:$(uniqid)_Context"],
["$(protocol_id)","sio:SIO_000008","this:$(pid)_$(uniqid)_Frequency","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration","sio:SIO_000221","this:$(pid)_$(uniqid)_Concentration_Unit","iri","this:$(uniqid)_Context"],


# Types
["this:$(pid)_ID","rdf:type","sio:SIO_000115","iri","this:$(uniqid)_Context"],
["this:$(pid)_Entity","rdf:type","sio:SIO_000498","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Role","rdf:type","sio:SIO_000016","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Role","rdf:type","obo:OBI_0000093","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","rdf:type","sio:SIO_000006","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","rdf:type","$(process_type)","iri","this:$(uniqid)_Context"],
["$(output_id)","rdf:type","sio:SIO_000015","iri","this:$(uniqid)_Context"],
["$(output_id)","rdf:type","$(output_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Input","rdf:type","sio:SIO_000015","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Input","rdf:type","$(input_type)","iri","this:$(uniqid)_Context"],
["$(target_id)","rdf:type","sio:SIO_000015","iri","this:$(uniqid)_Context"],
["$(target_id)","rdf:type","$(target_type)","iri","this:$(uniqid)_Context"],

["$(agent_id)","rdf:type","sio:SIO_000015","iri","this:$(uniqid)_Context"],
["$(agent_id)","rdf:type","$(agent_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Attribute","rdf:type","sio:SIO_000614","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Attribute","sio:SIO_000332","$(attribute_type2)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Attribute","rdf:type","$(attribute_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Unit","rdf:type","sio:SIO_000074","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Unit","rdf:type","$(unit_type)","iri","this:$(uniqid)_Context"],

["$(protocol_id)","rdf:type","sio:SIO_001043","iri","this:$(uniqid)_Context"],
["$(protocol_id)","rdf:type","obo:OBI_0000272","iri","this:$(uniqid)_Context"],
["$(substance_id)","rdf:type","sio:SIO_011126","iri","this:$(uniqid)_Context"],
["$(substance_id)","rdf:type","obo:NCIT_C177929","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Route","rdf:type","sio:SIO_001107","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Route","rdf:type","$(route_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Activity","rdf:type","sio:SIO_000006","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Activity","rdf:type","$(activity_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Intensity","rdf:type","sio:SIO_001212","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Intensity","rdf:type","$(intensity_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration","rdf:type","sio:SIO_001088","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration","rdf:type","obo:NCIT_C25488","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdf:type","sio:SIO_001367","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdf:type","$(frequency_type)","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration_Unit","rdf:type","sio:SIO_000074","iri","this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration_Unit","rdf:type","$(unit_type)","iri","this:$(uniqid)_Context"],

# Labels
["this:$(pid)_ID","rdfs:label","Identifier","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_Entity","rdfs:label","Person","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Role","rdfs:label","Patient role","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","rdfs:label","$(model) measurement process","xsd:string", "this:$(uniqid)_Context"],
["$(output_id)","rdfs:label","$(model) measurement output","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Input","rdfs:label","$(model) input","xsd:string", "this:$(uniqid)_Context"],
["$(target_id)","rdfs:label","$(model) target","xsd:string", "this:$(uniqid)_Context"],
["$(agent_id)","rdfs:label","$(model) agent","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Attribute","rdfs:label","$(model) attribute","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Unit","rdfs:label","$(model) unit of measurement","xsd:string", "this:$(uniqid)_Context"],
["$(protocol_id)","rdfs:label","$(model) protocol","xsd:string", "this:$(uniqid)_Context"],
["$(substance_id)","rdfs:label","$(model) chemical substance","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Route","rdfs:label","$(model) route","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Activity","rdfs:label","$(model) activity","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Intensity","rdfs:label","$(model) intensity","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration","rdfs:label","$(model) concentration","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Frequency","rdfs:label","$(model) frequency","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration_Unit","rdfs:label","$(model) concentration unit","xsd:string", "this:$(uniqid)_Context"],


# Values
["this:$(pid)_ID","sio:SIO_000300","$(pid)","xsd:string", "this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000300","$(value_string)","xsd:string", "this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000300","$(value_date)","xsd:date", "this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000300","$(value_float)","xsd:float", "this:$(uniqid)_Context"],
["$(output_id)","sio:SIO_000300","$(value_integer)","xsd:integer", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Process","rdfs:comments","$(comments)","xsd:string", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Frequency","sio:SIO_000300","$(frequency_value)","xsd:integer", "this:$(uniqid)_Context"],
["this:$(pid)_$(uniqid)_Concentration","sio:SIO_000300","$(concentration_value)","xsd:float", "this:$(uniqid)_Context"],


# Context:
## Temporal context
# ["this:$(uniqid)_Context","sio:SIO_000687","this:$(uniqid)_Date","iri"],
["this:$(uniqid)_Context","sio:SIO_000687","this:$(uniqid)_Age","iri"],
["this:$(uniqid)_Context","sio:SIO_000680","this:$(uniqid)_Startdate","iri"],
["this:$(uniqid)_Context","sio:SIO_000681","this:$(uniqid)_Enddate","iri"],

["this:$(uniqid)_Context","rdf:type","obo:NCIT_C62143","iri"],
# ["this:$(uniqid)_Date","rdf:type","sio:SIO_000418","iri"],
# ["this:$(uniqid)_Date","rdf:type","obo:NCIT_C25164","iri"],
["this:$(uniqid)_Age","rdf:type","sio:SIO_001013","iri"],
["this:$(uniqid)_Age","rdf:type","obo:NCIT_C25150","iri"],
["this:$(uniqid)_Startdate","rdf:type","sio:SIO_000031","iri"],
["this:$(uniqid)_Enddate","rdf:type","sio:SIO_000032","iri"],

# ["this:$(uniqid)_Date","rdfs:label","$(model) date when it ocurred: $(date)","xsd:string"],
["this:$(uniqid)_Age","rdfs:label","$(model) age when it ocurred: $(age)","xsd:string"],
["this:$(uniqid)_Startdate","rdfs:label","$(model) startdate: $(startdate)","xsd:string"],
["this:$(uniqid)_Enddate","rdfs:label","$(model) enddate: $(enddate)","xsd:string"],

["this:$(uniqid)_Context","sio:SIO_000300","$(uniqid)","xsd:string"],
# ["this:$(uniqid)_Date","sio:SIO_000300","$(date)","xsd:date"],
["this:$(uniqid)_Age","sio:SIO_000300","$(age)","xsd:float"],
["this:$(uniqid)_Startdate","sio:SIO_000300","$(startdate)","xsd:date"],
["this:$(uniqid)_Enddate","sio:SIO_000300","$(enddate)","xsd:date"],

## Timeline:
["this:$(uniqid)_Context","sio:SIO_000068","this:$(pid)_Timeline","iri"],
["this:$(pid)_Timeline","sio:SIO_000332","this:$(pid)_Person","iri"],
["this:$(pid)_Person","sio:SIO_000671","this:$(pid)_Identifier","iri"],
["this:$(pid)_Timeline","rdf:type","sio:SIO_000417","iri"],
["this:$(pid)_Timeline","rdf:type","obo:NCIT_C54576","iri"],
["this:$(pid)_Person","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_Identifier","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_Identifier","sio:SIO_000300","$(pid)","xsd:string"],

## Event:
["this:$(uniqid)_Context","sio:SIO_000068","this:$(pid)_$(event_id)_Event","iri"],
["this:$(pid)_$(event_id)_Event","rdf:type","obo:NCIT_C25499","iri"],
["this:$(pid)_$(event_id)_Event","sio:SIO_000300","$(event_id)","xsd:string"]
]

config = dict(
  source_name = "source_cde_test",
  configuration = "default",   
  csv_name = "/mnt/data/CDE",
  basicURI = "this"
)

builder = EMB(config, prefixes, triplets)
test = builder.transform_YARRRML()
# test = builder.transform_OBDA()
# test = builder.transform_ShEx()
# test = builder.transform_SPARQL()
print(test)
