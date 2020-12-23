from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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