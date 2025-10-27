# VecLSTM: A Scalable Vectorized Framework for Trajectory Prediction and Activity Recognition

> **Status:**  *Submitted to IEEE ICDE 2026*  
> **Authors:** Solmaz Seyed Monir, Dongfang Zhao  
> **Affiliation:** Database Research Group, University of Washington  

---


##  Overview

**VecLSTM** introduces a scalable trajectory modeling framework that bridges *deep sequence learning* and *vector databases*.  
The system converts irregular spatiotemporal trajectories into fixed-shape **feature–time tensors**, enabling efficient **CNN–LSTM** modeling and **metadata-aware caching** for reuse across training sessions.

---

##  Key Contributions

- **Task-agnostic vectorization:**  
  Transforms each trajectory into a fixed feature–time tensor with complexity $\mathcal{O}(N){+}\mathcal{O}(KF)$ and no geographic gridding.

- **Hybrid CNN–LSTM encoder:**  
  Captures spatial and temporal correlations while fusing metadata via concatenation.

- **Persistent vector store:**  
  Persists $(\text{key}(T),V)$ pairs for metadata-aware reuse and analytically quantifies cache-induced speedup.

- **Experimental results:**  
  Achieves **F1 = 0.86** on *GeoLife* with **74.2 % training-time reduction**, and maintains **RMSE ≈ 0.46–0.47** across 1–5 s horizons on *highD*.

---

##  System Design

The framework decouples feature extraction from sequence modeling:

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

![GeoLife Data](https://github.com/solmazsm/VecLSTM/blob/master/datasets/data/data-Geolife.jpg?raw=true)


### HighD Dataset
The HighD dataset is a large-scale, drone-captured vehicle trajectory dataset from German highways. It includes 110,000 vehicle trajectories over 16,500 tracks, recorded at 25 Hz with high accuracy. Each trajectory contains data on position, velocity, acceleration, and lane changes, making it suitable for multi-agent interaction modeling and trajectory prediction.

- **Dataset details**: [HighD Dataset](https://www.highd-dataset.com/)
- **Usage**: The HighD dataset helps us evaluate the model's ability to predict vehicle trajectories on highways.
![Drone HighD](https://levelxdata.com/wp-content/uploads/2023/09/droneHighD-450x300.png) 

## Results

| Dataset | Domain | Metric | VecLSTM Result |
|----------|---------|---------|----------------|
| GeoLife  | Human mobility | F1 = 0.86 | 74.2 % faster than baselines |
| highD    | Vehicle trajectories | RMSE = 0.46–0.47 | Consistent across 1–5 s horizons |

---


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
# Project Structure

The following is the structure of this project:

```plaintext
VecLSTM/
├─ vectorization/      # dynamic vectorization layer
├─ models/             # CNN–LSTM modules
├─ storage/            # relational/vector store adapter
├─ datasets/           # loaders for GeoLife, highD
├─ scripts/            # train/eval/visualization
├─ figures/            # figures for paper/site
└─ README.md

```

 

For any questions, concerns, or comments for improvements, etc, please create an issue on the issues page for this project, or email the authors directly.

