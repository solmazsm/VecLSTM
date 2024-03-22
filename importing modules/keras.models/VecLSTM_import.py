;==========================================
; Title: VecLSTM_import
; Author: anonymous - ECML PKDD 2024 - conference
; Date:   21 March 2024
;==========================================

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.utils import to_categorical
import numpy as np
from sklearn.metrics import classification_report
