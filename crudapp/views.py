from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def calculate(request):
    if request.method == "POST":
        value1 = float(request.POST['value1'])
        value2 = float(request.POST['value2'])
        action = request.POST['action']

        if action == '+':
            result = value1 + value2
        elif action == '-':
            result = value1 - value2
        elif action == '*':
            result = value1 * value2
        elif action == '/':
            result = value1 / value2
        else:
            result = "invalid action!"

        return HttpResponse(f"The result is: {result}")

    return render(request, 'math.html')

