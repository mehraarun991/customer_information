from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import OrderForm

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_orders, 'pending': pending,
               'delivered': delivered}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    product = Products.objects.all()
    context = {'product': product}
    return render(request, 'accounts/products.html', context)

def customer(request, pk_test):
    custom = Customer.objects.get(id=pk_test)
    orders = custom.order_set.all()
    total_count = orders.count()
    context = {'customer': custom, 'orders': orders, 'total_count': total_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print("Printing post method: ", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/accounts')
    context = {'order': order}
    return render(request, 'accounts/delete_form.html', context)