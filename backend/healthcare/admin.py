from django.contrib import admin
from .models import Choice, Question, Step

admin.site.register(Step)
admin.site.register(Choice)
admin.site.register(Question)

# Register your models here.
