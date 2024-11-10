import cv2
import netron
import requests
import seaborn as sns
import numpy as np
import pickle as pkl

from matplotlib import pyplot as plt

from scipy.stats.mstats import winsorize
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter, laplace

import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, BatchNormalization, ReLU, GlobalAveragePooling1D, Dense, Dropout, MaxPool1D, Flatten
from tensorflow.keras.layers import ReLU, LeakyReLU, PReLU, ELU
from tensorflow.keras.callbacks import LearningRateScheduler, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers.schedules import ExponentialDecay

from PIL import Image, ImageOps
from io import BytesIO

import torch

from transformers import DonutProcessor, VisionEncoderDecoderModel
from transformers import TrOCRProcessor, TFAutoModelForVision2Seq
from transformers import AutoModel, AutoTokenizer

import Levenshtein