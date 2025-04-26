from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from General.forms import contactForm,aloginForm
from General.models import contactModel,ALogin,userdata,ProductModel,signupdata
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request,"index.html")


def brandf(request):
    return  render(request,"products.html")

def household(request):
    return  render(request,"household.html")


def vegetables(request):
    return  render(request,"vegetables.html")


def kitchen(request):
    return  render(request,"kitchen.html")


def softdrink(request):
    return  render(request,"drinks.html")

def petfood(request):
    return  render(request,"pet.html")

def frozen(request):
    return  render(request,"frozen.html")

def breadb(request):
    return  render(request,"bread.html")

def events(request):
    return  render(request,"events.html")

def about(request):
    return  render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    form=contactForm()
    return render(request,"mail.html",{"form":form})

def ContactData(request):
    if request.method=='POST':
            name=request.POST.get("name")
            mob=request.POST.get("mob")
            email=request.POST.get("email")
            subj=request.POST.get("subj")
            msg=request.POST.get("msg")
            cm=contactModel(name=name,mob=mob,email=email,subj=subj,msg=msg)
            cm.save()
            return HttpResponse("<script>alert('Thanks for contact as soon as we contact you ');window.location.href='/contact'</script>")
    else:
      return HttpResponse(
       "<script>alert('Your Request is not completed');window.location.href='/contact'</script>")



def loginreg(request):
    return  render(request,"login.html")

def loginData(request):
    if request.method=='POST':
        userid=request.POST.get("Username")
        passwd=request.POST.get("passwd")
    try:
        lg=ALogin.objects.get(userid=userid)
        if lg.userid == userid and lg.passwd == passwd:
                request.session["aid"]=userid    #set the session values

                return HttpResponse(
                    "<script>alert('Thanks welcome to Our Next Zone ');window.location.href='/dashboard'</script>")
        else:
                return HttpResponse(
                    "<script>alert('Inavlid userid Or Password');window.location.href='/loginreg'</script>")

    except ALogin.DoesNotExist:
        return HttpResponse(
            "<script>alert('Inavlid userid Or Password');window.location.href='/loginreg'</script>")



@csrf_exempt
def check(request):
    return  render(request,"checkout.html")

def userorder(request):
    if request.method=='POST':
        fname=request.POST.get("name")
        mob=request.POST.get("mob")
        lmark=request.POST.get("lmark")
        town=request.POST.get("town")
        addtype=request.POST.get("atype")
        data=userdata(fname=fname,mob=mob,lmark=lmark,town=town,atype=addtype)
        data.save()
        return HttpResponse(
            "<script>alert('Thanks Your Order is completed on same address ');window.location.href='/checkout'</script>")
    else:
        return HttpResponse("<script>alert('Your Order is not completed');window.location.href='/checkout'</script>")


def payment(request):
    return render(request,"payment.html")

def priv(request):
    return render(request,"privacy.html")

def faq(request):
    return render(request,"faqs.html")

def singl(request):
    return render(request,"single.html")
def signupdata(request):
    # return render (request,'signup.html')
# def SignupPage(request):
    if request.method=='POST':
        susername=request.POST.get('susername')
        semail=request.POST.get('semail')
        spassword=request.POST.get('spass1')
        spass2=request.POST.get('spass2')

        if spassword!=spass2:
            return HttpResponse("Your password and conform password are not Same!!")
        else:

            my_user=User.objects.create_user(susername,semail,spassword,)
            my_user.save()
            return redirect('loginreg')
