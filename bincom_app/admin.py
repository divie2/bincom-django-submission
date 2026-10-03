from django.contrib import admin
from .models import State,LGA,Ward,PollingUnit,PollingUnitResult
admin.site.register([State,LGA,Ward,PollingUnit,PollingUnitResult])
