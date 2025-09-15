"""
Created on 22 july 2025
@author: Ramyaa
"""

import open3d as o3d
import numpy as np

# Step 1: Load the Point Cloud
pcd = o3d.io.read_point_cloud("/home/divya1/PCD_Honda/Data/sample_1.pcd")
print("Original Point Cloud:")
print(pcd)
o3d.visualization.draw_geometries([pcd], window_name="Original Point Cloud")

# Step 2: Remove NaN (non-finite) Values
pcd.remove_non_finite_points()
print("After removing NaNs:", len(pcd.points))
o3d.visualization.draw_geometries([pcd], window_name="After Cleaning (NaNs Removed)")

# Step 3: Radius Outlier Filtering
pcd, ind = pcd.remove_radius_outlier(nb_points=5, radius=0.1)
print("After Radius Outlier Filtering:", len(pcd.points))
o3d.visualization.draw_geometries([pcd], window_name="After Radius Outlier Filtering")

# Step 4: Statistical Outlier Filtering
pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=5, std_ratio=2.0)
print("After Statistical Outlier Filtering:", len(pcd.points))
o3d.visualization.draw_geometries([pcd], window_name="After Statistical Outlier Removal")

# Step 5: Centering the Point Cloud
center = np.mean(np.asarray(pcd.points), axis=0)
pcd.translate(-center)
print("Centered point cloud at:", np.mean(np.asarray(pcd.points), axis=0))
o3d.visualization.draw_geometries([pcd], window_name="After Centering")

# Step 6: Normalization
points = np.asarray(pcd.points)
scale = np.max(np.linalg.norm(points, axis=1))
points /= scale
pcd.points = o3d.utility.Vector3dVector(points)
print("Normalized point cloud scale.")
o3d.visualization.draw_geometries([pcd], window_name="After Normalizing")

# Step 7: Save the Processed Point Cloud
o3d.io.write_point_cloud("/home/divya1/PCD_Honda/Data/preprocessed.pcd", pcd)
print("Saved preprocessed point cloud.")

# Step 8: Voxel Grid Downsampling
voxel_down = pcd.voxel_down_sample(voxel_size=0.05)  # 5 cm voxel
print("After Voxel Grid Downsampling:", voxel_down)
o3d.visualization.draw_geometries([voxel_down], window_name="Voxel Downsampling")

# Step 9: Uniform Downsampling
uniform_down = pcd.uniform_down_sample(every_k_points=10)
print("After Uniform Downsampling:", uniform_down)
o3d.visualization.draw_geometries([uniform_down], window_name="Uniform Downsampling")
