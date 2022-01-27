import streamlit as st
import joblib
import base64
def run():
    def set_bg_hack(main_bg):
        '''
        A function to unpack an image from root folder and set as bg.
        The bg will be static and won't take resolution of device into account.
        Returns
        -------
        The background.
        '''
        # set bg name
        main_bg_ext = "png"
            
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    set_bg_hack('background.png')
run()
model = joblib.load('Sentiment_Analyzer')
st.title('Sentiment Analyzer of movie reviews')
input = st.text_input('Enter your review:')
output = model.predict([input])
if st.button('Predict'):
  st.title(output[0])
