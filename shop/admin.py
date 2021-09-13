from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Race)
admin.site.register(SellAPet)
admin.site.register(SitAPet)
admin.site.register(SellFood)
admin.site.register(DonateAPet)