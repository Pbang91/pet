from django.views import View
from django.http  import JsonResponse
from .models      import *
import json


class OwnerView(View):
     def post(self, request):
         data = json.loads(request.body)
         Owner.objects.create(name = data["name"], email = data["email"], age = data["age"])
         return JsonResponse({"result": "Created"}, status = 201)

     def get(self, request):
         result_key = []
         owner_list = Owner.objects.all()
         for owner in owner_list:
             dog_list = owner.dog_set.all()
             dogs = []
             for dog in dog_list:
                 dog_informaiton = {
                    "name" : dog.name,
                    "age" : dog.age
                 }
                 dogs.append(dog_informaiton)
             result = {
                    "name"  : owner.name,
                    "email" : owner.email,
                    "age"   : owner.age,
                    "dog_list" : dogs
                }
             result_key.append(result)
         return JsonResponse({"result" : result_key}, status = 200)


class DogView(View):
     def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(id = data["owner_id"]).id
        Dog.objects.create(name = data["name"], owner_id = owner)
	    # owner = Owner.objects.get(id=data["owner_id"])
        # Dog.objects.create(name = data["name"], owner = owner)
        return JsonResponse({"result" : "Created"}, status = 201)
     
     def get(self, request):
         results = []