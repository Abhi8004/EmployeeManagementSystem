from django.contrib import admin
from testapp.models import School,Student,User

# Register your models here.
#class UserManagerAdmin(admin.ModelAdmin):
    #list_display=('email','password')

class UserAdmin(admin.ModelAdmin):
    list_display=('school','studentgrade','email', 'phone', 'is_verified')

class SchoolAdmin(admin.ModelAdmin):
    list_display=('studentname','studentclass','email','city','pincode','password')
    search_fields=('studentname',)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','studentclass','email','rollno','studentgrade')
    list_filter=('studentclass',)
    search_fields=('name',)

admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)
#admin.site.register(UserManager,UserManagerAdmin)
admin.site.register(User,UserAdmin)
