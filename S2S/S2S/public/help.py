from django.db import connection

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