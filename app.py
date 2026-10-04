import streamlit as st
from gtts import gTTS
import io, random, datetime

st.set_page_config(page_title="Asmaa Super Academy V8 FINAL", page_icon="🇰🇷", layout="wide")st.markdown("<style>.stApp{background:linear-gradient(135deg,#fce4ec,#e8f5e9,#e1bee7)} .stButton>button{background:#ec407a;color:white;border-radius:12px}</style>", unsafe_allow_html=True)
st.markdown("<style>.stApp{background:#000000;color:white} .stButton>button{background:#ec407a;color:white;border-radius:12px} h1,h2,h3,p,span{color:white !important}</style>", unsafe_allow_html=True)
def speak(t):
    try:
        fp=io.BytesIO(); gTTS(text=t, lang='ko').write_to_fp(fp); st.audio(fp.getvalue(), format='audio/mp3')
    except: st.write(t)

if 'streak' not in st.session_state: st.session_state.streak=0
if 'score' not in st.session_state: st.session_state.score=0

# 200 كلمة
common_200 = [("나","أنا"),("너","أنت"),("우리","نحن"),("집","بيت"),("학교","مدرسة"),("물","ميه"),("밥","أكل"),("사랑","حب"),("친구","صديق"),("가족","عائلة"),("시간","وقت"),("사람","شخص"),("오늘","اليوم"),("내일","بكرة"),("어제","امبارح"),("아침","صباح"),("점심","غدا"),("저녁","عشاء"),("밤","ليل"),("낮","نهار"),("가다","يذهب"),("오다","يأتي"),("먹다","يأكل"),("마시다","يشرب"),("자다","ينام"),("보다","يرى"),("듣다","يسمع"),("말하다","يتكلم"),("공부하다","يذاكر"),("일하다","يعمل"),("크다","كبير"),("작다","صغير"),("좋다","جيد"),("예쁘다","جميل"),("한국","كوريا"),("이집트","مصر"),("중국","الصين"),("공항","مطار"),("비행기","طيارة"),("책","كتاب"),("음악","موسيقى"),("돈","فلوس"),("엄마","ماما"),("아빠","بابا"),("선생님","مدرس"),("하나","1"),("둘","2"),("열","10"),("빨강","أحمر"),("파랑","أزرق"),("하늘","سماء"),("바다","بحر"),("차","عربية"),("왜","لماذا"),("어디","أين"),("네","نعم"),("감사합니다","شكرا")]

hangul_full = ["ㄱ= g/k","ㄴ= n","ㄷ= d/t","ㄹ= r/l","ㅁ= m","ㅂ= b/p","ㅅ= s","ㅇ= ng","ㅈ= j","ㅊ= ch","ㅋ= k","ㅌ= t","ㅍ= p","ㅎ= h"]
greetings_full = [("안녕하세요","السلام عليكم"),("안녕","هاي"),("감사합니다","شكرا"),("사랑해요","بحبك"),("괜찮아요","تمام"),("잘 자요","تصبح على خير"),("축하해요","مبروك")]
airport_full = [("비행기","طيارة"),("공항","مطار"),("여권","باسبور"),("티켓","تذكرة"),("출구","مخرج"),("화장실","حمام"),("짐","شنط")]

korean_food_full = [("김치","كيمتشي"),("비빔밥","بيبيمباب"),("불고기","بولجوجي"),("떡볶이","توكبوكي"),("라면","راميون"),("김밥","كيمباب"),("잡채","جابتشي")]
egyptian_food_kr = [("코샤리","كشري"),("몰로키아","ملوخية"),("타아메야","طعمية"),("마흐시","محشي"),("코프타","كفتة"),("오므 알리","أم علي")]
chinese_food_kr = [("짜장면","جاجانغميون"),("짬뽕","جامبونغ"),("딤섬","ديم سوم"),("탕수육","تانجسويوك"),("훠궈","هوت بوت")]

korean_drinks_full = [("바나나 우유","لبن موز"),("소주","سوجو"),("식혜","شكهيه"),("보리차","شاي شعير")]
egyptian_drinks_full = [("히비스커스","كركديه"),("소비아","سوبيا"),("사탕수수 주스","عصير قصب"),("타마린드","تمر هندي"),("사흘라브","سحلب"),("망고 주스","مانجو")]
chinese_drinks_full = [("버블티","بابل تي"),("우롱차","أولونغ"),("자스민차","ياسمين")]

