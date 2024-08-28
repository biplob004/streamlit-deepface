import streamlit as st
from deepface import DeepFace
import json
import os

st.title("🎭 Facial Verification Application")

uploaded_file1 = st.file_uploader("Choose the first image...", type=["jpg", "jpeg", "png", "webp"], key="1")
uploaded_file2 = st.file_uploader("Choose the second image...", type=["jpg", "jpeg", "png", "webp"], key="2")

# List of models for face verification
models = [
    "VGG-Face", 
    "Facenet", 
    "Facenet512", 
    "OpenFace", 
    "DeepFace", 
    "DeepID", 
    "ArcFace", 
    "Dlib", 
    "SFace",
    "GhostFaceNet",
]

threshold = st.slider("Set verification threshold:", 0.0, 1.0, 0.68)


img_path1 = "img1.jpg"
img_path2 = "img2.jpg"


if uploaded_file1 is not None and uploaded_file2 is not None:
    # Save the uploaded files to a temporary location


    with open(img_path1, "wb") as f:
        f.write(uploaded_file1.getbuffer())
    
    with open(img_path2, "wb") as f:
        f.write(uploaded_file2.getbuffer())
    
    # Model selection dropdown
    model_name = st.selectbox("Select a model for verification:", models)

    # Face verification
    try:
        result = DeepFace.verify(
            img1_path=img_path1,
            img2_path=img_path2,
            model_name=model_name,
            threshold=threshold
        )

        # Display the results
        st.subheader("🔍 Verification Results:")
        st.markdown(f"<strong>Verified:</strong> {result['verified']}", unsafe_allow_html=True)
        st.markdown(f"<strong>Distance:</strong> {result['distance']}", unsafe_allow_html=True)
        st.markdown(f"<strong>Threshold:</strong> {result['threshold']}", unsafe_allow_html=True)
        st.markdown(f"<strong>Model:</strong> {result['model']}", unsafe_allow_html=True)
        st.markdown(f"<strong>Similarity Metric:</strong> {result['similarity_metric']}", unsafe_allow_html=True)

        # Optionally, display the uploaded images
        st.image(uploaded_file1, caption='Uploaded Image 1', use_column_width=True)
        st.image(uploaded_file2, caption='Uploaded Image 2', use_column_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Add some footer information
st.markdown("---")
st.markdown("This application uses the DeepFace library for facial analysis and verification.")
st.markdown("🌐 Developed by [Biplob D.](https://github.com/biplob004)")

# Clean up temporary files
if os.path.exists(img_path1):
    os.remove(img_path1)
if os.path.exists(img_path2):
    os.remove(img_path2)
