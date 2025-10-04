# 🎵 K-Pop Trivia Bot

Belajar K-Pop sambil seru-seruan trivia dengan EduKPop Bot! 💜✨
Aplikasi ini dibangun menggunakan Streamlit dan Gemini API untuk memberikan pertanyaan trivia, evaluasi jawaban, dan fun facts seputar dunia K-Pop.
---

## 🚀 Fitur
- Pertanyaan trivia K-Pop interaktif 🎶
- Evaluasi jawaban otomatis ([CORRECT] ✅ atau [WRONG] ❌)
- Skor & jumlah pertanyaan ditampilkan di sidebar 📈
- Penjelasan edukatif + fun facts K-Pop 💡
- Kosakata bahasa Korea sederhana ✍️
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

4. **Buat folder .streamlit/ di root project lalu tambahkan file secrets.toml**:
   ```bash
   [general]
   GEMINI_API_KEY = "your_api_key_here"


**Menjalankan Aplikasi**:
```bash
streamlit run kpop_trivia_bot.py
```

🌐 Deploy ke Streamlit Cloud
1. Push project ini ke GitHub.
2. Masuk ke Streamlit Cloud → New App → pilih repo kamu.
3. Tambahkan Secrets melalui menu:
   Buka App → Settings → Secrets
   Tambahkan:
    ```bash
    GEMINI_API_KEY="your_api_key_here"
    ```
4. Klik Deploy → aplikasi siap digunakan! 🎉

