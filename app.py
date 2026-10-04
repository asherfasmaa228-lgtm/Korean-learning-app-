import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="Korean Learning App", page_icon="🇰🇷")

st.title("🇰🇷 Korean Learning App - SRW")
st.write("Learn Korean with sound & quiz!")

# البيانات الجديدة
data = {
    "Basics": [
        ("Hello", "안녕하세요", "Annyeonghaseyo"),
        ("Thank you", "감사합니다", "Kamsahamnida"),
        ("Sorry", "미안합니다", "Mianhamnida"),
    ],
    "Restaurant 🍜": [
        ("Water please", "물 주세요", "Mul juseyo"),
        ("Delicious!", "맛있어요!", "Mashisseoyo!"),
        ("Bill please", "계산서 주세요", "Gyesanseo juseyo"),
    ],
    "Travel ✈️": [
        ("Where is the station?", "역이 어디예요?", "Yeogi eodiyeyo?"),
        ("How much?", "얼마예요?", "Eolmayeyo?"),
        ("Help me", "도와주세요", "Dowajuseyo"),
    ],
    "University 🎓": [
        ("I am a student", "저는 학생이에요", "Jeoneun haksaeng-ieyo"),
        ("Let's study together", "같이 공부해요", "Gachi gongbuhaeyo"),
    ]
}

def speak(text):
    tts = gTTS(text=text, lang='ko')
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    st.audio(buf, format='audio/mp3')

# Tabs
tab1, tab2 = st.tabs(["📚 Learn", "📝 Quiz"])

with tab1:
    cat = st.selectbox("Choose Category:", list(data.keys()))
    for eng, kor, roman in data[cat]:
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(f"**{eng}** - {kor} `({roman})`")
        with col2:
            if st.button("🔊", key=kor):
                speak(kor)

with tab2:
    st.subheader("Quick Quiz!")
    q = st.radio("What does '감사합니다' mean?", ["Hello", "Thank you", "Sorry"])
    if st.button("Submit"):
        if q == "Thank you":
            st.success("Correct! 정답이에요! 🎉")
            st.balloons()
        else:
            st.error("Try again!")
