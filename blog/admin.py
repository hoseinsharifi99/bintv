from django.contrib import admin

from blog.models import Post, Rating


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)

class RatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rating, RatingAdmin)