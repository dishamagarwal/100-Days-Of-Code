run the following in your terminal to set up automated scripting everyday at 3AM

~ crontab -e
~ 0 3 * * * //Users/username/file/path/flight_tracker/app.py

Running TODO:

1. Instead of putting in your flight info just put in your PNR and have it look it up (theres an open source lib for this - https://github.com/iangcarroll/pnrsh), then you can just add flight # alternatives and it infers the origin/dest/date based on the PNR
so i.e. instead of inputting
2024-1-5 JAX-NYC DL000 you can just give your PNR and a list of alternatives like
ABC123,DL001,DL002,DL003

#1 gets bonus points if instead of enumerating alternatives you can write some custom filters in a basic DSL

More bonus points if I can compose those filters

2. ⁠For only the flight you actually booked (I.e. have a PNR for) it should try to automatically submit this form for you the day after https://www.delta.com/bagsontime — not sure how hard it is to scrape bag logs but at minimum you can just spam it every time