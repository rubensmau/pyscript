import pandas as pd
import sqlite3 as sql

# create df
election_df = pd.read_csv("https://researchbriefings.files.parliament.uk/documents/CBP-8749/HoC-GE2019-results-by-constituency-csv.csv")

print (election_df.columns)
election_df.drop(['ons_id', 
                  'ons_region_id',
                  'county_name',
                  'region_name',
                  'country_name',
                  'constituency_type',
                  'declaration_time',
                  'mp_gender'
                  ], axis=1, inplace=True)
print (election_df.columns)

# create db
conn = sql.connect('elections.db')
election_df.to_sql('elections', conn)

election_df.to_csv('elections.csv')
