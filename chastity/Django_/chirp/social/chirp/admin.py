from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Chirp

# Unregister Groups
admin.site.unregister(Group)

# Mix Profile info into User Info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    mode = User
    # Just display username fileds on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)


# Register Chirp
admin.site.register(Chirp) 