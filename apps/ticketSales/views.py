from typing import Any
from django.shortcuts import render
from .models import concertModel,locationModel,timeModel
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import searchForm,ConcertForm
from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def concertListView(request):
    res=searchForm(request.GET)
    if res.is_valid():
        concert=res.cleaned_data["searchConcert"]
        concert=concertModel.objects.filter(Name__contains=concert)
    else:
        concert=concertModel.objects.all()
    media=settings.MEDIA_URL
    context={
            "media":media,
            "concerts":concert,
            "searchForm":res
        }
    return render(request,"ticketSales/listconcert.html",context)
    # if request.method=="GET":
    #     sf=searchForm()
    #     res=concertModel.objects.all()
    #     media=settings.MEDIA_URL
    #     context={
    #         "concerts":res,
    #         "media":media,
    #         "searchForm":sf
    #     }
    #     return render(request,"ticketSales/listconcert.html",context)
    # elif request.method=="POST":
    #     concert=request.POST.get("searchConcert")
    #     concert=concertModel.objects.filter(Name__contains=concert)
    #     media=settings.MEDIA_URL
    #     context={
    #         "concerts":concert,
    #         "media":media
    #     }
    #     return render(request,"ticketSales/listconcert.html",context)
# @login_required
# def listOfLocations(request):
#     locs=locationModel.objects.all()
#     context={
#         "locations":locs
#     }
#     return render(request,'ticketSales/locationtemplate.html',context)


class locationsViews(ListView):
    template_name="ticketSales/locationtemplate.html"
    model=locationModel
    context_object_name="locations"
        
        

def concertDetails(request,concertId):
    concert=concertModel.objects.get(pk=concertId)
    context={
        "media":settings.MEDIA_URL,
        "concert":concert
    }
    return render(request,"ticketSales/detail.html",context)
@login_required
def timesInfo(request):
    times=timeModel.objects.all()
    context={
        "times":times
    }
    return render(request,'ticketSales/sans.html',context)

def concertEditView(request,concert_id):
    cnrt=concertModel.objects.get(pk=concert_id)
    mda=settings.MEDIA_URL
    if request.method=="POST":
        concertForm=ConcertForm(request.POST,request.FILES,instance=cnrt)
        concertForm.save()

        return HttpResponseRedirect(reverse(concertListView))
    else:
        concertForm=ConcertForm(instance=cnrt)
    context={
            "concertForm":concertForm,
            "concert":cnrt,
            "poster":cnrt.Poster,
            "media":mda
            
        }
    return render(request,"ticketSales/concertEdit.html",context)

