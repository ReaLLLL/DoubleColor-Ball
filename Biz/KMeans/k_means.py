#!/usr/bin/python
from numpy import *
from util.fileUtil import get_data_from_db_aggregate


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
    central_ids = mat(zeros((k,n)))
    for j in range(n):
        min_j = min(data[:,j])
        range_j = float(max(data[:,j]) - min_j)
        central_ids[:,j] = min_j + range_j*random.rand(k,1)
    return central_ids


def k_means(data, k, dist_meas=dist_eclud, create_cent=rand_cent):
    m = shape(data)[0]
    cluster_assment = mat(zeros((m,2)))
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
    cluster_assment=mat(zeros((m, 2)))
    central_id_0 = mean(data, axis=0).tolist()[0]
    cent_list = [central_id_0]
    for j in range(m):
        cluster_assment[j, 1] = dist_meas(mat(central_id_0), data[j, :])**2
    while len(cent_list) < k:
        lowest_sse = inf
        for i in range(len(cent_list)):
            pts_in_curr_cluster = data[nonzero(cluster_assment[:,0].A==i)[0],:]
            centro_id_mat, split_cluster_ass = k_means(pts_in_curr_cluster, 2, dist_meas)
            sse_split = sum(split_cluster_ass[:,1])
            sse_not_split = sum(cluster_assment[nonzero(cluster_assment[:,0].A!=i)[0],1])
            print "sseSplit, and notSplit: ",sse_split,sse_not_split
            if (sse_split + sse_not_split) < lowest_sse:
                best_cent_to_split = i
                best_new_cents = centro_id_mat
                best_cluster_ass = split_cluster_ass.copy()
                lowest_sse = sse_split + sse_not_split
        best_cluster_ass[nonzero(best_cluster_ass[:,0].A == 1)[0],0] = len(cent_list)
        best_cluster_ass[nonzero(best_cluster_ass[:,0].A == 0)[0],0] = best_cent_to_split
        print 'the bestCentToSplit is: ',best_cent_to_split
        print 'the len of bestClustAss is: ', len(best_cluster_ass)
        cent_list[best_cent_to_split] = best_new_cents[0,:].tolist()[0]
        cent_list.append(best_new_cents[1,:].tolist()[0])
        cluster_assment[nonzero(cluster_assment[:,0].A == best_cent_to_split)[0],:]= best_cluster_ass
    return mat(cent_list), cluster_assment


orig_mat = convert_list_to_matrix(get_data_from_db_aggregate('DOUBLECOLOR_BALL'))

mat, cluster = bin_k_mean(orig_mat, 24)

print '===========Result============='
print mat

print cluster

