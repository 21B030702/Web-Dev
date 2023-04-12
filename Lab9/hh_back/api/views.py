from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def all_companies(request):
    if request.method == "GET":
       companies = Company.objects.all()
       companies_json = [p.to_json() for p in companies]
       return JsonResponse(companies_json)
    elif request.method == "POST":
         data = json.loads(request.body)
         company = Company.objects.create(name = data.get('name'), description = data.get('description'), city = data.city('city'), adress = data.adress('adress'))
         return JsonResponse(company.to_json())
@csrf_exempt    
def one_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'message': "Company doesn't exist"}, status = 404)
    if request.method == "GET":
       return JsonResponse(company.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        company.name = data.get('name')
        company.description = data.get('description')
        company.city = data.get('city')
        company.adress = data.get('adress')
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == "DELETE":
         company.delete()
         return JsonResponse({'deleted': True})
@csrf_exempt
def company_vacancies_by_id(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancies.all()
        vacancies_json = [p.to_json() for p in vacancies]
    except Company.DoesNotExist:
          return JsonResponse({'message': "Company with such id doesn't exist,"}, status = 404)  
    if request.method == "GET":
       return JsonResponse(vacancies_json, safe=False)
    elif request.method == "POST":
         data = json.loads(request.body)
         vacancy = Vacancy.objects.create(name = data.get('name'), description = data.get('description'), city = data.get('city'), adress = data.get('adress'))
         return JsonResponse(vacancy.to_json())  
@csrf_exempt    
def all_vacancies(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == "POST":
         data = json.loads(request.body)
    try:
        company = Company.objects.get(id=data.get('company'))
    except Company.DoesNotExist:
        return JsonResponse({'message': "Vacancy doesn't exist"}, status = 400)
    vacancy = Vacancy.objects.create(name = data.get('name'), description = data.get('description'), city = data.get('city'), adress = data.get('adress'))  
    return JsonResponse(vacancy.to_json())  
@csrf_exempt
def one_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'message': "Vacancy with such an id doesn't exist"}, status=404)
    if request.method == "GET":
        return JsonResponse(vacancy.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        try:
            company = Company.objects.get(id=data.get("company"))
        except Company.DoesNotExist:
            return JsonResponse({'message': "Company with such an id doesn't exist"}, status=400)
        vacancy.name = data.get('name')
        vacancy.description = data.get('description')
        vacancy.salary = data.get('salary')
        vacancy.company = company
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == "DELETE":
        vacancy.delete()
        return JsonResponse({'deleted': True})
@csrf_exempt
def top_ten(request):
    if request.method == "GET":
       vacancies = Vacancy.objects.order_by('-salary')[:10]
       vacancies_json = [vacancy.to_json() for vacancy in vacancies]
       return JsonResponse(vacancies_json, safe = False)