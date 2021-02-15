from django.contrib import admin

from .models import CourseSubscription, LearningProgress


class CourseProgressInline(admin.TabularInline):
    model = LearningProgress


@admin.register(CourseSubscription)
class SubscriptionAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = CourseProgressInline,

