from flask_babel import _
from app.email import send_email
from flask import render_template, current_app


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset Your Password'),
               sender='2965047454@qq.com',
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
