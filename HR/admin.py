from django.contrib import admin
from .models import Tutor
from .models import Graduation
from .models import Subject
from .models import Education


class TutorAdmin(admin.ModelAdmin):
    fields = ['name', 'gender', 'subject_teach', 'education', 'region', 'time']
        
#class GraduationAdmin(admin.ModelAdmin):
    
class SubjectAdmin(admin.ModelAdmin):
    fields = ['title', 'level']
#class EducationAdmin(admin.ModelAdmin):

admin.site.register(Tutor, TutorAdmin)
admin.site.register(Graduation)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Education)

