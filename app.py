import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Maternal Health Risk Classification",
    page_icon="👶",
    layout="centered"
)

st.title("Maternal Health Risk Classification")
st.write("Silakan jawab pertanyaan berikut untuk mengetahui tingkat risiko kesehatan Anda selama kehamilan.")

# Create form
with st.form("health_form"):
    st.write("### Informasi Umum")
    
    # Age input with categories
    age_category = st.radio(
        "1. Berapakah usia Anda?",
        ["Di bawah 20 tahun", "20-25 tahun", "26-30 tahun", "31-35 tahun", "36-40 tahun", "Di atas 40 tahun"]
    )
    
    st.write("### Tekanan Darah")
    
    # Blood pressure categories
    bp_category = st.radio(
        "2. Bagaimana kondisi tekanan darah Anda? (Berdasarkan pemeriksaan terakhir)",
        [
            "Normal (Systolic: 90-120, Diastolic: 60-80)",
            "Prehipertensi (Systolic: 120-140, Diastolic: 80-90)",
            "Hipertensi (Systolic: >140, Diastolic: >90)",
            "Rendah (Systolic: <90, Diastolic: <60)"
        ]
    )
    
    st.write("### Gula Darah")
    
    # Blood sugar categories
    bs_category = st.radio(
        "3. Bagaimana level gula darah Anda?",
        [
            "Normal (4.0-7.0 mmol/L)",
            "Sedikit Tinggi (7.1-11.0 mmol/L)",
            "Tinggi (>11.0 mmol/L)",
            "Rendah (<4.0 mmol/L)"
        ]
    )
    
    st.write("### Suhu Tubuh")
    
    # Body temperature categories
    temp_category = st.radio(
        "4. Bagaimana suhu tubuh Anda?",
        [
            "Normal (97.8-99.0°F / 36.5-37.2°C)",
            "Sedikit Tinggi (99.1-100.4°F / 37.3-38.0°C)",
            "Tinggi (>100.4°F / >38.0°C)",
            "Rendah (<97.8°F / <36.5°C)"
        ]
    )
    
    st.write("### Detak Jantung")
    
    # Heart rate categories
    hr_category = st.radio(
        "5. Bagaimana detak jantung Anda?",
        [
            "Normal (60-100 bpm)",
            "Tinggi (>100 bpm)",
            "Rendah (<60 bpm)"
        ]
    )
    
    submitted = st.form_submit_button("Prediksi Tingkat Risiko")

