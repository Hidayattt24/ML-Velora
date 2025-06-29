# 🤱 Maternal Health Risk Classification System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.2-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🎯 **AI-powered maternal health risk assessment system** that helps healthcare professionals identify and classify pregnancy-related health risks using machine learning algorithms.

## ✨ Features

- 🔬 **Smart Classification**: Automatically categorizes maternal health risks into High, Medium, and Low risk levels
- 🚀 **RESTful API**: Fast and scalable API built with FastAPI
- 💻 **Interactive Web Interface**: User-friendly Streamlit dashboard
- 📊 **Real-time Predictions**: Instant risk assessment based on vital health parameters
- 📈 **High Accuracy**: 84% classification accuracy with robust performance metrics
- 🔒 **Input Validation**: Comprehensive parameter validation for reliable results

## 🏥 Health Parameters

The system analyzes the following maternal health indicators:

| Parameter | Range | Unit |
|-----------|-------|------|
| **Age** | 13-60 | years |
| **Systolic BP** | 70-200 | mmHg |
| **Diastolic BP** | 40-120 | mmHg |
| **Blood Sugar** | 1.0-20.0 | mmol/L |
| **Body Temperature** | 95.0-105.0 | °F |
| **Heart Rate** | 40-200 | bpm |

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/maternal-health-risk-classification.git
   cd maternal-health-risk-classification
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### 🔧 Backend API (FastAPI)
```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```
📍 API will be available at: `http://localhost:8000`

#### 🖥️ Frontend Interface (Streamlit)
```bash
streamlit run app.py --server.port 8501
```
📍 Web interface will be available at: `http://localhost:8501`

## 📊 Model Performance

Our machine learning model achieves impressive performance metrics:

| Risk Level | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| **High Risk** | 92% | 91% | 91% | 53 |
| **Low Risk** | 90% | 83% | 86% | 87 |
| **Medium Risk** | 71% | 81% | 76% | 58 |
| **Overall Accuracy** | - | - | **84%** | 198 |

## 🛠️ Usage Examples

### 📡 API Endpoints

#### Health Check
```bash
curl -X GET "http://localhost:8000/"
```

#### Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 25,
    "systolicBP": 120,
    "diastolicBP": 80,
    "BS": 7.5,
    "bodyTemp": 98.6,
    "heartRate": 72
  }'
```

### 💻 Command Line Interface

#### Generate Classification Report
```bash
python ClassificationReport.py
```

#### Predict from CSV File
```bash
python Predictionfromcsv.py path/to/your/data.csv
```

#### Direct Prediction
```bash
python Prediction.py 25 120 80 7.5 98.6 72
```

## 📁 Project Structure

```
maternal-health-risk-classification/
├── 📄 api.py                 # FastAPI backend server
├── 🖥️ app.py                 # Streamlit frontend interface
├── 📊 ClassificationReport.py # Model performance analysis
├── 🔮 Prediction.py          # Direct prediction script
├── 📈 Predictionfromcsv.py   # CSV batch prediction
├── 🧠 Train.py               # Model training script
├── 📋 requirements.txt       # Python dependencies
├── 🤖 Clf/                   # Trained model files
├── 📊 Dataset/               # Training and testing data
├── 🧪 Testsubject/           # Sample test cases
└── 📖 README.md              # This file
```

## 🧪 Test Cases

Sample test subjects are provided in the `Testsubject/` directory:

| Name | Age | Systolic BP | Diastolic BP | Blood Sugar | Body Temp | Heart Rate | Risk Level |
|------|-----|-------------|--------------|-------------|-----------|------------|------------|
| Lidia | 48 | 120 | 80 | 11.0 | 98.0 | 88 | **High Risk** |
| Georgia | 20 | 110 | 60 | 7.0 | 100.0 | 70 | **Medium Risk** |
| Nikoleta | 17 | 110 | 75 | 13.0 | 101.0 | 76 | **High Risk** |
| Eirini | 23 | 100 | 85 | 7.5 | 98.0 | 66 | **Low Risk** |
| Aggeliki | 19 | 120 | 90 | 6.8 | 98.0 | 60 | **Medium Risk** |

## 📚 API Documentation

Interactive API documentation is available when running the FastAPI server:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔧 Development

### Training the Model
```bash
python Train.py
```

The trained model will be saved in the `Clf/` directory.

### Requirements
- Python 3.10+
- scikit-learn==1.0.2
- numpy==1.22.0
- FastAPI
- Streamlit
- uvicorn
- pandas

See `requirements.txt` for the complete list of dependencies.

## 📊 Dataset

The training data is sourced from a Kaggle dataset focusing on maternal health risks during pregnancy.

**Source**: [Maternal Health Risk Data](https://www.kaggle.com/csafrit2/maternal-health-risk-data)

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kaggle community for providing the maternal health dataset
- scikit-learn team for the excellent machine learning library
- FastAPI and Streamlit teams for the amazing frameworks

## 📞 Support

If you have any questions or need help, please:

- 🐛 [Open an issue](https://github.com/yourusername/maternal-health-risk-classification/issues)
- 💬 [Start a discussion](https://github.com/yourusername/maternal-health-risk-classification/discussions)
- 📧 Contact the maintainers

---

<div align="center">
  <p>Made with ❤️ for maternal healthcare</p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>