from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from public.models import User, House

# Create your views here.
def index(request):
	# tenant = Tenant.objects.get(pk = 1)
	return render(request, 'tenant/index.html', locals())

def test(request):
	test_id = request.GET.get("test_id")
	data = {"test_id":test_id}
	return JsonResponse(data)






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