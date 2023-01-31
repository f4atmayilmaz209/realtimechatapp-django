from django.contrib import admin
from .models import Profile,Friend,ChatMessage


admin.site.register([Profile,Friend,ChatMessage])