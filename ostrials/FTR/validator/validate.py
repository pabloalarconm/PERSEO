from pyshex import ShExEvaluator
from rdflib import Namespace

rdf = """
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
    @prefix ftr: <https://www.w3id.org/ftr#> .
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix doap: <http://usefulinc.com/ns/doap#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix dqv: <http://www.w3.org/ns/dqv#> .
    @prefix vivo: <http://vivoweb.org/ontology/core#> .

    <https://w3id.org/foops/test/DOC1> a ftr:Test , dcat:DataService ;
        dcat:contactPoint <https://orcid.org/0000-0003-0454-7145> ;
        dcterms:creator <https://orcid.org/0000-0003-0454-7145> ;
        dcterms:creator <https://orcid.org/0000-0003-3587-0367> ;
        dcterms:title "HTML availability"^^xsd:string ;
        rdfs:label "DOC1"^^xsd:string ;
        vivo:abbreviation "DOC1"^^xsd:string ;
        dcterms:license <http://creativecommons.org/licenses/by/2.0/> ;
        dqv:inDimension <https://w3id.org/fair/principles/terms/R1> ;
        dcterms:description "This check verifies if the ontology has an HTML documentation"^^xsd:string ; # Falta explicar PASS y FAIL
        dcterms:contactPoint <https://oeg.fi.upm.es> ;
        dcat:version "0.0.1"^^xsd:string ;
        dcterms:identifier <https://w3id.org/foops/test/DOC1> ;
        dcat:keyword "HTML availability"^^xsd:string , "Test"^^xsd:string , "Reusable"^^xsd:string ;
        <http://semanticscience.org/resource/SIO_000233> <https://w3id.org/foops/metric/DOC1> ;
        doap:repository <https://w3id.org/foops/repository> .
    <https://orcid.org/0000-0003-0454-7145> a vcard:Individual;
        vcard:fn "Daniel Garijo"^^xsd:string ;
        vcard:hasEmail <mailto:dgarijo@upm.es> .
    <https://orcid.org/0000-0003-3587-0367> a vcard:Individual;
        vcard:fn "Maria Poveda"^^xsd:string ;
        vcard:hasEmail <mailto:m.poveda@upm.es> .
    <https://w3id.org/fair/principles/terms/R1> a <https://w3id.org/fair/principles/terms/FAIR-SubPrinciple> ;
        rdfs:label "R1"^^xsd:string ;
        vivo:abbreviation "R1"^^xsd:string ;
        dcterms:description "meta(data) are richly described with a plurality of accurate and relevant attributes."^^xsd:string .
    <https://oeg.fi.upm.es> a vcard:Organization .
    <https://w3id.org/foops/repository>
    foaf:homePage <https://github.com/oeg-upm/fair_ontologies> .
    <https://w3id.org/foops/metric/DOC1> a dqv:Metric .
"""
# rdf_graph = Graph()
# rdf = rdf_graph.parse(data=rdf_data, format="turtle")

shex = """
:organizationShape IRI {
  vcard:organization-name xsd:string? ;
  a [vcard:Organization] ;
}

:individualShape IRI {
  vcard:fn xsd:string? ;
  vcard:hasEmail IRI? ;
  a [vcard:Individual] ;
}

:testShape IRI {
  a [ftr:Test dcat:DataService]+ ;
  dcterms:identifier IRI ;
  dcterms:title xsd:string ;
  dcterms:description xsd:string ;
  dcterms:keyword xsd:string* ;
  vivo:abbreviation xsd:string ;
  dqv:inDimension IRI? ;
  dcat:endpointDescription xsd:string? ;
  dcat:endpointURL IRI? ;
  doap:repository IRI? ;
  dcterms:type IRI? ;
  dcterms:license IRI ;
  dcat:theme IRI? ;
  dcterms:version xsd:string ;
  adms:versionNotes xsd:string? ;
  dcat:contactPoint @:organizationShape* ;
  dcterms:creator @:organizationShape* ;
  dcat:contactPoint @:individualShape* ;
  dcterms:creator @:individualShape+ ;
  sio:SIO_000233 @:metricShape ;
}

:metricShape IRI {
	a [dqv:Metric]
}
"""



# Define the target node and shape
target_node = "https://w3id.org/foops/test/DOC1"
target_shape = "http://www.example.org/me#testShape"

results = ShExEvaluator(rdf=rdf, schema=shex).evaluate(target_node, target_shape)
for r in results:
    if r.result:
        print("PASS")
    else:
        print(f"FAIL:\n {r.reason}")

# # Perform validation
# evaluator = ShExEvaluator(rdf=rdf_graph, schema=shex_schema)
# results = evaluator.evaluate(target_node, target_shape)

# # Output results
# for result in results:
#     print(f"Node: {result.focus}")
#     print(f"Shape: {result.shape}")
#     print(f"Valid: {result.result}")
#     if not result.result:
#         print("Reason:")
#         print(result.reason)
