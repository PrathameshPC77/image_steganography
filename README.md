# 🔐 Image Steganography Web App

A simple and interactive **Streamlit web application** for hiding and revealing secret messages inside image files using **LSB (Least Significant Bit) steganography**.

Built using **Python, Streamlit, Pillow, and NumPy**.

---

## ✨ Features

- 🖼️ Upload an image and hide a secret message inside it
- 💬 Extract hidden messages from encoded images
- 🎯 Uses LSB manipulation to embed binary data without visibly altering the image
- 🧠 Clean and intuitive UI built with Streamlit

---

## 📸 Sample Output

### 🔧 Encoding Mode
![Encode Screenshot](https://github.com/PrathameshPC77/image_steganography/blob/main/output/output-1.png)

### 🕵️ Decoding Mode
![Decode Screenshot](https://github.com/PrathameshPC77/image_steganography/blob/main/output/output-2.png)

---

## 🚀 Getting Started

### 📦 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PrathameshPC77/image_steganography.git
    cd image_steganography

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt

3. Run the Streamlit app:

    ```bash
    streamlit run app.py

## 🛠️ Tech Stack
- Streamlit

- Python

- Pillow (PIL)

- NumPy

## 📂 Project Structure

    image_steganography/
    ├── app.py                 # Main Streamlit app
    ├── requirements.txt       # Dependencies
    ├── sample.jpg             # Optional test image
    ├── output/           # App screenshots
    │   ├── output-1.png
    │   └── output-2.png
    ├── .gitignore
    ├── files/
    │   ├── steganography.ipynb
    │   └── steganography.py
    └── README.md

## 📥 Encode Example
1. Upload any .jpg or .png image

2. Type your secret message

3. Download the encoded image

## 🔎 Decode Example
1. Upload the encoded image

2. The hidden message will be extracted and displayed

## 📜 License
This project is open-source under the MIT License.
