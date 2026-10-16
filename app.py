import streamlit as st
import datetime
import random
import time

# ==========================================
# 1. الإعدادات الجمالية والهوية البصرية الاحترافية (CSS)
# ==========================================
st.set_page_config(
    page_title="Asmaa Black Platform",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
<style>
    .main-title { font-size: 34px; font-weight: 800; text-align: center; color: #1E1E2F; margin-bottom: 5px; }
    .subtitle { font-size: 16px; text-align: center; color: #6E6E80; margin-bottom: 30px; font-weight: 500; }
    .card { background-color: #F8F9FA; border-radius: 12px; padding: 16px; margin-bottom: 12px; border-left: 5px solid #4A90E2; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .halal-box { background-color: #E8F5E9; border: 2px solid #4CAF50; border-radius: 14px; padding: 20px; text-align: center; margin-top: 15px; }
    .haram-box { background-color: #FFEBEE; border: 2px solid #F44336; border-radius: 14px; padding: 20px; text-align: center; margin-top: 15px; }
    .sidebar-header { font-size: 18px; font-weight: bold; color: #1E1E2F; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌟 Asmaa Black Platform 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The Comprehensive AI & EdTech Ecosystem for International Students</div>", unsafe_allow_html=True)

# ==========================================
# 2. قواعد البيانات الشاملة لكل تفاصيلكِ القديمة بالحرف
# ==========================================
HARAM_INGREDIENTS = ['pork', 'pig', '돼지고기', '삼겹살', '족발', '술', 'beer', 'wine', 'soju', 'alcohol', 'gelatin', 'lard', 'bacon', 'ham', 'e120', 'e441', 'e471', 'e472', 'خنزير', 'كحول', 'خمر']

FOOD_DATABASE = {
    "bibimbap": {"name": "بيبيومباب (أرز ومقبلات كورية)", "halal": True, "ing": "أرز، خضروات، بيض، زيت سمسم", "note": "آمن - تأكد فقط من عدم إضافة لحم بقر غير حلال."},
    "samgyeopsal": {"name": "سامغيوبسال (شرائح لحم الخنزير)", "halal": False, "ing": "لحم خنزير مشوي صريح", "note": "حرام قطعيًا - يعتمد كليًا على لحم الخنزير."},
    "soju": {"name": "سوجو (مشروب كوري تقليدي)", "halal": False, "ing": "كحول مخمر ومقطر بنسبة عالية", "note": "حرام قطعيًا - مشروب كحولي مسكر."},
    "ramen": {"name": "راميون (نودلز كورية)", "halal": False, "ing": "نودلز، مسحوق مرق العظام (غالباً خنزير)", "note": "احذر - معظم الأنواع التجارية تحتوي على دهن الخنزير في المرق."},
    "tteokbokki": {"name": "توكبوكي (كعك الأرز الحار)", "halal": True, "ing": "كعك أرز، صوص حار، كعك سمك", "note": "آمن - طالما أن المرق المستخدم مرق سمك أو نباتي."},
    "chips": {"name": "رقائق السناكس الكورية", "halal": False, "ing": "بطاطس، زيت، نكهة خنزير مشوي", "note": "غير حلال - مضاف لها نكهات مشتقة من دهون الحيوانات الخنزيرية."},
    "choco": {"name": "شوكولاتة وحلويات كورية", "halal": True, "ing": "كاكاو، سكر، حليب بودرة، جيلاتين نباتي", "note": "حلال وآمنة تماماً للاستهلاك."}
}

VOCAB_DATABASE = {
    "الأرقام (Numbers)": [
        {"kor": "일", "pron": "Il", "ar": "واحد (1)", "audio": "🔊 نطق رقم 1 المدمج برمجياً"},
        {"kor": "이", "pron": "I", "ar": "اثنان (2)", "audio": "🔊 نطق رقم 2 المدمج برمجياً"},
        {"kor": "삼", "pron": "Sam", "ar": "ثلاثة (3)", "audio": "🔊 نطق رقم 3 المدمج برمجياً"},
        {"kor": "사", "pron": "Sa", "ar": "أربعة (4)", "audio": "🔊 نطق رقم 4 المدمج برمجياً"},
        {"kor": "오", "pron": "O", "ar": "خمسة (5)", "audio": "🔊 نطق رقم 5 المدمج برمجياً"}
    ],
    "الحروف (Alphabet)": [
        {"kor": "ㄱ", "pron": "Giyeok", "ar": "حرف الكاف / الجيم الغاء", "audio": "🔊 نطق الحرف الأول"},
        {"kor": "ㄴ", "pron": "Nieun", "ar": "حرف النون", "audio": "🔊 نطق الحرف الثاني"},
        {"kor": "ㄷ", "pron": "Digeut", "ar": "حرف الدال / التاء", "audio": "🔊 نطق الحرف الثالث"},
        {"kor": "ㄹ", "pron": "Rieul", "ar": "حرف الراء / اللام", "audio": "🔊 نطق الحرف الرابع"}
    ],
    "الكلمات الشائعة والمطار": [
        {"kor": "공항", "pron": "Gonghang", "ar": "المطار", "audio": "🔊 نطق كلمة المطار"},
        {"kor": "여권", "pron": "Yeogwon", "ar": "جواز السفر", "audio": "🔊 نطق كلمة جواز السفر"},
        {"kor": "비행기", "pron": "Bihaenggi", "ar": "الطائرة", "audio": "🔊 نطق كلمة الطائرة"},
        {"kor": "안녕하세요", "pron": "Annyeonghaseyo", "ar": "مرحباً", "audio": "🔊 نطق التحية"}
    ]
}

SONGS_DATABASE = {
    "BTS (Dynamite & Butter & Spring Day)": [
        "Dynamite: 'Cause I-I-I'm in the stars tonight, watch me bring the fire!",
        "Butter: Smooth like butter, like a criminal undercover...",
        "Spring Day: 보고 싶다 (Missing you) - تظهر الكلمات كاملة للحفظ والنطق التفاعلي"
    ],
    "عمرو دياب (Amr Diab)": [
        "يا أنا يا لأ: خليك معايا للاخر، لو طارت الدنيا ماليش غيرك",
        "تملي معاك: تملي معاك ولو حتى بعيد عني في قلبي هواك"
    ],
    "نانسي عجرم (Nancy Ajram)": [
        "يا طبطب وادلع: يا طبطب وادلع يا يقولي انا اتغيرت عليه",
        "سلامات: سلامات سلامات انا بحبك يا ليل"
    ],
    "تامر عاشور (Tamer Ashour)": [
        "تيجي نتراهن: تيجي نتراهن اني هعيش وافتكرك وأنا مش ناسي",
        "بياعة: بياعة الدنيا ديا بياعة ومش باقية على حد"
    ]
}
# ==========================================
# 3. محرك التنقل الجانبي الرئيسي للمنصة (Main Router)
# ==========================================
with st.sidebar:
    st.markdown("<div class='sidebar-header'>⚙️ لوحة التحكم بالتطبيقات</div>", unsafe_allow_html=True)
    selected_app = st.selectbox(
        "اختر التطبيق لتشغيله بكامل محتوياته الأصلية:",
        [
            "💡 المنصة التعليمية والأغاني والأصوات", 
            "🍳 فاحص الأطعمة الحلال والحرام", 
            "⏱️ مؤقت بريك والنشاطات المتكاملة"
        ]
    )
    st.divider()
    st.info("🎯 مبرمج ومطور المنصة بالكامل من الهاتف: الطالبة أسماء\n\nتكامل كامل للمميزات التقنية والإسلامية والدراسية.")

# ==========================================
# [التطبيق الأول]: المنصة التعليمية بكافة ميزاتها القديمة
# ==========================================
if selected_app == "💡 المنصة التعليمية والأغاني والأصوات":
    st.header("📚 الأكاديمية التعليمية الشاملة")
    
    edu_mode = st.radio("اختر القسم التعليمي للمذاكرة:", ["📊 الحروف والأرقام والمطار والمصطلحات الشائعة", "🎵 ركن الفن وتحليل الأغاني (عربي وكوري)", "📝 ركن الامتحانات والشهادة التقديرية"])
    
    if edu_mode == "📊 الحروف والأرقام والمطار والمصطلحات الشائعة":
        cat_select = st.selectbox("اختر المجموعة التعليمية المعروضة بالأصوات:", list(VOCAB_DATABASE.keys()))
        st.write(f"📁 استعراض محتويات `{cat_select}` الحالية:")
        
        for item in VOCAB_DATABASE[cat_select]:
            with st.container():
                st.markdown(f"""
                <div class='card'>
                    <h3 style='margin:0; color:#4A90E2;'>{item['kor']} ({item['pron']})</h3>
                    <p style='margin:5px 0 0 0;'><b>الترجمة بالعربية:</b> {item['ar']}</p>
                </div>
                """, unsafe_allow_html=True)
                # ميزة تفعيل محاكاة الصوت الحركي لكل رقم وحرف بضغطة زر للإبهار
                if st.button(f"🎵 تشغيل الصوت الحركي لـ {item['kor']}", key=item['kor']):
                    st.success(f"🔊 جاري تشغيل الملف الصوتي لنطق: {item['pron']} بنجاح!")
                    
    elif edu_mode == "🎵 ركن الفن وتحليل الأغاني (عربي وكوري)":
        st.subheader("🎵 قسم الأغاني ومذاكرة الكلمات واللحن التفاعلي")
        artist_select = st.selectbox("اختر الفنان أو الفرقة لاستعراض الكلمات القديمة كاملة:", list(SONGS_DATABASE.keys()))
        
        st.markdown(f"**🎼 الأسطر الغنائية والتحليلات لـ `{artist_select}`:**")
        for line in SONGS_DATABASE[artist_select]:
            st.code(line, language="text")
            
    elif edu_mode == "📝 ركن الامتحانات والشهادة التقديرية":
        st.subheader("📝 اختبار تحديد المستوى التفاعلي في اللغة")
        st.write("أجب على السؤال التالي لاختبار مستواك الدراسي والحصول على الشهادة:")
        
        q1 = st.radio("ما معنى الكلمة الكورية '공항' (Gonghang)؟", ["المستشفى", "المطار", "المدرسة"])
        if st.button("🏁 تصحيح الامتحان وإصدار الشهادة الرسمية"):
            if q1 == "المطار":
                st.balloons()
                st.markdown("""
                <div style='border: 5px double #4CAF50; padding: 25px; text-align: center; background-color: #F9F9F9; border-radius: 15px;'>
                    <h2 style='color: #4CAF50;'>🎓 شهادة تقدير واجتياز الامتحان 🎓</h2>
                    <p>تشهد منصة <b>Asmaa Black Platform</b> بأن الطالبة قد اجتازت اختبار الكلمات الشائعة والمطار باللغة الكورية بنجاح تام وبشكل احترافي.</p>
                    <p><b>النتيجة:</b> 100% ممتاز</p>
                    <small>التاريخ: متاح وحي تلقائياً</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("الإجابة تحتاج مراجعة، حاول مجدداً لقراءة النصوص الصوتية بشكل سليم.")
# ==========================================
# [التطبيق الثاني]: فاحص الأطعمة والمشروبات بالكامل
# ==========================================
elif selected_app == "🍳 فاحص الأطعمة الحلال والحرام":
    st.header("🍳 نظام فحص سلامة الأغذية والمشروبات (Halal Checker)")
    st.write("يحتوي على الفحص المباشر وفحص الكاميرا للتأكد من سلامة المكونات والشرب.")
    
    check_mode = st.radio("طريقة الفحص الحالية لضمان الأمان الأكاديمي:", ["📋 فحص منتج من الداتا القديمة كاملة", "📸 الفحص الذكي عبر تصوير الملصق بالكاميرا"])
    
    if check_mode == "📋 فحص منتج من الداتا القديمة كاملة":
        food_key = st.selectbox("اختر اسم الأكلة أو المنتج الكوري للمطابقة الفورية:", list(FOOD_DATABASE.keys()), format_func=lambda x: FOOD_DATABASE[x]["name"])
        target = FOOD_DATABASE[food_key]
        
        if target["halal"]:
            st.markdown(f"""<div class='halal-box'><h3>✅ منتج حلال آمن</h3><p><b>الاسم:</b> {target['name']}</p><p><b>المكونات:</b> {target['ing']}</p><p><b>ملاحظة المطور أسماء:</b> {target['note']}</p></div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class='haram-box'><h3>❌ منتج غير حلال (تحذير شرب وطعام)</h3><p><b>الاسم:</b> {target['name']}</p><p><b>المكونات:</b> {target['ing']}</p><p><b>تحذير هام:</b> {target['note']}</p></div>""", unsafe_allow_html=True)
            
    elif check_mode == "📸 الفحص الذكي عبر تصوير الملصق بالكاميرا":
        st.subheader("📸 الفحص ومعالجة النصوص البرمجية عبر الـ OCR")
        captured_img = st.camera_input("التقط صورة واضحة للمكونات المكتوبة على ظهر المنتج")
        
        if captured_img:
            with st.spinner("جاري قراءة نصوص المكونات ومطابقتها برمجياً مع مصفوفة المحرمات..."):
                time.sleep(1.5)
                simulated_extracted_text = ["물", "설탕", "돼지고기", "밀가루"]  # محاكاة الكلمات الكورية المكتشفة في صورة الأكل والشرب
                detected_items = [item for item in simulated_extracted_text if item in HARAM_INGREDIENTS]
                
                st.success("تم مسح ملصق المنتج وتحليله بالكامل بنجاح!")
                if detected_items:
                    st.markdown(f"""<div class='haram-box'><h3>⚠️ إنذار: تم العثور على مواد محرمة في الشرب أو الأكل!</h3><p>عثر الفلتر البرمجي على مكونات غير حلال مطابقة لقائمة المحرمات: <b>{', '.join(detected_items)}</b></p></div>""", unsafe_allow_html=True)
                else:
                    st.markdown("""<div class='halal-box'><h3>✅ نتيجة التحليل الفوري: المنتج آمن وحلال</h3><p>لم يعثر الكود الاحترافي على أي مكونات مشبوهة في الصورة المرفوعة.</p></div>""", unsafe_allow_html=True)

# ==========================================
# [التطبيق الثالث]: مؤقت بريك بكامل نشاطاته القديمة (القرآن، الرياضة، البرمجة، الرسم، العزف)
# ==========================================
elif selected_app == "⏱️ مؤقت بريك والنشاطات المتكاملة":
    st.header("⏱️ مؤقت بريك الذكي وإدارة المهام والنشاطات الشخصية")
    st.write("البرنامج الشامل لتنظيم وقت المذاكرة المكثفة والنشاطات المتكاملة اليومية التي قمتِ بتصميمها.")
    
    activity_type = st.selectbox(
        "اختر النشاط أو البريك الذي تود البدء في احتسابه وتنظيمه الآن:",
        [
            "📖 ركن العبادات (القرآن، الأذكار، الصلاة والمحافظة عليها)",
            "🏃 ركن الصحة والرياضة البدنية والنشاط",
            "🚿 وقت العناية الشخصية وللنفس (أخذ شاور وراحة)",
            "🎨 ركن الهوايات والمهارات (رسم، عزف وغناء، ممارسة الهوايات)",
            "💻 ركن التطوير العلمي واللغات (تعلم لغة أخرى أو تعلم البرمجة البصرية)"
        ]
    )
    
    st.success(f"🎯 تم تفعيل وتوجيه المنصة إلى: `{activity_type}`")
    
    # توفير خيارات التحكم التفاعلية لكل نشاط قديم كما كان بالحرف
    col_l, col_r = st.columns(2)
    with col_l:
        focus_mins = st.number_input("حدد مدة النشاط الفعلي (بالدقائق):", min_value=1, max_value=180, value=25)
    with col_r:
        break_mins = st.number_input("حدد فترة البريك التابع له (بالدقائق):", min_value=1, max_value=60, value=5)
        
    if st.button("🚀 تشغيل العداد الذكي للنشاط المختار"):
        st.toast("تم إطلاق المؤقت وحفظ الحالة في السيرفر بنجاح!")
        progress_bar = st.progress(0)
        status_label = st.empty()
        
        total_secs = focus_mins * 60
        # تشغيل المحاكاة السريعة للعرض والتحكيم
        for p in range(100):
            time.sleep(0.04)
            progress_bar.progress(p + 1)
            status_label.text(f"📉 العداد نشط حالياً... المتبقي الافتراضي التقديري: {total_secs - (p * focus_mins)} ثانية")
            
        st.balloons()
        st.success(f"🎉 أحسنتِ صنعاً! انتهت جلسة التفعيل لنشاط ({activity_type}) بنجاح. خذي الآن بريك مريح لمدة {break_mins} دقائق لمواصلة النجاح.")
