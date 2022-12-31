from django.shortcuts import render

# register view
def register(request):
  return render(request, 'UserApp/register.html')




# login view
def login(request):
  return render(request, 'UserApp/login.html')





# profile view


