"""
Created on 22 july 2025
@author: Ramyaa
"""

import open3d as o3d
import numpy as np
import os
import matplotlib.pyplot as plt


# Step 1: Load the Point Cloud
desktop_path = os.path.expanduser("~/Desktop/00001.pcd")
pcd = o3d.io.read_point_cloud(desktop_path)
print("Original point clouds:", pcd)
o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")



### Euclidean distance between two points ###
points = np.asarray(pcd.points)

p1 = points[100]
p2 = points[300]

dist = np.linalg.norm(p1-p2) # compute Euvlidean distance
print("Euclidean distance between point 100 and 300:", dist)




### Cluster Bounding Boxes:AABB & OBB ###
# Step 2: Choose a cluster (use DBSCAN to find clusters)
labels = np.array(pcd.cluster_dbscan(eps=0.2, min_points=10))
cluster_index = 0 # cluster ID 0
indices = np.where(labels == cluster_index)[0]
cluster_pcd = pcd.select_by_index(indices)

# Step 3: Add Bounding Box (AABB)
box1 = cluster_pcd.get_axis_aligned_bounding_box()
box1.color = (1, 0, 0) # Red box

# Step 4: Oriented Bounding Box (OBB)
box2 = cluster_pcd.get_oriented_bounding_box()
box2.color = (0, 1, 0) # Green box

# Step 4: Visualize
o3d.visualization.draw_geometries([cluster_pcd, box1, box2], window_name="Cluster with Bounding Box")



### Visualize Plane and Outliers ###
# Step 2:Plane segmentation
plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)

# Step 3:Separate inliers (plane) and outliers
inlier_cloud = pcd.select_by_index(inliers)
outlier_cloud = pcd.select_by_index(inliers, invert=True)

# Step 3:Color the inliers green and outliers red
inlier_cloud.paint_uniform_color([1, 0, 0])   # Green
outlier_cloud.paint_uniform_color([0, 1, 0])  # Red

# Step 4:Visualize
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])




### Plane Fitting & Point to plane distance ###
### Plane Fitting ###
points = np.asarray(pcd.points)
# Fit a Plane using RANSAC & Compute Point-to-Plane Distance
# Segment a plane from the point cloud using RANSAC
plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)

[a, b, c, d] = plane_model
print(f"Plane equation: {a:.3f}x + {b:.3f}y + {c:.3f}z + {d:.3f} = 0")


### Point to plane distance calculation
# Pick the 0th point in the cloud – the one whose distance to the plane you want to calculate.
x, y, z = points[0]

dist_to_plane = abs(a*x + b*y + c*z + d) / np.sqrt(a**2 + b**2 + c**2)  # Compute distance to plane
print("Distance of point 0 to plane:", dist_to_plane)

