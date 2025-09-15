'''
Created on 22 july 2025
@author: Ramyaa

1. Loads your .pcd file
2. Applies DBSCAN clustering
3. Colors each cluster differently
4. Prints total points, number of clusters, and noise points
5. Visualizes the clustered and colored point cloud
'''

import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the .pcd file
pcd = o3d.io.read_point_cloud("~/Desktop/00001.pcd")
print("Loaded point cloud with", np.asarray(pcd.points).shape[0], "points.")
o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")

# Step 2: Apply DBSCAN (tuned parameters)
labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=10, print_progress=True))

# Step 3: Cluster statistics
total_points = len(labels)
unique_clusters = len(set(labels)) - (1 if -1 in labels else 0)
noise_points = np.sum(labels == -1)
print("\n📊 Clustering Summary:")
print("Total points:", total_points)
print("Unique clusters (excluding noise):", unique_clusters)
print("Noise points:", noise_points)

# Step 4: Color clusters
max_label = labels.max()
colors = plt.get_cmap("tab20")(labels / (max_label + 1 if max_label >= 0 else 1))
# colors = colors[:, :3]  # Convert to RGB only BEFORE assigning
# colors[labels < 0] = [0, 0, 0]  # Now this works correctly
colors[labels < 0] = [0, 0, 0, 1]  # RGBA: black + full opacity
pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

# Step 5: Visualize clustered point cloud
o3d.visualization.draw_geometries([pcd], window_name="DBSCAN Clustering")

# How to Count Clusters:
unique_labels = set(labels)
num_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)
print("Total clusters (excluding noise):", num_clusters)