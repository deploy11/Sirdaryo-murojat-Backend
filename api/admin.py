from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from import_export import resources

class ResultResorcesS(resources.ModelResource):
    class Meta:
        model = Sorov
        fields = ['fish','idpassport','Yashashmanzili','mfynomi','kochanomi','telefonraqami','rasmvavidio','ariza_mazmuni','matn']

class ResultAdminS(ImportExportModelAdmin):
    list_display = ['fish','idpassport','Yashashmanzili','mfynomi','kochanomi','telefonraqami',]
    resource_class = ResultResorcesS

class ResultResorcesH(resources.ModelResource):
    class Meta:
        model = Hokimiyat

class ResultAdminH(ImportExportModelAdmin):

    resource_class = ResultResorcesH

admin.site.register(Sorov,ResultAdminS)

admin.site.register(Hokimiyat,ResultAdminH)
admin.site.register(Orinbosar)
admin.site.register(Tashkilotlar)