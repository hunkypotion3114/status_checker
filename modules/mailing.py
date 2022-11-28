import email.message as msg
import smtplib

def mail_sender(reciever,message):
    # Create message container     
    new_msg = msg.EmailMessage()
    new_msg.add_header("From","sender@outlook.com")
    new_msg.add_header("To",reciever)
    new_msg.set_content(message)
    
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    except Exception as e:
        print(e)
        server = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
    # Identify connection with gmail client     
    server.ehlo()
    # Start TLS Encryption     
    server.starttls()
    # Re-identify with gmail client - and login     
    server.ehlo()
    server.login("sender@outlook.com",'PASSWORD') # May use dot env to make it more secure..
    # Send mail     
    server.sendmail("sender@outlook.com",reciever,new_msg.as_string())
    print("Mail Sent")
    # Quit server     
    server.quit()