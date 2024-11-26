from embuilder.builder import EMB

prefixes = dict(
    rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
    rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
    prov = "http://www.w3.org/ns/prov#",
    ftr = "https://w3id.org/ftr#",
    dcat = "https://www.w3.org/ns/dcat#",
    sio = "http://semanticscience.org/resource/",
    dcterms = "http://purl.org/dc/terms/",
    codemeta = "https://codemeta.github.io/terms/",
    adms = "http://www.w3.org/ns/adms#",
    vivo = "http://vivoweb.org/ontology/core#",
    doap = "http://usefulinc.com/ns/doap#",
    dqv = "http://www.w3.org/ns/dqv#"
)

triplets = [

# Test
["this:$(uniqid)_Test","rdf:type","ftr:Test","iri"],
["this:$(uniqid)_Test","rdf:type","dcat:DataService","iri"],

["this:$(uniqid)_Test","dcterms:identifier","$(identifier)","iri"],
["this:$(uniqid)_Test","dcterms:title","$(title)","xsd:string"],
["this:$(uniqid)_Test","dcterms:description","$(description)","xsd:string"],
["this:$(uniqid)_Test","dcterms:keyword","$(keyword)","xsd:string"],
["this:$(uniqid)_Test","ftr:indicator","$(indicator)","iri"],
["this:$(uniqid)_Test","dcat:endpointDescription","$(endpoint_description)","xsd:string"],
["this:$(uniqid)_Test","dcat:endpointURL","$(endpoint_url)","iri"],
["this:$(uniqid)_Test","doap:repository","$(source_code)","iri"],
["this:$(uniqid)_Test","dcterms:type","$(type)","iri"],
["this:$(uniqid)_Test","dcterms:license","$(license)","iri"],
["this:$(uniqid)_Test","dcat:theme","$(theme)","iri"],
["this:$(uniqid)_Test","dcterms:version","$(version)","xsd:string"],
["this:$(uniqid)_Test","adms:versionNotes","$(version_notes)","xsd:string"],

["this:$(uniqid)_Test","dcat:contactPoint","$(contact)","iri"],
["$(contact)","rdf:type","vcard:Organization","iri"],
["$(contact)","rdf:type","vcard:Individual","iri"],
["$(contact)","vcard:fn","$(vc_name)","xsd:string"],
["$(contact)","vcard:email","$(vc_email)","xsd:string"],
["$(contact)","vcard:organization-name","$(org_name)","xsd:string"],

["this:$(uniqid)_Test","dcterms:creator","$(creator)","iri"],
["$(creator)","rdf:type","vcard:Organization","iri"],
["$(creator)","rdf:type","vcard:Individual","iri"],
["$(creator)","vcard:fn","$(vc_name)","xsd:string"],
["$(creator)","vcard:email","$(vc_email)","xsd:string"],
["$(creator)","vcard:organization-name","$(org_name)","xsd:string"],

["this:$(uniqid)_Test","sio:SIO_000233","this:$(uniqid)_Metric","iri"],

# Metric
["this:$(uniqid)_Metric","rdf:type","dqv:Metric","iri"],
["this:$(uniqid)_Metric","dcterms:identifier","$(identifier)","iri"],
["this:$(uniqid)_Metric","dcterms:title","$(title)","xsd:string"],
["this:$(uniqid)_Metric","dcterms:description","$(description)","xsd:string"],
["this:$(uniqid)_Metric","dcterms:keyword","$(keyword)","xsd:string"],
["this:$(uniqid)_Metric","dqv:inDimension","$(dimension)","iri"],
["this:$(uniqid)_Metric","vivo:abbreviation","$(abbrevation)","xsd:string"],
["this:$(uniqid)_Metric","dcat:landingPage","$(homepage)","iri"],
["this:$(uniqid)_Metric","dcat:theme","$(theme)","iri"],
["this:$(uniqid)_Metric","dcterms:version","$(version)","xsd:string"],
["this:$(uniqid)_Metric","ftr:status","$(status)","iri"],


["this:$(uniqid)_Metric","dcat:contactPoint","$(contact)","iri"],
["$(contact)","rdf:type","prov:Organization","iri"],
["$(contact)","rdf:type","prov:Person","iri"],
["$(contact)","vcard:fn","$(vc_name)","xsd:string"],
["$(contact)","vcard:email","$(vc_email)","xsd:string"],

["this:$(uniqid)_Metric","dcterms:creator","$(creator)","iri"],
["$(creator)","rdf:type","prov:Organization","iri"],
["$(creator)","rdf:type","prov:Person","iri"],
["$(creator)","vcard:fn","$(vc_name)","xsd:string"],
["$(creator)","vcard:email","$(vc_email)","xsd:string"],

["this:$(uniqid)_Metric","sio:SIO_000234","this:$(uniqid)_Test","iri"]
]

config = dict(
  source_name = "source_cde_test",
  configuration = "default",   
  csv_name = "/mnt/data/CARE.csv",
  basicURI = "this"
)

builder = EMB(config, prefixes, triplets)
# test = builder.transform_YARRRML()
# test = builder.transform_OBDA()
test = builder.transform_ShEx()
# test = builder.transform_SPARQL()
print(test)