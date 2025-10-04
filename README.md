# 🎵 K-Pop Trivia Bot

K-Pop Trivia Bot adalah chatbot interaktif berbasis **Streamlit** dan **Google Gemini API**.  
Bot ini dibuat untuk memberikan kuis seru seputar dunia K-Pop dan menampilkan skor secara real-time.  
Cocok untuk penggemar K-Pop yang ingin menguji pengetahuan mereka dengan cara yang fun!

---

## 🚀 Fitur
- Kuis trivia tentang K-Pop (acak setiap pertanyaan)
- Skor ditampilkan di sidebar
- Respon AI yang interaktif menggunakan **Gemini API**
- Dibangun dengan **Streamlit** → simple UI berbasis web

---

## 🛠️ Teknologi
- [Python 3](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Google Generative AI (Gemini API)](https://ai.google.dev/)  

---

## 📦 Instalasi

1. **Clone repo ini**:
   ```bash
   git clone https://github.com/username/kpop-trivia-bot.git
   cd kpop-trivia-bot

2. **Buat Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Tambahkan API Key Gemini di file .streamlit/secrets.toml:**:
   ```bash
   GEMINI_API_KEY = "masukkan_api_key_kamu"

**Menjalankan Aplikasi**:
```bash
streamlit run kpop_trivia_bot.py

