# Facial Analysis Application

🎭 **Facial Analysis Application** is a web app built using Streamlit and the DeepFace library. This application allows users to upload an image and receive an analysis of various facial attributes, including age, gender, race, and emotion.

## Features

- **Image Upload**: Users can upload images in various formats (JPG, JPEG, PNG, WEBP).
- **Facial Analysis**: The application analyzes the uploaded image and provides insights on:
  - Age
  - Gender
  - Race
  - Emotion
- **User-Friendly Interface**: A simple and intuitive interface powered by Streamlit.

## Technologies Used

- **Streamlit**: For creating the web application.
- **DeepFace**: For performing facial analysis.
- **Python**: The primary programming language.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/biplob004/streamlit-deepface.git
   cd streamlit-deepface
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.

## Usage

1. Click on the "Choose an image..." button to upload an image file.
2. Once the image is uploaded, the application will display the analysis results, including age, gender, race, and emotion.
3. The uploaded image will be shown along with the analysis results.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Acknowledgments

- DeepFace library for facial recognition and analysis.
- Streamlit for building the web application interface.

## Author

🌐 Developed by [Biplob D.](https://github.com/biplob004)
