from django.shortcuts import render

# Create your views here.
from .models import Image

def location (request,id):
    location=Image.filter_by_location(id=id)
    print(location)
    locate=Location.objects.all()
    return render(request,'location.html',{"location":location,'locate':locate})



def welcome(request):
    images=Image.get_all_image()
    return render(request,'welcome.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        searched_photos=Image.search_by_category(search_term)
        message=f"{search_term}"
        print(searched_photos)
        return render(request,"search.html",{"message":message,"photos":searched_photos})
    else:
        message="you have no seach Photo"
        return render(request,'search.html',{"message":message})

def image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render (request,"all-photo/image.html",{"image":image})

def filter_by_location(request,location_id):
    images=Image.filter_by_location(id=location_id)
    return render(request,'location.html',{"images":images})
