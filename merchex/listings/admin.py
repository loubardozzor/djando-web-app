from django.contrib import admin
from listings.models import Band
from listings.models import Listing
from listings.models import Contact

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')


admin.site.register(Listing, ListingAdmin)
admin.site.register(Contact)


# Register your models here.
