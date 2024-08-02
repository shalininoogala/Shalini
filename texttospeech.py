import streamlit as st
from gtts import gTTS
from io import BytesIO # To handle Audio data 
def generate_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content'].strip()
 
# Function to convert text to speech and display audio in Streamlit
def text_to_speech_and_display(text):
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)    #Reset the stream position for beginning                        
   
    # Display the audio file in Streamlit
    st.audio(audio_fp, format="audio/mp3")
 
# Streamlit App
st.title("Text to Speech App")
st.write("Hi, how can I help you today?")
 
# User input
user_input = st.text_input("Type your text here:")
 
if st.button("Submit"):
    if user_input:
        st.write("Processing your input...")
        try:
            # Debug print
            st.write("User input received:", user_input)
 
            # Convert user input to speech and display audio
            text_to_speech_and_display(user_input)
           
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please enter some text")
