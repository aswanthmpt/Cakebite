from django.contrib import admin
from .models import Category,Subcategory,Product,Ads

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Subcategory,SubcategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','price','price_1kg','price_2kg','design_2price','category','image','image_2','image_3','image_4','desc','stock','available','weight','flavour','type','shape']
    list_editable=['price','category','price_1kg','price_2kg','design_2price','image','image_2','image_3','image_4','desc','stock','available','weight','flavour','type','shape']
    list_per_page=10
admin.site.register(Product,ProductAdmin)

class AdsAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Ads,AdsAdmin)
    