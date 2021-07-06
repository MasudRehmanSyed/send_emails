import smtplib, random as rd, datetime as dt, pandas as pd
from pathlib import Path


my_email = MY_EMAIL
pass = MY_PASSWORD
# access mailbox create an object
letter_number = f'./letter_templates/letter_{rd.randint(1,3)}.txt'
file = open('quotes.txt', 'r')
quotes_list = [l for l in file]
file.close()
qoute = ''.join(rd.choice(quotes_list))
now = dt.datetime.now()
year = now.year
this_month = now.month
hour = now.hour
bday_letter = None
day_of_week = now.weekday()
today = now.day


def send_email(wishes, email):
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        # secure connection transport layer security tls
        connection.starttls()
        connection.login(user=my_email, password=pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f'Subject:Surprise\n\n{wishes}')


def read_letter(name):
    letter = Path(letter_number).read_text()
    letter = letter.replace('[NAME]', name)
    return letter


df = pd.read_csv('birthdays.csv')

t = df.loc[(df.month == this_month) & (df.day == today)]
new_letter = read_letter(t.name.to_string(index=False))
new_email = t.email.to_string(index=False)
print(new_letter, new_email)
send_email(wishes=new_letter, email=new_email)
