from django import forms

from accounts.models import Tutor
from .tasks import prepare_email, send_email


class SendMailForm(forms.Form):
    recipient = forms.ModelChoiceField(
        Tutor.objects.order_by('last_name'),
        empty_label="Выберите получателя",
        label='',
        error_messages={'required': 'Выберите получателя'}
    )
    subject = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Тема'}),
        error_messages={'required': 'Напишите тему сообщения'}
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}),
        error_messages={'required': 'Напишите сообщение'}
    )

    def task_send_email(self, sender):
        to, subject, message = prepare_email(sender, **self.cleaned_data)
        send_email.delay(subject, message, to)
