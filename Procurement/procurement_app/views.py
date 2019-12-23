from django.shortcuts import render,redirect,reverse
from .models import User_details,Product_details
import datetime

date = datetime.datetime.now()

def home(request):
    return render(request,'home.html')



def admin_login(request):
    email = request.POST.get('emailid')
    epass = request.POST.get('password')
    if email == 'admin' and epass == 'admin':
        return render(request,"admin_page.html")
    else:
        return redirect(reverse('admin_sign_in')+"?error_message=Wrong Credentials..!")

def admin_logout(request):
    return redirect(reverse('admin_home'))


def adding_Product(request):
    if request.method == 'POST':
        pid = request.POST['product_id']
        pname = request.POST['product_name']
        pdes = request.POST['product_description']
        pcb = request.POST['created_by']
        # pimage = request.FILES['file']

        Product_details(product_id=pid,product_name=pname,product_description=pdes,created_date=date,created_by=pcb).save()
        return render(request,'admin_page.html',{"mes":"Product Added Successfully"})
        # else:
        #     return redirect(reverse('product_add')+"?error_message=Some Wrong Detail Entered")
    else:
        return redirect(reverse('product_add')+"?error_message=Some Wrong Detail Entered")


def sign_in(request):
    uemail = request.POST.get('emailid')
    upass=request.POST.get('password')
    User_details(email=uemail,password=upass)
    qs = User_details.objects.filter(email=uemail,password=upass)
    if qs:
        request.session['user'] = uemail
        return render(request,'user_page.html')
    else:
        return redirect(reverse('user_home')+"?error_message=Wrong details")


def user_logout(request):
    del request.session['user']
    return redirect(reverse('user_home'))


def user_Sign_Up(request):
    if request.method == 'POST':
        uname = request.POST['Username']
        email = request.POST['email']
        upass = request.POST['password']
        addr = request.POST['address']
        num = request.POST['number']
        User_details(user_name=uname,email=email,password=upass,address=addr,contact_no=num).save()
        return render(request,'user_home.html',{"msg":"User Successfully Registered"})
    else:
        return redirect(reverse('user_signup')+"?error_message=Something is Wrong...!")

def user_cancel_req(request):
    if request.method == 'GET':

        t1 = request.POST['title']
        t2 = request.POST['pid']
        t3 = request.POST['pqty']
        t4 = request.POST['due_date']
        t5 = request.POST['comments']
        t6 = request.POST['status']
        t7 = request.POST['reqesterid']
        t8 = request.POST['request to']
        t9 = request.POST['cancel']

        User_details(title=t1, pid=t2, pqty=t3, due_date=t4, comments=t5, status=t6, registerid=t7, requestto=t8,
                     description=t9).save()
        return render(request, 'user_cancel_request.html', {"msg": "User Successfully Registered"})
    else:
        return redirect(reverse('user_signup') + "?error_message=Something is Wrong...!")


def user_raise_req(request):
    if request.method == 'POST':

        t1 = request.POST['title']
        t2 = request.POST['pid']
        t3 = request.POST['pqty']
        t4 = request.POST['due_date']
        t5 = request.POST['comments']
        t6 = request.POST['status']
        t7 = request.POST['reqesterid']
        t8 = request.POST['request to']
        t9 = request.POST['description']
        t10 = request.POST['submit']
        print("this method has been called")

        # ProcurementRequest(req_title=t1, req_product_id = t2,req_prod_quantity=t3, req_due_date=t4, req_comments=t5, req_status=t6, requester_id=t7, created_by=t8).save()
        if form.is_valid():
            messages.success(request, 'Form submission successful')
        return render(request, 'user_raisehome.html', {"msg": "User Successfully Registered"})
    else:
        return redirect(reverse('user_signup') + "?error_message=Something is Wrong...!")


def user_raisehome(request):
    print("inside the user_raisehome")
    t1 = request.POST['title']
    t2 = request.POST['pid']
    t3 = request.POST['pqty']
    t4 = request.POST['due_date']
    t5 = request.POST['comments']
    t6 = request.POST['status']
    t7 = request.POST['reqesterid']
    t8 = request.POST['request to']
    t9 = request.POST['description']
    t10 = request.POST['submit']
    qs = ProcurementRequest.objects.filter(req_title=t1, req_product_id = t2,req_prod_quantity=t3, req_due_date=t4, req_comments=t5, req_status=t6, requester_id=t7, created_by=t8).save()
      
    # qs = User_details.objects.filter(title=t1, pid=t2, pqty=t3, due_date=t4, comments=t5, status=t6, registerid=t7,
    #                                  requestto=t8,
    #                                  description=t9, submit=t10)
    if qs:
        request.session['user'] = uemail
        return render(request, 'user_raisehome.html')
    else:
        return redirect(reverse('user_home') + "?error_message=Wrong details")


