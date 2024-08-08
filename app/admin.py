from django.contrib import admin
from .models import ChaiVariety, ChaiReviews, store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('ChaiVarieties', )
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
