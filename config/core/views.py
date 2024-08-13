from django.shortcuts import render

# Create your views here.
def example(request):
    return render(request, 'core/example.html')

def reg(request):
    return render(request, "core/reg.html") 