import streamlit as st
import numpy as np
from PIL import Image

st.title("MNIST 手写数字识别（演示版）")

uploaded_file = st.file_uploader("上传手写数字图片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("L")
    img = img.resize((28,28))
    st.image(img, width=150)

    # 演示预测，随机返回
    pred = np.random.randint(0,10)
    st.success(f"预测结果：{pred}")