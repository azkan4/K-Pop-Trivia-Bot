import streamlit as st
import google.generativeai as genai

# =====================
# KONFIGURASI GEMINI
# =====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# =====================
# HELPER FUNCTION
# =====================
def ask_gemini(prompt: str) -> str:
    """Kirim prompt ke Gemini dan ambil jawaban"""
    response = model.generate_content(prompt)
    return response.text if response else "Maaf, tidak ada jawaban."

def init_session():
    """Inisialisasi state untuk percakapan & skor"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question_count" not in st.session_state:
        st.session_state.question_count = 0

# =====================
# STREAMLIT APP
# =====================
st.set_page_config(page_title="EduKPop Bot 🎶", page_icon="🎤")
init_session()

# =====================
# SIDEBAR (selalu render duluan)
# =====================
with st.sidebar:
    st.title("📊 Skor Kamu")
    st.metric("Skor", st.session_state.score)
    st.metric("Jumlah Pertanyaan", st.session_state.question_count)
    st.caption("💡 Tips: Ketik juga pertanyaan seputar K-Pop untuk belajar lebih banyak!")

# =====================
# MAIN AREA
# =====================
st.title("🎤 EduKPop Bot 🎶")
st.caption("Belajar K-Pop sambil seru-seruan trivia! 💜✨")

# Tampilkan percakapan sebelumnya
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input dari user
if prompt := st.chat_input("Jawab pertanyaan trivia atau tanya tentang K-Pop di sini..."):
    # Simpan input user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prompt ke Gemini → lebih edukatif
    system_prompt = f"""
    Kamu adalah EduKPop Bot, gabungan antara bot trivia dan edukasi.
    Aturan:
    1. Berikan pertanyaan trivia K-Pop singkat (1 per giliran).
    2. Jika user menjawab, cek apakah benar atau salah → tuliskan evaluasi **dengan tag [CORRECT] atau [WRONG]** di awal respon.
    3. Jika benar, beri penjelasan edukatif singkat (misalnya sejarah, arti lagu, atau fun fact).
    4. Jika salah, jelaskan jawaban yang benar + edukasi singkat.
    5. Tambahkan kosakata bahasa Korea sederhana terkait topik kalau bisa.
    6. Respon selalu ceria & penuh emotikon 💜✨🎶
    Pertanyaan ke-{st.session_state.question_count + 1}.
    Skor saat ini: {st.session_state.score}.
    Jawaban/tanya user: {prompt}.
    """

    response = ask_gemini(system_prompt)

    # Update skor otomatis kalau ada jawaban benar
    if response.startswith("[CORRECT]"):
        st.session_state.score += 1

    st.session_state.question_count += 1

    # Simpan jawaban bot
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
