from django.shortcuts import render, redirect, reverse
from .models import User_details, Product_details
import datetime

date = datetime.datetime.now()


def home(request):
    return render(request, 'home.html')


def admin_login(request):
    email = request.POST['emailid']
    epass = request.POST['password']
    if email == 'admin' and epass == 'admin':
        return render(request, "admin_page.html")
    else:
        return redirect(reverse('admin_sign_in') + "?error_message=Wrong Credentials..!")


def admin_logout(request):
    return redirect(reverse('admin_home'))


def adding_Product(request):
    if request.method == 'POST':
        pid = request.POST['product_id']
        pname = request.POST['product_name']
        pdes = request.POST['product_description']
        pcb = request.POST['created_by']
        pimage = request.FILES['file']

        Product_details(product_id=pid, product_name=pname, product_description=pdes, created_date=date, created_by=pcb,
                        product_image=pimage).save()
        return render(request, 'admin_page.html', {"mes": "Product Added Successfully"})
        # else:
        #     return redirect(reverse('product_add')+"?error_message=Some Wrong Detail Entered")
    else:
        return redirect(reverse('product_add') + "?error_message=Some Wrong Detail Entered")


def sign_in(request):
    uemail = request.POST['emailid']
    upass = request.POST['password']
    qs = User_details.objects.filter(email=uemail, password=upass)
    if qs:
        request.session['user'] = uemail
        return render(request, 'user_page.html')
    else:
        return redirect(reverse('user_home') + "?error_message=Wrong details")


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
        User_details(user_name=uname, email=email, password=upass, address=addr, contact_no=num).save()
        return render(request, 'user_home.html', {"msg": "User Successfully Registered"})
    else:
        return redirect(reverse('user_signup') + "?error_message=Something is Wrong...!")
