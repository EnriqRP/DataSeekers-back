from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Users
import json

# Create your views here.
# Using Django ORM

class UsersView(View): 
   
   #NO RESTRICTION CSRF
   @method_decorator(csrf_exempt)
    
    # CROSS SITE REQUEST FORGERY
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

   #GET METHOD
   def  get(self,request, id=0):
    
        if (id > 0):
            users = list(Users.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                data = {'message': "Success", 'users': user}
            else:
                data = {'message': "Company not found..."}
            return JsonResponse(data)
        else:
            users = list(Users.objects.values())
            if len(users) > 0:
                data = {'message': "Success", 'users': users}
            else:
                data = {'message': "User not found..."}
            return JsonResponse(data)

   # POST METHOD
   def  post(self,request):
      jd = json.loads(request.body)
      Users.objects.create(name=jd['name'])
      data = {'message': "Success"}
      return JsonResponse(data)

   # PUT METHOD
   def put(self,request):
        jd = json.loads(request.body)
        user = list(Users.objects.filter(id=id).values())
        if len(user) > 0:
            user = Users.objects.get(id=id)
            user.name = jd['name']
            user.save()
            data = {'message': "Success"}
        else:
            data = {'message': "User not found..."}
        return JsonResponse(data)

   # DELETE METHOD
   def delete(self,request, id):
        users = list(Users.objects.filter(id=id).values())
        if len(users) > 0:
            Users.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "User not found..."}
        return JsonResponse(data)