from django.contrib import admin
from .models import Module, Job, Skill, Recommendation, AdminRequest, Message, Chat
# Register your models here.
admin.site.register(Module),
admin.site.register(Job),
admin.site.register(Skill),
admin.site.register(Recommendation),
admin.site.register(AdminRequest),
admin.site.register(Message),
admin.site.register(Chat)

