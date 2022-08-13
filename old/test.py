import numpy as np


data_3d=np.load("data/data_3d_h36m.npz",allow_pickle=True)
data_2d=np.load("data/data_2d_h36m_gt.npz",allow_pickle=True)
keypoints_metadata = data_2d['metadata'].item()
keypoints_symmetry = keypoints_metadata['keypoints_symmetry']
kps_left, kps_right = list(keypoints_symmetry[0]), list(keypoints_symmetry[1])
# joints_left, joints_right = list(dataset.skeleton().joints_left()), list(dataset.skeleton().joints_right())
keypoints = data_2d['positions_2d'].item()

# print(data)
data3d_item=data_3d['positions_3d'].item()
for subject in data3d_item:
    for action in data3d_item[subject]:
        # p3=
        # for cam_idx, kps in enumerate(keypoints[subject][action][0]):
        #     print(cam_idx,len(kps))
        for i,p3 in enumerate( data3d_item[subject][action]):
            cam3d=keypoints[subject][action][0][1][i] #cam 3d
            pix2d=keypoints[subject][action][1][2][i] #pix 2d
            print(len(cam3d),len(pix2d))
# print(data['positions_3d'].item())