# Convert categorical answers to numerical values
if submitted:
    # Age conversion
    age_map = {
        "Di bawah 20 tahun": 18,
        "20-25 tahun": 23,
        "26-30 tahun": 28,
        "31-35 tahun": 33,
        "36-40 tahun": 38,
        "Di atas 40 tahun": 42
    }
    age = age_map[age_category]
    
    # Blood pressure conversion
    if bp_category == "Normal (Systolic: 90-120, Diastolic: 60-80)":
        systolic_bp = 115
        diastolic_bp = 75
    elif bp_category == "Prehipertensi (Systolic: 120-140, Diastolic: 80-90)":
        systolic_bp = 130
        diastolic_bp = 85
    elif bp_category == "Hipertensi (Systolic: >140, Diastolic: >90)":
        systolic_bp = 150
        diastolic_bp = 95
    else:  # Low
        systolic_bp = 85
        diastolic_bp = 55
    
    # Blood sugar conversion
    if bs_category == "Normal (4.0-7.0 mmol/L)":
        bs = 5.5
    elif bs_category == "Sedikit Tinggi (7.1-11.0 mmol/L)":
        bs = 9.0
    elif bs_category == "Tinggi (>11.0 mmol/L)":
        bs = 12.0
    else:  # Low
        bs = 3.5
    
    # Temperature conversion
    if temp_category == "Normal (97.8-99.0°F / 36.5-37.2°C)":
        body_temp = 98.6
    elif temp_category == "Sedikit Tinggi (99.1-100.4°F / 37.3-38.0°C)":
        body_temp = 99.5
    elif temp_category == "Tinggi (>100.4°F / >38.0°C)":
        body_temp = 101.0
    else:  # Low
        body_temp = 97.0
    
    # Heart rate conversion
    if hr_category == "Normal (60-100 bpm)":
        heart_rate = 80
    elif hr_category == "Tinggi (>100 bpm)":
        heart_rate = 110
    else:  # Low
        heart_rate = 55
    
    # Prepare data for API
    data = {
        "Age": age,
        "SystolicBP": systolic_bp,
        "DiastolicBP": diastolic_bp,
        "BS": bs,
        "BodyTemp": body_temp,
        "HeartRate": heart_rate
    }
    
    try:
        # Make prediction request to API
        response = requests.post("http://localhost:8000/predict", json=data)
        result = response.json()
        
        # Display results
        st.write("---")
        st.subheader("Hasil Prediksi")
        
        risk_level = result["risk_level"]
        
        if risk_level == "high risk":
            st.error("Tingkat Risiko: RISIKO TINGGI")
            st.warning("""
            ⚠️ Perhatian:
            - Segera konsultasikan kondisi Anda dengan dokter atau bidan
            - Lakukan pemeriksaan kesehatan secara menyeluruh
            - Ikuti semua saran dan petunjuk dari tenaga medis
            """)
        elif risk_level == "mid risk":
            st.warning("Tingkat Risiko: RISIKO MENENGAH")
            st.info("""
            ℹ️ Rekomendasi:
            - Lakukan pemeriksaan rutin sesuai jadwal
            - Perhatikan pola makan dan istirahat
            - Konsultasikan setiap perubahan kondisi dengan tenaga medis
            """)
        else:
            st.success("Tingkat Risiko: RISIKO RENDAH")
            st.info("""
            ✅ Rekomendasi:
            - Lanjutkan pemeriksaan kehamilan secara rutin
            - Pertahankan pola hidup sehat
            - Tetap waspada terhadap perubahan kondisi
            """)
            
        # Display input parameters in a more readable format
        st.write("---")
        st.subheader("Ringkasan Kondisi")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("🔹 Usia:", age_category)
            st.write("🔹 Tekanan Darah:", bp_category)
            st.write("🔹 Gula Darah:", bs_category)
            
        with col2:
            st.write("🔹 Suhu Tubuh:", temp_category)
            st.write("🔹 Detak Jantung:", hr_category)
            
    except Exception as e:
        st.error(f"Terjadi kesalahan: {str(e)}")

# Add information about the parameters
with st.expander("ℹ️ Informasi Parameter Kesehatan"):
    st.write("""
    ### Penjelasan Parameter:
    
    1. **Tekanan Darah**
       - Normal: 90-120/60-80 mmHg
       - Prehipertensi: 120-140/80-90 mmHg
       - Hipertensi: >140/>90 mmHg
    
    2. **Gula Darah**
       - Normal: 4.0-7.0 mmol/L
       - Sedikit Tinggi: 7.1-11.0 mmol/L
       - Tinggi: >11.0 mmol/L
    
    3. **Suhu Tubuh**
       - Normal: 36.5-37.2°C (97.8-99.0°F)
       - Demam Ringan: 37.3-38.0°C (99.1-100.4°F)
       - Demam: >38.0°C (>100.4°F)
    
    4. **Detak Jantung**
       - Normal: 60-100 detak per menit
       - Tinggi: >100 detak per menit
       - Rendah: <60 detak per menit
    """)

# Add footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ untuk kesehatan ibu hamil")
st.markdown("""
⚠️ **Perhatian**: Aplikasi ini hanya alat bantu dan tidak menggantikan pemeriksaan medis profesional.
Selalu konsultasikan kondisi Anda dengan dokter atau bidan yang menangani kehamilan Anda.
""") 