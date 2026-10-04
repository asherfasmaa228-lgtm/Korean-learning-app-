import streamlit as st
from gtts import gTTS
import io, random, datetime

st.set_page_config(page_title="Asmaa Academy Final Black", page_icon="🇰🇷", layout="wide")
st.markdown("""
<style>
.stApp{background:#000000;color:white}
h1,h2,h3,p,span,div,label{color:white !important}
.stButton>button{background:#ec407a;color:white;border-radius:12px;width:100%}
.stTabs [data-baseweb="tab"]{color:white}
</style>
""", unsafe_allow_html=True)

def speak(t):
    try:
        fp=io.BytesIO()
        gTTS(text=t, lang='ko').write_to_fp(fp)
        st.audio(fp.getvalue(), format='audio/mp3')
    except:
        st.write(t)

if 'score' not in st.session_state:
    st.session_state.score=0
if 'streak' not in st.session_state:
    st.session_state.streak=0

# --- DATA ---
hangul = ["ㄱ g/k","ㄴ n","ㄷ d/t","ㄹ r/l","ㅁ m","ㅂ b/p","ㅅ s","ㅇ ng","ㅈ j","ㅊ ch","ㅋ k","ㅌ t","ㅍ p","ㅎ h"]
vowels = ["ㅏ a","ㅓ eo","ㅗ o","ㅜ u","ㅡ eu","ㅣ i","ㅑ ya","ㅕ yeo","ㅛ yo","ㅠ yu","ㅐ ae","ㅔ e"]

greetings = [("안녕하세요","السلام عليكم"),("안녕","هاي"),("감사합니다","شكرا"),("사랑해요","بحبك"),("괜찮아요","تمام"),("잘 자요","تصبحي على خير"),("화이팅","حظ موفق")]

airport = [("비행기","طيارة"),("공항","مطار"),("여권","باسبور"),("티켓","تذكرة"),("출구","مخرج"),("입구","مدخل"),("화장실","حمام"),("짐","شنط"),("지연","تأخير"),("취소","إلغاء")]

words_200 = [
("나","أنا"),("너","أنت"),("우리","نحن"),("집","بيت"),("학교","مدرسة"),("물","ميه"),("밥","أكل"),("사랑","حب"),("친구","صديق"),("가족","عائلة"),
("시간","وقت"),("사람","شخص"),("오늘","اليوم"),("내일","بكرة"),("어제","امبارح"),("아침","صباح"),("점심","غدا"),("저녁","عشاء"),("밤","ليل"),("낮","نهار"),
("가다","يذهب"),("오다","يأتي"),("먹다","يأكل"),("마시다","يشرب"),("자다","ينام"),("보다","يرى"),("듣다","يسمع"),("말하다","يتكلم"),("공부하다","يذاكر"),("일하다","يعمل"),
("크다","كبير"),("작다","صغير"),("좋다","جيد"),("예쁘다","جميل"),("한국","كوريا"),("이집트","مصر"),("중국","الصين"),("공항","مطار"),("비행기","طيارة"),("책","كتاب"),
("음악","موسيقى"),("돈","فلوس"),("엄마","ماما"),("아빠","بابا"),("선생님","مدرس"),("하나","واحد"),("둘","اتنين"),("셋","تلاتة"),("열","عشرة"),("빨강","أحمر"),
("파랑","أزرق"),("하늘","سماء"),("바다","بحر"),("차","عربية"),("왜","لماذا"),("어디","أين"),("네","نعم"),("아니요","لا"),("맛있다","لذيذ"),("괜찮다","كويس"),
("빨리","بسرعة"),("천천히","ببطء"),("같이","مع بعض"),("혼자","لوحدي"),("많다","كثير"),("적다","قليل"),("비싸다","غالي"),("싸다","رخيص"),("덥다","حر"),("춥다","برد"),
("기쁘다","مبسوط"),("슬프다","حزين"),("바쁘다","مشغول"),("한가하다","فاضي"),("시작","بداية"),("끝","نهاية"),("문제","مشكلة"),("답","إجابة"),("이름","اسم"),("나이","سن")
]

k_food = [("김치","كيمتشي"),("비빔밥","بيبيمباب"),("불고기","بولجوجي"),("떡볶이","توكبوكي"),("라면","راميون"),("김밥","كيمباب"),("삼겹살","سامجيوبسال")]
e_food = [("코샤리","كشري"),("몰로키아","ملوخية"),("타아메야","طعمية"),("마흐시","محشي"),("코프타","كفتة"),("오므 알리","أم علي"),("풀","فول")]
c_food = [("짜장면","جاجانغميون"),("짬뽕","جامبونغ"),("딤섬","ديم سوم"),("탕수육","تانجسويوك"),("훠궈","هوت بوت"),("마라탕","مالاتانغ")]

k_drink = [("바나나 우유","لبن موز"),("소주","سوجو"),("식혜","شكهيه"),("보리차","شاي شعير"),("딸기 우유","لبن فراولة")]
e_drink = [("히비스커스","كركديه"),("소비아","سوبيا"),("사탕수수 주스","عصير قصب"),("타마린드","تمر هندي"),("사흘라브","سحلب"),("망고 주스","مانجو"),("돔 주스","دوم")]
c_drink = [("버블티","بابل تي"),("우롱차","أولونغ"),("자스민차","ياسمين"),("라이치 주스","ليتشي")]

