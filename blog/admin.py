from django.contrib import admin

from blog.models import Post


# Register your models here.
# 데코레이터를 사용하지 않을 경우
# admin.site.register()

# 데코레이터 사용
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Post 객체를 보여줄 때, id, title, modify_dt 를 화면에 출력하라고 지정한다.
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
