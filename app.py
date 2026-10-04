import streamlit as st
from gtts import gTTS
import io, random, datetime

st.set_page_config(page_title="Asmaa Korean Academy V7", page_icon="🇰🇷", layout="wide")
st.markdown("<style>.stApp{background: linear-gradient(135deg,#fce4ec,#e1bee7)}.stButton>button{background:#ec407a;color:white;border-radius:20px}</style>", unsafe_allow_html=True)

def speak(t,l='ko'):
    try:
        fp=io.BytesIO(); gTTS(text=t, lang=l if l in ['ko','ar','en','zh'] else 'ko').write_to_fp(fp); st.audio(fp.getvalue(), format='audio/mp3')
    except: st.write(t)

if 'streak' not in st.session_state: st.session_state.streak=0
if 'i' not in st.session_state: st.session_state.i=0
if 'flip' not in st.session_state: st.session_state.flip=False
if 'quiz_score' not in st.session_state: st.session_state.quiz_score=0

hangul = [("ㄱ","g/k","ㅏ","a"),("ㄴ","n","ㅓ","eo"),("ㄷ","d/t","ㅗ","o"),("ㄹ","r/l","ㅜ","u"),("ㅁ","m","ㅡ","eu"),("ㅂ","b/p","ㅣ","i")]
numbers = [(1,"하나 hana / 일 il"),(2,"둘 dul / 이 i"),(3,"셋 set / 삼 sam"),(4,"넷 net / 사 sa"),(5,"다섯 daseot / 오 o"),(10,"열 yeol / 십 sip"),(20,"스물 seumul / 이십 isip"),(100,"백 baek")]
grammar = [("SOV","أنا تفاحة آكل = 나는 사과를 먹어요"),("는/은","موضوع الجملة"),("를/을","مفعول به"),("요","احترام")]
greetings = [("안녕하세요","annyeonghaseyo","السلام عليكم"),("안녕","annyeong","هاي"),("감사합니다","gamsahamnida","شكرا"),("사랑해","saranghae","بحبك"),("괜찮아요","gwaenchanayo","كله تمام")]
airport = [("비행기","bihaenggi","طيارة"),("공항","gonghang","مطار"),("여권","yeogwon","باسبور"),("출구","chulgu","مخرج"),("어디예요?","eodiyeyo?","فين؟"),("화장실","hwajangsil","حمام"),("티켓","tiket","تذكرة")]
common = [("물","mul","ميه"),("밥","bap","رز/أكل"),("집","jip","بيت"),("학교","hakgyo","مدرسة"),("친구","chingu","صديق"),("가족","gajok","عائلة")]
korean_food = [("김치","kimchi","كيمتشي"),("비빔밥","bibimbap","بيبيمباب"),("불고기","bulgogi","بولجوجي"),("떡볶이","tteokbokki","توكبوكي"),("삼겹살","samgyeopsal","سامجيوبسال"),("김밥","kimbap","كيمباب"),("라면","ramyeon","راميون")]
egyptian_food_kr = [("코샤리","kosyari","كشري"),("몰로키아","molrokia","ملوخية"),("풀 메다메스","pul medames","فول"),("타아메야","taameya","طعمية"),("마흐시","mahshi","محشي"),("코프타","kopeuta","كفتة"),("오므 알리","omu ali","أم علي")]
chinese_food_kr = [("짜장면","jjajangmyeon","جاجانغميون"),("짬뽕","jjamppong","جامبونغ"),("마파두부","mapa dubu","مابو توفو"),("딤섬","dimseom","ديم سوم"),("북경오리","bukgyeong ori","بط بكين"),("탕수육","tangsuyuk","تانجسويوك")]
korean_drinks = [("바나나 우유","banana uyu","لبن موز"),("소주","soju","سوجو"),("막걸리","makgeolli","ماكولي"),("식혜","sikhye","شكهيه"),("미숫가루","misutgaru","ميشوتجارو"),("보리차","boricha","شاي شعير")]
egyptian_drinks_kr = [("히비스커스","hibiseukeoseu","كركديه"),("소비아","sobia","سوبيا"),("사탕수수 주스","satang susu juseu","عصير قصب"),("타마린드","tamarindeu","تمر هندي"),("망고 주스","manggo juseu","مانجو"),("사흘라브","sahllabeu","سحلب")]
chinese_drinks_kr = [("버블티","beobeulti","بابل تي"),("우롱차","urongcha","شاي أولونغ"),("자스민차","jaseumincha","شاي ياسمين"),("리치 주스","richi juseu","عصير ليتشي")]
bts_songs = [("Dynamite","다이너마이트"),("Butter","버터"),("Spring Day","봄날"),("Boy With Luv","작은 것들을 위한 시"),("IDOL","아이돌")]
violin_bts = [("Dynamite - Violin","다이너마이트 바이올린 🎻"),("Spring Day - Violin","봄날 바이올린 🎻")]
chinese_songs = [("My Love","我的爱"),("Ni Hao","你好"),("Yue Liang","月亮")]
egyptian_songs_kr = [("هايجيلي موجوع","하이질리 마우주우"),("يا طبطب","야 타브타브"),("3 دقات","세 다카트")]
word_of_day = [("오늘 단어: 사랑","حب"),("오늘 단어: 행복","سعادة"),("오늘 단어: 꿈","حلم")]

