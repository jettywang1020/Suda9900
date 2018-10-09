def knn_model(tag):
	samples = [[0,1,0,1,1,0],[0,1,1,0,0,1],[1,0,1,0,0,1]]
	feature = ['new','old','high_price','low_price','Amenities<4','Amenities>=4']
	all_class = {0:[0,1,0,1,1,0],1:[0,1,1,0,0,1], 2:[1,0,1,0,0,1]}
	from sklearn.neighbors import NearestNeighbors
	neigh = NearestNeighbors(n_neighbors=1)
	neigh.fit(samples)
	simi, class_ = neigh.kneighbors(tag)
	if simi <= 2:	
		return all_class[class_[0][0]]