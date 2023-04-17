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
       return JsonResponse([i.to_json() for i in companies], safe=False)
    elif request.method == "POST":
         data = json.loads(request.body)
         company = Company.objects.create(name = data.get('name'), description = data.get('description'), city = data.city('city'), adress = data.adress('adress'))
         return JsonResponse(company.to_json())
@csrf_exempt    
def one_company(request, id):
    try:
        comp = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(comp.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
       
        new_company_name = data.get('name', comp.name)
        comp.name = new_company_name

        disc = data.get('description', comp.description)
        comp.description = disc

        city = data.get('city', comp.city)
        comp.city = city

        address = data.get('address', comp.address)
        comp.address = address

        comp.save()
        return JsonResponse(comp.to_json())


    elif request.method == 'DELETE':
        comp.delete()
        return JsonResponse({'deleted': True})
@csrf_exempt
def company_vacancies_by_id(request, id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, status=400)

        vacancies = company.vacancies.all()
        data = []
        for vacancy in vacancies:
            data.append({
                'company_name': company.name,
                'name': vacancy.name,
                'description': vacancy.description,
                'salary': vacancy.salary,
                'company_id': company.id
            })
        return JsonResponse(data, safe=False)
     
@csrf_exempt    
def all_vacancies(request):
    if request.method == "GET":
        vac = Vacancy.objects.all()
        data = []
        for v in vac:
            data.append({
                'name': v.name,
                'description': v.description,
                'salary': v.salary,
                'company_id': v.company.id
            })
        return JsonResponse(json.dumps(data, ensure_ascii=False), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vac_name = data.get('name', '')
        vac_description = data.get('description', '')
        vac_salary = data.get('salary', '')
        vac_company = data.get('company', '')
        vacancy = Vacancy.objects.create(name=vac_name, description=vac_description, salary=vac_salary, company_id=vac_company)

        vacancy_data = {
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company_id': vacancy.company_id
        }
        return JsonResponse(json.dumps(vacancy_data), safe=False)  
@csrf_exempt
def one_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'message': "Vacancy with such an id doesn't exist"}, status=404)
    if request.method == "GET":
        data = {
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company_name': vacancy.company.name,
            'company_id': vacancy.company.id
        }
        return JsonResponse(data, safe = False)
    elif request.method == "DELETE":
        vacancy.delete()
        return JsonResponse({'deleted': True})
@csrf_exempt
def top_ten(request):
    if request.method == "GET":
       vacancies = Vacancy.objects.order_by('-salary')[:10]
       data = []
       for vacancy in vacancies:
            data.append({
                'name': vacancy.name,
                'company': vacancy.company.name,
                'description': vacancy.description,
                'salary': vacancy.salary,
            })
       return JsonResponse(data, safe=False)