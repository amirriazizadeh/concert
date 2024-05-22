from django.shortcuts import render
from .models import concertModel
# Create your views here.
def concertListView(request):
    res=concertModel.objects.all()
    context={
        "concerts":res
    }
    return render(request,"ticketSales/listconcert.html",context)