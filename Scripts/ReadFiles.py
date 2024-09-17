import pandas as pd
import streamlit as st
#column defination like column_name, index and length.
column_defination=pd.read_csv("Python_reading_files_sorting_based_on_indexes/Inputs_Required/column_def.csv")
#source file path.
source_file_path=r"Python_reading_files_sorting_based_on_indexes/Inputs_Required/txtfile.txt"
column_data=[[] for _ in range ( len(column_defination))]
with open (source_file_path,'r') as file1:
    lines=file1.readlines()

for line in lines:
    for i, row in column_defination.iterrows():
        index=row['index']
        length=row['length']
        column_data[i].append(line[index:index+length].strip())

extracted_data={f'Column{i+1}': column_data[i] for i in range(len(column_defination))}
extracted_df=pd.DataFrame(extracted_data,dtype=str)

st.title('Welcome to the ETL-TEST-UI-Astra')
st.menu["Home","Read_files"]