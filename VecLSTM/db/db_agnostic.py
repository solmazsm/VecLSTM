
# The provided table schema for veclstm_trajectories is designed to be dataset-agnostic—it can store trajectory data from any dataset, including both:
 # The highD dataset (vehicle trajectories)
# The Geolife (human/trajectory) dataset (such as GPS traces of people)

CREATE TABLE IF NOT EXISTS veclstm_trajectories (
    traj_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    start_time DATETIME,
    end_time DATETIME,
    transport_mode VARCHAR(20),
    avg_speed FLOAT,
    vectorized_tensor JSON NOT NULL,
    label INT
);
