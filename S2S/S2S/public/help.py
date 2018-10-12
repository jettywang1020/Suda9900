from django.db import connection
from public.models import *

# help functions

def RunSQL(sql):
	with connection.cursor() as cursor:
		cursor.execute(sql)
		rows = cursor.fetchall()
		fieldnames = [name[0] for name in cursor.description]
		results = []
		for row in rows:
			result = {}
			for i in range(len(row)):
				result[fieldnames[i]] = row[i]
			results.append(result)
	return results

def reivew_calculate(id):
	house_feature_r = [0 for _ in range(12)]
	reviews = 0
	house_feature = {'accuracy':0,'location':0,'communication':0,'check_in':0,'cleanliness':0,'value':0}
	house_rate = House_Rate.objects.all()
	if house_rate:
		for house_r in house_rate:
			if house_r.house_id == id:
				house_feature_r[0] += house_r.accuracy
				house_feature_r[1] += 1
				house_feature_r[2] += house_r.location
				house_feature_r[3] += 1
				house_feature_r[4] += house_r.communication
				house_feature_r[5] += 1
				house_feature_r[6] += house_r.check_in
				house_feature_r[7] += 1
				house_feature_r[8] += house_r.cleanliness
				house_feature_r[9] += 1
				house_feature_r[10] += house_r.value
				house_feature_r[11] += 1
		if house_feature_r[1]:
			house_feature['accuracy'] = round(house_feature_r[0]/house_feature_r[1])
			reviews += house_feature['accuracy']
		if house_feature_r[3]:
			house_feature['location'] = round(house_feature_r[2]/house_feature_r[3])
			reviews += house_feature['location']
		if house_feature_r[5]:
			house_feature['communication'] = round(house_feature_r[4]/house_feature_r[5])
			reviews += house_feature['communication']
		if house_feature_r[7]:
			house_feature['check_in'] = round(house_feature_r[6]/house_feature_r[7])
			reviews += house_feature['check_in']
		if house_feature_r[9]:
			house_feature['cleanliness'] = round(house_feature_r[8]/house_feature_r[9])
			reviews += house_feature['cleanliness']
		if house_feature_r[11]:
			house_feature['value'] = round(house_feature_r[10]/house_feature_r[11])
			reviews += house_feature['value']
		reviews = round(reviews/6)
	return reviews 