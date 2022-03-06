import requests
import logging
from decouple import config

NOTIFICATION_API = config('NOTIFICATION_API')
NOTIFICATION_SENDER = config('NOTIFICATION_SENDER')
logger = logging.getLogger('django')


def create_and_send_mail(owner, url, domain_title):
    user_email = owner.email
    if not user_email:
        logger.warning(f"No mail found for {owner.username}!")
        return
    email_data = compose_email(user_email, url, domain_title)
    logger.debug(f"Sending email with data: {email_data}")
    send_mail(email_data)


def compose_email(recipient, url, domain_title):
    return {
        "template_name": "basic_template.html",
        "sender": NOTIFICATION_SENDER,
        "recipients": [recipient],
        "render_data": {"url": url, "domain_title": domain_title},
        "subject": f"Article Scrapper: Subject of interest found for your search of {domain_title}"
    }


def send_mail(mail_data):
    result = requests.post(NOTIFICATION_API, json=mail_data)
    if result.status_code != 200:
        logger.error('Failed to send notification!')
