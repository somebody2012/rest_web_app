#!/usr/bin/python
# -*- coding: UTF-8 -*-


EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '443135581@qq.com'  # 发件箱
EMAIL_HOST_PASSWORD = 'pdagirgkgrqubggc'  # 开启POP3/SMTP服务
SERVER_EMAIL = '443135581@qq.com'  # 与发件箱一致
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# ADMINS = [('John', '443135581@qq.com')]  # 邮件接收人，可以有多个
ADMINS = [('John', '443135581@qq.com')]  # 邮件接收人，可以有多个
EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
