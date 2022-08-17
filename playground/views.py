from django.core.mail import EmailMessage, BadHeaderError,mail_admins, send_mail
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

def say_hello(request):
    try: 
        message = BaseEmailMessage(
            template_name = 'emails/hello.html',
            context = {'name': 'selena'},
        )
        message.send(['selena@byby.com'])       
    except BadHeaderError:
        pass

    # try: 
    #     message = EmailMessage('subject', 'messgae', 'info@kimkim.com',['selna@attachedfile.com'])
    #     message.attach_file('playground/static/images/dog.jpg')
    #     message.send()
    # except BadHeaderError:
    #     pass
    return render(request, 'hello.html', {'name': 'hehe'})
