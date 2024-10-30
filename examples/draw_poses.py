'''
 visualization
'''

import numpy as np
import open3d as o3d
import os

# read gt pose to draw the matches
seq_id = '06'
poses = np.loadtxt(f"D:/kitti/dataset/poses/{seq_id}.txt")
poses_xyz = poses[:, (3,7,11)] # actually cam pose
poses_o3d = o3d.geometry.PointCloud()
poses_o3d.points = o3d.utility.Vector3dVector(poses_xyz)
o3d.visualization.draw_geometries([poses_o3d])
