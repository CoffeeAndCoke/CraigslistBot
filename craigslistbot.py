# -*- coding: utf-8 -*-
import sys, json
import bs4
import requests
import re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


if len(sys.argv) > 1:
    address = (sys.argv[1])
else:
    print "ERROR!"
    print "Usage: python script.py URL"
    sys.exit(1);


craigslist = requests.get(address)
craigslist.raise_for_status()
soup = bs4.BeautifulSoup(craigslist.text, "html.parser")
type(soup)

#grab the dates and the titles of the craigslist posts
postDate = soup.findAll("time", { "class" : "result-date" })
postTitle = soup.findAll("a", {"class": "result-title hdrlnk"})

#convert the times into datetime objects and save to a stackDate
#save the post title in a seperate stack
stackDates = []
stackTitles = []
for x in range(0, 5):
    st = (re.search('datetime="(.+?)" title', str(postDate[x])).group(1))
    postDateTimeObj = datetime.strptime(st , '%Y-%m-%d %H:%M')
    stackDates.append(postDateTimeObj)
    stackTitles.append(str(postTitle[x].get_text()))

text = ""
print "Here are the top 5 software posts:\n"
for x, y in zip(stackDates, stackTitles):
    text += "Time Posted: " + (str(x) + "\nTitle: " + (y) + "\n\n")
print text


me = raw_input("Please enter your email address: ")
password = raw_input("Please enter your email password: ")
you = raw_input("Please enter the email to which to send the results: ")

msg = MIMEText(text)
msg['Subject'] = "Top 5 Software Job Post from Austin's Craigslist"
msg['From'] = me
msg['To'] = you


server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(me, password)
server.sendmail(me, [you], msg.as_string())
print "email sent!"
server.quit()
