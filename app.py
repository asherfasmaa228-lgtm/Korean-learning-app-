import streamlit as st
from gtts import gTTS
import io, random, datetime

st.set_page_config(page_title="Asmaa V7 Giant", page_icon="🥤", layout="wide")
st.markdown("<style>.stApp{background:#0a0a0a;color:white} h1{color:#ff4b9a!important}</style>", unsafe_allow_html=True)

def speak(t,l='ko'):
    try:
        fp=io.BytesIO(); gTTS(text=t,lang=l).write_to_fp(fp); st.audio(fp.getvalue(), format='audio/mp3')
    except: st.write(t)

if 'streak' not in st.session_state: st.session_state.streak=1
if 'i' not in st.session_state: st.session_state.i=0; st.session_state.sc=0
if 'flip' not in st.session_state: st.session_state.flip=False

# بيانات
words_day = [("사랑 Sarang","حب"),("보고싶다 Bogosipda","وحشتني"),("예쁘다 Yeppeuda","جميلة")]
today_word = random.choice(words_day)

korean_foods = [("비빔밥 Bibimbap رز بالخضار","https://images.unsplash.com/photo-1590301157890-48185b27968c"),("떡볶이 Tteokbokki كعك حار","https://images.unsplash.com/photo-1498654896293-37aacf113fd9"),("김치 Kimchi","https://images.unsplash.com/photo-1580651315530-69c8e0021612"),("불고기 Bulgogi","https://images.unsplash.com/photo-1546069901-ba9599a7e63c"),("김밥 Kimbap","https://images.unsplash.com/photo-1563245372-f21724e3856d")]
egyptian_foods = [("코샤리 Koshari كشري","https://images.unsplash.com/photo-1512058564366-18510be2db19"),("몰로키아 Molokhia ملوخية","https://images.unsplash.com/photo-1547592180-85f173990554")]
chinese_foods = [("딤섬 Dimsum ديم سام","https://images.unsplash.com/photo-1563245372-f21724e3856d"),("짜장면 Jjajangmyeon","https://images.unsplash.com/photo-1552611052-33e04de081de")]

# المشروبات الجديدة كلها بالكوري
drinks_korean = [("바나나우유 Banana Uyu - لبن موز","اشهر مشروب كوري"),("소주 Soju - سوجو","مشروب كوري مشهور"),("막걸리 Makgeolli - ماكولي","رز مسكر"),("식혜 Sikhye - شيكيه","مشروب رز حلو"),("유자차 Yuja Cha - شاي يوجا","شاي بالليمون الكوري")]
drinks_egyptian = [("히비스커스차 Hibiscus Cha - كركديه","كركديه بارد"),("소비아 Sobia - سوبيا","سوبيا مصري"),("사탕수 주스 Qasab Juice - عصير قصب","عصير قصب"),("망고 주스 Mango Juice - مانجو","مانجو مصري"),("타마린드 Tamarind - تمر هندي","تمر هندي")]
drinks_chinese = [("버블티 Bubble Tea - بابل تي","شاي بالفقاعات"),("우롱차 Oolong Cha - شاي اولونج","شاي صيني"),("자스민차 Jasmine Cha - شاي ياسمين","شاي ياسمين")]

st.title("🇰🇷🥤 Asmaa V7 - الأكاديمية العملاقة")
c1,c2,c3 = st.columns(3)
c1.metric("🔥", f"{st.session_state.streak} يوم")
c2.metric("كلمة اليوم", today_word[0])
c3.metric("نقاط", st.session_state.sc)

st.info(f"كلمة اليوم: {today_word[0]} = {today_word[1]}")
if st.button("🔊 اسمعي كلمة اليوم"): speak(today_word[0].split()[0])

t1,t2,t3,t4,t5,t6,t7 = st.tabs(["🔤 حروف وارقام ومطار وقواعد","🍱 كل الاكل","🥤 كل المشروبات بالكوري","🎤 كل الاغاني BTS صيني مصري","🃏 كروت + 🤖 شات AI","📝 امتحان 50","🏆 شهادة"])

with t1:
    st.subheader("الحروف Hangul")
    st.write("ㄱ=g ج, ㄴ=n ن, ㅏ=a ا, ㅗ=o و, ㅎ=h هـ")
    if st.button("가나다라마"): speak("가나다라마")
    st.divider()
    st.write("**ارقام:** 하나 1, 둘 2, 셋 3, 넷 4, 다섯 5, 열 10, 스무 20, 백 100")
    st.write("**مطار:** 공항 مطار, 비행기 طيارة, 여권 باسبور, 출구 مخرج, 어디예요؟ فين؟")
    st.write("**تحية:** 안녕하세요 أهلا رسمي, 안녕 هاي, 감사합니다 شكرا, 죄송합니다 اسف")
    st.write("**قاعدة SOV:** 나는 물을 마셔요 = انا مياه اشرب")
    st.write("**كلمات شائعة:** 물 مياه, 밥 اكل, 사랑 حب, 친구 صاحب, 예쁘다 جميل, 보고싶다 وحشتني")

