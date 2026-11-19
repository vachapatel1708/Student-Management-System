from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Q
from.models import Student,Payment

# Create your views here.

@login_required(login_url='login/')
def home(request):
    return render(request,'home.html')

def showlist(request):
    student = Student.objects.all()
    search = request.GET.get('search')

    if search:
        student = student.filter(
            Q(name__icontains=search)
        )


    for s in student:
        paid = Payment.objects.filter(name=s).aggregate(
            total=Sum('payment_amount')
        )['total']

        if paid is None:
            paid = 0

        s.paid = paid
        s.remain = s.fees - paid

    return render(request,'showlist.html',{'student':student})

def addstudent(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')  
        phone = request.POST.get('phone')  
        city = request.POST.get('city')  
        course = request.POST.get('course')  
        fees = request.POST.get('fees')  
        image = request.FILES.get('image') 

        s = Student(name=name,gender=gender,phone=phone,city=city,course=course,fees=fees,image=image)
        s.save()
        
        return redirect(showlist)

    return render(request,'addstudent.html')

def studentdetail(request,id):
    s = Student.objects.get(id=id)

    return render(request,'studentdetail.html',{'s':s})

def delete(request, id):
    s1 = Student.objects.get(id=id)
    print(s1)
    s1.delete()

    return redirect(showlist)

def update(request,id):
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.name = request.POST.get('name')
        s1.gender = request.POST.get('gender')
        s1.phone = request.POST.get('phone')
        s1.city = request.POST.get('city')
        s1.course = request.POST.get('course')
        s1.fees = request.POST.get('fees')
        s1.image = request.FILES.get('image')

        s1.save()

        return redirect(showlist)

    else:
        return render(request,'updatestudent.html',{'s1':s1})

def showpayment(request):
    payment = Payment.objects.all()
    
    return render(request,'showpayment.html',{'payment':payment})

def addpayment(request):

    student = Student.objects.all()

    if request.method == 'POST':
        name = int(request.POST.get('student'))
        payment_amount = request.POST.get('payment_amount')
        date = request.POST.get('date')
        taken_by = request.POST.get('taken_by')
        payment_method = request.POST.get('payment_method')
        
        student = Student.objects.get(id=name)
        
        p = Payment.objects.create(name=student,payment_amount=payment_amount,date=date,taken_by=taken_by,payment_method=payment_method)
        p.save()

        return redirect(showlist)

    return render(request,'addpayment.html',{'student':student})

def attendance(request):
    return render(request,'attendance.html')

def mark_attendance(request):
    return render(request,'markattendance.html')

def exam(request):
    return render(request,'exam.html')

def about(request):
    return render(request,'about.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect(home)
        else:
            return render(request,'login.html',{'error':'invalid username or password'})

    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error':'username already exits'})
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect(login)

    return render(request,'register.html')

def user_logout(request):
    logout(request)
    return redirect(login)

