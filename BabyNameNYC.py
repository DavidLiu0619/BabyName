import streamlit as st
import pandas as pd

# Load the dataset
file_path = 'Popular_Baby_Names_20240515.csv'
baby_names_df = pd.read_csv(file_path)

# Normalize names to ensure consistency
baby_names_df["Child's First Name"] = baby_names_df["Child's First Name"].str.upper()

# Function to get top 10 names based on gender and ethnicity
def get_top_10_names(gender, ethnicity):
    filtered_data = baby_names_df[(baby_names_df['Gender'] == gender) & (baby_names_df['Ethnicity'] == ethnicity)]
    name_counts = filtered_data.groupby("Child's First Name")['Count'].sum().reset_index()
    top_10_names = name_counts.sort_values(by='Count', ascending=False).head(10)
    return top_10_names

# Streamlit app layout
st.title('Top 10 Baby Names')
st.write('Select gender and ethnicity to see the top 10 baby names.')

# Dropdown menus for gender and ethnicity
gender = st.selectbox('Gender', baby_names_df['Gender'].unique())
ethnicity = st.selectbox('Ethnicity', baby_names_df['Ethnicity'].unique())

# Display top 10 names
if st.button('Show Top 10 Names'):
    top_10_names = get_top_10_names(gender, ethnicity)
    st.write(f'Top 10 Names for {gender} - {ethnicity}')
    st.table(top_10_names)

# To run the app, use the command: streamlit run app.py
