import streamlit as st
import sqlite3
import datetime

st.title("學生宿舍報修")

location = st.selectbox("宿舍棟別",[
"第一棟",
"第二棟",
"第三棟",
"餐廳",
"娛樂室",
"其他"
])

room = st.text_input("寢室編號")

reporter = st.text_input("通報人")

description = st.text_area("問題描述")

if st.button("提交報修"):

    time = datetime.datetime.now().strftime("%Y%m%d%H%M")

    order_id = "D"+time

    conn = sqlite3.connect("repairs.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO repairs
    (order_id,category,location,room,reporter,repair_time,description,status)
    VALUES (?,?,?,?,?,?,?,?)
    """,(
    order_id,
    "宿舍",
    location,
    room,
    reporter,
    time,
    description,
    "待處理"
    ))

    conn.commit()
    conn.close()

    st.success("報修成功")