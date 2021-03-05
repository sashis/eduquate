from django.contrib import admin

from .models import CourseSubscription, LearningProgress


class LearningProgressInline(admin.TabularInline):
    model = LearningProgress

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'lesson':
            pk = request.resolver_match.kwargs['object_id']
            subscription = CourseSubscription.objects.get(pk=pk)
            kwargs['queryset'] = subscription.course.lessons
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = LearningProgressInline,

    def get_inlines(self, request, obj):
        return super().get_inlines(request, obj) if obj else []
