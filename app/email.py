from flask_mail import  Message
# from flask_module import Module
# from flask.ext.mail import Mail, Message
from flask import render_template
from . import mail


def mail_message(subject, template, to, **kwargs):
    '''
    
    '''
    sender_email = "calebkimutai@gmail.com"

    email = Message(subject, sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)