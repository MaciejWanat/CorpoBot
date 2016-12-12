from rivescript import RiveScript
from polDel import polishDel

import datetime
import re

logs = open("logs.txt","a")
now = datetime.datetime.now()

bot = RiveScript(utf8=True)
bot.unicode_punctuation = re.compile(r'[.,!?;:]')
bot.load_directory("./resources")
bot.sort_replies()

print("Witaj! Mam na imię CorpoBot i moim zadaniem jest przybliżyć Ci ofertę firmy Corpo. Możemy też trochę pogadać.\n"
      "Jeśli Ci się znudzi, po prostu wpisz 'koniec'!\n"
      "Jeśli brakuje Ci pomysłu, o czym moglibyśmy pogadać, poproś mnie o pomoc.\n"
      "Czy chcesz abym przedstawił Ci naszą ofertę?")

'''
print("Witaj! Mam na imię MusicoBot i chciałbym pogadać z Tobą o muzyce. Jaki jest twój ulubiony gatunek?")
'''
logs.write((now.strftime("%Y-%m-%d %H:%M"))+"\n\n") #date of conversation time

while True:

    msg = input('Ty > ')
    logs.write("Użytkownik > \t" + msg + "\n") # logs write
    msg = polishDel(msg)
    msg = re.sub(r':[\)*\(]', "", msg)

    #print("\nNapisałeś : '" + msg + "'\n")
    if msg == 'koniec':

        logs.write("\n---------------------------------\n\n")
        logs.close()
        quit()

    reply = bot.reply("localuser", msg)

    logs.write("CorpoBot   > \t" + reply + "\n") # logs write
    print(reply)

