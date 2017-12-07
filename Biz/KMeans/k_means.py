#!/usr/bin/python
from numpy import *


def convert_list_to_matrix(list):
    total_list = []
    for i in list:
        tmplist = []
        tmplist.append(i[u'_id'][u'weekday'])
        tmplist.append(i[u'_id'][u'blue'])
        tmplist.append(i[u'totalCount'])
        total_list.append(tmplist)
    return mat(total_list)


def dist_eclud(vec1, vec2):
    return sqrt(sum(power(vec1-vec2,2)))

def rand_cent(data, k):
    n = shape(data)[1]
    central_ids = mat(zeros(k,n))
    for j in range(n):
        min_j = min(data[:,j])
        range_j = float(max(data[:,j]) - min_j)
        central_ids[:,j] = min_j + range_j*random.rand(k,1)
    return central_ids

def k_means(data, k, dist_meas=dist_eclud, create_cent=rand_cent):
    m = shape(data)[0]
    cluster_assment = mat(zeros(m,2))
    center_ids = create_cent(data, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = inf; min_index = -1
            for j in range(k):
                dist_j_i = dist_meas(center_ids[j,:], data[i,:])
                if dist_j_i < min_dist:
                    min_dist = dist_j_i; min_index = j
            if cluster_assment[i,0] != min_index:
                cluster_changed = True
            cluster_assment[i,:] = min_index, min_dist**2
        print center_ids
        for cent in range(k):
            pts_in_clust = data[nonzero(cluster_assment[:,0].A==cent)[0]]
            center_ids[cent,:] = mean(pts_in_clust, axis=0)
    return center_ids, cluster_assment


def bin_k_mean(data, k, dist_meas=dist_eclud):
    m = shape(data)[0]
    clusterAssment=mat(zeros(m, 2))
    central_id_0 = mean(data, axis=0).tolist()[0]
    cent_list = [central_id_0]
    for j in range(m):
        clusterAssment[j, 1] = dist_meas(mat(central_id_0), data[j, :])**2
    while len(cent_list) < k:
        lowest_sse = inf
        for i in range(len(cent_list)):
            pts_in_curr_cluster = data[nonzero(clusterAssment[:,0].A==i)[0],:]
            #central_id_mat, split_clust_ass =

