from django.contrib import admin

# Register your models here.

from testapp.models import Truecomp
from testapp.models import Smart
from testapp.models import PDB
from testapp.models import DMS
# Register your models here.
class TruecompAdmin(admin.ModelAdmin):
    list_display=['TC','title','content','attendees','date']
admin.site.register(Truecomp,TruecompAdmin)

class SmartAdmin(admin.ModelAdmin):
    list_display=['TC','title','content','attendees','date']
admin.site.register(Smart,SmartAdmin)
class PdbAdmin(admin.ModelAdmin):
    list_display=['TC','title','content','attendees','date']
admin.site.register(PDB,PdbAdmin)
class DmsAdmin(admin.ModelAdmin):
    list_display=['TC','title','content','attendees','date']
admin.site.register(DMS,DmsAdmin)
