from django.contrib import admin

# Register your models here.
from .models import Post,Comment

class CommentInline(admin.TabularInline):
    model=Comment
    extra = 5
    min_num=3
    max_num=5
    verbose_name='댓글'
    

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=('id','image','content','create_at','view_count','writer')
    list_filter=('create_at',)
    search_fields=('id','content')
    readonly_fields=('create_at',)
    inlines=[CommentInline]
    actions=['make_published']
    
    def make_published(modeladmin,request,queryset):
        for item in queryset:
            item.content='운영 규정 위반으로 인한 게시글 삭제 처리'
            item.save()

#admin.site.register(Comment)
