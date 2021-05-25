from boltiot import Email
import requests, json, config


def send_mail(subject, body, ifprint = False):
    mailer = Email(config.MAILGUN_API_KEY, config.SANDBOX_URL, config.SENDER_EMAIL, config.RECIPIENT_EMAIL)
    response = mailer.send_email(subject, body)
    response_text = json.loads(response.text)

    if(ifprint):
        print(response_text)
    if response_text['message'] == 'Queued. Thank you.':
        return True
    else:
        return False


#send_mail("Hi", "Hello")
