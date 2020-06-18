from django.contrib import admin

from profiles_api import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Club, models.ClubAdmin)
admin.site.register(models.role)
