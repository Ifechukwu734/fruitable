import smtplib
sender_email = 'ifechukwuaugustine61@gmail.com'
app_password = 'bhaxxbgyzqddsbml' 
message = 'This is a dummy email'
receiver = ['ifechukwuraphael30@gmail.com']

try:
    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Use SSL
    smtp_obj.ehlo()  # Identify yourself to the server
    print("Connection established successfully!")
    smtp_obj.login(sender_email, app_password)
    smtp_obj.sendmail(sender_email, receiver , message )
except smtplib.SMTPConnectError as e:
    print(f"Error: {e}. Unable to connect to the SMTP server.")
except Exception as e:
    print(f"Error: {e}")




