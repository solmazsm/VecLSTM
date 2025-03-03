# VecLSTM: Trajectory Prediction and Activity Recognition

VecLSTM is a deep learning framework designed to enhance trajectory prediction and activity recognition tasks. The model integrates advanced techniques, including vectorization, CNN for spatial feature extraction, and LSTM for temporal modeling. It aims to improve predictive accuracy while ensuring computational efficiency, especially for large-scale trajectory data.

This research work has been submitted to IEEE Transactions on Big Data: <a href="https://www.computer.org/digital-library/journals/bd/cfp-ieee-transactions-on-big-data" target="_blank"><em>IEEE Transactions on Big Data, 2025</em></a>

## Overview

Trajectory prediction and activity recognition are critical for understanding dynamic systems such as transportation and urban mobility. VecLSTM addresses scalability and computational challenges in processing high-dimensional trajectory data:

- **Vectorization Layer**: Preprocessing raw GPS data into efficient vector representations.
- **CNN-based Feature Extractor**: Capturing spatial dependencies from the trajectory data.
- **LSTM Network**: Modeling temporal dependencies to capture sequential patterns.
- **Metadata**: Enriched metadata, such as temporal and spatial data, activity labels, and user information, to further improve the model's performance.

VecLSTM achieves state-of-the-art performance on real-world datasets such as GeoLife and HighD, reducing training times by 74.2% and attaining an RMSE of 0.468 and a weighted F1-score of 0.86.

## Datasets

### GeoLife Dataset
The GeoLife dataset contains GPS trajectories from 182 users over three years, providing a comprehensive view of outdoor activities. It includes 1,467,652 samples with 7 distinct labels. This dataset is ideal for training models that predict human activity from trajectory data.

- **Dataset details**: [GeoLife Dataset](https://www.microsoft.com/en-us/research/project/geolife/)
- **Usage**: The GeoLife dataset is used to evaluate the VecLSTM model on large-scale real-world trajectory data.

### HighD Dataset
The HighD dataset is a large-scale, drone-captured vehicle trajectory dataset from German highways. It includes 110,000 vehicle trajectories over 16,500 tracks, recorded at 25 Hz with high accuracy. Each trajectory contains data on position, velocity, acceleration, and lane changes, making it suitable for multi-agent interaction modeling and trajectory prediction.

- **Dataset details**: [HighD Dataset](https://www.highd-dataset.com/)
- **Usage**: The HighD dataset helps us evaluate the model's ability to predict vehicle trajectories on highways.
![Drone HighD](https://levelxdata.com/wp-content/uploads/2023/09/droneHighD-450x300.png) 
## Methodology

VecLSTM follows these key steps:

1. **Data Preprocessing**: Raw GPS data is cleaned, normalized, and prepared for model training.
2. **Vectorization**: A vectorization function transforms trajectory data into a 10x10 grid, storing spatial and temporal features.
3. **CNN and LSTM Model**: A CNN-based model extracts spatial features, and an LSTM captures temporal dependencies from the vectorized data.
4. **Model Training**: The model is trained on the preprocessed and vectorized trajectory data to predict future trajectory points or activity labels.

## Results

VecLSTM was evaluated on two large-scale real-world datasets:

- **GeoLife**: RMSE of 0.468 and a weighted F1-score of 0.86.
- **HighD**: Reduced training time by 74.2%.

### Comparative Evaluation of RMSE, MAE, and MSE Metrics

The bar chart below shows the performance of four distinct models across three error metrics (RMSE, MAE, and MSE), highlighting the effectiveness of VecLSTM in predictive accuracy:



## Installation

To install and run the VecLSTM model, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/solmazsm/VecLSTM.git
    cd VecLSTM
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the model:
    ```bash
    python train_model.py
    ```



## Acknowledgments

- **GeoLife Dataset**: [Microsoft Research](https://www.microsoft.com/en-us/research/project/geolife/)
- **HighD Dataset**: [HighD Dataset](https://www.highd-dataset.com/)
- **VecLSTM**: Developed as part of our research on trajectory prediction and activity recognition.

For any questions, concerns, or comments for improvements, etc, please create an issue on the issues page for this project, or email the authors directly.

