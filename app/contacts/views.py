from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SendMailForm


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'contacts/contacts_email.html'
    form_class = SendMailForm