bts_songs = ["Dynamite","Butter","Spring Day","Boy With Luv","IDOL","Fake Love","DNA"]
bp_songs = ["How You Like That BLACKPINK","Kill This Love","DDU-DU DDU-DU"]
twice_songs = ["What is Love? TWICE","Fancy","Cheer Up"]
other_groups = ["Stray Kids - God Menu","SEVENTEEN - God of Music","NewJeans - Hype Boy","LE SSERAFIM","IVE - I AM"]
chinese_songs_full = ["My Love 我的爱","Ni Hao 你好","Yue Liang 月亮","Tian Mi Mi 甜蜜蜜"]
egyptian_songs_kr = ["هايجيلي موجوع - 하이질리","يا طبطب - 야 타브타브","3 دقات - 세 다카트","بنت الجيران"]
violin_list = ["BTS Dynamite Violin 🎻","BTS Spring Day Violin 🎻","BLACKPINK Violin 🎻"]

st.title("🇰🇷 أكاديمية أسماء V8 النهائي الكامل")
menu = st.sidebar.selectbox("📚 القائمة", ["الحروف","الأرقام","التحيات","المطار","200 كلمة","الأكل","المشروبات","الأغاني + فرق كتير + كمان","امتحانات","الشهادة"])

if menu=="الحروف":
    for h in hangul_full: st.write(h)
elif menu=="الأرقام":
    st.write("1= 하나 / 일, 2= 둘 / 이, 10= 열 / 십, 100= 백")
elif menu=="التحيات":
    for ko,ar in greetings_full:
        if st.button(f"{ko} = {ar}", key=ko): speak(ko)
elif menu=="المطار":
    for ko,ar in airport_full:
        if st.button(f"{ko} = {ar}", key=ko): speak(ko)
elif menu=="200 كلمة":
    s=st.text_input("ابحثي")
    for ko,ar in common_200:
        if s in ar or s=="":
            if st.button(f"{ko} = {ar}", key=ko+ar): speak(ko)
elif menu=="الأكل":
    t1,t2,t3=st.tabs(["كوري","مصري","صيني"])
    with t1:
        for ko,ar in korean_food_full: st.write(f"{ko}={ar}")
    with t2:
        for ko,ar in egyptian_food_kr: st.success(f"{ko}={ar}")
    with t3:
        for ko,ar in chinese_food_kr: st.info(f"{ko}={ar}")
elif menu=="المشروبات":
    t1,t2,t3=st.tabs(["كوري","مصري","صيني"])
    with t1:
        for ko,ar in korean_drinks_full: st.write(f"{ko}={ar}")
    with t2:
        for ko,ar in egyptian_drinks_full: st.success(f"{ko}={ar}")
    with t3:
        for ko,ar in chinese_drinks_full: st.info(f"{ko}={ar}")
elif menu=="الأغاني + فرق كتير + كمان":
    t1,t2,t3,t4,t5=st.tabs(["BTS","فرق تانية","صيني","مصري","كمان"])
    with t1:
        for s in bts_songs: st.write(f"🎵 {s}")
    with t2:
        for s in bp_songs: st.write(f"🖤 {s}")
        for s in twice_songs: st.write(f"💖 {s}")
        for s in other_groups: st.write(f"⭐ {s}")
    with t3:
        for s in chinese_songs_full: st.write(s)
    with t4:
        for s in egyptian_songs_kr: st.write(s)
    with t5:
        for v in violin_list: st.write(f"🎻 {v}")
elif menu=="امتحانات":
    q=st.radio("김치؟",["كيمتشي","محشي"])
    if st.button("جاوبي"):
        if q=="كيمتشي": st.success("صح!"); st.session_state.score+=1
    st.write(f"Score: {st.session_state.score}")
elif menu=="الشهادة":
    st.balloons()
    st.header("🎓 شهادة Asmaa V8")
    st.write("200 كلمة + أكل + شرب + أغاني فرق كتير + كمان")
    st.write(f"{datetime.date.today()}")
