"""
Created on 22 july 2025
@author: Ramyaa
"""

import open3d as o3d

#read_point_cloud() loads the .pcd file
pcd = o3d.io.read_point_cloud("~/Desktop/00001.pcd")
print(pcd)

#draw_geometries() opens a 3D viewer
o3d.visualization.draw_geometries([pcd])

#Saves the point cloud to a new file
#Can save as .pcd or .ply format
o3d.io.write_point_cloud("~/Desktop/newfile.pcd",pcd)

'''
Inspecting Point Cloud Arrays:

What is NumPy?

    NumPy = Numerical Python

    Used to store and work with numbers efficiently

    Array is like a table of numbers (rows × columns)

Common terms:

    np.asarray() → Convert Open3D data to NumPy array

    .shape → Tells how many rows and columns

    Easy to do math on entire arrays (faster than loops)
'''

import numpy as np

'''
Why use NumPy arrays?

    To store and work with numbers

    To do math on many numbers at once

    Super useful for 3D points, images, sensor data, etc.
    
'''

#Converts point cloud to a NumPy array
points = np.asarray(pcd.points)
print(points)

#Use it to see x, y, z values of each point
print(points.shape)

'''
    points is a NumPy array that holds all your 3D points.

    points.shape tells you the size of that array.

(36723, 3) means:

    You have 36,723 points in your point cloud.

    Each point has 3 values → x, y, and z.

So this array is like a table with:

    36,723 rows (one for each point)

    3 columns (x, y, z)
'''

print(points[:5])

'''
points is a 2D array → Each row = one 3D point

points[:5] = First 5 points

Each number represents a position in space (X, Y, Z)
'''

colors = np.asarray(pcd.colors)
normals = np.asarray(pcd.normals)


'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# These are your first 5 points
points = np.array([
    [25.29, -19.54, 15.44],
    [22.74, -20.44, 6.78],
    [21.60, -20.93, 2.99],
    [22.65, -18.34, 4.18],
    [21.26, -19.59, 1.81]
])

# 3D plot setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the 5 points
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='red', marker='o')

# Labeling axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('First 5 Points from Point Cloud')

plt.show()
'''