from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.views import generic
from django.views.generic.edit  import CreateView
from django.views.generic import  View
from .models import Stock
from .forms import StockForm
from django.http import HttpResponseRedirect, request


from django.shortcuts import render,redirect


#Lists all stocks or create a new onedef transport_new(request):
   ##return render(request,'music/transport_edit.html',{'form':form})
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
def index(request):
    return render(request, 'companies/index.html')
class StockList(APIView):
    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks,many=True)
        return Response(serializer.data)
    def post(self):
        pass
