import sib_api_v3_sdk
import os
import environ
from django.template.loader import render_to_string
from sib_api_v3_sdk.rest import ApiException
environ.Env.read_env(os.path.join("Portfolio/.env"))


def init_smpt_service():
    configuration = sib_api_v3_sdk.Configuration()

    configuration.api_key[
        "api-key"] = os.environ.get("SEND_IN_BLUE_API_KEY")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    return api_instance


def send_email(form_details):
    receiver_email = os.environ.get("RECEIVER_EMAIL")
    receiver_name = os.environ.get("RECEIVER_NAME")

    sender_name = form_details.POST.get('full_name')
    sender_email = form_details.POST.get('email')

    email_subject = form_details.POST.get('subject')

    html = render_to_string(
        "partials/sub-partials/contactform.html", {
            "name": sender_name,
            "mobile": form_details.POST.get("from_mobile"),
            "website": sender_email,
            "message": form_details.POST.get('message'),
        }
    )

    sender = {"name": sender_name, "email": sender_email}
    to = [{"email": receiver_email, "name": receiver_name}]
    headers = {"Website enquiry": "contact form"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, headers=headers, html_content=html, sender=sender, subject=email_subject)
    try:
        init_smpt_service().send_transac_email(send_smtp_email)
        return True
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        return False

