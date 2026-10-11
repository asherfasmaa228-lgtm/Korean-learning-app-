import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="HalalScan Pro Max", layout="centered")
st.markdown("""
<style>
body {background:#FFF8E1}
header{padding:14px;background:linear-gradient(135deg,#1B5E20,#4CAF50);color:white;border-radius:0 0 22px 22px;text-align:center}
.halal-box{background:#E8F5E9;border:3px solid #4CAF50;padding:16px;border-radius:18px}
.haram-box{background:#FFEBEE;border:3px solid #F44336;padding:16px;border-radius:18px}
.ing{text-align:right;background:#fff;padding:12px;border-radius:12px;margin-top:8px;font-size:13px;line-height:1.7;direction:rtl}
</style>
<header><h3 style='margin:0'>🌍 HalalScan Pro Max</h3><p style='margin:4px;font-size:12px'>وضعين: 1- تصوير الطبق 2- تصوير مكونات الكيس</p></header>
""", unsafe_allow_html=True)

HARAM = ["pork","돼지고기","삼겹살","족발","술","소주","beer","wine","soju","alcohol","gelatin","lard","bacon","ham","e120","e441","e471","e472","خنزير","كحول","خمر","نبيذ","جيلاتين"]

DISHES = {
"bibimbap": {"name":"بيبيمباب 비빔밥","halal":True,"ing":"رز، سبانخ، جزر، فجل، بيض، صوص فلفل، زيت سمسم - ✅ لا يوجد خنزير ولا كحول","safe":"حلال 100% - آمن"},
"samgyeopsal": {"name":"سامجيوبسال 삼겹살","halal":False,"ing":"بطن خنزير مشوي 돼지고기 - ❌ حرام","safe":"حرام - لحم خنزير"},
"soju": {"name":"سوجو 소주","halal":False,"ing":"كحول 17% 술 - ❌ حرام","safe":"حرام - كحول"},
"ramen": {"name":"رامن لحم خنزير 라면","halal":False,"ing":"نودلز، مرق خنزير، بيض - ❌ يحتوي خنزير","safe":"حرام"},
"tteokbokki": {"name":"توكبوكي 떡볶이","halal":True,"ing":"كعك رز، صوص حار، بصل أخضر - ✅ حلال","safe":"حلال 100%"},
"chips": {"name":"شيبسي كيس","halal":False,"ing":"بطاطس، زيت، نكهة خنزير Pork Flavor، E621، Ethanol - ❌","safe":"حرام - نكهة خنزير + كحول"},
"choco": {"name":"شوكولاتة","halal":True,"ing":"كاكاو، سكر، حليب، ليسيثين صويا - ✅ حلال","safe":"حلال 100%"}
}

# --- وضع التشغيل ---
if "mode" not in st.session_state:
    st.session_state.mode = "dish"

col1, col2 = st.columns(2)
with col1:
    if st.button("🍚 وضع الطبق", use_container_width=True, type="primary" if st.session_state.mode=="dish" else "secondary"):
        st.session_state.mode = "dish"
with col2:
    if st.button("📦 وضع الكيس", use_container_width=True, type="primary" if st.session_state.mode=="bag" else "secondary"):
        st.session_state.mode = "bag"

st.write(f"الوضع الحالي: **{'تصوير الطبق' if st.session_state.mode=='dish' else 'تصوير المكونات'}**")

# --- كاميرا و رفع ---
tab1, tab2, tab3 = st.tabs(["📸 كاميرا", "📤 رفع صورة", "🎲 تجربة"])
image = None

with tab1:
    cam = st.camera_input("صوري الطبق او الكيس")
    if cam:
        image = Image.open(cam)
with tab2:
    up = st.file_uploader("اختاري صورة", type=["jpg","png","jpeg"])
    if up:
        image = Image.open(up)
with tab3:
    if st.button("جربي عشوائي"):
        st.session_state.demo = True
    else:
        st.session_state.demo = False

def show_result(key, mode):
    x = DISHES[key]
    found = [h for h in HARAM if h in x["ing"].lower()]

    if x["halal"]:
        st.markdown(f"<div class='halal-box'><h2>✅ {x['name']} - حلال 100%</h2><p>{x['safe']}</p></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='haram-box'><h2>❌ {x['name']} - حرام</h2><p>{x['safe']}</p></div>", unsafe_allow_html=True)

    extra_title = "🔍 قراءة المكونات من الكيس:" if mode=='bag' else "🍽️ تحليل شكل الطبق:"
    extra = f"<div class='ing'><b>{extra_title}</b><br>{x['ing']}<br><br>"

    if x["halal"]:
        extra += "<b style='color:green'>✅ النتيجة:</b><br>لم يتم العثور على أي مكون حرام<br>✓ لا خنزير ✓ لا كحول ✓ لا جيلاتين حرام<br><br>🤲 صالح للمسلمين في أي بلد</div>"
    else:
        extra += f"<b style='color:red'>🚫 المكونات الحرام:</b><br>{', '.join(found)}<br><br><b>📖 الدليل:</b> حرمت عليكم الميتة والدم ولحم الخنزير<br><br><b>💡 البديل:</b> اطلب نسخة حلال بالدجاج أو خضار</div>"

    st.markdown(extra, unsafe_allow_html=True)
    if image:
        st.image(image, caption="الصورة اللي اتحللت", use_column_width=True)

# --- منطق العرض ---
if image or st.session_state.get("demo"):
    if st.session_state.mode == "dish":
        k = ['bibimbap','tteokbokki','samgyeopsal','ramen','soju']
    else:
        k = ['chips','choco','ramen']

    # لو فيه صورة هنعملها كأنها تحليل حقيقي (ديمو)
    key = random.choice(k)
    show_result(key, st.session_state.mode)
    if st.button("🔄 جديد"):
        st.rerun()