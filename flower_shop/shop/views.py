from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Flower, Order

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def catalog(request):
    flowers = Flower.objects.all()
    return render(request, 'catalog.html', {'flowers': flowers})

@login_required
def create_order(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = Flower.objects.get(id=flower_id)
        order = Order.objects.create(user=request.user)
        order.flowers.add(flower)
        order.save()
        return redirect('catalog')
    return redirect('catalog')
