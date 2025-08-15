# 🍷 Wine Quality Prediction - End-to-End MLOps Project

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![MLOps](https://img.shields.io/badge/MLOps-Pipeline-orange)

## 📋 Overview

This is a comprehensive **End-to-End MLOps project** that predicts wine quality based on various chemical properties. The project implements a complete machine learning pipeline from data ingestion to model deployment with a web interface.

The model uses **ElasticNet Regression** to predict wine quality scores based on 11 chemical features such as acidity, sugar content, pH levels, and alcohol percentage.

## 🏗️ Architecture

The project follows MLOps best practices with a modular pipeline architecture:

```
📦 MLOps Pipeline
├── 🔄 Data Ingestion
├── ✅ Data Validation  
├── 🔧 Data Transformation
├── 🤖 Model Training
├── 📊 Model Evaluation
└── 🚀 Model Deployment
```

## 🚀 Features

- **End-to-End ML Pipeline**: Automated workflow from data ingestion to deployment
- **Web Interface**: User-friendly Flask web application for predictions
- **Docker Support**: Containerized application for easy deployment
- **Modular Design**: Clean, maintainable code structure
- **Configuration Management**: YAML-based configuration system
- **Logging**: Comprehensive logging throughout the pipeline
- **Model Persistence**: Trained models saved using joblib

## 🛠️ Technology Stack

- **Language**: Python 3.10
- **ML Framework**: Scikit-learn
- **Web Framework**: Flask
- **Data Processing**: Pandas, NumPy
- **Containerization**: Docker
- **Configuration**: YAML
- **Model Algorithm**: ElasticNet Regression

## 📁 Project Structure

```
📂 End-to-end/
├── 📱 app.py                    # Flask web application
├── 🐳 Dockerfile               # Docker configuration
├── 🔧 main.py                  # Main pipeline execution
├── ⚙️ params.yaml              # Model parameters
├── 📋 requirements.txt         # Dependencies
├── 🗂️ schema.yaml             # Data schema
├── 🔧 setup.py                 # Package setup
├── 📝 tamplate.py              # Template generator
├── 
├── 📊 artifacts/               # Generated artifacts
│   ├── data_ingestion/         # Raw and processed data
│   ├── data_transformation/    # Train/test splits
│   ├── data_validation/        # Validation reports
│   ├── model_evaluation/       # Model metrics
│   └── model_training/         # Trained models
├── 
├── ⚙️ config/                  # Configuration files
│   └── config.yaml             # Main configuration
├── 
├── 📓 research/                # Jupyter notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   └── 05_model_evaluation.ipynb
├── 
├── 🏗️ src/end_to_end_project/  # Main package
│   ├── components/             # ML components
│   ├── config/                 # Configuration management
│   ├── entity/                 # Data entities
│   ├── pipeline/               # Pipeline stages
│   └── utils/                  # Utility functions
├── 
├── 🎨 static/                  # Web assets (CSS, JS)
└── 📄 templates/               # HTML templates
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10+
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/rajwaAth/MLOps-Project.git
cd MLOps-Project
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the complete pipeline**
```bash
python main.py
```

5. **Start the web application**
```bash
python app.py
```

6. **Access the application**
```
http://localhost:8080
```

### Docker Setup

1. **Build Docker image**
```bash
docker build -t wine-quality-app .
```

2. **Run Docker container**
```bash
docker run -p 8080:8080 wine-quality-app
```

## 🔄 Pipeline Stages

### 1. Data Ingestion
- Downloads wine quality dataset from remote source
- Extracts and stores data in artifacts directory
- **Location**: `src/end_to_end_project/components/data_ingestion.py`

### 2. Data Validation
- Validates data schema and quality
- Checks for missing values and data types
- Generates validation status report
- **Location**: `src/end_to_end_project/components/data_validation.py`

### 3. Data Transformation
- Splits data into training and testing sets
- Applies feature scaling and preprocessing
- **Location**: `src/end_to_end_project/components/data_transformation.py`

### 4. Model Training
- Trains ElasticNet regression model
- Uses hyperparameters from `params.yaml`
- Saves trained model as joblib file
- **Location**: `src/end_to_end_project/components/model_training.py`

### 5. Model Evaluation
- Evaluates model performance on test data
- Generates metrics (RMSE, MAE, R²)
- Saves evaluation results
- **Location**: `src/end_to_end_project/components/model_evaluation.py`

## 🌐 Web Application

The Flask web application provides an intuitive interface for wine quality prediction:

### Features:
- **Input Form**: Enter wine chemical properties
- **Real-time Prediction**: Get instant quality predictions
- **Results Display**: View prediction with input summary

### Input Parameters:
- Fixed Acidity
- Volatile Acidity  
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

## 📊 Model Performance

The ElasticNet regression model is configured with:
- **Alpha**: 0.1 (regularization strength)
- **L1 Ratio**: 0.05 (balance between L1 and L2 regularization)

Performance metrics are automatically generated and stored in `artifacts/model_evaluation/metrics.json`.

## 📝 Configuration

### Main Configuration (`config/config.yaml`)
- Defines paths for all pipeline stages
- Configures data sources and destinations
- Sets up artifact directories

### Model Parameters (`params.yaml`)
- ElasticNet hyperparameters
- Easily adjustable for experimentation

## 🚀 Deployment Options

### Local Deployment
```bash
# Option A: run with default port (8080)
python app.py

# Option B: run on a custom port (e.g., 5000)
# PowerShell
$env:PORT=5000; python app.py
# CMD
set PORT=5000 && python app.py
```

### Docker Deployment
```bash
docker build -t wine-quality-app .
docker run -p 8080:8080 wine-quality-app
```

### Cloud Deployment
The application is containerized and ready for deployment on:
- AWS ECS/EKS
- Google Cloud Run
- Azure Container Instances
- Heroku

## 🔮 Future Enhancements

- [ ] **CI/CD Pipeline**: GitHub Actions for automated testing and deployment
- [ ] **Model Monitoring**: MLflow integration for experiment tracking
- [ ] **API Documentation**: Swagger/OpenAPI documentation
- [ ] **Advanced Models**: Experiment with Random Forest, XGBoost
- [ ] **Feature Engineering**: Advanced feature selection and creation
- [ ] **Real-time Monitoring**: Model performance monitoring in production
- [ ] **A/B Testing**: Framework for model comparison
- [ ] **Database Integration**: Store predictions and user interactions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**mrath**
- Email: thoriq004@gmail.com
- GitHub: [@rajwaAth](https://github.com/rajwaAth)

## 🙏 Acknowledgments

- Dataset source: [Wine Quality Dataset](https://github.com/entbappy/Branching-tutorial/raw/master/winequality-data.zip)
- Inspiration from MLOps best practices and community

---

<div align="center">
  <h3>⭐ If you found this project helpful, please give it a star! ⭐</h3>
</div>