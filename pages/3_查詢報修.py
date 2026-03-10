import streamlit as st
import sqlite3
import pandas as pd

st.title("報修查詢")

name = st.text_input("輸入申請人")

if st.button("查詢"):

    conn = sqlite3.connect("repairs.db")

    df = pd.read_sql(
    f"SELECT * FROM repairs WHERE reporter='{name}'",
    conn
    )

    st.dataframe(df)