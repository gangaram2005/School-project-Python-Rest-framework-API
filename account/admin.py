from django.contrib import admin
from account.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Custom banako user lai register gareko
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email","name","tc","user_type", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc","user_type"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc","user_type", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email","name"]
    ordering = [ "id","name"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)

# Add class model admin
@admin.register(AddClass)
class ClassAdmin(admin.ModelAdmin):
    list_display=['id','name']
    
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display=['id','name','address']

admin.site.register(Shift)
admin.site.register(Grouptime)
admin.site.register(Year)
admin.site.register(Branch)
admin.site.register(Subject)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','title','description','duration']

