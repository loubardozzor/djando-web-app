from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands' : bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band}) # nous passons l'id au modèle
    

def about(request):
    return render(request, 'listings/about.html')

def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings_list.html',
                  {'listings' : listings})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing' : listing})



def contact(request):
    return render(request, 'listings/contact.html')
