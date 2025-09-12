CREATE OR REPLACE LOAD_EXCEL(file_path string, sheet string, src_stage string, target_table string)
RETURNS VARIANT
LANGUAGE PYTHON
RUNTIME_VERSION = '3.11'
PACKAGES = ('snowflake-snowpark-python','pandas','openpyxl')
HANDLER = 'main'
AS
$$
import openpyxl
import os, sys, csv
import pandas as pd

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session, file_path, sheet, src_stage, target_table):
    str_stg_name = f"@{src_stage}"
    xl_file = pd.ExcelFile(session.file.get_stream(os.path.join(str_stg_name,file_path)))
    data_df = pd.read_excel(xl_file, sheet_name = sheet)
    tablename = target_table.split('.')
    if len(tablename)==3:
      target_db = tablename[0]
      target_schema = tablename[1]
      target_tab = tablename[2]
    if len(tablename) == 2:
      target_db = None
      target_schema = tablename[0]
      target_tab = tablename[1]
    if len(tablename == 1:
      target_db = None
      target_schema = None
      target_tab = tarblename[0]
    session.write_pandas( df = data_df, table_name = target_tab, database = target_db, schema = target_schema, auto_create_table = True, overwrite = True)
    return "Data Loaded to "+target_table
$$
