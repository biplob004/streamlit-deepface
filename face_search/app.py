import streamlit as st
from deepface import DeepFace
import os
from PIL import Image
import tempfile
import pandas as pd

st.title("🎭 Facial Matching Application")

# Directory path to search for matching images
db_path = st.text_input("Enter the directory path to search for matching images:", value="./images")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])



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

threshold = st.slider("Set matching threshold: ", 0.0, 1.0, 0.68)
model_name = st.selectbox("Select a model for verification:", models)

if uploaded_file is not None and db_path:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        img_path = tmp_file.name

    try:
        # Find matching images in the specified directory
        dfs = DeepFace.find(img_path=img_path, 
                            db_path=db_path, 
                            threshold=threshold,
                            model_name=model_name)
        
        if dfs:
            # Concatenate all DataFrames in the list
            df = pd.concat(dfs, ignore_index=True)
            # print(df, '=========================')
            
            if not df.empty:
                st.subheader("🔍 Matching Images Found:")
                st.markdown(f"Total matches found: {len(df)}")

                # Display the matching images in a grid view
                num_columns = 3
                columns = st.columns(num_columns)
                
                for i, row in df.iterrows():
                    image_path = row['identity']
                    image = Image.open(image_path)
                    
                    with columns[i % num_columns]:
                        st.image(image, caption=os.path.basename(image_path), use_column_width=True)

            else:
                st.warning("No matching images found.")
        else:
            st.warning("No matching images found.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("This application uses the DeepFace library to find and display matching images from a specified directory.")
st.markdown("🌐 Developed by [Biplob D.](https://github.com/biplob004)")