st.title("🇰🇷 أكاديمية أسماء الكورية V7 - النهائية")
st.write(f"🔥 Streak: {st.session_state.streak} يوم")

menu = st.sidebar.selectbox("القائمة", ["الحروف","الأرقام","القواعد","التحية","المطار","كلمات","الأكل كله","المشروبات كلها","الأغاني + كمان","كروت حفظ","شات كوري","الامتحان الشامل","الشهادة"])

if menu=="الحروف":
    st.header("الحروف"); [st.write(f"{h[0]}={h[1]}, {h[2]}={h[3]}") for h in hangul]
elif menu=="الأرقام":
    [st.write(f"{n[0]} = {n[1]}") for n in numbers]
elif menu=="القواعد":
    [st.write(f"{g[0]}: {g[1]}") for g in grammar]
elif menu=="التحية":
    [st.write(f"{g[0]} ({g[1]}) = {g[2]}") for g in greetings]
elif menu=="المطار":
    [st.button(f"{a[0]} - {a[2]}", key=a[0]) and speak(a[0]) for a in airport]
elif menu=="كلمات":
    [st.button(f"{c[0]} = {c[2]}", key=c[0]) and speak(c[0]) for c in common]
elif menu=="الأكل كله":
    st.subheader("🇰🇷 أكل كوري"); [st.write(f"{x[0]} - {x[2]}") for x in korean_food]
    st.subheader("🇪🇬 أكل مصري بالكوري"); [st.write(f"{x[0]} = {x[2]}") for x in egyptian_food_kr]
    st.subheader("🇨🇳 أكل صيني بالكوري"); [st.write(f"{x[0]} = {x[2]}") for x in chinese_food_kr]
elif menu=="المشروبات كلها":
    st.subheader("🥤 مشروبات كورية")
    [st.write(f"{d[0]} = {d[2]}") for d in korean_drinks]
    st.subheader("🥤 مشروبات مصرية بالكوري")
    [st.success(f"{d[0]} = {d[2]}") for d in egyptian_drinks_kr]
    st.subheader("🥤 مشروبات صينية بالكوري")
    [st.info(f"{d[0]} = {d[2]}") for d in chinese_drinks_kr]
elif menu=="الأغاني + كمان":
    st.subheader("BTS"); [st.write(x[0]) for x in bts_songs]
    st.subheader("🎻 بالكمان"); [st.write(v[0]) for v in violin_bts]
    st.subheader("صيني"); [st.write(x[0]) for x in chinese_songs]
    st.subheader("مصري بالكوري"); [st.write(x[0]) for x in egyptian_songs_kr]
elif menu=="الامتحان الشامل":
    st.header("امتحان");
    if st.button("ابدأي"): st.balloons()
elif menu=="الشهادة":
    st.balloons(); st.header("🎓 شهادة Asmaa - Korean Expert")
