import streamlit as st
import datetime
import random
import time

# ==========================================
# 1. إعدادات المنصة الموحدة والهوية البصرية
# ==========================================
st.set_page_config(
    page_title="Asmaa Black Platform",
    page_icon="🚀",
    layout="centered"
)

# تطبيق تصميم CSS احترافي وموحد للمنصة
st.markdown("""
<style>
    .main-title { font-size:32px; font-weight:bold; text-align:center; color:#1E1E1E; margin-bottom:10px; }
    .subtitle { font-size:18px; text-align:center; color:#555555; margin-bottom:30px; }
    .halal-box { background-color:#E8F5E9; border: 2px solid #4CAF50; border-radius:12px; padding:20px; text-align:center; margin-bottom:15px; }
    .haram-box { background-color:#FFEBEE; border: 2px solid #F44336; border-radius:12px; padding:20px; text-align:center; margin-bottom:15px; }
    .card { background-color:#F8F9FA; border-radius:10px; padding:15px; margin-bottom:10px; border-left: 5px solid #007BFF; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌟 Asmaa Black Platform 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>الأكاديمية والمنظومة التعليمية المتكاملة للطلاب الدوليين في كوريا</div>", unsafe_allow_html=True)

# ==========================================
# 2. قواعد البيانات المنظمة (Database Simulation)
# ==========================================
# قاعدة بيانات الأطعمة والمكونات
HARAM_INGREDIENTS = ['pork', 'pig', '돼지고기', '삼겹살', '족발', '술', 'beer', 'wine', 'soju', 'alcohol', 'gelatin', 'lard', 'bacon', 'ham', 'e120', 'e441', 'e471', 'e472']

FOOD_DATABASE = {
    "bibimbap": {"name": "بيبيومباب (بيمبامب)", "halal": True, "ing": "أرز، خضروات، بيض، زيت سمسم", "safe": "آمن - تأكد فقط من عدم إضافة لحم غير حلال."},
    "samgyeopsal": {"name": "سامغيوبسال (شرائح لحم الخنزير)", "halal": False, "ing": "لحم خنزير مشوي", "safe": "حرام - يحتوي على لحم خنزير صريح."},
    "soju": {"name": "سوجو (مشروب كوري)", "halal": False, "ing": "كحول مخمر 17%", "safe": "حرام - مشروب كحولي مسكر."},
    "ramen": {"name": "راميون (نودلز كورية)", "halal": False, "ing": "نودلز، مرق خنزير، بهارات", "safe": "احذر - معظم الأنواع التقليدية تحتوي على مستخلصات الخنزير."},
    "tteokbokki": {"name": "توكبوكي (كعك الأرز الحار)", "halal": True, "ing": "كعك أرز، صوص حار، كعك سمك", "safe": "آمن - طالما أن صوص كعك السمك لا يحتوي على نكهات لحوم."},
    "chips": {"name": "شيبسي كوري", "halal": False, "ing": "بطاطس، زيت، نكهة خنزير، محسّن طعم E621", "safe": "حرام - يحتوي على نكهة دهن الخنزير."},
    "choco": {"name": "شوكولاتة كورية", "halal": True, "ing": "كاكاو، سكر، حليب، جيلاتين نباتي", "safe": "آمن حلال 100%."}
}

# قاعدة بيانات الأغاني الكورية المشهورة لتعلم الكلمات
SONGS_DATABASE = {
    "Dynamite (BTS)": ["'Cause I-I-I'm in the stars tonight", "So watch me bring the fire and set the night alight", "Shining through the city with a little funk and soul", "Light it up like dynamite, whoa oh oh"],
    "Butter (BTS)": ["Smooth like butter, like a criminal undercover", "Gon' pop like trouble breaking into your heart like that", "Cool shade, stunner, yeah, I owe it all to my mother", "Hot like summer, yeah, I'm making you sweat like that"],
    "Spring Day (BTS)": ["보고 싶다 (Missing you)", "이렇게 말하니까 더 보고 싶다 (Saying this makes me miss you more)", "너희 사진을 (Looking at your photo)", "보고 있어도 보고 싶다 (Even when looking, I miss you)"],
    "DDU-DU DDU-DU (BLACKPINK)": ["착한 얼굴에 그렇지 못한 태도 (A kind face with an unkind attitude)", "가녀린 몸매 속 가려진 Volume은 두배로 (Twice the volume hidden in a slender body)", "거침없이 직진 굳이 보진 않지 눈치 (Straight forward without hesitation)"],
    "Kill This Love (BLACKPINK)": ["천사 같은 Hi 끝엔 악마 같은 Bye (After a sweet hello, there's always a bitter good-bye)", "매번 미칠듯한 High 뒤엔 뱉어야 하는 Price (Every crazy high has a price you have to pay)"]
}

# قاعدة بيانات المفردات الكورية المنظمة في مصفوفة ذكية لتقليل حجم الكود
KOREAN_VOCABULARY = [
    {"kor": "안녕하세요", "pron": "Annyeonghaseyo", "ar": "مرحباً", "type": "👋 التحيات"},
    {"kor": "감사합니다", "pron": "Gamsahabnida", "ar": "شكراً لك", "type": "👋 التحيات"},
    {"kor": "사랑해요", "pron": "Saranghaeyo", "ar": "أحبك", "type": "👋 التحيات"},
    {"kor": "밥", "pron": "Bap", "ar": "أرز / طعام", "type": "🍎 الأطعمة والمشروبات"},
    {"kor": "물", "pron": "Mul", "ar": "ماء", "type": "🍎 الأطعمة والمشروبات"},
    {"kor": "고기", "pron": "Gogi", "ar": "لحم", "type": "🍎 الأطعمة والمشروبات"},
    {"kor": "학교", "pron": "Hakgyo", "ar": "مدرسة", "type": "🏫 الحياة اليومية"},
    {"kor": "친구", "pron": "Chingu", "ar": "صديق", "type": "🏫 الحياة اليومية"},
    {"kor": "한국", "pron": "Hanguk", "ar": "كوريا", "type": "🏫 الحياة اليومية"}
]

# ==========================================
# 3. القائمة الجانبية الاحترافية للتنقل (Sidebar Router)
# ==========================================
with st.sidebar:
    st.image("https://unsplash.com", caption="المطور: أسماء", use_container_width=True)
    st.markdown("### 🛠️ لوحة التحكم بالمنصة")
    app_mode = st.selectbox(
        "اختر التطبيق الذي تود تشغيله:",
        ["1. المنصة التعليمية (اللغة والأغاني)", "2. فاحص الأطعمة (حلال وحرام)", "3. منظم الوقت الذكي (بريك)"]
    )
    st.divider()
    st.info("تم التطوير برؤية برمجية احترافية لخدمة طلاب منحة GKS.")

# ==========================================
# 应用 1: المنصة التعليمية (اللغة والأغاني)
# ==========================================
if app_mode == "1. المنصة التعليمية (اللغة والأغاني)":
    st.header("📚 الأكاديمية الكورية لتعليم اللغات والفنون")
    
    edu_tabs = st.tabs(["🔤 قاموس الكلمات الذكي", "🎵 تعلم عبر الكيبوب (K-Pop)"])
    
    with edu_tabs[0]:
        st.subheader("💡 قاموس الكلمات التفاعلي")
        st.write("تم تنظيم الكلمات برمجياً ضمن فئات لتسهيل الحفظ:")
        
        # فلترة الكلمات باستخدام حلقة تكرارية احترافية ونظيفة بدلاً من تكرار الأسطر
        categories = ["الكل", "👋 التحيات", "🍎 الأطعمة والمشروبات", "🏫 الحياة اليومية"]
        selected_cat = st.selectbox("تصفية حسب الفئة:", categories)
        
        for item in KOREAN_VOCABULARY:
            if selected_cat == "الكل" or item["type"] == selected_cat:
                with st.container():
                    st.markdown(f"""
                    <div class='card'>
                        <h4 style='margin:0; color:#007BFF;'>{item['kor']} ({item['pron']})</h4>
                        <p style='margin:5px 0 0 0; color:#333;'><b>الترجمة:</b> {item['ar']} | <span style='color:#777;'>{item['type']}</span></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
    with edu_tabs[1]:
        st.subheader("🎵 ركن الكيبوب وتعلم النطق")
        st.write("اختر أغنيتك المفضلة لاستعراض كلماتها البرمجية المأخوذة من قاعدة البيانات:")
        
        selected_song = st.selectbox("اختر الأغنية:", list(SONGS_DATABASE.keys()))
        st.markdown(f"**🎼 الأسطر الشعرية والكلمات لأغنية `{selected_song}`:**")
        
        # استعراض الكلمات بحلقة تكرارية احترافية ومبسطة جداً
        for line in SONGS_DATABASE[selected_song]:
            st.code(line, language="text")

# ==========================================
# 应用 2: فاحص الأطعمة (حلال وحرام)
# ==========================================
elif app_mode == "2. فاحص الأطعمة (حلال وحرام)":
    st.header("🍳 نظام فحص الأطعمة الذكي للمغتربين")
    st.write("هذا النظام يطابق المكونات برمجياً مع قائمة المحرمات لضمان سلامة الأطعمة في شرق آسيا.")
    
    food_tabs = st.tabs(["🔍 فحص منتج من الداتا", "📸 محاكاة فحص صورة منتج"])
    
    with food_tabs[0]:
        st.subheader("📋 اختر منتجاً من القائمة الجاهزة")
        product_key = st.selectbox("اختر اسم الأكلة أو المنتج الكوري:", list(FOOD_DATABASE.keys()), format_func=lambda x: FOOD_DATABASE[x]["name"])
        
        prod_data = FOOD_DATABASE[product_key]
        if prod_data["halal"]:
            st.markdown(f"""<div class='halal-box'><h3>✅ حلال (Halal)</h3><p><b>المنتج:</b> {prod_data['name']}</p><p><b>المكونات:</b> {prod_data['ing']}</p><p><b>ملاحظة السلامة:</b> {prod_data['safe']}</p></div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class='haram-box'><h3>❌ غير حلال (Contains Haram)</h3><p><b>المنتج:</b> {prod_data['name']}</p><p><b>المكونات:</b> {prod_data['ing']}</p><p><b>ملاحظة السلامة:</b> {prod_data['safe']}</p></div>""", unsafe_allow_html=True)

    with food_tabs[1]:
        st.subheader("📷 فحص ذكي عبر الكاميرا والـ OCR")
        st.write("التقط صورة للمكونات المكتوبة على ظهر المنتج بالكورية، وسيقوم النظام برمجياً بمحاكاة استخراج الكلمات ومطابقتها:")
        
        uploaded_image = st.camera_input("التقط صورة لملصق المكونات الغذائية")
        
        if uploaded_image:
            with st.spinner("جاري معالجة الصورة واستخراج النصوص برمجياً عبر الـ OCR..."):
                time.sleep(1.5) # محاكاة وقت المعالجة التقنية الحقيقية
                
                # فحص محاكي ذكي حقيقي (مطابقة كلمات عشوائية مستخرجة من المكونات الحرام للتأكيد)
                simulated_ocr_text = ["돼지고기", "물", "설탕", "gelatin"]
                found_haram = [ing for ing in simulated_ocr_text if ing in HARAM_INGREDIENTS]
                
                st.success("تم مسح الصورة بنجاح!")
                st.write("**النصوص البرمجية المكتشفة في الصورة:** `돼지고기, 물, 설탕, gelatin`")
                
                if found_haram:
                    st.markdown(f"""<div class='haram-box'><h3>⚠️ تحذير: المنتج غير حلال!</h3><p>تم العثور على مكونات محرمة مستخرجة من الصورة: {', '.join(found_haram)}</p></div>""", unsafe_allow_html=True)
                else:
                    st.markdown("""<div class='halal-box'><h3>✅ المنتج حلال ومطابق للمواصفات</h3><p>لم يتم العثور على أي مكونات مشبوهة في النصوص المقروءة.</p></div>""", unsafe_allow_html=True)

# ==========================================
# 应用 3: منظم الوقت الذكي (بريك)
# ==========================================
elif app_mode == "3. منظم الوقت الذكي (بريك)":
    st.header("⏱️ مؤقت بريك الذكي لإدارة الوقت (Pomodoro)")
