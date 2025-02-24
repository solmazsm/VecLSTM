# VecLSTM
<p>This folder contains all the necessary implementations required to replicate the studies presented at <a href="https://www.computer.org/digital-library/journals/bd/cfp-ieee-transactions-on-big-data" target="_blank"><em>IEEE Transactions on Big Data, 2025</em></a>. 

# Dataset
The GeoLife dataset, encompassing GPS trajectories from 182 users over three years, offers a comprehensive view of outdoor activities. We utilized the Geolife GPS trajectory dataset, containing 1,467,652 samples with 7 distinct labels. The neural network architecture, designed for this dataset, incorporated LSTM layers followed by a Dense layer, boasting a total of 71,357 trainable parameters.

Additionally, we leverage the HighD dataset, a large-scale, drone-captured vehicle trajectory dataset from German highways. It includes 110,000 vehicle trajectories over 16,500 tracks, recorded at 25 Hz with high accuracy. Each trajectory contains data on position, velocity, acceleration, and lane changes, making it ideal for modeling multi-agent interactions and trajectory predictions. This dataset provides valuable insights into complex spatial-temporal dependencies, which are critical for advancing our models.


<h3>Download Datasets</h3>
    <ul>
        <li>The GeoLife dataset can be downloaded <a href="https://www.microsoft.com/en-us/download/details.aspx?id=52367" target="_blank">here</a>.</li>
        <li>The HighD dataset is available <a href="https://levelxdata.com/highd-dataset/" target="_blank">here</a>.</li>
    </ul>
    
<h2>Vectorization</h2>
    <p>The <strong>vectorization_function_VecLSTM</strong> was developed to normalize and vectorize the latitude, longitude, and altitude data into a structured 10x10 grid. This transformation optimizes the input data for neural network processing.</p>
    
    <h2>Database Connection</h2>
    <p>A MySQL database connection was established to store and retrieve the vectorized data efficiently. This approach ensures that the trajectory data is both easily accessible and manageable, particularly for large datasets.</p>

## Training LSTM Model without Vectorization:

Built and compiled an LSTM model with two LSTM layers and a Dense layer for classification.
Measured and recorded the training time without vectorization.
Trained the model on the resampled training data.
Evaluated the model's performance on the test set using confusion matrix, classification report, and weighted F1-score.

## Vectorization Process
Measured the time taken for vectorization.
Vectorized each trajectory and stored the vectorized data into the MySQL database.

## CNN Model Integration
CNN Model: Convolutional Neural Network (CNN) model (cnn_model) for extracting spatial features from trajectory data.
Integration: Combined the outputs of both LSTM and CNN models using the concatenate layer.
Training: Trained the combined model (model) on the integrated data from both LSTM and CNN.

## Evaluation and Comparison
Performance Evaluation: Evaluated the hybrid model on the test set, calculated RMSE, MAE, and MSE.
compare training times between LSTM-only and combined LSTM + CNN models.

## Evaluation Implementation

 Performed several steps to preprocess trajectory data, train an LSTM model, and compare the performance with and without vectorization.
 Performed several steps to preprocess trajectory data, train an Hybrid model, and compare the performance with and without vectorization.
 Compared the training times with and without vectorization.
 Retrieved and displayed the vectorized data from the database.

 This entire process demonstrates the steps taken to preprocess data, apply machine learning models, handle data storage and retrieval in a database, and compare the efficiency of different approaches.

For any questions, concerns, or comments for improvements, etc, please create an issue on the issues page for this project, or email the authors directly.

    

