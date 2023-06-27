from django.contrib import admin

from blog.models import Post


# Register your models here.
# 데코레이터를 사용하지 않을 경우
# admin.site.register()

# 데코레이터 사용
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt') # Post 객체를 보여줄 때, id, title, modify_dt 를 화면에 출력하라고 지정한다.
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

