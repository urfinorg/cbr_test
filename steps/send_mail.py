import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail_by_yandex(username,password,toaddrs_list,msg_text,fromaddr=None,subject="Test mail",attachment_path_list=None):

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(username,password)
    
    msg = MIMEMultipart()
    sender = fromaddr
    recipients = toaddrs_list
    msg['Subject'] = subject
    
    if fromaddr is not None:
        msg['From'] = sender
        
    msg['To'] = ", ".join(recipients)
       
    if attachment_path_list is not None:
        for filename in attachment_path_list:
            try:              
                attachment = open(filename, "rb") 
                p = MIMEBase('application', 'octet-stream') 
                p.set_payload((attachment).read()) 
                encoders.encode_base64(p) 
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
                msg.attach(p) 
            except:
                print("could not attache file")
    
    msg.attach(MIMEText(msg_text,'html'))
    
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()