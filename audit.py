import streamlit as st

st.title("⚖️ نظام التدقيق الشرعي الآلي")
st.sidebar.header("مراجعة مستندات المرابحة")

# 1. قائمة التحقق الشرعية (Checklist)
st.write("### قائمة التحقق من الامتثال")

ownership = st.checkbox("هل قام المصرف بحيازة السيارة (ملكية تامة) قبل بيعها للعميل؟")
possession_date = st.checkbox("هل تاريخ الحيازة يسبق تاريخ عقد البيع؟")
interest_free = st.checkbox("هل العقد خالٍ من فوائد التأخير الربوية؟")
no_hidden_fees = st.checkbox("هل جميع الرسوم واضحة ومحددة في العقد؟")

# 2. منطق اتخاذ القرار
if st.button("إصدار تقرير التدقيق"):
    all_checked = ownership and possession_date and interest_free and no_hidden_fees
    
    if all_checked:
        st.balloons()
        st.success("✅ العملية متوافقة مع الضوابط الشرعية ويمكن تمريرها للقسم المالي.")
    else:
        st.error("❌ العملية غير متوافقة شرعياً! يرجى مراجعة النقاط المحددة أعلاه.")
        if not ownership: st.write("- مخالفة: لا يمكن بيع ما لا تملك.")
        if not possession_date: st.write("- مخالفة: خلل في ترتيب تواريخ الحيازة والبيع.")
        if not interest_free: st.write("- مخالفة: وجود شروط ربوية ممنوعة.")
        if not no_hidden_fees: st.write("- مخالفة: عدم وضوح الرسوم (غرر).")

st.info("هذه الأداة مصممة لدعم الهيئة الشرعية في فحص عقود المرابحة.")