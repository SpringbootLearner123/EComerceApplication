from django.shortcuts import render,HttpResponse
from General.models import contactModel,userdata,ProductModel,ALogin

# Create your views here.
def dashboard(request):
    if(request.session.has_key("aid")):
        return render(request, "dashboard.html")
    else:
        return HttpResponse("<script>alert('Login First then Goto next zone ');window.location.href='/loginreg'</script>")

def contactmgmt(request):
    if (request.session.has_key("aid")):
     data=contactModel.objects.all()
     return render(request,"contactmgmt.html",{'data':data})
    else:
        return HttpResponse("<script>alert('Login First then Goto next zone ');window.location.href='/loginreg'</script>")



def ordermgmt(request):
    if (request.session.has_key("aid")):
     return render(request,"ordermgmt.html")
    else:
        return HttpResponse(
            "<script>alert('Login First then Goto next zone ');window.location.href='/loginreg'</script>")

def productmgmt(request):
    if(request.session.has_key("aid")):
        data=ProductModel.objects.all()
        return render(request,"productmgmt.html",{'data':data})
    else:
        return HttpResponse(
            "<script>alert('Login First then Goto next zone ');window.location.href='/loginreg'</script>")
def addproduct(request):
    if (request.session.has_key("aid")):
     return render(request,"add products.html")
    else:
        return HttpResponse(
            "<script>alert('Login First then Goto next zone ');window.location.href='/loginreg'</script>")

def delContact(request,id):
    r=contactModel.objects.get(id=id)
    r.delete()
    return HttpResponse("<script>alert('Record deleted');window.location.href='/contactmgt'</script>")


def Alogout(request):
    try:
        del request.session['aid']
    except:
        pass
    return HttpResponse(
        "<script>alert('You are logout');window.location.href='/loginreg'</script>")






