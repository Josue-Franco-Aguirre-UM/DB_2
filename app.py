import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

def _extract_employees_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return pd.DataFrame()

    df = df.rename(columns={
        'codigo_Empleado': 'code',
        'Empleado': 'employee',
        'Email': 'email',
    })

    df['code'] = df['code'].astype(str)
    return df

def _extract_employees_details_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return pd.DataFrame()

    df = df.rename(columns={
        'Codigo_Empleado': 'code',
        'Área': 'area',
        'Horario': 'schedule',
    })

    df['code'] = df['code'].astype(str)
    return df

engine = create_engine('mysql+pymysql://root:@localhost/employees_db')

st.title("Upload employee information Excel files")

uploaded_file_employees = st.file_uploader("Employee list Excel file", type=["xls", "xlsx"])
uploaded_file_details = st.file_uploader("Employee details list Excel file", type=["xls", "xlsx"])

df_employees = pd.DataFrame()
df_details = pd.DataFrame()

if uploaded_file_employees is not None:
    st.write("Employee list file was uploaded successfully.")
    df_employees = _extract_employees_from_excel(uploaded_file_employees)
    st.write(df_employees)

if uploaded_file_details is not None:
    st.write("Employee details file was uploaded successfully.")
    df_details = _extract_employees_details_from_excel(uploaded_file_details)
    st.write(df_details)

if st.button("Upload to Database"):
    if not df_employees.empty and not df_details.empty:
        combined_df = pd.merge(df_employees, df_details, on='code')
        st.write("Combined DataFrame:")
        st.write(combined_df)
        
        combined_df.to_sql('employees_combined', con=engine, if_exists='append', index=False)
        
        df_employees.to_sql('employees', con=engine, if_exists='append', index=False)
        df_details.to_sql('employee_details', con=engine, if_exists='append', index=False)
        
        st.success("Employee data has been uploaded to the database.")
    else:
        st.error("Please upload both Employee list and Employee details Excel files.")