import streamlit as st
from gtts import gTTS
import tempfile
from google import genai
from google.genai import types

# Konfigurasi Gemini
client = genai.Client(api_key="AIzaSyALCocxowNCmrH9FCrnWekjAE0_TLCqeT0")

system_instruction='Kamu adalah seorang pendongeng terbaik di dunia, kamu bisa memberi cerita dongeng dengan tema apapun dan suasana apapun, entah sedih, lucu, atau lainnya. Bicaralah seperti layaknya seorang Pendongeng sejati. Tidak perlu menjelaskan ulang tentang siapa kamu, cukup langsung berikan dongengnya saja'

chat_config = types.GenerateContentConfig(
    system_instruction=system_instruction)

st.title("📚 AI Storyteller dengan Suara")

prompt = st.text_input("Mau didongengin tentang apa, nak?", "Kasih aku dongeng pengantar tidur, bu")

if st.button("Buat Cerita"):
    # 1. Dapatkan story dari Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=chat_config,
        contents=prompt
    )
    story = response.text

    st.subheader("📖 Cerita")
    st.write(story)

    # 2. Convert ke suara pakai gTTS
    tts = gTTS(story, lang="id")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts.save(tmp_file.name)
        audio_path = tmp_file.name

    # 3. Tampilkan audio di Streamlit
    st.subheader("🔊 Cerita Versi Audio")
    st.audio(audio_path, format="audio/mp3")
