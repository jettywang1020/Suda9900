from django.shortcuts import render
from public.models import Tenant, Landlord, House

# Create your views here.
def index(request):
	landlord = Landlord.objects.get(pk = 1)
	return render(request, 'landlord/index.html', {'landlord': landlord})


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