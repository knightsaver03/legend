from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import pytz, os
from datetime import datetime
from django.contrib.auth.models import User
from .models import ProjectType , ExardProduct

from django.contrib import messages


# Create your views here.

def startup_view(request):
    return render(request, 'inventory_management/home.html')

def login_view(request):
    return render(request, 'inventory_management/login.html')

def admin_login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to custom admin dashboard
        else:
            error_message = 'Invalid credentials or not an admin user.'
    return render(request, 'inventory_management/adminLogin.html', {'error_message': error_message})

@login_required
def admin_dashboard_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    project_types = ProjectType.objects.all()
    return render(request, 'inventory_management/admin_dashboard.html', {
        'admin_name': admin_name,
        'greeting': greeting,
        'project_types': project_types
    })

@login_required
def add_user_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    import pytz
    from datetime import datetime
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    project_types = ProjectType.objects.all()

    
@login_required
def remove_user_view(request):
    admin_name = request.user.get_full_name() or request.user.username
    # Get current time in Indian/Delhi timezone
    import pytz
    from datetime import datetime
    india_tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(india_tz)
    hour = now.hour
    if hour < 12:
        greeting = 'Good morning'
    elif hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'

    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                error_message = "Cannot remove a superuser."
            else:
                user.delete()
                return redirect('admin_dashboard')
        except User.DoesNotExist:
            error_message = "User does not exist."
        return render(request, 'inventory_management/admin_dashboard.html', {
            'error_message': error_message,
            'admin_name': admin_name,
            'greeting': greeting
        })
    return redirect('admin_dashboard')





def inventoryLogin_view(request):
    return render(request, 'inventory_management/inventoryhome.html')

# from django.shortcuts import render, redirect
# from .forms import AddExhardForm
# from .models import ExardProduct
# import pandas as pd

# def exhardForm_view(request):
#     # excel_path = r"C:/Users/navne/Downloads/legend/legend/inventory_management/data/master_data.xlsx"
#     # df = pd.read_excel(excel_path, engine='openpyxl')
#     # alpha_number_list = df['AlphaNumber'].dropna().unique().tolist()

#     # if request.POST:
#     #     form = AddExhardForm(request.POST)
#     #     if form.is_valid():

#     #         print("Hi there ")
#     #         alpha_number = request.POST.get['alpha_number']
#     #         added_quantity = request.POST.get['quantity']

#     #         # Try to get the product from the database
#     #         product, created = ExardProduct.objects.get_or_create(alpha_number=alpha_number)
#     #         product.quantity += added_quantity
#     #         product.save()

#     #         return redirect('exhardForm')
#     # else:
#     #     form = AddExhardForm()

#     return render(request, 'inventory_management/exhardForm.html', {'form': form})


from django.shortcuts import render, redirect
from .models import ExardProduct
from .forms import AddExhardForm

def exhardForm_view(request):
    excel_path = r"C:/Users/navne/Downloads/legend/legend/inventory_management/data/master_data.xlsx"
    df = pd.read_excel(excel_path, engine='openpyxl')
    alpha_numbers = df['AlphaNumber'].dropna().unique().tolist()

    
    if request.method == 'POST':
        form = AddExhardForm(request.POST)
        if form.is_valid():

            print("Ho ter")
            # Get the product and quantity to add
            product = form.cleaned_data['alpha_number']
            added_quantity = form.cleaned_data['quantity']
            # Update the product's quantity
            product.quantity += added_quantity
            product.save()
            return redirect('exhardForm')  # Redirect to the same form after success
    else:
        form = AddExhardForm()
    return render(request, 'inventory_management/exhardForm.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import AddExhardForm
from .models import ExardProduct
import pandas as pd

def exhardForm_view(request):
    excel_path = r"C:/Users/navne/Downloads/legend/legend/inventory_management/data/master_data.xlsx"
    df = pd.read_excel(excel_path, engine='openpyxl')
    alpha_number_list = df['AlphaNumber'].dropna().unique().tolist()

    if request.POST:
        form = AddExhardForm(request.POST)
        if form.is_valid():

            print("Hi there ")
            alpha_number = request.POST.get['alpha_number']
            added_quantity = request.POST.get['quantity']

            # Try to get the product from the database
            product, created = ExardProduct.objects.get_or_create(alpha_number=alpha_number)
            product.quantity += added_quantity
            product.save()

            return redirect('exhardForm')
    else:
        form = AddExhardForm()

    return render(request, 'inventory_management/exhardForm.html', {'form': form})






