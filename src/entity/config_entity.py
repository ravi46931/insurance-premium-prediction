import os
from src.constants import *
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    DATA_INGESTION_ARTIFACT_DIR = os.path.join (ARTIFACT_DIR, DATA_INGESTION_ARTIFACT_DIR)
    DATA_FILE_PATH = os.path.join(DATA_INGESTION_ARTIFACT_DIR, DATA_FILE_NAME)

@dataclass
class DataTransformationConfig:
    DATA_TRANSFORMATION_ARTIFACT_DIR = os.path.join (ARTIFACT_DIR, DATA_TRANSFORMATION_ARTIFACT_DIR)
    TRAIN_TRANSFORM_FILE_PATH = os.path.join(DATA_TRANSFORMATION_ARTIFACT_DIR, TRAIN_TRANSFORM_FILE_NAME)
    TEST_TRANSFORM_FILE_PATH = os.path.join(DATA_TRANSFORMATION_ARTIFACT_DIR, TEST_TRANSFORM_FILE_NAME)
    PREPROCESSOR_FILE_PATH = os.path.join(DATA_TRANSFORMATION_ARTIFACT_DIR, PREPROCESSOR_FILE_NAME)

@dataclass
class ModelTrainerConfig:
    MODEL_TRAINER_ARTIFACT_DIR = os.path.join (ARTIFACT_DIR, MODEL_TRAINER_ARTIFACT_DIR)
    MODELS_DIR_PATH = os.path.join (MODEL_TRAINER_ARTIFACT_DIR, MODELS_DIR)
    TOP_MODELS_NAME_FILE_PATH = os.path.join (MODEL_TRAINER_ARTIFACT_DIR, TOP_MODELS_NAME_FILE_NAME)

@dataclass
class ModelEvaluationConfig:
    MODEL_EVALUATION_ARTIFACT_DIR = os.path.join (ARTIFACT_DIR, MODEL_EVALUATION_ARTIFACT_DIR)
    TRAIN_METRICS_FILE_PATH = os.path.join(MODEL_EVALUATION_ARTIFACT_DIR, TRAIN_METRICS)
    TEST_METRICS_FILE_PATH = os.path.join(MODEL_EVALUATION_ARTIFACT_DIR, TEST_METRICS)
    BEST_MODEL_METRICS_FILE_PATH = os.path.join(MODEL_EVALUATION_ARTIFACT_DIR, BEST_MODEL_METRICS)
    BEST_MODEL_FILE_PATH = os.path.join(MODEL_EVALUATION_ARTIFACT_DIR, BEST_MODEL)


