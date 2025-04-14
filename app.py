import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image as keras_image

# Load the model
model = tf.keras.models.load_model("model/fake_logo_detector.h5")

# Prediction function
def predict(img):
    img = img.resize((150, 150))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    prediction = model.predict(img_array)
    return prediction[0][0]

# Custom CSS for responsiveness
st.markdown("""
    <style>
    body {
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
    }

    .header, .main, .footer {
        width: 100%;
        margin: auto;
        text-align: center;
        padding: 2rem;
    }

    .header {
        background-color: #0d6efd;
        color: white;
    }

    .main {
        background-color: #ffffff;
        color: #212529;
        max-width: 900px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-radius: 12px;
    }

    .footer {
        background-color: #343a40;
        color: #ced4da;
        border-top: 3px solid #495057;
        font-size: 0.9rem;
    }

    .footer a {
        color: #f8f9fa;
        text-decoration: none;
    }

    .footer a:hover {
        text-decoration: underline;
    }

    .info-box {
        text-align: left;
        margin-top: 1rem;
    }

    @media (max-width: 768px) {
        .main, .header, .footer {
            padding: 1rem;
        }
        .header h1 {
            font-size: 1.8rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header">
        <img src="https://img.icons8.com/color/96/artificial-intelligence.png" width="70"/>
        <h1>Fake Logo Detector</h1>
        <p>AI-powered tool to verify the authenticity of brand logos</p>
    </div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.markdown('<div class="main">', unsafe_allow_html=True)

st.subheader("📤 Upload Logo Image")
uploaded_file = st.file_uploader("Choose a logo image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="🖼️ Uploaded Logo", use_column_width=True)

    with st.spinner("🔍 Analyzing the logo..."):
        result = predict(img)

    if result > 0.5:
        st.image("https://img.icons8.com/color/96/high-risk.png", width=60)
        st.error(f"🚨 This appears to be a FAKE logo\nConfidence: {result*100:.2f}%")
    else:
        st.image("https://img.icons8.com/color/96/checked--v1.png", width=60)
        st.success(f"✅ This appears to be a GENUINE logo\nConfidence: {(1 - result)*100:.2f}%")

st.markdown('</div>', unsafe_allow_html=True)

# --- EXTRA SECTIONS ---
with st.expander("📘 About Us"):
    st.markdown("""
    This project is designed to detect fake brand logos using deep learning. 
    It helps consumers and businesses validate logo authenticity through an easy-to-use web interface.

    **Developed by:** Soni Jaisraj Prajapati  
    **College:** BNN College, Bhiwandi  
    **Guided by:** Prof. Prachi Thakur
    """)

with st.expander("❓ Help"):
    st.markdown("""
    1. Click on 'Choose a logo image...'
    2. Upload a JPG or PNG file of the logo
    3. The app will classify it as **Real** or **Fake**

    For technical issues, contact: [support@fakelogodetector.com](mailto:support@fakelogodetector.com)
    """)

with st.expander("📄 Terms and Conditions"):
    st.markdown("""
    - This tool is for educational and demonstration purposes.
    - Results are based on trained data and may vary with untrained logos.
    - No legal responsibility is assumed for classification output.
    """)

with st.expander("📬 Contact Us"):
    st.markdown("""
    **Email:** [soniprajapati180104@gmail.com](mailto:soniprajapati180104@gmail.com)  
    **Phone:** +91-9762265005  
    """)

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        © 2025 Fake Logo Detector • BNN College Bhiwandi<br>
        Guided by Prof. Prachi Thakur | Created by Soni Jaisraj Prajapati
    </div>
""", unsafe_allow_html=True)
