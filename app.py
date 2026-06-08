import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# 加载已经训练好的模型
model = load_model("mnist_cnn.keras")

st.title("MNIST 手写数字识别")

uploaded_file = st.file_uploader("上传手写数字图片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # 打开图片并转换为灰度
    img = Image.open(uploaded_file).convert("L")
    img = img.resize((28,28))
    st.image(img, caption="你上传的图片", width=150)
    
    # 转为模型输入
    arr = np.array(img)/255.0
    arr = arr.reshape(1,28,28,1)
    
    # 预测
    pred = model.predict(arr)
    digit = np.argmax(pred)
    
    st.success(f"预测结果：{digit}")