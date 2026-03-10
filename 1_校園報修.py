import streamlit as st
import sqlite3
import datetime
import os

st.title("校園報修")

location = st.selectbox("報修地點",[
"忠孝樓",
"仁愛樓",
"信義樓",
"和平樓",
"科學館",
"綜合大樓",
"體育館",
"其他"
])

room = st.text_input("教室處室/標的物件")

reporter = st.text_input("申請人")

description = st.text_area("問題描述")

photo = st.file_uploader("上傳故障照片")

if st.button("提交報修"):

    time = datetime.datetime.now().strftime("%Y%m%d%H%M")

    order_id = "R"+time

    photo_path=""

    if photo:

        os.makedirs("uploads",exist_ok=True)

        photo_path=f"uploads/{photo.name}"

        with open(photo_path,"wb") as f:
            f.write(photo.getbuffer())

    conn = sqlite3.connect("repairs.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO repairs
    (order_id,category,location,room,reporter,repair_time,description,photo,status)
    VALUES (?,?,?,?,?,?,?,?,?)
    """,(
    order_id,
    "校園",
    location,
    room,
    reporter,
    time,
    description,
    photo_path,
    "待處理"
    ))

    conn.commit()
    conn.close()

    st.success(f"報修成功！單號:{order_id}")