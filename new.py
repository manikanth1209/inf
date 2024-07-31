
import smtplib
def send_simple_email(sender_email, sender_password, recipient_email, subject, body):
    email_message = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, email_message)
    server.quit()
    print("Email sent successfully!")

sender_email = "manikanthyadav218@gmail.com"
sender_password = "vuyi rtei gcwd kzgg"
recipient_email = "dbsreddy3@gmail.com"
subject = "akka bagundha Bava"
body = "This is a test.json email sent from gayatri "
send_simple_email(sender_email, sender_password, recipient_email,subject,body)
