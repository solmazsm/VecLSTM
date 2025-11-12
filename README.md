<p align="center">
  <img src="https://img.shields.io/badge/Under%20Review%20at%20IEEE%20ICDE%202026-0033A0?style=for-the-badge&labelColor=0033A0&color=0033A0&logoColor=white" />
</p>



<h1 align="center">VecLSTM: A Scalable Data Management System for Spatio-Temporal Modeling with Dynamic Vectorization</h1>

<p align="center">
  <a href="https://students.washington.edu/solmazsm/"><strong>Solmaz Seyed Monir</strong></a><sup>1</sup>, 
  <a href="https://www.cs.washington.edu/people/faculty/zhao-dongfang/"><strong>Dr. Dongfang Zhao</strong></a><sup>1</sup>
</p>


<p align="center">
  <sup>1</sup>Database Research Group (HPDIC Lab) • University of Washington
</p>

<p align="center">
  <a href="https://github.com/solmazsm/VecLSTM">
    <img src="https://img.shields.io/badge/Code-000000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://arxiv.org/abs/2409.19258">
    <img src="https://img.shields.io/badge/arXiv-CC0000?style=for-the-badge&logo=arxiv&logoColor=white" />
  </a>
</p>


---

##  Overview

**VecLSTM** introduces a scalable trajectory modeling framework that bridges *deep sequence learning* and *vector databases*.  
The system converts irregular spatiotemporal trajectories into fixed-shape **feature–time tensors**, enabling efficient **CNN–LSTM** modeling and **metadata-aware caching** for reuse across training sessions.

---

##  Key Contributions

- **Vectorization Layer:**  
  Introduces a task-agnostic vectorization mechanism that converts irregular spatiotemporal trajectories into fixed-size feature–time tensors, preserving spatial relationships without geographic gridding.   Transforms each trajectory into a fixed feature–time tensor with complexity $\mathcal{O}(N){+}\mathcal{O}(KF)$.

- **Scalable Modeling Pipeline:**  
  Captures spatial and temporal correlations while fusing metadata via concatenation.

- **Persistent vector store:**  
  Persists $(\text{key}(T),V)$ pairs for metadata-aware reuse and analytically quantifies cache-induced speedup.

- **Performance & Efficiency:**  
  Achieves **F1 = 0.86** on *GeoLife* with **74.2 % training-time reduction**, and maintains **RMSE ≈ 0.46–0.47** across 1–5 s horizons on *highD*.

---

### System Design

The architecture modularizes spatial feature extraction and temporal sequence modeling.

Trajectory prediction and activity recognition are critical for understanding dynamic systems such as transportation and urban mobility. VecLSTM addresses scalability and computational challenges in processing high-dimensional trajectory data:

<p align="center">

<table>
<tr>
<td width="48%" style="border: 1px solid #ddd; border-radius: 12px; padding: 16px; vertical-align: top;">
<b>VecLSTM System Design</b><br>
VecLSTM provides a unified spatio-temporal data management workflow that dynamically vectorizes raw trajectory records into structured feature–time sequences.
</td>

<td width="48%" style="border: 1px solid #ddd; border-radius: 12px; padding: 16px; vertical-align: top;">
<b>Scalable Modeling Pipeline</b><br>
VecLSTM is a hybrid CNN–LSTM model that preserves motion continuity and supports efficient caching of reusable trajectory embeddings.
</td>
</tr>

<tr>
<td width="48%" style="border: 1px solid #ddd; border-radius: 12px; padding: 16px; vertical-align: top;">
<b>Performance & Efficiency</b><br>
Demonstrates state-of-the-art results on GeoLife and HighD, achieving a 74.2% training-time reduction while maintaining stable RMSE (0.46–0.47) across multi-second prediction horizons.
</td>

<td width="48%" style="border: 1px solid #ddd; border-radius: 12px; padding: 16px; vertical-align: top;">
<b>Complexity</b><br>
VecLSTM achieveslinear-time sequence processing, with per-trajectory complexity:
<div align="center"><code>O(L) + O(KF)</code></div>
where L is the trajectory length and <b>K, F</b> are fixed vectorization constants.
Because <b>K</b> and <b>F</b> do not scale with data size, the overhead remains effectively constant, yielding <b>sublinear cost</b> compared to attention-based models (e.g., Transformer complexity <code>O(L²)</code>).
</td>
</tr>
</table>


</p>

- **Vectorization Layer:** The vectorization mechanism converts irregular spatio-temporal trajectories into fixed-size feature–time tensors using value-distribution binning rather than geographic gridding, preserving relative spatial variation while avoiding coordinate warping or map-based discretization.
- **Metadata:** Enriched metadata, such as temporal and spatial data, activity labels, and user information, to further improve the model's performance.
- **Practical Deployment Insight:** VecLSTM Provides guidance on selecting tensor resolution and temporal window size, showing how metadata-aware caching accelerates retraining and real-time inference in large-scale systems.

## Datasets

### GeoLife Dataset
The GeoLife dataset consists of GPS trajectories from 182 users collected over five years (Apr 2007–Aug 2012), covering 17,000+ trips, 1.2 M km of travel, and 48,000 hours.  
In our experiments, we use a curated subset with 1,467,652 rows and six columns.   
We further integrate enriched metadata with contextual attributes, making this dataset ideal for human-activity prediction from trajectory data.

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


## Installation & Setup

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
## Running VecLSTM

The repo includes a Docker Compose setup for fully reproducible experiments.

**Requirements**: [Docker](https://docs.docker.com/get-docker/)

1. Build and start:
    ```bash
    docker-compose up --build
    ```
2. The API will be available at `localhost:8000`, MySQL at `localhost:3306`.

  - Access endpoints via the `veclstm_api` container (see `/main.py` for available routes).
 - Model outputs (trajectory embeddings) are stored in MySQL.
---
    
# VecLSTM Structure

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

