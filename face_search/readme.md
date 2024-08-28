# 🎭 Facial Matching Application

This application uses the [DeepFace](https://github.com/serengil/deepface) library to analyze facial features and find matching images from a specified directory. Users can upload an image and select a model for verification, allowing for a robust facial matching experience.

## Features

- Upload images in various formats (JPG, JPEG, PNG, WEBP).
- Choose from multiple facial recognition models.
- Set a matching threshold for image verification.
- Display matching images in a user-friendly interface.

## Technologies Used

- [Streamlit](https://streamlit.io/) for the web application framework.
- [DeepFace](https://github.com/serengil/deepface) for facial recognition.
- [PIL](https://pillow.readthedocs.io/en/stable/) for image processing.
- [Pandas](https://pandas.pydata.org/) for data manipulation.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/biplob004/streamlit-deepface.git
   cd streamlit-deepface
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to `http://localhost:8501`.

## Usage

1. Enter the directory path where the images are stored.
2. Upload an image you want to match.
3. Select the facial recognition model from the dropdown list.
4. Adjust the matching threshold using the slider.
5. View the matching images displayed on the screen.

## Contribution

Contributions are welcome! If you have suggestions for improvements or want to report issues, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Developed by [Biplob D.](https://github.com/biplob004)
- Special thanks to the developers of the DeepFace library for their excellent work in facial recognition.

---

This application uses the DeepFace library to find and display matching images from a specified directory.
