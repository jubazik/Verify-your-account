from django.shortcuts import render




def home_block(request):
    return render(request, 'block/home_block.html')
# Create your views here.
