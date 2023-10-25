from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields': ['message']})
	]
	list_displat = ('message')

admin.site.register(Message, MessageAdmin)
# Register your models here.
