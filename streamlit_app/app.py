import time
from dataclasses import dataclass

import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas

from helper import preprocess, load_model
from predict import predict

@dataclass
class CanvasSetup:
    stroke_width: int = 50
    stroke_color: str = "#000000"
    background_color: str = "#eee"
    update_streamlit: bool = True
    height: int = 500
    width: int = 500
    drawing_mode: str = "freedraw"
    key: str = "canvas"

class NumberPredictorApp:
    def __init__(self):
        if "model" not in st.session_state:
            st.session_state.model = load_model()
   
    def predict_button_action(self):
        preprocessed_drawing = preprocess(self.predict_input)
        prediction, prediction_proba = predict(preprocessed_drawing,st.session_state.model)
        return prediction, prediction_proba
   
    def windows(self,canvas_setup: CanvasSetup):

        st.title("Number Predictor")
      
        canvas_result = st_canvas(
            stroke_width=canvas_setup.stroke_width,
            stroke_color=canvas_setup.stroke_color,
            background_color=canvas_setup.background_color,
            update_streamlit=canvas_setup.update_streamlit,
            height=canvas_setup.height,
            width=canvas_setup.width,
            drawing_mode=canvas_setup.drawing_mode,
            key=canvas_setup.key,
        )
        self.predict_input = canvas_result.image_data
        
        predict_button_clicked = st.button("Predict")

        if predict_button_clicked:
             with st.spinner("Predicting..."):
                prediction, prediction_proba = self.predict_button_action()
                time.sleep(1)
                
                st.header(f"prediction = {prediction}")

                data_series = pd.Series(prediction_proba, name='Probability')
                df = pd.DataFrame(data_series)

                st.bar_chart(df)

def main():
    app = NumberPredictorApp()
    app.windows(CanvasSetup())

if __name__ == "__main__":
    app = NumberPredictorApp()
    app.windows(CanvasSetup())