import streamlit as st
import datetime
import random
import time

# ====================================================================
# 1. الإعدادات البرمجية الأساسية وحقن الهوية البصرية (Custom CSS)
# ====================================================================
st.set_page_config(
    page_title="Asmaa-EduCore Platform",
    page_icon="🚀",
    layout="centered"
)

# تصميم واجهة مستخدم مخصصة واحترافية تلغي المظهر التقليدي لـ Streamlit
st.markdown("""
<style>
    /* تنسيق العناوين والنصوص العامة */
    .main-title { font-size: 34px; font-weight: 800; text-align: center; color: #1E1E2F; margin-bottom: 5px; }
    .subtitle { font-size: 16px; text-align: center; color: #6E6E80; margin-bottom: 30px; font-weight: 500; }
    
    /* تصميم بطاقات عرض الكلمات الكورية */
    .vocab-card { 
        background-color: #F8F9FA; 
        border-radius: 12px; 
        padding: 16px; 
        margin-bottom: 12px; 
        border-left: 5px solid #4A90E2;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .vocab-kor { font-size: 20px; font-weight: bold; color: #4A90E2; margin: 0; }
    .vocab-details { font-size: 14px; color: #333333; margin: 5px 0 0 0; }
    
    /* تصميم صناديق التنبيه الذكية للأطعمة */
    .halal-box { 
        background-color: #E8F5E9; 
        border: 2px solid #4CAF50; 
        border-radius: 14px; 
        padding: 20px; 
        text-align: center; 
        margin-top: 15px; 
    }
    .haram-box { 
        background-color: #FFEBEE; 
        border: 2px solid #F44336; 
        border-radius: 14px; 
        padding: 20px; 
        text-align: center; 
        margin-top: 15px; 
    }
    
    /* تجميل القائمة الجانبية */
    .sidebar-header { font-size: 18px; font-weight: bold; color: #1E1E2F; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# عرض الترويسة الثابتة للمنصة في الأعلى
st.markdown("<div class='main-title'>🌟 Asmaa-EduCore 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The All-in-One Digital Ecosystem for International Students in South Korea</div>", unsafe_allow_html=True)

# ====================================================================
# 2. قواعد البيانات الهيكلية (Structured Core Databases)
# ====================================================================

# قاعدة بيانات المكونات غير الحلال للمطابقة البرمجية الصارمة
HARAM_INGREDIENTS = [
    'pork', 'pig', '돼지고기', '삼겹살', '족발', '술', 'beer', 'wine', 
    'soju', 'alcohol', 'gelatin', 'lard', 'bacon', 'ham', 'e120', 'e441', 'e471', 'e472'
]

# قاعدة بيانات الأطعمة الجاهزة للفحص السريع
FOOD_DATABASE = {
    "bibimbap": {"name": "بيبيومباب (أرز ومقبلات كورية)", "halal": True, "ing": "أرز، خضروات متنوعة، بيض، زيت سمسم", "note": "آمن تماماً. تأكد فقط في المطاعم من عدم إضافة لحم بقر غير مذبوح حلال."},
    "samgyeopsal": {"name": "سامغيوبسال (شرائح لحم البطن)", "halal": False, "ing": "لحم خنزير صريح مشوي", "note": "محرم قطعيًا لأنه يعتمد كليًا على لحم الخنزير."},
    "soju": {"name": "سوجو (المشروب الكوري التقليدي)", "halal": False, "ing": "كحول مخمر ومقطر بنسبة تتراوح بين 16-25%", "note": "محرم قطعيًا لأنه مشروب كحولي مسكر."},
    "ramen": {"name": "راميون (النودلز الكورية سريعة التحضير)", "halal": False, "ing": "نودلز، مسحوق مرق العظام (غالباً خنزير أو بقر غير حلال)، بهارات", "note": "احذر بشدة؛ معظم الأنواع التجارية التقليدية في كوريا تحتوي على مستخلصات دهن الخنزير في المرق."},
    "tteokbokki": {"name": "توكبوكي (كعك الأرز الحار)", "halal": True, "ing": "كعك أرز مضغوط، صوص الكوتشوجانغ الحار، كعك السمك", "note": "آمن بشكل عام، طالما أن المرق المستخدم في الطهي مرق سمك وليس مرق لحم خنزير."},
    "chips": {"name": "رقائق البطاطس والمقرمشات الكورية", "halal": False, "ing": "بطاطس، زيت نباتي، نكهة لحم الخنزير المدخن، محسّن طعم E621", "note": "غير حلال؛ الكثير من السناكس الكورية تُضاف لها نكهات مشتقة من دهون الحيوانات."},
    "choco": {"name": "شوكولاتة وحلويات كورية كلاسيكية", "halal": True, "ing": "مسحوق الكاكاو، سكر، حليب بودرة، جيلاتين نباتي (البكتين)", "note": "حلال وآمنة للاستهلاك."}
}

# قاعدة بيانات مخصصة لتعلم اللغة عبر نصوص الأغاني الشهيرة
KPOP_DATABASE = {
    "Dynamite (BTS)": [
        "'Cause I-I-I'm in the stars tonight", 
        "So watch me bring the fire and set the night alight", 
        "Shining through the city with a little funk and soul", 
        "Light it up like dynamite, whoa oh oh"
    ],
    "Butter (BTS)": [
        "Smooth like butter, like a criminal undercover", 
        "Gon' pop like trouble breaking into your heart like that", 
        "Cool shade, stunner, yeah, I owe it all to my mother"
    ],
    "Spring Day (BTS)": [
        "보고 싶다 (Missing you / أشتاق إليك)", 
        "이렇게 말하니까 더 보고 싶다 (Saying this makes me miss you more / قول هذا يضاعف اشتياقي)", 
        "너희 사진을 보고 있어도 보고 싶다 (Even looking at your photo, I still miss you / حتى وأنا أنظر لصورتك أشتاق إليك)"
    ],
    "DDU-DU DDU-DU (BLACKPINK)": [
        "착한 얼굴에 그렇지 못한 태도 (A kind face with an unkind attitude / وجه طيب ولكن بأسلوب جريء)", 
        "가녀린 몸매 속 가려진 Volume은 두배로 (Twice the volume hidden in a slender body)", 
        "거침없이 직진 굳ي 보진 않지 눈치 (Straight forward without hesitation)"
    ]
}

# مصفوفة المفردات الكورية المنظمة لتقليص مساحة الكود البرمجي وعرضها ديناميكيًا
KOREAN_VOCABULARY = [
    {"kor": "안녕하세요", "pron": "Annyeonghaseyo", "ar": "مرحباً / السلام عليكم", "cat": "👋 التحيات والترحيب"},
    {"kor": "감사합니다", "pron": "Gamsahabnida", "ar": "شكراً جزيلاً", "cat": "👋 التحيات والترحيب"},
    {"kor": "사랑해요", "pron": "Saranghaeyo", "ar": "أحبك", "cat": "👋 التحيات والترحيب"},
    {"kor": "죄송합니다", "pron": "Joesonghabnida", "ar": "أنا آسف", "cat": "👋 التحيات والترحيب"},
    {"kor": "밥", "pron": "Bap", "ar": "طعام / أرز مطبوخ", "cat": "🍎 الأطعمة والمشروبات"},
    {"kor": "물", "pron": "Mul", "ar": "ماء", "type": "🍎 الأطعمة والمشروبات", "cat": "🍎 الأطعمة والمشروبات"},
    {"kor": "고기", "pron": "Gogi", "ar": "لحم", "cat": "🍎 الأطعمة والمشروبات"},
    {"kor": "술", "pron": "Sul", "ar": "مشروب كحولي", "cat": "🍎 الأطعمة والمشروبات"},
    {"kor": "학교", "pron": "Hakgyo", "ar": "مدرسة / جامعة", "cat": "🏫 الحياة الأكاديمية واليومية"},
    {"kor": "친구", "pron": "Chingu", "ar": "صديق / زميل", "cat": "🏫 الحياة الأكاديمية واليومية"},
    {"kor": "한국", "pron": "Hanguk", "ar": "كوريا الجنوبية", "cat": "🏫 الحياة الأكاديمية واليومية"},
    {"kor": "공부", "pron": "Gongbu", "ar": "الدراسة / المذاكرة", "cat": "🏫 الحياة الأكاديمية واليومية"}
]

# ====================================================================
# 3. نظام توجيه الصفحات وعزل التطبيقات (Sidebar Router)
# ====================================================================
with st.sidebar:
    st.markdown("<div class='sidebar-header'>⚙️ لوحة تحكم المنصة</div>", unsafe_allow_html=True)
    
    # محرك العزل الأساسي: اختيار التطبيق يفصل الشاشة تماماً عن باقي الأكواد
    selected_app = st.selectbox(
        "اختر النظام الفرعي لتشغيله:",
        [
            "💡 أكاديمية اللغة الكورية", 
            "🍳 فاحص الأطعمة الحلال الحركي", 
            "⏱️ مؤقت بريك الذكي (Pomodoro)"
        ]
    )
    st.divider()
    # إبراز توقيعكِ كمطورة للمنصة لإبهار اللجنة
    st.info("🎯 مبرمج ومطور المنصة: الطالبة أسماء\n\nتحدي الإمكانيات عبر البرمجة السحابية بالهاتف.")

# ====================================================================
# [التطبيق الأول]: أكاديمية اللغة الكورية
# ====================================================================
if selected_app == "💡 أكاديمية اللغة الكورية":
    st.header("📚 الأكاديمية الكورية التفاعلية")
    st.write("نظام مبسط ومطور لمساعدة الطلاب العرب على إتقان المفردات الكورية وفهم البنية اللغوية برمجياً.")
    
    edu_tabs = st.tabs(["🔤 قاموس الكلمات الذكي", "🎵 ركن الفن والـ K-Pop"])
    
    with edu_tabs[0]:
        st.subheader("📑 تصفح الكلمات حسب الفئة")
        vocab_filter = st.selectbox("اختر فئة الكلمات لعرضها:", ["عرض جميع الكلمات", "👋 التحيات والترحيب", "🍎 الأطعمة والمشروبات", "🏫 الحياة الأكاديمية واليومية"])
        
        # حلقة تكرارية احترافية (Loop) بديلًا لتكرار مئات الأسطر يدويًا
        for item in KOREAN_VOCABULARY:
            if vocab_filter == "عرض جميع الكلمات" or item["cat"] == vocab_filter:
                st.markdown(f"""
                <div class='vocab-card'>
                    <div class='vocab-kor'>{item['kor']}</div>
                    <div class='vocab-details'>
                        <b>النطق اللاتيني:</b> {item['pron']} <br>
                        <b>المعنى بالعربية:</b> {item['ar']} <br>
                        <small style='color: #888;'>التصنيف: {item['cat']}</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
    with edu_tabs[1]:
        st.subheader("🎵 تحليل نصوص الأغاني الكورية")
        st.write("اختر أغنيتك المفضلة لاستعراض الكلمات وفهم طريقة تركيب الجمل النطقية:")
        
        chosen_song = st.selectbox("اختر الأغنية لاستخراج بياناتها الكودية:", list(KPOP_DATABASE.keys()))
        st.markdown(f"**🎼 الأسطر البرمجية الحالية لأغنية `{chosen_song}`:**")
        
        # استعراض الكلمات بحلقة نظيفة وقصيرة
        for text_line in KPOP_DATABASE[chosen_song]:
            st.code(text_line, language="text")

# ====================================================================
# [التطبيق الثاني]: فاحص الأطعمة الحلال الحركي
# ====================================================================
elif selected_app == "🍳 فاحص الأطعمة الحلال الحركي":
    st.header("🔍 نظام التحقق المنطقي من سلامة الأغذية")
    st.write("يقوم هذا النظام بمطابقة مكونات المنتجات برمجياً مع مصفوفة المحرمات لضمان التزام الطلاب المسلمين بالشريعة الإسلامية.")
    
    food_tabs = st.tabs(["📋 فحص منتج من قاعدة البيانات", "📸 محاكاة الفحص الضوئي وصور الملصقات"])
    
    with food_tabs[0]:
        st.subheader("⚙️ فحص عبر الاختيار المباشر")
        selected_food_key = st.selectbox("اختر اسم الأكلة أو المنتج الكوري المشهور:", list(FOOD_DATABASE.keys()), format_func=lambda x: FOOD_DATABASE[x]["name"])
        
        target_food = FOOD_DATABASE[selected_food_key]
        if target_food["halal"]:
