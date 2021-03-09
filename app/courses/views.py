from django.views import generic

from courses.models import Course


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link_enabled'] = True
        return context


class IndexPageView(CourseListView):
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.with_rating(ordered=True)[:3]