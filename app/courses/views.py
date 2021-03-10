from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from courses.models import Course


class TutorAccessMixin(UserPassesTestMixin):
    permission_denied_message = 'logged-in user must be a tutor'

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_tutor


class CourseListView(generic.ListView):
    model = Course


class CourseDetailView(generic.DetailView):
    model = Course


class IndexPageView(CourseListView):
    template_name = 'courses/index.html'

    def get_queryset(self):
        return self.model.objects.with_rating(ordered=True)[:3]


class CourseCreate(TutorAccessMixin, generic.CreateView):
    model = Course
    fields = 'name', 'description'

    def form_valid(self, form):
        form.instance.tutor = self.request.user.tutor
        messages.success(self.request, 'Вы успешно создали курс!')
        return super().form_valid(form)


class CourseUpdate(TutorAccessMixin, generic.UpdateView):
    model = Course
    fields = 'name', 'description'

    def form_valid(self, form):
        messages.success(self.request, 'Изменения сохранены!')
        return super().form_valid(form)


class CourseDelete(TutorAccessMixin, generic.DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Курс удалён.')
        return super().delete(request, *args, **kwargs)
