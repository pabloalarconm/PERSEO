from Hefesto.main import Hefesto
import pandas as pd


df_cde = pd.read_csv("../../test_hefesto/OFFICIAL_DATA_INPUT.csv")
# print(df_cde)

# Birthdate information
col_birthdate = "birthdate"
df_cde[col_birthdate] = pd.to_datetime(df_cde[col_birthdate])

df_cde["Birth_datetime"] = df_cde[col_birthdate]
df_cde["Year_of_birth"] = df_cde[col_birthdate].dt.year
df_cde["Month_of_birth"] = df_cde[col_birthdate].dt.month
df_cde["Day_of_birth"] = df_cde[col_birthdate].dt.day

print(df_cde)

# Sex information

# col_sex = "sex_uri"
# df_cde["gender_source_value"] = df_cde.loc[:, col_sex]
# df_cde["gender_concept_id"] = df_cde.loc[:, col_sex]

# df_cde = df_cde.replace({
#     'gender_concept_id' : {
#         'http://purl.obolibrary.org/obo/NCIT_C16576' : 8532, # Female
#         'http://purl.obolibrary.org/obo/NCIT_C20197' : 8507, # Male
#         'http://purl.obolibrary.org/obo/NCIT_C124294' : 4086451, # Undertermined
#         'http://purl.obolibrary.org/obo/NCIT_C17998':  4086451 # Unknown as Undetermined
#         }
#     })
# # print(df_cde)


# Status and Death date information:
# TODO : This person_id will be registered in the DEATH table including date etc.

# Care pathway information:

