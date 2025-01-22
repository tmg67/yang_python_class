import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#cwgq abls ajdx bdtm app passwords

#email credentials
sender_email = "yangjitamang9@gmail.com"
receiver_email = "rumancha12@gmail.com"
password = "cwgq abls ajdx bdtm"

#craete the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email"

#email body
body = "hello, this a test email sent from python"
message.attach(MIMEText(body, "plain"))

#send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("email sent successfully!")
except Exception as e:
    print(f"error: {e}")