# devault-atm
A python ATM for DeVault\

v. 0.01 - IS WHAT IT IS ALPHA\
Terminal only\
Known problems: delight wallet throws error if there are unconfirmed transactions

Hey! So this is my first python program. I saw the lightning ATM by @21isenough (https://github.com/21isenough/LightningATM)
and thought that I could do something like that for DeVault. One youtube python basics tutorial later I started coding and this is the result.
You can find me in the DeVault Discord https://discord.gg/JnRZ7BB 

Pest

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Proof of concept vid of the DeVault ATM I am working on.<a href="https://twitter.com/DeVaultCrypto?ref_src=twsrc%5Etfw">@DeVaultCrypto</a> <a href="https://twitter.com/hashtag/devault?src=hash&amp;ref_src=twsrc%5Etfw">#devault</a> <a href="https://twitter.com/search?q=%24dvt&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$dvt</a> <a href="https://t.co/jcEZCQXlG5">pic.twitter.com/jcEZCQXlG5</a></p>&mdash; Pest (@pestdesmadre) <a href="https://twitter.com/pestdesmadre/status/1192302105219997696?ref_src=twsrc%5Etfw">November 7, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
