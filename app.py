import streamlit as st
import numpy as np

st.title("MNIST 手写数字识别（演示版）")

uploaded_file = st.file_uploader("上传手写数字图片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, width=150, caption="你上传的图片")
    # 演示随机预测
    pred = np.random.randint(0,10)
    st.success(f"预测结果：{pred}")