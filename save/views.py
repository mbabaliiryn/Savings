from django.shortcuts import render
from models import CustomUser, balance
def profile(request):
    user = balance.objects.get(CustomUser=request.CustomUser)
    return render(request,'home.html',{"balance":CustomUser.balance})

    

