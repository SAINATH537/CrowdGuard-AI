from django.contrib import admin

from .models import AlarmHistory, Anomaly, User

admin.site.register(User)
admin.site.register(Anomaly)
admin.site.register(AlarmHistory)
