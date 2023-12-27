from scraper import Scraper
import csv
import concurrent.futures
from smtplib import SMTP_SSL

FILE = "flights.csv"
flights = []
sender = "disha.junkmail@gmail.com"

with open(FILE, 'r') as file:
    print("Loading...", end='', flush=True)
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        date, origin, dest, flnum, alert_price, email = row
        flights.append((date, origin, dest, flnum, int(alert_price), email))

def scrape_flight(idx):
    DATE, ORIGIN, DEST, FLNUM, alert_price, email = flights[idx]
    scraper = Scraper(DATE, ORIGIN, DEST, FLNUM)
    price = scraper.get_price()
    
    flights[idx] = (DATE, ORIGIN, DEST, FLNUM, alert_price, price, email)

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    flight_idxs = list(range(len(flights)))
    results = list(executor.map(scrape_flight, flight_idxs))

print("\r          ")
emails_sent = 0

try:
    connection = SMTP_SSL(host='smtp.gmail.com', port=465)
    connection.login(sender, "apoe qfms nkgu jjcg")

    for DATE, ORIGIN, DEST, FLNUM, alert_price, price, email in flights:
        output = f"{DATE} | {ORIGIN} -> {DEST} ({FLNUM}) ----- {alert_price} -> "

        if price is not None:
            alert_diff_txt = "" if price >= alert_price else f"     !!! BELOW ALERT !!!"
            output += f"{price}{alert_diff_txt}"
            if price < alert_price:
                emails_sent += 1
                connection.sendmail(sender, email, f"Subject: Flight Change Alert\n\n{output}")
        else:
            output += "<price unavailable>"
        print(output) 
    
    # -----for testing if the email sends correctly : everyday email triggers to self-----
    # if connection:
    #     message = f"Emails sent today were: {emails_sent}" if emails_sent > 0 else "No emails sent today."
    #     connection.sendmail(sender, sender, "Subject:Update For Flights Changed\n\n" +message)

finally:
    if connection:
        connection.close()