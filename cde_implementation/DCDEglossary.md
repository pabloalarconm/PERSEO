## Glossary for all identified DCDE:

## DCDE - Body measurement:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: Child of http://purl.obolibrary.org/obo/NCIT_C25404
    - Suggestions:
        *    Quantitation (please use this by default) http://purl.obolibrary.org/obo/NCIT_C48937
        *    Estimate (http://purl.obolibrary.org/obo/NCIT_C25498)
- **outputURI**: http://purl.obolibrary.org/obo/NCIT_C93940
- **inputURI**: None
- **inputLabel**: None
- **targetURI**: None
- **targetLabel**: None
- **attributeURI**: Child of Personal Attribute: http://purl.obolibrary.org/obo/NCIT_C19332
- **value**: Resulting value from this observation
- **datatype**: xsd:float (by default but could be another different datatype)
- **valueIRI**: None
- **unitURI**: Child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- **unitLabel**: Human readable label that describes unit of measurement (ex: Kilogram)
- **model**: Body_measurement
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure

## DCDE - Laboratory measurement:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: child of http://purl.obolibrary.org/obo/NCIT_C25404
    - Suggestions:
        *    Quantitation (please use this by default) http://purl.obolibrary.org/obo/NCIT_C48937
        *    Estimate (http://purl.obolibrary.org/obo/NCIT_C25498)
- **outputURI**: http://purl.obolibrary.org/obo/NCIT_C93940
- **inputURI**: Material input represented as Child of Anatomic, Structure, System, or Substance http://purl.obolibrary.org/obo/NCIT_C12219 (ex: obo:Urine)
- **inputLabel**: Human readable label that described this material input (ex: Urine)
- **attributeURI**: Child of Personal Attribute: http://purl.obolibrary.org/obo/NCIT_C19332
- **value**: Resulting value from this analysis
- **datatype**: Datatype used to define the resulting value, (ex: xsd:float)
- **valueIRI**: None
- **targetURI**: Compound being measured in the sample. Child of Drug, Food, Chemical or Biomedical Material http://purl.obolibrary.org/obo/NCIT_C1908 (ex: obo:Creatinine http://purl.obolibrary.org/obo/NCIT_C399)
- **targetLabel**: Human readable label that describes this compound (ex: Creatinine)
- **unitURI**: Child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- **unitLabel**: Human readable label that describes unit of measurement (ex: Milligram) 
- **model**: Lab_measurement
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure


## DCDE - Imaging:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: child of Imaging technique http://purl.obolibrary.org/obo/NCIT_C17369  (example: obo:Digital X-Ray http://purl.obolibrary.org/obo/NCIT_C18001)
- **outputURI**: http://purl.obolibrary.org/obo/NCIT_C19477
- **inputURI**: None
- **inputLabel**: None
- **targetURI**: Child of Anatomic Structure, System, or Substance http://purl.obolibrary.org/obo/NCIT_C12219 (ex: obo:Palmar Region http://purl.obolibrary.org/obo/NCIT_C33252)
- **targetLabel**: Human readable label that describes this body part (ex: Palmar Region)
- **attributeURI**: http://purl.obolibrary.org/obo/NCIT_C94607
- **value**: Preferably a URI-based GUID of the file (must be a GUID system compatible with RDF Resource identifiers)
- **datatype**: xsd:string
- **valueIRI**: None
- **unitURI**: None
- **unitLabel**: None
- **model**: Imaging
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure



## DCDE - Medications:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: http://purl.obolibrary.org/obo/NCIT_C25538
- **outputURI**: None
- **inputURI**: Child of Route of Administration http://purl.obolibrary.org/obo/NCIT_C38114 (example: obo:Sublingual Route of Administration http://purl.obolibrary.org/obo/NCIT_C38300 )
- **inputLabel**: Human readable label that describes this route (example: Sublingual)
- **attributeURI**: None
- **value**: Dose value prescribe to the patient
- **valueFrequency**: Frequency value prescribe to the patient
- **datatype**: xsd:float(by default others like xsd:integer are also an option)
- **valueIRI**: None
- **unitURI**: Child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- **unitLabel**: Human readable label that describes unit of measurement (ex: Milligram) 
- **frequencyURI**: Child of obo:Temporal Qualifier http://purl.obolibrary.org/obo/NCIT_C21514 (ex: obo:Per Day)
- **frequencyLabel**: Human readable label that describes frequency (ex: per day)
- **atcURI**: ATC URI-code for drugs components. (example: https://www.whocc.no/atc_ddd_index/?code=A07EA01)
- **model**: Medications
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure


## DCDE - Treatment:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: Child of Intervention or Procedure http://purl.obolibrary.org/obo/NCIT_C25218 (ex: obo:Transplant Conditioning http://purl.obolibrary.org/obo/NCIT_C64468 )
- **outputURI**: Any conceptual entity presented at this process (ex obo:Fludarabine http://purl.obolibrary.org/obo/NCIT_C1094 )
- **inputURI**: None
- **inputLabel**: None
- **targetURI**: None
- **targetLabel**: None
- **attributeURI**: http://purl.obolibrary.org/obo/NCIT_C25178
- **value**: Human readable label that describes the resulting value of this treatment
- **datatype**: Any datatype that is describe at this treatment result
- **valueIRI**: None
- **unitURI**: Child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- **unitLabel**: Human readable label that describes unit of measurement (ex: Milligram) 
- **model**: Treatment
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure


## DCDE - Clinical trials:

- **pid**: Patient unique identifier
- **context_id**: *(OPTIONAL)* Contextual identifier in case you want to relate several data elements under a common context (ex: certain diagnosis/pehnotype relationship or some elements under same visit occurrence)
- **processURI**: http://purl.obolibrary.org/obo/NCIT_C71104
- **outputURI**: http://purl.obolibrary.org/obo/NCIT_C115575
- **inputURI**: http://purl.obolibrary.org/obo/NCIT_C16696
- **inputLabel**: Human readable label that describes this medical center.
- **targetURI**: None
- **targetLabel**: None
- **attributeURI**: http://purl.obolibrary.org/obo/NCIT_C2991
- **value**: Human readable label that defines clinical trial final output
- **valueInput**: GUID for this medical center where this clinical trial is taking place.
- **datatype**: xsd:string
- **valueIRI**: Orphanet disease ontology (full URL such as http://www.orpha.net/ORDO/Orphanet_100031)
- **unitURI**: None
- **unitLabel**: None
- **model**: Clinical_trials
- **startdate**: ISO 8601 formatted start date of observation
- **enddate**: (OPTIONAL) ISO 8601 formatted enddate of observation in case it is different from `startdate`.
- **comments**: Human readable comments of any kind related to this procedure
