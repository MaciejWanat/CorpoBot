from rivescript import RiveScript
from polDel import polishDel

import re

bot = RiveScript(utf8=True)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("./resources")
bot.sort_replies()

print("Witaj! Mam na imię CorpoBot i moim zadaniem jest przybliżyć Ci ofertę firmy Corpo. Możemy też trochę pogadać.\n"
      "Jeśli Ci się znudzi, po prostu wpisz 'koniec'!\n"
      "Jeśli brakuje Ci pomysłu, o czym moglibyśmy pogadać, poproś mnie o pomoc.\n"
      "W czym mogę Ci pomóc?")

while True:

    msg = input('Ty > ')
    msg = polishDel(msg)
    msg = re.sub(r':[\)*\(]', "", msg)

    if msg == 'koniec':
        quit()

    reply = bot.reply("localuser", msg)

    print(reply)

