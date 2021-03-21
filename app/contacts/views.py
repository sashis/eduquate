from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SendMailForm


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'contacts/contacts.html'
    form_class = SendMailForm
    success_url = reverse_lazy('courses:list')

    def form_valid(self, form):
        form.task_send_email(self.request.user)
        recipient = form.cleaned_data['recipient']
        messages.success(self.request, f'Сообщение для {recipient} добавлено в очередь на отправку.')
        return super().form_valid(form)
