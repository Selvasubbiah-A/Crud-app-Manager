from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee 
from .forms import EmployeeForm
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and user.is_active and user.is_staff:
            auth.login(request, user)
            return redirect('crud-page')  # Redirect to the CRUD page
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')



def crud_view(request):
    if request.method == 'GET':
        return render(request, 'crud.html')
    
    elif request.method == 'POST':
        form_data = request.POST
        return redirect('crud-page')
    
def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        phone_number = request.POST['phoneNumber']
        position = request.POST['position']
        state = request.POST['state']
        country = request.POST['country']
        
        # Create a new Employee object and save it to the database
        employee = Employee(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            position=position,
            state=state,
            country=country
        )
        employee.save()
        
        view_employees_url = reverse('view_employees')
        return redirect(view_employees_url) # Redirect to the View page after successful submission
    
    return render(request, 'add.html')

def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'view.html', {'employees': employees})


def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def delete_employee(request,id):
    employees = Employee.objects.get(id = id)
    employees.delete()
    view_employees_url = reverse('view_employees')
    return redirect(view_employees_url) 