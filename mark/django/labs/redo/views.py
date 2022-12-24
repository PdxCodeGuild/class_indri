from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    conversions = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000,
        "yd" : 0.9144,
        "in" : 0.0254
    }
    if request.method == "GET":
        return render(request, 'redo/index.html')
    else:
        form = request.POST
        value = float(form['value'])
        from_unit = form['from_unit']
        to_unit = form['to_unit']
        
        meters = value * conversions[from_unit]
        
        result = round((meters * (1/conversions[to_unit])), 3)
        
    context = {
        'result':result,
        'value':value,
        'from_unit':from_unit,
        'to_unit':to_unit,
    }
    return render(request, 'redo/index.html', context)

    