from django.contrib import admin
from .models import Contact,Dummy,Solution

# Register your models here.
admin.site.site_header='EDTECH'
admin.site.site_title='EDTECH ADMIN'
admin.site.index_title='OVERVIEW'
admin.site.register(Contact)
admin.site.register(Dummy)
admin.site.register(Solution)