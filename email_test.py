import sys,re,time,itchat,os
from itchat.content import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
buff = []
max_length = 5
mail_host="smtp.163.com"
mail_user="billvace@163.com"    
mail_pass="Tigerlele1"  #SMTP 授权密码
sender = 'billvace@163.com'
receivers = '1847069979@qq.com'
Keys = ["贝贝","急","作业","EE","IA"]
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True, isGroupChat=False, isMpChat=False)
def personal_msg(msg):
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    msg_time = msg['CreateTime']
    msg_id = msg['MsgId']
    msg_content = None
    msg_share_url = None
    if msg['Type'] == 'Text' or msg['Type'] == "Friends":
        full_message = msg_time_rec + "  " + msg_from + ' send a ' + msg['Type'] + ' : ' + msg['Text']
        for key in Keys:
            if key in msg['Text']:
                buff.append(full_message)
    if len(buff) >= max_length:
        mail(buff)
def mail(msg):
    msg = msg[0]+'\n'+msg[1]+'\n'+msg[2]+'\n'+msg[3]+'\n'+msg[4]
    message = MIMEText(msg, 'plain', 'utf-8')
    message['from'] = 'billvace@163.com'
    message['to'] =  '1847069979@qq.com'
    subject = 'Notice'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
itchat.auto_login(hotReload=True)
itchat.run()
