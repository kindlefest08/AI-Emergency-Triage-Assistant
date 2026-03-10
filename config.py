import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'dataset')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

TRIAGE_MODEL_PATH = os.path.join(MODEL_DIR, 'triage_model.pkl')
DETERIORATION_MODEL_PATH = os.path.join(MODEL_DIR, 'deterioration_model.pkl')
VECTORIZER_PATH = os.path.join(MODEL_DIR, 'vectorizer.pkl')

PATIENT_DATA_PATH = os.path.join(DATA_DIR, 'patient_data.csv')
DETERIORATION_DATA_PATH = os.path.join(DATA_DIR, 'deterioration_data.csv')
