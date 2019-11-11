# devault-atm
A python ATM for DeVault\
\
USE AT OWN RISK!\

v. 0.01 - IS WHAT IT IS ALPHA\
Terminal only\
Known problems: delight wallet throws error if there are unconfirmed transactions

Hey! So this is my first python program. I sae the lightning ATM by @21isenough (https://github.com/21isenough/LightningATM)
and thought that I could do something like that for DeVault. One youtube tutorial w python basics later I started coding and this is the result.
You can find me in the DeVault Discord https://discord.gg/JnRZ7BB 

Pest

\
plans: gui, building the actual thing etc..
\
included example log file\
\
devault_atm.py
this is the app

\
delight.py\
talks to delight daemon\

qr.py\
reads qr codes w webcam using opencv and zbar

coinslot.py\
reads coinslot via USB encoder

coingecko_price.py\
has functions to get coinprice
