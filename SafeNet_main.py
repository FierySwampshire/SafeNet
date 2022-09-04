import streamlit as st
import tensorflow as tf
from tensorflow import keras
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import numpy as np
import requests
import cv2

st.set_page_config(layout="wide")

@tf.function
def preprocess_img(img_path, preprocess_fun, img=None):
    if img_path:
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(64, 64))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        img_array = preprocess_fun(img_array)
        img_array = img_array / 255
    elif img:
        img_array = img
        img_array = tf.image.resize(img_array, (64, 64))
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        img_array = preprocess_fun(img_array)
        img_array = img_array / 255
    return img_array

@st.cache(allow_output_mutation=True, show_spinner=True)
def load_model():
    MODEL = tf.keras.models.load_model('optimized_model.tflite')
    preprocess_function = tf.keras.applications.densenet.preprocess_input
    return MODEL, preprocess_function

# chain tf.function and st.cache together

# Second preprocess function
def preprocess_img_two(preprocess_fun, img):
    img_array = img
    img_array = tf.image.resize(img_array, (64, 64))
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    img_array = preprocess_fun(img_array)
    img_array = img_array / 255
    return img_array


Model, preprocess_function = load_model()


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def predict(img):
    return Model.predict(img)


st.image("logo.png", use_column_width=True)

def display_prediction(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = preprocess_img(preprocess_fun=preprocess_function, img=img)
    prediction = predict(img)
    # write prediction on image:
    cv2.putText(img, f"Prediction: {prediction}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    if prediction["Normal"]<prediction.all():
        type = prediction.get("type")
        probablity = prediction.get("probablity")
        requests.post("https://safenet.hop.sh/send")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

col1, col2, col3, col4 = st.columns(4)

with col1:
    ctx = webrtc_streamer(key="sample", video_frame_callback=display_prediction)
with col2:
    ctx_2 = webrtc_streamer(key="sample2", video_frame_callback=display_prediction)
with col3:
    ctx_3 = webrtc_streamer(key="sample3", video_frame_callback=display_prediction)
with col4:
    ctx_4 = webrtc_streamer(key="sample4", video_frame_callback=display_prediction)

col5, col6, col7, col8 = st.columns(4)

with col5:
    ctx_5 = webrtc_streamer(key="sample5", video_frame_callback=display_prediction)
with col6:
    ctx_6 = webrtc_streamer(key="sample6", video_frame_callback=display_prediction)
with col7:
    ctx_7 = webrtc_streamer(key="sample7", video_frame_callback=display_prediction)
with col8:
    ctx_8 = webrtc_streamer(key="sample8", video_frame_callback=display_prediction)

# Add to sidebar:
if st.button("Trigger Warning"):
    requests.post("https://safenet.hop.sh/send")

