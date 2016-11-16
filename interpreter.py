from rivescript import RiveScript
from polDel import polishDel

import re

bot = RiveScript(utf8=True)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("./resources")
bot.sort_replies()

print("Witaj! Mam na imię CorpoBot i moim zadaniem jest przybliżyć Ci ofertę firmy Corpo. Możemy też trochę pogadać.\n" \
      "Jeśli Ci się znudzi, po prostu wpisz 'Koniec'!\n"
      "W czym mogę Ci pomóc?")
while True:

    msg = polishDel(input('Ty > '))\
#   print("napisałeś '" + msg + "'")
    if msg == 'Koniec':
        quit()

    reply = bot.reply("localuser", msg)
    print('', reply)
