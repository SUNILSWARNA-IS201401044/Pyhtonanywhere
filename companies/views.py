from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Stock1
from .serializers import StockSerializer
from django.views import generic
from django.views.generic.edit  import CreateView
from django.views.generic import  View
from .forms import StockForm
from django.http import  request
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
#Lists all stocks or create a new onedef transport_new(request):
   ##return render(request,'music/transport_edit.html',{'form':form})
@csrf_exempt
def transport_new(request):
    if request.method == "POST":
        print "hello"
        form = StockForm(request.POST)
        if form.is_valid():
            print "hello"
        #    instance = Transport(file_field=request.FILES['logo'])
         #   instance.save()
            Transport1 = form.save()
            Transport1.save()
            return redirect('companies:index')
    else:
        form = StockForm()
    return render(request, 'companies/transport_edit.html', {'form': form})
@csrf_exempt
def index(request):
    all_albums = Stock1.objects.all()
    albums = {'s1':[],'s2':[],'s3':[]}
    for x in xrange(0,all_albums.count()):
        if  x % 3 == 0:
            albums['s1'].append(all_albums[x])
        elif  x % 3 == 1:
            albums['s2'].append(all_albums[x])
        else:
            albums['s3'].append(all_albums[x])

    return render(request, 'companies/index.html',{'albums':albums})
def albdetail(request, album_id):
    album =Stock1.objects.get(pk=album_id)

    return render(request, 'companies/imgdetail.html', {'album': album})

def test(request):
    return render(request,'companies/test.html')
def service(request):
    return render(request,'companies/service.html')
def team(request):
    return render(request,'companies/team.html')
def login(request):
    return render(request,'companies/newLogin.html')
def register(request):
    return render(request,'companies/newRegister.html')

def problems(request):
    all_albums = Stock1.objects.all()
    albums = {'s1':[],'s2':[],'s3':[]}
    for x in xrange(0,all_albums.count()):
        if  x % 3 == 0:
            albums['s1'].append(all_albums[x])
        elif  x % 3 == 1:
            albums['s2'].append(all_albums[x])
        else:
            albums['s3'].append(all_albums[x])

    return render(request,'companies/problems.html',{'albums':albums})
def contact(request):
    if request.method=="POST":
        li=[]
        li.append(str(request.POST['email']))
        li.append('ramuklinus369@gmail.com')
        try:
            spe=send_mail('From'+' '+str(request.POST['name'])+' '+'About'+' ' +str(request.POST['subject']),request.POST['message'],'ramuklinus369@gmail.com',li)
            messages.success(request,'Send Mail Succesfullu')
            return redirect('companies:test')
        except:
            return HttpResponse("Could not process your Request")
    else:
        messages.success(request,'Send Mail Succesfullu')
        return render(request,'companies/contact.html')
class StockList(APIView):
    def get(self,request):
        stocks=Stock1.objects.all()
        serializer=StockSerializer(stocks,many=True)
        content = {'user_count': serializer.data}
        return Response(content)
    def post(self):
        pass
class StockList1(APIView):
    def get(self,request,album_id):
        stocks=Stock1.objects.get(id=album_id)
        serializer=StockSerializer(stocks)
        ls=[]
        #s.append(serializer.data)
        m=serializer.data

        k=str(m['data'])
        m=k.replace("\n","")
        m=m.replace('\r','')
        #ls.append(k)
        #ls.append(type(k))
        return Response(m)
        #content = {'user_count': ls}
        #return Response(content)
    def post(self):
        pass
