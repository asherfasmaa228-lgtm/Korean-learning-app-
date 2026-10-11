import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="Barik Pro - منظم وقتك", layout="centered", page_icon="🕌")

# --- CSS ---
st.markdown("""
<style>
.card{background:rgba(255,255,255,.06);border:1px solid rgba(212,175,55,.3);border-radius:20px;padding:14px;margin:10px 0}
.logo{font-size:22px;font-weight:900;color:#d4af37}
.pill{min-width:70px;background:rgba(255,255,255,.06);border-radius:12px;padding:7px;text-align:center;font-size:10px;display:inline-block;margin:2px}
.pill.next{background:#d4af37;color:#000;font-weight:800}
.slot{background:linear-gradient(90deg,rgba(212,175,55,.15),rgba(255,255,255,.03));border-radius:12px;padding:10px;margin:4px 0;border-right:4px solid #d4af37;display:flex;justify-content:space-between}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card"><div class="logo">بريك | Barik Pro</div><div style="font-size:11px;opacity:.7">بني سويف - الشروق 6:52 | الظهر 12:43 | المغرب 6:34 - منظم أسبوعي شامل</div></div>', unsafe_allow_html=True)

# --- بيانات الصلاة ---
prayers = [
    {"n":"الفجر","t":"05:27"},
    {"n":"الشروق","t":"06:52"},
    {"n":"الظهر","t":"12:43"},
    {"n":"العصر","t":"16:04"},
    {"n":"المغرب","t":"18:34"},
    {"n":"العشاء","t":"19:50"},
]

cols = st.columns(6)
for i,p in enumerate(prayers):
    is_next = p["n"]=="المغرب"
    with cols[i]:
        st.markdown(f"<div class='pill {'next' if is_next else ''}'><div>{p['n']}</div><b>{p['t']}</b></div>", unsafe_allow_html=True)

st.info("🕋 القبلة 132° - بني سويف - القادمة: المغرب 6:34")
st.write(f"⏰ الآن: {datetime.now().strftime('%I:%M %p')} - بني سويف")

# --- التابات الرئيسية ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📅 الأسبوع", "📿 الأذكار", "📖 القرآن", "📚 فقه وقصص", "📝 يومي"])

# --- 1. الأسبوع ---
with tab1:
    if "weekData" not in st.session_state:
        st.session_state.weekData = {
            0: [{"time":'08:00',"type":'📚 درس / مذاكرة',"title":'مذاكرة المنحة الكورية',"done":False}],
            3: [{"time":'05:40',"type":'📿 الأذكار',"title":'أذكار بعد الفجر 5:27',"done":False},
                {"time":'06:52',"type":'📖 قرآن',"title":'قراءة قرآن بعد الشروق',"done":False},
                {"time":'09:00',"type":'📚 درس / مذاكرة',"title":'دروس المنحة',"done":False},
                {"time":'17:00',"type":'🈶 لغة جديدة - كوري',"title":'كوري 20 كلمة',"done":False},
                {"time":'18:40',"type":'📿 الأذكار',"title":'أذكار المساء قبل المغرب',"done":False}],
        }

    days = ["السبت","الأحد","الإثنين","الثلاثاء","الأربعاء","الخميس","الجمعة"]
    day = st.selectbox("اختاري اليوم", range(7), format_func=lambda x: days[x], index=3)

    list_tasks = st.session_state.weekData.get(day, [])
    done = sum(1 for s in list_tasks if s["done"])
    total = len(list_tasks)
    perc = int(done/total*100) if total else 0
    st.progress(perc, text=f"{perc}% مكتمل - {done} من {total}")

    for i, s in enumerate(list_tasks):
        col_a, col_b = st.columns([4,1])
        with col_a:
            st.markdown(f"<div class='slot'>{s['time']} | {s['type']} - {s['title']}</div>", unsafe_allow_html=True)
        with col_b:
            if st.button("✅" if s["done"] else "⭕", key=f"done{day}{i}"):
                st.session_state.weekData[day][i]["done"] = not s["done"]
                st.rerun()

    st.divider()
    st.write("**+ أضيفي وقت جديد**")
    c1,c2 = st.columns(2)
    with c1:
        nType = st.selectbox("النوع", ["📚 درس / مذاكرة","🚿 عناية بالنفس","💪 رياضة","🈶 لغة كورية","🎨 برمجة","🗣️ ثقة بالنفس"])
    with c2:
        nTime = st.time_input("الوقت")
    nTitle = st.text_input("العنوان", placeholder="مثلاً: مذاكرة كوري TOPIK")
    if st.button("➕ أضيفي للجدول", use_container_width=True):
        if day not in st.session_state.weekData:
            st.session_state.weekData[day] = []
        st.session_state.weekData[day].append({"time":nTime.strftime("%H:%M"),"type":nType,"title":nTitle or nType,"done":False})
        st.rerun()

# --- 2. الأذكار ---
with tab2:
    azkar_filter = st.radio("فلتر", ["الكل","الصباح","المساء","بعد الصلاة","النوم"], horizontal=True)

    allAzkar=[
        {"cat":'الصباح',"title":'أذكار الصباح (بعد الفجر 5:27)',"text":'أصبحنا وأصبح الملك لله، لا إله إلا الله وحده لا شريك له... (3 مرات)'},
        {"cat":'الصباح',"title":'آية الكرسي',"text":'الله لا إله إلا هو الحي القيوم...'},
        {"cat":'المساء',"title":'أذكار المساء (قبل المغرب 6:34)',"text":'أمسينا وأمسى الملك لله...'},
        {"cat":'المساء',"title":'التسبيح 100',"text":'سبحان الله وبحمده 100 مرة'},
        {"cat":'بعد الصلاة',"title":'بعد الصلاة',"text":'أستغفر الله 3، اللهم أنت السلام...'},
        {"cat":'النوم',"title":'أذكار النوم',"text":'باسمك اللهم أموت وأحيا، سورة الملك'},
        {"cat":'الكل',"title":'دعاء الهم',"text":'لا إله إلا الله العظيم الحليم...'},
    ]
    for z in allAzkar:
        if azkar_filter=="الكل" or z["cat"]==azkar_filter or (azkar_filter=="الكل"):
            with st.expander(f"{z['title']}"):
                st.write(z["text"])
                st.button("قرأته ✅", key=z["title"]+z["cat"])

# --- 3. القرآن ---
with tab3:
    surahs=['الفاتحة','البقرة','آل عمران','النساء','المائدة','الأنعام','الأعراف','الأنفال','التوبة','يونس','هود','يوسف','الرعد','إبراهيم','الحجر','النحل','الإسراء','الكهف','مريم','طه','الأنبياء','الحج','المؤمنون','النور','الفرقان','الشعراء','النمل','القصص','العنكبوت','الروم','لقمان','السجدة','الأحزاب','سبأ','فاطر','يس','الصافات','ص','الزمر','غافر','فصلت','الشورى','الزخرف','الدخان','الجاثية','الأحقاف','محمد','الفتح','الحجرات','ق','الذاريات','الطور','النجم','القمر','الرحمن','الواقعة','الحديد','المجادلة','الحشر','الممتحنة','الصف','الجمعة','المنافقون','التغابن','الطلاق','التحريم','الملك','القلم','الحاقة','المعارج','نوح','الجن','المزمل','المدثر','القيامة','الإنسان','المرسلات','النبأ','النازعات','عبس','التكوير','الانفطار','المطففين','الانشقاق','البروج','الطارق','الأعلى','الغاشية','الفجر','البلد','الشمس','الليل','الضحى','الشرح','التين','العلق','القدر','البينة','الزلزلة','العاديات','القارعة','التكاثر','العصر','الهمزة','الفيل','قريش','الماعون','الكوثر','الكافرون','النصر','المسد','الإخلاص','الفلق','الناس']

    qSearch = st.text_input("ابحثي عن سورة... مثلاً البقرة / يس / الملك")
    filtered = [s for s in surahs if qSearch in s] if qSearch else surahs[:15]

    for idx, s in enumerate(filtered):
        col1,col2 = st.columns([3,1])
        col1.write(f"**{surahs.index(s)+1}. {s}** - الجزء { (surahs.index(s)//4)+1 }")
        if col2.button("اقرأي", key=f"q{idx}"):
            st.link_button(f"افتحي سورة {s} في quran.com", f"https://quran.com/ar/{surahs.index(s)+1}")

    st.divider()
    st.write("📖 **مصحف القراءة**")
    st.info("اختاري سورة للقراءة... بسم الله الرحمن الرحيم - لو عايزة المصحف الكامل افتحي quran.com")
    st.link_button("افتحي المصحف الكامل", "https://quran.com/ar")

# --- 4. فقه ---
with tab4:
    fiqh = st.selectbox("اختاري", ["فقه الصلاة","فقه الوضوء","قصص الأنبياء","تعلم مهارة"])
    if fiqh=="فقه الصلاة":
        st.write("**أركان الصلاة:** النية، القيام، الفاتحة، الركوع، السجود... الظهر 12:43 - 4 فرض، 4 سنة قبل")
    elif fiqh=="فقه الوضوء":
        st.write("**فرائض:** غسل الوجه، اليدين للمرفقين، مسح الرأس، غسل الرجلين - **سنن:** البسملة، السواك...")
    elif fiqh=="قصص الأنبياء":
        st.write("**يوسف:** صبر على البلاء فصار عزيز مصر - **مريم:** طهارة وعفة - **موسى:** مواجهة الظلم")
    else:
        st.write("1. برمجة تطبيقات: MIT App Inventor\n2. رسم: 10 دقايق يومياً\n3. ثقة بالنفس: اتكلمي قدام المراية 2 دقيقة\n4. كوري: Duolingo")

# --- 5. يومي ---
with tab5:
    st.write(f"📝 **مراجعة يوم {datetime.now().strftime('%A')}**")
    if "notes" not in st.session_state:
        st.session_state.notes = []

    dailyNote = st.text_area("اكتبي هنا: النهارده عملت ايه؟ حسيتي بإيه؟", height=150)
    if st.button("💾 احفظي نوتة اليوم"):
        if dailyNote:
            st.session_state.notes.append({"date":datetime.now().strftime("%Y-%m-%d %H:%M"), "text":dailyNote})
            st.success("اتحفظت!")

    for n in reversed(st.session_state.notes[-3:]):
        st.markdown(f"<div style='background:rgba(255,255,255,.05);border:1px dashed #d4af37;border-radius:12px;padding:10px;margin:8px 0'><div style='font-size:10px;opacity:.7'>{n['date']}</div><div>{n['text']}</div></div>", unsafe_allow_html=True)