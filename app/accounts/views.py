from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import UserCreationForm
from .models import User


class UserSignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name_suffix = "_signup"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('accounts:edit')
    template_name_suffix = "_edit"
    # template_name = "registration/edit.html"

    def get_object(self):
        return self.request.user

    def get_form_class(self):
        self.fields = ('first_name', 'last_name', 'gender',
                       'birth_date', 'city', 'img')
        if self.request.user.is_teacher:
            self.fields = self.fields + ('bio', )
        return super().get_form_class()

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно обновлен.')
        return super().form_valid(form)
