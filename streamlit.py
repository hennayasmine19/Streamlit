import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Visualization")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Basic Statistics")
    st.write(df.describe())
    
    st.subheader("Missing Values")
    st.write(df.isnull().sum())
    
    # Column selection for visualization
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_columns:
        st.subheader("Visualizations")
        column = st.selectbox("Select a numeric column for visualization", numeric_columns)
        
        # Histogram
        st.subheader("Histogram")
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Boxplot
        st.subheader("Boxplot")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[column], ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found in the dataset for visualization.")
