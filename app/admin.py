from django.contrib import admin
from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'date', 'salary')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ['title', 'description', 'salary'] # can also use tuple
    search_help_text = "Enter your parameter(s)"
    #fields = (('title', 'description'), 'expiry', 'salary') #specific fields to display OR...
    #exclude = ('title',)  # all fields excluding these.
    #fieldsets
    fieldsets = (
        ('Basic Information', {
            'fields' :('title', 'description')
        }),
        ('More information', {
            'classes':('collapse', 'wide'),
            'fields':(('expiry', 'salary'), 'slug') #like fields in a tuple will group together)
        })
    )

# Register your models here.
admin.site.register(JobPost, JobAdmin)
