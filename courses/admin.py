from django.contrib import admin

from .models import Course, Lesson


class LessonsInline(admin.TabularInline):
    model = Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = LessonsInline,

    list_display = 'name', 'tutor'
    fields = 'name', 'tutor', 'description'
