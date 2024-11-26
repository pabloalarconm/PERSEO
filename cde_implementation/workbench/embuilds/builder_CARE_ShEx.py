from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [

# # Nodes
# ["this:$(pid)_Identifier","sio:SIO_000020","this:$(pid)_$(uniqid)_Role","iri"],
# ["this:$(pid)_Individual","sio:SIO_000228","this:$(pid)_$(uniqid)_Role","iri"],
# ["this:$(pid)_$(uniqid)_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Process","iri"],
# ["this:$(pid)_$(uniqid)_Process","sio:SIO_000291","$(target_id)","iri"],
# ["this:$(pid)_$(uniqid)_Process","sio:SIO_000139","$(agent_id)","iri"],
# ["this:$(pid)_$(uniqid)_Process","sio:SIO_000230","this:$(pid)_$(uniqid)_Input","iri"],
# ["this:$(pid)_$(uniqid)_Process","sio:SIO_000229","$(output_id)","iri"],
# ["this:$(pid)_$(uniqid)_Process","sio:SIO_000339","$(protocol_id)","iri"],
# ["$(output_id)","sio:SIO_000628","this:$(pid)_$(uniqid)_Attribute","iri"],
# ["$(output_id)","sio:SIO_000221","this:$(pid)_$(uniqid)_Unit","iri"],
# ["$(protocol_id)","sio:SIO_000028","$(substance_id)","iri"],
# ["$(protocol_id)","sio:SIO_000028","this:$(pid)_$(uniqid)_Action_specification","iri"],
# ["$(protocol_id)","sio:SIO_000028","this:$(pid)_$(uniqid)_Concentration","iri"],
# ["$(protocol_id)","sio:SIO_000028","this:$(pid)_$(uniqid)_Frequency","iri"],
# ["this:$(pid)_$(uniqid)_Concentration","sio:SIO_000221","this:$(pid)_$(uniqid)_Specification_unit","iri"],
# ["this:$(pid)_$(uniqid)_Specific_process","sio:SIO_000325","this:$(pid)_$(uniqid)_Process","iri"],


# # Types
# # ["this:$(pid)_Identifier","rdf:type","obo:NCIT_C164337","iri"],
# ["this:$(pid)_Identifier","rdf:type","sio:SIO_000115","iri"],
# # ["this:$(pid)_Individual","rdf:type","obo:NCIT_C25190","iri"],
# ["this:$(pid)_Individual","rdf:type","sio:SIO_000498","iri"],
# ["this:$(pid)_$(uniqid)_Role","rdf:type","sio:SIO_000016","iri"],
# ["this:$(pid)_$(uniqid)_Role","rdf:type","obo:OBI_0000093","iri"],
# ["this:$(pid)_$(uniqid)_Process","rdf:type","sio:SIO_000006","iri"],
# ["this:$(pid)_$(uniqid)_Process","rdf:type","$(process_type)","iri"],
# ["this:$(pid)_$(uniqid)_Specific_process","rdf:type","sio:SIO_000006","iri"],
# ["this:$(pid)_$(uniqid)_Specific_process","rdf:type","$(specific_process_type)","iri"],
# ["$(output_id)","rdf:type","sio:SIO_000015","iri"],
# ["$(output_id)","rdf:type","$(output_type)","iri"],
# ["this:$(pid)_$(uniqid)_Input","rdf:type","sio:SIO_000015","iri"],
# ["this:$(pid)_$(uniqid)_Input","rdf:type","$(input_type)","iri"],
# ["$(target_id)","rdf:type","sio:SIO_000015","iri"],
# ["$(target_id)","rdf:type","$(target_type)","iri"],
# ["$(agent_id)","rdf:type","sio:SIO_000015","iri"],
# ["$(agent_id)","rdf:type","$(agent_type)","iri"],
# ["this:$(pid)_$(uniqid)_Attribute","rdf:type","sio:SIO_000614","iri"],
# ["this:$(pid)_$(uniqid)_Attribute","rdf:type","$(attribute_type)","iri"],
# ["this:$(pid)_$(uniqid)_Unit","rdf:type","sio:SIO_000074","iri"],
# ["this:$(pid)_$(uniqid)_Unit","rdf:type","$(unit_type)","iri"],

# ["$(protocol_id)","rdf:type","sio:SIO_000090","iri"],
# ["$(protocol_id)","rdf:type","$(protocol_type)","iri"],
# ["$(substance_id)","rdf:type","sio:SIO_000315","iri"],
# ["$(substance_id)","rdf:type","$(substance_type)","iri"],
# ["this:$(pid)_$(uniqid)_Action_specification","rdf:type","sio:SIO_000091","iri"],
# ["this:$(pid)_$(uniqid)_Action_specification","rdf:type","$(activity_type)","iri"],
# ["this:$(pid)_$(uniqid)_Concentration","rdf:type","sio:SIO_001088","iri"],
# ["this:$(pid)_$(uniqid)_Concentration","rdf:type","$(concentration_type)","iri"],
# ["this:$(pid)_$(uniqid)_Frequency","rdf:type","sio:SIO_001367","iri"],
# ["this:$(pid)_$(uniqid)_Frequency","rdf:type","$(frequency_type)","iri"],
# ["this:$(pid)_$(uniqid)_Specification_unit","rdf:type","sio:SIO_000074","iri"],
# ["this:$(pid)_$(uniqid)_Specification_unit","rdf:type","$(concentration_unit_type)","iri"],

# # Labels
# ["this:$(pid)_Identifier","rdfs:label","Identifier","xsd:string"],
# ["this:$(pid)_Individual","rdfs:label","Subject","xsd:string"],
# ["this:$(pid)_$(uniqid)_Role","rdfs:label","Patient role","xsd:string"],
# ["this:$(pid)_$(uniqid)_Process","rdfs:label","$(model) assessment process","xsd:string"],
# ["$(output_id)","rdfs:label","$(model) measurement output","xsd:string"],
# ["this:$(pid)_$(uniqid)_Input","rdfs:label","$(model) input","xsd:string"],
# ["$(target_id)","rdfs:label","$(model) target","xsd:string"],
# ["$(agent_id)","rdfs:label","$(model) agent","xsd:string"],
# ["this:$(pid)_$(uniqid)_Attribute","rdfs:label","$(model) attribute","xsd:string"],
# ["this:$(pid)_$(uniqid)_Unit","rdfs:label","$(model) unit of measurement","xsd:string"],
# ["$(protocol_id)","rdfs:label","$(model) specification","xsd:string"],
# ["$(substance_id)","rdfs:label","$(model) functional specification or substance","xsd:string"],
# ["this:$(pid)_$(uniqid)_Action_specification","rdfs:label","$(model) action or route specification","xsd:string"],
# ["this:$(pid)_$(uniqid)_Concentration","rdfs:label","$(model) concentration specification","xsd:string"],
# ["this:$(pid)_$(uniqid)_Frequency","rdfs:label","$(model) frequency specification","xsd:string"],
# ["this:$(pid)_$(uniqid)_Specification_unit","rdfs:label","$(model) concentration specification unit","xsd:string"],


# # Values
# ["this:$(pid)_Identifier","sio:SIO_000300","$(pid)","xsd:string"],
# ["$(output_id)","sio:SIO_000300","$(value_string)","xsd:string"],
# ["$(output_id)","sio:SIO_000300","$(value_date)","xsd:date"],
# ["$(output_id)","sio:SIO_000300","$(value_float)","xsd:float"],
# ["$(output_id)","sio:SIO_000300","$(value_integer)","xsd:integer"],
# ["this:$(pid)_$(uniqid)_Process","rdfs:comments","$(comments)","xsd:string"],
# ["this:$(pid)_$(uniqid)_Frequency","sio:SIO_000300","$(frequency_value)","xsd:integer"],
# ["this:$(pid)_$(uniqid)_Concentration","sio:SIO_000300","$(concentration_value)","xsd:float"],


# Context:
## Temporal context
["this:$(uniqid)_Context","sio:SIO_000687","this:$(uniqid)_Age","iri"],
["this:$(uniqid)_Context","sio:SIO_000680","this:$(uniqid)_Startdate","iri"],
["this:$(uniqid)_Context","sio:SIO_000681","this:$(uniqid)_Enddate","iri"],

["this:$(uniqid)_Context","rdf:type","obo:NCIT_C62143","iri"],
["this:$(uniqid)_Age","rdf:type","sio:SIO_001013","iri"],
["this:$(uniqid)_Age","rdf:type","obo:NCIT_C25150","iri"],
["this:$(uniqid)_Startdate","rdf:type","sio:SIO_000031","iri"],
["this:$(uniqid)_Startdate","rdf:type","obo:NCIT_C68616","iri"],
["this:$(uniqid)_Enddate","rdf:type","sio:SIO_000032","iri"],
["this:$(uniqid)_Enddate","rdf:type","obo:NCIT_C68617","iri"],


["this:$(uniqid)_Age","rdfs:label","$(model) age when it ocurred: $(age)","xsd:string"],
["this:$(uniqid)_Startdate","rdfs:label","$(model) startdate: $(startdate)","xsd:string"],
["this:$(uniqid)_Enddate","rdfs:label","$(model) enddate: $(enddate)","xsd:string"],

["this:$(uniqid)_Context","sio:SIO_000300","$(uniqid)","xsd:string"],
["this:$(uniqid)_Age","sio:SIO_000300","$(age)","xsd:float"],
["this:$(uniqid)_Startdate","sio:SIO_000300","$(startdate)","xsd:date"],
["this:$(uniqid)_Enddate","sio:SIO_000300","$(enddate)","xsd:date"],

## Timeline:
["this:$(uniqid)_Context","sio:SIO_000068","this:$(pid)_Timeline","iri"],
["this:$(pid)_Timeline","sio:SIO_000332","this:$(pid)_Person","iri"],
["this:$(pid)_Person","sio:SIO_000671","this:$(pid)_Person_identifier","iri"],

["this:$(pid)_Timeline","rdf:type","sio:SIO_000417","iri"],
["this:$(pid)_Timeline","rdf:type","obo:NCIT_C54576","iri"],
["this:$(pid)_Person","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_Person","rdf:type","obo:NCIT_C25190","iri"],
["this:$(pid)_Person_identifier","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_Person_identifier","rdf:type","obo:NCIT_C164337","iri"],

["this:$(pid)_Person_identifier","sio:SIO_000300","$(pid)","xsd:string"],

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
# test = builder.transform_YARRRML()
# test = builder.transform_OBDA()
test = builder.transform_ShEx()
# test = builder.transform_SPARQL()
print(test)
