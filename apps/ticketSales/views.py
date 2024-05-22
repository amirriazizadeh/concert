from django.shortcuts import render
from .models import concertModel,locationModel
from django.conf import settings
# Create your views here.
def concertListView(request):
    res=concertModel.objects.all()
    media=settings.MEDIA_URL
    context={
        "concerts":res,
        "media":media
    }
    return render(request,"ticketSales/listconcert.html",context)

def listOfLocations(request):
    locs=locationModel.objects.all()
    context={
        "locations":locs
    }
    return render(request,'ticketSales/locationtemplate.html',context)


def concertDetails(request,concertId):
    concert=concertModel.objects.get(pk=concertId)
    context={
        "media":settings.MEDIA_URL,
        "concert":concert
    }
    return render(request,"ticketSales/detail.html",context)