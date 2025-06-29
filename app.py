import streamlit as st
from PIL import Image
import numpy as np
import io

def encode_message(img, message):
    img = img.convert('RGB')
    data = np.array(img)
    flat_data = data.flatten()

    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'

    if len(binary_message) > len(flat_data):
        st.error("Message too long for this image.")
        return None

    for i in range(len(binary_message)):
        flat_data[i] = (flat_data[i] & 0xFE) | int(binary_message[i])

    new_data = flat_data.reshape(data.shape)
    encoded_img = Image.fromarray(new_data.astype('uint8'), 'RGB')
    return encoded_img

def decode_message(img):
    img = img.convert('RGB')
    data = np.array(img).flatten()

    binary_message = ''
    for value in data:
        binary_message += str(value & 1)

    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''
    for c in chars:
        if c == '11111110':  # EOF marker
            break
        message += chr(int(c, 2))
    return message

st.title("🔐 Image Steganography Web App")

mode = st.radio("Choose mode:", ["Encode", "Decode"])

if mode == "Encode":
    uploaded_img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    secret_message = st.text_area("Enter your secret message:")

    if uploaded_img and secret_message:
        img = Image.open(uploaded_img)
        encoded_img = encode_message(img, secret_message)

        if encoded_img:
            st.success("✅ Message encoded successfully!")
            buf = io.BytesIO()
            encoded_img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(label="Download Encoded Image", data=byte_im, file_name="encoded_image.png", mime="image/png")

elif mode == "Decode":
    uploaded_img = st.file_uploader("Upload an encoded image", type=["png", "jpg", "jpeg"])

    if uploaded_img:
        img = Image.open(uploaded_img)
        hidden_message = decode_message(img)
        st.success("🕵️ Hidden message:")
        st.code(hidden_message)
