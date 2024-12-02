import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email():
    message = Mail(
        from_email='joell848@gmail.com',  # 替換為您的發件人電子郵件
        to_emails='joell848@gmail.com',  # 替換為收件人電子郵件
        subject='Hello from SendGrid',
        plain_text_content='This is a test email sent from GitHub Actions using SendGrid.',
        html_content='<strong>This is a test email sent from GitHub Actions using SendGrid.</strong>'
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f'Email sent! Response status code: {response.status_code}')
        print(f'Response body: {response.body}')
        print(f'Response headers: {response.headers}')
    except Exception as e:
        print(f'Error sending email: {e}')

if __name__ == '__main__':
    send_email()
