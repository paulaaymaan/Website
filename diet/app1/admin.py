from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Survey,DietPlan

class SurveyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Survey, SurveyAdmin)

admin.site.register(DietPlan)