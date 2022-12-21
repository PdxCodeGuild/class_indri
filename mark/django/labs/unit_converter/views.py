from django.shortcuts import render

# Create your views here.
def unit_converter(request):
    if request.method =="GET":
        return render(request, '')
    else:
        distance = float(request.POST['distance'])
        unit = request.POST['unit']
        result = uc(distance, unit)
        return render(request, '', {'result':result})