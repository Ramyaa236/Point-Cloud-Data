'''
Created on 22 july 2025
@author: Ramyaa

1. Loading the .pcd file
2. Simulating color-coded clusters
3. Adding bounding boxes
4. Adding a line annotation
5. Visualizing everything
6. (Optional) Exporting a screenshot
'''

import open3d as o3d
import numpy as np

# Step 1: Load the point cloud
pcd = o3d.io.read_point_cloud("~/Desktop/00001.pcd")
print("Loaded point cloud:", pcd)

# Step 2: Simulate 3 clusters by splitting the point cloud manually
points = np.asarray(pcd.points)
n = len(points)
cluster1 = pcd.select_by_index(np.arange(0, n//3))
cluster2 = pcd.select_by_index(np.arange(n//3, 2*n//3))
cluster3 = pcd.select_by_index(np.arange(2*n//3, n))

# Step 3: Apply unique colors to each cluster
cluster1.paint_uniform_color([1, 0, 0])  # Red
cluster2.paint_uniform_color([0, 1, 0])  # Green
cluster3.paint_uniform_color([0, 0, 1])  # Blue

# Step 4: Add a bounding box around one cluster
bbox = cluster2.get_axis_aligned_bounding_box()
bbox.color = (1, 1, 0)  # Yellow box

# Step 5: Add a line from origin to center of that cluster
start_point = [0, 0, 0]
end_point = bbox.get_center().tolist()
line_points = [start_point, end_point]
line_indices = [[0, 1]]

line = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(line_points),
    lines=o3d.utility.Vector2iVector(line_indices)
)
line.colors = o3d.utility.Vector3dVector([[0, 1, 1]])  # Cyan

# Step 6: Visualize everything together
o3d.visualization.draw_geometries(
    [cluster1, cluster2, cluster3, bbox, line],
    window_name=" Advanced Visualization"
)

# Step 7 (Optional): Save screenshot of the final view
vis = o3d.visualization.Visualizer()
vis.create_window(visible=False)
vis.add_geometry(cluster1)
vis.add_geometry(cluster2)
vis.add_geometry(cluster3)
vis.add_geometry(bbox)
vis.add_geometry(line)
vis.poll_events()
vis.update_renderer()
vis.capture_screen_image("/visual_output.png")
vis.destroy_window()
print("Screenshot saved to: visual_output.png")
