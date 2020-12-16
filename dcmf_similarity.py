
def linkweights_to_similarity(df1, alpha):
  import pandas as pd
  from numpy.linalg import inv
  from numpy.linalg import matrix_power
  link_1_list = list(df1['nodeid1'])
  link_2_list = list(df1['nodeid2'])
  link_list_1 = link_1_list + link_2_list
  link_list_1 = sorted(list(dict.fromkeys(link_list_1)))
  k = len(link_list_1)
  dict_1_ = dict(zip(link_list_1,range(0, len(link_list_1))))

  dict1_1 = dict()
  for index, row in df1.iterrows():
    if (((row['nodeid1'], row['nodeid2'])) or ((row['nodeid2'], row['nodeid1']))) in dict1_1.keys():
    
      index = index + 1
      continue
    dict1_1[(dict_1_[row['nodeid1']]), (dict_1_[row['nodeid2']])] = row['linkweight']


  print((dict1_1))
  A1 = [0 for i in range(k) for j in range(k)]
  A1 = np.matrix(A1).reshape(k, k)

  for (i, j) in list(dict1_1.keys()):

    A1[i, j] = dict1_1[(i, j)]

  print(A1)
  D1 = [0 for i in range(k) for j in range(k)]
  D1 = np.matrix(D1).reshape(k, k)
  D_1 = (np.sum(A1 , axis=1))
  VOL_G1 = sum(D_1)
  print(D_1)
  for i in range(k):
    if D_1[i] != 0:
      D1[i,i] = (1/D_1[i])
  
  print(D1)

  A1 = np.matrix(A1)
  A1_ = [0 for i in range(k) for j in range(k)]
  A1_ = np.matrix(A1_)
  A1_ = A1_.reshape(k, k)
  A1_ = A1*(alpha)

  eye1 = np.eye(k)
  Sgra = (eye1 - np.dot(A1_, (D1)))
  Sgra = inv(Sgra)
  Sgra = np.dot(Sgra, A1_)
  print(Sgra)
  link_weight_list = []
  for index, row in df1.iterrows():
    link_weight_list.append(Sgra[dict_1_[row['nodeid1']], dict_1_[row['nodeid2']]])




  df1['linkweight1'] = list(link_weight_list)
  return df1
