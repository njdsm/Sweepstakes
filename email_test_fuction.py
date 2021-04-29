import smtplib


def email_contestants(email, message, sweepstakes_name, fullname):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            # Enter your companies email and password here to send emails.
            smtp.login('njdsmtest@gmail.com', '%^TY56ty%^TY56ty')

            msg = f'Subject: {sweepstakes_name}\n\nHello {fullname}. Below are the results of the contest\n\n{message}'
            smtp.sendmail("njdsm@gmail.com", email, msg)
    except:
        print("Email address not valid")