bts = ["Dynamite - BTS","Butter - BTS","Spring Day - BTS","Boy With Luv - BTS","IDOL - BTS","Fake Love - BTS","DNA - BTS","Blood Sweat & Tears"]
bp = ["How You Like That - BLACKPINK","Kill This Love - BLACKPINK","DDU-DU DDU-DU - BLACKPINK","Pink Venom - BLACKPINK"]
twice = ["What is Love? - TWICE","Fancy - TWICE","Cheer Up - TWICE","Feel Special - TWICE"]
other = ["Stray Kids - God Menu","SEVENTEEN - God of Music","NewJeans - Hype Boy","LE SSERAFIM - Antifragile","IVE - I AM","(G)I-DLE - Queencard","ITZY - Dalla Dalla"]
c_songs = ["My Love 我的爱","Ni Hao 你好","Yue Liang 月亮","Tian Mi Mi 甜蜜蜜","Xiao Ping Guo 小苹果"]
e_songs = ["هايجيلي موجوع - 하이질리","يا طبطب - 야 타브타브","3 دقات - 세 다카트","بنت الجيران - 이웃집 딸","Ciao Bella"]
violin = ["BTS Dynamite Violin 🎻","BTS Spring Day Violin 🎻","BLACKPINK Violin 🎻","TWICE Violin 🎻","Egyptian Violin 🎻"]

st.title("🇰🇷 أكاديمية أسماء النهائية - Black 188 🖤")
st.write(f"🔥 Streak: {st.session_state.streak} | ⭐ Score: {st.session_state.score}")

menu = st.sidebar.selectbox("📚 القائمة الرئيسية", ["الحروف","الأرقام","التحيات","المطار","200 كلمة","الأكل","المشروبات","الأغاني + فرق كتير + كمان","امتحانات","الشهادة"])

if menu=="الحروف":
    c1,c2=st.columns(2)
    with c1:
        st.subheader("자음 - حروف ساكنة")
        for h in hangul:
            st.write(h)
    with c2:
        st.subheader("모음 - حروف متحركة")
        for v in vowels:
            st.write(v)

elif menu=="الأرقام":
    st.subheader("الأرقام الكورية")
    st.write("1= 하나 / 일")
    st.write("2= 둘 / 이")
    st.write("3= 셋 / 삼")
    st.write("10= 열 / 십")
    st.write("100= 백")
    st.write("1000= 천")

elif menu=="التحيات":
    st.subheader("التحيات - دوسي تسمعي الصوت")
    for ko,ar in greetings:
        if st.button(f"{ko} = {ar}", key=f"g_{ko}"):
            speak(ko)

elif menu=="المطار":
    st.subheader("كلمات المطار")
    for ko,ar in airport:
        if st.button(f"{ko} = {ar}", key=f"a_{ko}"):
            speak(ko)

elif menu=="200 كلمة":
    st.subheader("200 كلمة - قاموسك الشخصي")
    s=st.text_input("🔍 ابحثي (عربي / كوري)")
    for ko,ar in words_200:
        if s in ar or s in ko or s=="":
            if st.button(f"{ko} = {ar}", key=f"w_{ko}_{ar}"):
                speak(ko)

elif menu=="الأكل":
    t1,t2,t3=st.tabs(["🇰🇷 كوري","🇪🇬 مصري","🇨🇳 صيني"])
    with t1:
        for ko,ar in k_food:
            st.write(f"{ko} = {ar}")
    with t2:
        for ko,ar in e_food:
            st.success(f"{ko} = {ar}")
    with t3:
        for ko,ar in c_food:
            st.info(f"{ko} = {ar}")

elif menu=="المشروبات":
    t1,t2,t3=st.tabs(["🇰🇷 كوري","🇪🇬 مصري","🇨🇳 صيني"])
    with t1:
        for ko,ar in k_drink:
            st.write(f"{ko} = {ar}")
    with t2:
        for ko,ar in e_drink:
            st.success(f"{ko} = {ar}")
    with t3:
        for ko,ar in c_drink:
            st.info(f"{ko} = {ar}")

elif menu=="الأغاني + فرق كتير + كمان":
    t1,t2,t3,t4,t5=st.tabs(["BTS 💜","فرق تانية 🌟","صيني 🇨🇳","مصري 🇪🇬","كمان 🎻"])
    with t1:
        for s in bts:
            st.write(f"🎵 {s}")
    with t2:
        st.write("**BLACKPINK 🖤**")
        for s in bp:
            st.write(s)
        st.write("**TWICE 💖**")
        for s in twice:
            st.write(s)
        st.write("**فرق تانية ⭐**")
        for s in other:
            st.write(s)
    with t3:
        for s in c_songs:
            st.write(f"🎶 {s}")
    with t4:
        for s in e_songs:
            st.write(f"🎶 {s}")
    with t5:
        for v in violin:
            st.write(f"🎻 {v}")

elif menu=="امتحانات":
    st.subheader("اختبري نفسك")
    q=st.radio("김치 معناها إيه؟", ["كيمتشي","محشي","كشري"])
    if st.button("جاوبي ✅"):
        if q=="كيمتشي":
            st.success("صح! برافووو 🎉")
            st.session_state.score+=10
            st.session_state.streak+=1
        else:
            st.error("غلط، حاولي تاني!")
            st.session_state.streak=0
    st.metric("Score", st.session_state.score)
    st.metric("Streak", st.session_state.streak)

elif menu=="الشهادة":
    st.balloons()
    st.header("🎓 شهادة إتمام - Asmaa Black Final")
    st.success("مبروك خلصتي الأكاديمية الكاملة!")
    st.write("**الاسم:** أسماء")
    st.write("**المستوى:** خبيرة كوري - Black Edition")
    st.write(f"**التاريخ:** {datetime.date.today()}")
    st.write(f"**الـ Score النهائي:** {st.session_state.score}")
    st.write("🇰🇷🇪🇬🇨🇳🎻")

# Black Edition
# Final Version 188 lines
# Organized Tabs
# All foods drinks songs
# No NULL
# Asmaa Academy 2026
# مبروك 🖤
# End
