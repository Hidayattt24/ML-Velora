from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pickle
import numpy as np
import os
from typing import Literal, Dict

app = FastAPI(
    title="Maternal Health Risk API",
    description="API untuk klasifikasi risiko kesehatan ibu hamil",
    version="1.0.0"
)

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain Next.js Anda di production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
model_paths = {
    'hr': 'Clr/HRiskClr.sav',
    'ml': 'Clr/MLRiskClr.sav'
}

for path in model_paths.values():
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
        
hrmodel = pickle.load(open(model_paths['hr'], 'rb'))
mlrmodel = pickle.load(open(model_paths['ml'], 'rb'))

class HealthData(BaseModel):
    Age: float = Field(..., ge=13, le=60, description="Usia ibu hamil (13-60 tahun)")
    SystolicBP: float = Field(..., ge=70, le=200, description="Tekanan darah sistolik (70-200 mmHg)")
    DiastolicBP: float = Field(..., ge=40, le=120, description="Tekanan darah diastolik (40-120 mmHg)")
    BS: float = Field(..., ge=1.0, le=20.0, description="Kadar gula darah (1.0-20.0 mmol/L)")
    BodyTemp: float = Field(..., ge=95.0, le=105.0, description="Suhu tubuh (95.0-105.0°F)")
    HeartRate: float = Field(..., ge=40, le=200, description="Detak jantung (40-200 bpm)")

    class Config:
        schema_extra = {
            "example": {
                "Age": 25,
                "SystolicBP": 120,
                "DiastolicBP": 80,
                "BS": 7.0,
                "BodyTemp": 98.6,
                "HeartRate": 80
            }
        }

class HealthRiskResponse(BaseModel):
    risk_level: str
    features: HealthData
    recommendations: Dict

def get_recommendations(risk_level: str) -> dict:
    recommendations = {
        "high risk": {
            "tindakan": [
                "Segera kunjungi dokter atau bidan",
                "Lakukan pemeriksaan menyeluruh",
                "Ikuti petunjuk tenaga medis dengan ketat"
            ],
            "pengawasan": "Perlu pengawasan medis intensif",
            "kontrol": "Kontrol mingguan atau sesuai anjuran dokter"
        },
        "mid risk": {
            "tindakan": [
                "Lakukan pemeriksaan rutin",
                "Jaga pola makan dan istirahat",
                "Pantau tekanan darah secara teratur"
            ],
            "pengawasan": "Perlu pengawasan medis reguler",
            "kontrol": "Kontrol 2 minggu sekali atau sesuai anjuran"
        },
        "low risk": {
            "tindakan": [
                "Lanjutkan pemeriksaan kehamilan rutin",
                "Pertahankan pola hidup sehat",
                "Konsumsi vitamin dan nutrisi yang cukup"
            ],
            "pengawasan": "Pengawasan medis normal",
            "kontrol": "Kontrol bulanan atau sesuai jadwal"
        }
    }
    return recommendations.get(risk_level, {})

@app.get("/")
def read_root():
    return {
        "message": "Selamat datang di API Klasifikasi Risiko Kesehatan Ibu Hamil",
        "version": "1.0.0",
        "endpoints": {
            "/predict": "POST - Prediksi risiko kesehatan",
            "/docs": "GET - Dokumentasi API"
        }
    }

@app.post("/predict", response_model=HealthRiskResponse)
def predict_risk(data: HealthData):
    try:
        # Validasi tambahan untuk tekanan darah
        if data.DiastolicBP >= data.SystolicBP:
            raise HTTPException(
                status_code=400,
                detail="Tekanan darah diastolik harus lebih rendah dari sistolik"
            )

        # Convert input data to numpy array
        features = np.array([[
            data.Age,
            data.SystolicBP,
            data.DiastolicBP,
            data.BS,
            data.BodyTemp,
            data.HeartRate
        ]])
        
        # First prediction to determine if high risk
        first_predict = hrmodel.predict(features)
        
        # Final prediction
        if first_predict[0] == 'a':
            final_predict = mlrmodel.predict(features)[0]
        else:
            final_predict = 'high risk'
            
        # Get recommendations
        recommendations = get_recommendations(final_predict)
            
        return {
            "risk_level": final_predict,
            "features": data,
            "recommendations": recommendations
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error validasi data: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}") 