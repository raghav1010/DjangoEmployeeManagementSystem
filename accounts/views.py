from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import EmployeeForm, SystemForm, DetailForm, LeaveForm
from django.shortcuts import render, redirect  
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Employee, System, Leave
from django.core.paginator import Paginator
from datetime import date, datetime
# Create your views here.


@login_required(login_url='/login')
def home(request):
    x=Employee.objects.filter(username=request.user)
    if x:
        emp = request.user.employee
        return render(request,'home2.html',{'employee':emp})
    else:
        employees = Employee.objects.all()
        paginator=Paginator(employees,3)
        page_num=request.GET.get('page',1)
        emp=paginator.page(page_num)
        return render(request,'home.html',{'employees':emp}) 

    

@login_required(login_url='/login')
def profile(request,id):
    if request.method == 'POST':
        emp=Employee.objects.get(id=id)
        p_form = DetailForm(request.POST,instance=emp)
        p_form.fields['role'].disabled= True
        p_form.fields['dept'].disabled= True
        if p_form.is_valid() :
            p_form.save()
            return redirect('/home')
    else:
        p_form = DetailForm(instance=Employee.objects.get(id=id))
        p_form.fields['role'].disabled= True
        p_form.fields['dept'].disabled= True
    context={'p_form': p_form}
    return render(request, 'profile.html',context )


@login_required(login_url='/login')
def emp_leave(request,id):
    u = User.objects.get(id=id)
    print(u)
    leave = Leave.objects.filter(owner=u)
    print(len(list(leave.values())))
    paginator=Paginator(leave,2)
    page_num=request.GET.get('page',1)
    lea=paginator.page(page_num)
    return render(request,'my_leave.html',{'lea':lea}) 

@login_required(login_url='/login')
def add_leave(request,id):
    
    if request.method=="POST":
        u = User.objects.get(id=id)
        form = LeaveForm(request.POST)
        st = request.POST.get("startdate")
        ed = request.POST.get("enddate")
        st = date.fromisoformat(st)
        ed = date.fromisoformat(ed)
        today_date = date.today()
        leave = Leave.objects.filter(owner=u)
        count_leave = len(list(leave.values()))
        if st>=today_date and ed>=today_date and ed>=st:
            if form.is_valid():
                if count_leave<3:
                    try:
                        print('a1')
                        new_form = form.save(commit=False)
                        print('a2')
                        new_form.owner = u
                        new_form.status = "Wait"
                        print('a3')
                        new_form.save()
                        print("form saved")
                        return redirect('leave',id=id)
                    except:
                        print(form.errors)
                else:
                    messages.error(request,"Your Leave Count has expired")
            else:
                print(form.errors)
        else:
            messages.error(request,"Please enter valid dates")
    # else:
    if request.method=="GET":
        form = LeaveForm()
    context = {'form': form }
    return render(request, 'add_leave.html', context)


@login_required(login_url='/login')
def detail(request,id):
    if request.method == 'POST':
        emp=Employee.objects.get(id=id)
        p_form = DetailForm(request.POST,instance=emp)
        p_form.fields['name'].disabled= True
        p_form.fields['fathername'].disabled= True
        p_form.fields['email'].disabled= True
        p_form.fields['gender'].disabled= True
        p_form.fields['DOB'].disabled= True
        if p_form.is_valid() :
            p_form.save()
            return redirect('/home')
    else:
        p_form = DetailForm(instance=Employee.objects.get(id=id))
        p_form.fields['name'].disabled= True
        p_form.fields['fathername'].disabled= True
        p_form.fields['email'].disabled= True
        p_form.fields['gender'].disabled= True
        p_form.fields['DOB'].disabled= True
    context={'p_form': p_form}
    return render(request, 'detail.html',context )

@login_required(login_url='/login')
def all_leaves(request):
    x=Employee.objects.filter(username=request.user)
    if x:
        emp = request.user.employee
        
    else:
        leavess = Leave.objects.all()
        paginator=Paginator(leavess,3)
        page_num=request.GET.get('page',1)
        leav=paginator.page(page_num)
        return render(request,'all_leaves.html',{'leaves':leav}) 

@login_required(login_url='/login')
def leave_detail(request,id):
    if request.method == 'POST':
        le=Leave.objects.get(id=id)
        p_form = LeaveForm(request.POST,instance=le)
        p_form.fields['name'].disabled= True
        p_form.fields['startdate'].disabled= True
        p_form.fields['enddate'].disabled= True
        if p_form.is_valid() :
            p_form.save()
            return redirect('/all_leaves')
    else:
        p_form = LeaveForm(instance=Leave.objects.get(id=id))
        p_form.fields['name'].disabled= True
        p_form.fields['startdate'].disabled= True
        p_form.fields['enddate'].disabled= True

    context={'p_form': p_form}
    return render(request, 'leave_detail.html',context)

def Register_Emp(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')
        
    context = {'form': form }
    return render(request, 'employee_registration.html', context)

def Register_Sys(request):
    form = SystemForm()
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')

    context = {'form': form }
    return render(request, 'admin_registration.html', context)

def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/home')
		else:
			messages.info(request, 'username or password is incorrect')

	context = {}
	return render(request, 'login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('/login')