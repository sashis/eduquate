from celery import shared_task
from django.core.mail import mail_admins, send_mail


def make_message_header(sender, recipient):
    header = [
        f'From: {sender.get_full_name()} <{sender.email}>',
        f'To: {recipient.get_full_name()} <{recipient.email}>'
    ]
    header_width = max(map(len, header))
    header.append('-' * header_width)
    return '\n'.join(header)


def prepare_email(sender, recipient=None, subject='', message=''):
    message_header = make_message_header(sender, recipient)
    return (
        recipient.email,
        subject,
        f'{message_header}\n{message}'
    )


@shared_task
def send_email(subject, body, recipient):
    send_mail(subject, body, None, [recipient])
    mail_admins(subject, body)
