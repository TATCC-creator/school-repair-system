import streamlit as st
import sqlite3
import pandas as pd

st.title("廠商維修平台")

conn = sqlite3.connect("repairs.db")

df = pd.read_sql("SELECT * FROM repairs",conn)

st.dataframe(df)

id = st.number_input("輸入維修單ID")

if st.button("確認收件"):

    cursor = conn.cursor()

    cursor.execute(
    "UPDATE repairs SET status='維修中' WHERE id=?",
    (id,)
    )

    conn.commit()

    st.success("已接單")