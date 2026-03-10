import streamlit as st
import sqlite3
import pandas as pd

st.title("管理員平台")

conn = sqlite3.connect("repairs.db")

df = pd.read_sql("SELECT * FROM repairs",conn)

st.dataframe(df)

id = st.number_input("輸入ID")

status = st.selectbox("更新狀態",
["待處理","維修中","完成"]
)

if st.button("更新"):

    cursor = conn.cursor()

    cursor.execute(
    "UPDATE repairs SET status=? WHERE id=?",
    (status,id)
    )

    conn.commit()

    st.success("更新成功")