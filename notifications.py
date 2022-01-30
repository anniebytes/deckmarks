import os
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_text(notification_message):
    message = client.messages \
    .create(
         body=notification_message,
         from_='+17755263551',
         to='+17142310526'
     )
    print(message.sid)

def send_email(notification_message):
    message = Mail(
        from_email='anniebytes@gmail.com',
        to_emails='isthiscode@gmail.com',
        subject='Deckmarks Notification',
        html_content=f'<strong>{notification_message}</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)