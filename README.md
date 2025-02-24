# VecLSTM
This folder contains all the necessary implementations required to replicate the studies presented at The Web Conference 2025.
# Dataset
The GeoLife dataset, encompassing GPS trajectories from 182 users over three years, offers a comprehensive view of outdoor activities. We utilized the Geolife GPS trajectory dataset, containing 1,467,652 samples with 7 distinct labels. The neural network architecture, designed for this dataset, incorporated LSTM layers followed by a Dense layer, boasting a total of 71,357 trainable parameters.

Additionally, we leverage the HighD dataset, a large-scale, drone-captured vehicle trajectory dataset from German highways. It includes 110,000 vehicle trajectories over 16,500 tracks, recorded at 25 Hz with high accuracy. Each trajectory contains data on position, velocity, acceleration, and lane changes, making it ideal for modeling multi-agent interactions and trajectory predictions. This dataset provides valuable insights into complex spatial-temporal dependencies, which are critical for advancing our models.


<h3>Download Datasets</h3>
    <ul>
        <li>The GeoLife dataset can be downloaded <a href="https://www.microsoft.com/en-us/download/details.aspx?id=52367" target="_blank">here</a>.</li>
        <li>The HighD dataset is available <a href="https://levelxdata.com/highd-dataset/" target="_blank">here</a>.</li>
    </ul>
    
# Vectorization
Defined a vectorization_function_VecLSTM to normalize and vectorize the latitude, longitude, and altitude data into a 10x10 grid.

# Database Connection
Established a connection to a MySQL database to store and retrieve vectorized data.

# Metadata Creation
Created a metadata column in the DataFrame by combining existing columns (time, latitude, longitude, altitude, label, and user).

# Training LSTM Model without Vectorization:

Built and compiled an LSTM model with two LSTM layers and a Dense layer for classification.
Measured and recorded the training time without vectorization.
Trained the model on the resampled training data.
Evaluated the model's performance on the test set using confusion matrix, classification report, and weighted F1-score.

# Vectorization Process
Measured the time taken for vectorization.
Vectorized each trajectory and stored the vectorized data into the MySQL database.

# CNN Model Integration
CNN Model: Convolutional Neural Network (CNN) model (cnn_model) for extracting spatial features from trajectory data.
Integration: Combined the outputs of both LSTM and CNN models using the concatenate layer.
Training: Trained the combined model (model) on the integrated data from both LSTM and CNN.

# Evaluation and Comparison
Performance Evaluation: Evaluated the hybrid model on the test set, calculated RMSE, MAE, and MSE.
compare training times between LSTM-only and combined LSTM + CNN models.

# Evaluation Implementation
The implementation and instructions to run evaluationcan be found <a href="https://anonymous.4open.science/r/VecLSTM-C91B">here</a>.

 Performed several steps to preprocess trajectory data, train an LSTM model, and compare the performance with and without vectorization.
 Performed several steps to preprocess trajectory data, train an Hybrid model, and compare the performance with and without vectorization.
 Compared the training times with and without vectorization.
 Retrieved and displayed the vectorized data from the database.

 This entire process demonstrates the steps taken to preprocess data, apply machine learning models, handle data storage and retrieval in a database, and compare the efficiency of different approaches.

For any questions, concerns, or comments for improvements, etc, please create an issue on the issues page for this project, or email the authors directly.
