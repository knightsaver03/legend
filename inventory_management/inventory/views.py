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

# def exhardForm_view(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Product_list')
#     else :
#         form = AddProductForm()
#         return render(request, 'inventory_management/exhardForm.html', {'form': form})
# def exhardForm_view(request):
#     excel_path = "C:/Users/SVE1NA/Documents/legend/inventory_management/data/master_data.xlsx"
#     df = pd.read_excel(excel_path, engine='openpyxl')
#     alpha_numbers = df['AlphaNumber'].dropna().unique().tolist()

#     if request.method == 'POST':
#         form = AddProductForm(request.POST)
#         if form.is_valid():
#             form.save()  # <-- saves to DB
#             return redirect('exhardForm')  # redirect to avoid form re-submission
#     else:
#         form = AddProductForm()

#     return render(request, 'inventory_management/exhardForm.html', {
#         'form': form,
#         'alpha_numbers': alpha_umbers,
#     })



# def update_exhard(request, product_id):
#     product = get_object_or_404(ExardProduct, id=product_id)
#     if request.method == 'POST':
#         form = AddProductForm(requnest.POST, instance=product)
#         if form.is_valid():
#             form.save()  # updates the existing book record
#             return redirect('Product_list')
#     else:
#         form = AddProductForm(instance=product)
#     return render(request, 'inventory_management/exhardForm.html', {'form': form})







# # views.py
# import os
# import pandas as pd
# from django.conf import settings
# from django.shortcuts import render


# def xhard_form_view(request):
#     excel_path = "C:/Users/SVE1NA/Documents/legend/inventory_management/data/master_data.xlsx"
#     df = pd.read_excel(excel_path, engine='openpyxl')
#     alpha_numbers = df['AlphaNumber'].dropna().unique().tolist()

#     # print("Alpha Numbers are :")
#     # print(alpha_numbers)

#     if request.method == 'POST':
#         selected_alpha = request.POST.get('alpha_number')
#         quantity = request.POST.get('quantity')
#         # Handle form submission logic here
#         print(f"AlphaNumber: {selected_alpha}, Quantity: {quantity}")

#     return render(request, 'inventory_management/exhardForm.html', {
#         'alpha_numbers': alpha_numbers,
#     })


# views.py
from django.shortcuts import render, redirect
from .forms import AddExhardForm
from .models import ExardProduct
import pandas as pd


# def exhardForm_view(request):
#     excel_path = r"C:/Users/navne/Downloads/legend/legend/inventory_management/data/master_data.xlsx"
#     if os.path.exists(excel_path):
#         df = pd.read_excel(excel_path, engine='openpyxl')
#         alpha_numbers = df['AlphaNumber'].dropna().unique().tolist()

#     if request.method == 'POST':
#         form = AddExhardForm(request.POST)
#         if form.is_valid():
#             product = form.cleaned_data['alpha_number']
#             added_quantity = request.POST.get['quantity']

#             product.quantity += added_quantity
#             product.save()
#             form.save()
#             messages.success(request, f"Added {added_quantity} to {product.alpha_number}. New quantity: {product.quantity}")
#             return redirect('exhard_form') 
#     else:
#         form = AddExhardForm()


#     ExardProduct=ExardProduct.objects.create(
#         alpha_number='alpha_number',  # Replace with actual data or leave empty
#         quantity = 'quantity'  # Default quantity, can be adjusted as needed
#     )

#     return render(request, 'inventory_management/exhardForm.html', {'form': form})

def exhardForm_view(request):
    print("Hi there ")
    excel_path = r"C:/Users/navne/Desktop/backend/legend/inventory_management/data/master_data.xlsx"
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path, engine='openpyxl')
        alpha_numbers = df['AlphaNumber'].dropna().unique().tolist()

    if request.POST:        

        form = AddExhardForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('exhard_form')
    return render(request, 'inventory_management/exhardForm.html', {'form': AddExhardForm()})


def upload_excel_view(request):
    if request.POST:
        form = AddExhardForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhard_form')
        else:
            print(form.errors)

    else: 
        form = AddExhardForm()
    return render(request, 'inventory_management/upload_excel.html', {'form':form})
