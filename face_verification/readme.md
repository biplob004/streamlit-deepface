# 🎭 Facial Verification Application

This application allows users to verify if two uploaded images belong to the same person using facial recognition technology. Built with Streamlit and the DeepFace library, it provides a user-friendly interface for image uploads and displays verification results.

## Features

- Upload two images in various formats (JPG, JPEG, PNG, WEBP).
- Select from multiple face verification models.
- Set a custom verification threshold.
- Display verification results including:
  - Verified status (True/False)
  - Distance between embeddings
  - Model used for verification
  - Similarity metric
- View uploaded images alongside the results.

## Technologies Used

- [Streamlit](https://streamlit.io/) - For building the web application.
- [DeepFace](https://github.com/serengil/deepface) - For facial recognition and verification.

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

## Usage

1. Open your web browser and go to `http://localhost:8501`.
2. Upload the first image and the second image.
3. Select a model for verification from the dropdown menu.
4. Adjust the verification threshold if necessary.
5. Click "Submit" to view the verification results.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Developed by [Biplob D.](https://github.com/biplob004)
- Thanks to the [DeepFace](https://github.com/serengil/deepface) library for providing the facial recognition capabilities.

---

This application uses the DeepFace library for facial analysis and verification.
