import streamlit as st
import pandas as pd
from io import BytesIO

st.header("CSV Cleaner 🧹")

st.write("Upload apni CSV file, main usse clean kar dunga!")

file = st.file_uploader("Choose CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    
    st.write("**Original Data:**")
    st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    st.dataframe(df.head())
    
    st.write("---")
    st.write("**Cleaning...**")
    
    # Remove duplicates
    df_cleaned = df.drop_duplicates()
    st.write(f"✓ Removed duplicates: {len(df) - len(df_cleaned)} rows deleted")
    
    # Remove empty rows
    df_cleaned = df_cleaned.dropna()
    st.write(f"✓ Removed empty cells")
    
    st.write("---")
    st.write("**Cleaned Data:**")
    st.write(f"Rows: {len(df_cleaned)}, Columns: {len(df_cleaned.columns)}")
    st.dataframe(df_cleaned.head())
    
    # Download button
    buf = BytesIO()
    df_cleaned.to_csv(buf, index=False)
    buf.seek(0)
    
    st.download_button(
        label="📥 Download Cleaned CSV",
        data=buf.getvalue(),
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
else:
    st.info("👆 Upar CSV upload karo start karne ke liye")
