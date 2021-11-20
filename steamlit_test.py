import streamlit as st

st.title('finance_demo')
file = st.file_uploader('请上传金融文件', type=['pdf'])
button = st.button("开始处理", key='True')
