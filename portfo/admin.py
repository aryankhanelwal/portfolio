from django.contrib import admin
from portfo.models import contact_me,Post
from portfo.views import post_Detail
# Register your models here.

admin.site.register(contact_me)
admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}

