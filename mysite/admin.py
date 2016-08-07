from django.contrib import admin
from mysite.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('product','pub_date')
    list_filter =('pub_date',)
    search_fields = ('product','description')

admin.site.register(Post, PostAdmin)