with t2:
    pick=st.selectbox("مطبخ:", ["كوري","مصري","صيني"], key="food")
    foods = korean_foods if pick=="كوري" else egyptian_foods if pick=="مصري" else chinese_foods
    for ko,img in foods:
        st.image(img, caption=ko, width=350)
        if st.button(f"نطق {ko}", key=ko+"f"): speak(ko.split()[0])

with t3:
    st.subheader("🥤 كل المشروبات بالكوري - نطق وكلام")
    dpick=st.selectbox("نوع المشروب:", ["كوري 🇰🇷","مصري 🇪🇬","صيني 🇨🇳"], key="drink")
    dlist = drinks_korean if "كوري" in dpick else drinks_egyptian if "مصري" in dpick else drinks_chinese
    for ko, desc in dlist:
        col1,col2 = st.columns([3,1])
        col1.write(f"**{ko}** - {desc}")
        if col2.button("🔊", key=ko+"d"): speak(ko.split()[0])
    st.divider()
    st.write("جملة مطعم: **이거 주세요 Igeo juseyo = ده لو سمحت**")
    if st.button("이거 주세요"): speak("이거 주세요")

with t4:
    st.subheader("BTS كل الاغاني + الكمان يعزف 🎻")
    bts_all = ["Dynamite","Butter","Spring Day 봄날","Fake Love","IDOL","Boy With Luv","Blood Sweat & Tears","DNA","MIC Drop","ON","Life Goes On","Permission to Dance","Euphoria Violin Ver.","Dynamite Violin Ver."]
    s=st.selectbox("BTS", bts_all); st.link_button("شغلي يوتيوب", f"https://www.youtube.com/results?search_query=BTS+{s}")
    if st.button("사랑 حب"): speak("사랑")
    st.divider()
    st.subheader("صيني 🇨🇳")
    cn=st.selectbox("صيني", ["My Love","Tong Hua童话","Ni De Da An你的答案"])
    if st.button("我爱你 Wo ai ni"): speak("我爱你",'zh')
    st.divider()
    st.subheader("مصري بالكوري 🇪🇬")
    eg=st.selectbox("مصري", ["هيجيلي موجوع - تامر عاشور","تملي معاك - عمرو دياب","مليونير"])
    st.write("هيجيلي موجوع = 아프게 올 거야 Apeuge ol geoya")
    if st.button("아프게 올 거야"): speak("아프게 올 거야")

with t5:
    st.subheader("🃏 كروت حفظ")
    cards=[("안녕하세요","أهلا"),("물","مياه"),("사랑","حب"),("바나나우유","لبن موز"),("히비스커스차","كركديه"),("감사합니다","شكرا")]
    card=random.choice(cards)
    if st.button(f"الكارت: {card[0] if not st.session_state.flip else card[1]} - اقلبي"): st.session_state.flip=not st.session_state.flip; st.rerun()
    st.divider()
    st.subheader("🤖 شات AI كوري - اسألي اي حاجة")
    msg=st.text_input("اكتبي: ازيك؟ بحبك؟ عايزة كركديه؟")
    if msg:
        if "ازيك" in msg: st.success("잘 지내요 Jal jinaeyo - انا كويسة!"); speak("잘 지내요")
        elif "بحبك" in msg: st.success("나도 사랑해 Nado saranghae"); speak("나도 사랑해")
        elif "كركديه" in msg or "مشروب" in msg: st.success("히비스커스차 주세요 Hibiscus cha juseyo - كركديه لو سمحت"); speak("히비스커스차 주세요")
        elif "شكرا" in msg: st.success("천만에요 Cheonmaneyo - العفو"); speak("천만에요")
        else: st.write("جربي تقولي: ازيك، بحبك، عايزة مشروب، شكرا")

with t6:
    st.subheader("امتحان 50 سؤال شامل الاكل والمشروبات")
    qs=[("안녕하세요؟","أهلا"),("물؟","مياه"),("바나나우유؟","لبن موز"),("히비스커스차؟","كركديه"),("비빔밥؟","رز"),("사랑؟","حب"),("공항؟","مطار"),("감사합니다؟","شكرا"),("하나؟","1"),("버블티؟","بابل تي")]*5
    if st.session_state.i < 50:
        q,a=qs[st.session_state.i]; st.write(f"سؤال {st.session_state.i+1}/50: {q} يعني ايه؟")
        ans=st.text_input("اجابتك:", key=f"an{st.session_state.i}")
        if st.button("التالي"):
            if ans: st.session_state.sc+=1
            st.session_state.i+=1; st.rerun()
    else:
        st.balloons(); st.success(f"يا أسماء جبتي {st.session_state.sc}/50")

with t7:
    if st.session_state.sc >= 20:
        st.success(f"🏆 شهادة Asmaa - Korean Expert {st.session_state.sc}/50")
        st.image("https://images.unsplash.com/photo-1620121478247-ec70f9a2e8ad", caption="شهادتك - خدي سكرين شوت!")
    else:
        st.write("خلصي الامتحان الاول عشان تاخدي الشهادة")
    if st.button("اعادة"): st.session_state.i=0; st.session_state.sc=0; st.rerun()

st.caption("By Asmaa - Beni Suef 💜 V7 Giant with Drinks & AI")
