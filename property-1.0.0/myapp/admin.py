from django.contrib import admin
from .models import User,Member,Chairman,Watchman,Event,Notice,Visitor
# Register your models here.
admin.site.register(User)
admin.site.register(Member)
admin.site.register(Chairman)
admin.site.register(Watchman)
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(Visitor)
