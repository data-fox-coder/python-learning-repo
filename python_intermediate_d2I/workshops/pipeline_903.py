# import modules and functions
import pandas as pd
from sqlalchemy import (
    create_engine,
    inspect,
    text,
    select,
    MetaData,
    Table,
)

from utils import clean_903_table, group_calcuation, time_difference
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Initialise session variable
collection_year = 2014
collection_end = datetime(collection_year, 3, 31)
filepath = "/workspaces/python-learning-repo/python_intermediate_d2I/workshops/data/903_database.db"
metadata_903 = MetaData()
dfs = {}

# Read in 903 database from SQL db
engine_903 = create_engine(f"sqlite+pysqlite:///{filepath}")
connection = engine_903.connect()
inspection = inspect(engine_903)
table_names = inspection.get_table_names()

# uncomment to check database connection
# print(table_names)

for table in table_names:
    current_table = Table(table, metadata_903, autoload_with=engine_903)
    with engine_903.connect() as con:
        stmt = select(current_table)
        result = con.execute(stmt).fetchall()
    dfs[table] = pd.DataFrame(result)

# Uncomment to check dataframes
# print(dfs.keys())
# print(dfs['header'])

# Clean all tables in 903
for key, df in dfs.items():
    dfs[key] = clean_903_table(df, collection_end)

# Uncomment to check cleaned dataframes
# print(dfs['header'])

### Session 2 End ###

# dict to store measure outputs
measure = {}

measure["Header by ethnicity"] = group_calcuation(
    dfs["header"], "ETHNICITY", "Header - Ethnicities"
)

measure["Header by age"] = group_calcuation(
    dfs["header"], "AGE_BUCKETS", "Header - Age Buckets"
)

# dfs['missing']['MISSING_DURATION'] = dfs['missing'].apply(
#     lambda x: relativedelta(x['MIS_END_dt'], x['MIS_START_dt']).normalized().days, axis=1
# )

dfs["missing"]["MISSING_DURATION"] = time_difference(
    dfs["missing"]["MIS_START_dt"], dfs["missing"]["MIS_END_dt"], business_days=True
)
print(dfs["missing"])
