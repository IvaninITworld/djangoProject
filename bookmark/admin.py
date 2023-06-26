from django.contrib import admin

from bookmark.models import Bookmark
# Register your models here.

# 테코레이터 패턴 x
# admin.site.regiter(Bookmark, BookmarkAdmin)

# 데코레인터 패턴 사용
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")