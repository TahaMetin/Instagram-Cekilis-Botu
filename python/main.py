import InstagramBot
import random
import time
from datetime import datetime

linkler = []
begenildi = []
bitisTarihleri = []
cekilisiYapaninTakipEttikleriniTakipEtList = []
cekilisiYapaninTakipEttikleriniTakipEttinMi = []
yorumBasiEtiketlemeler = []
f = open("çekilişler.txt", 'r')
for line in f:
    if line == "\n":
        break
    x = line.rpartition('|')
    cekilisiYapaninTakipEttikleriniTakipEttinMi.append(x[2].strip("\n"))
    x = x[0].rpartition('|')
    cekilisiYapaninTakipEttikleriniTakipEtList.append(x[2])
    x = x[0].rpartition('|')
    bitisTarihleri.append(x[2])
    x = x[0].rpartition('|')
    begenildi.append(x[2])
    x = x[0].rpartition('|')
    yorumBasiEtiketlemeler.append(x[2])
    x = x[0].rpartition('|')
    linkler.append(x[2])

f.close()

while True:
    girilmisLink = False
    linkInput = input("Çekiliş postunun linkini gir (girecek link kalmadığında 0 gir) : ")
    for link in linkler:
        if link == linkInput:
            print('Bu link daha önce girilmiş.')
            girilmisLink = True
    if(girilmisLink):
        continue
    if linkInput == '0':
        break
    begenildi.append('h')
    bitisTarihi = input("Çekilişin açıklanma/bitiş tarihini gir ( 06/11/2001 formatında) : ")
    cekilisiYapaninTakipEttikleriniTakipEt = input("Çekilişi yapanın takip ettiklerini takip etmek gerekiyor mu ? (E/H) : ")
    yorumBasiEtiketleme = input("Her yorumda kaç kişi etiketlenmeli? :")
    cekilisiYapaninTakipEttikleriniTakipEtList.append(cekilisiYapaninTakipEttikleriniTakipEt)
    linkler.append(linkInput)
    bitisTarihleri.append(bitisTarihi)
    yorumBasiEtiketlemeler.append(yorumBasiEtiketleme)
    cekilisiYapaninTakipEttikleriniTakipEttinMi.append('h')
    print("-----------------------------------------------------------------")


f= open("çekilişler.txt", 'w')

for i in range(len(linkler)):
    f.write(linkler[i]+'|')
    f.write(yorumBasiEtiketlemeler[i]+'|')
    f.write(begenildi[i]+'|')
    f.write(bitisTarihleri[i]+'|')
    f.write(cekilisiYapaninTakipEttikleriniTakipEtList[i]+'|')
    f.write(cekilisiYapaninTakipEttikleriniTakipEttinMi[i])
    f.write("\n")

f.close()

print("Bot çalışmaya başladı")

bot = InstagramBot.InstagramBot('yildiznisaaa', 'instagramçekiliş')
bot.signIn()

while 1:
    for i in range(len(linkler)):
        if 'h' == begenildi[i]:
            bot.likePost(linkler[i])
            begenildi[i] = 'e'
        if cekilisiYapaninTakipEttikleriniTakipEtList[i].upper() == 'E' and 'h' == cekilisiYapaninTakipEttikleriniTakipEttinMi[i]:
            bot.goPosterProfile()
            bot.followPosterFollowings()
            cekilisiYapaninTakipEttikleriniTakipEttinMi[i] = 'e'
        bot.comment(linkler[i], yorumBasiEtiketlemeler[i])
    randomSleepTime = random.randint(180, 420)
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")
    print(dt_string, end='--> ')
    print("sonraki yorum " + str(int(randomSleepTime / 60)) + " dakika " + str(randomSleepTime % 60) + " saniye sonra atılacak")
    f = open("çekilişler.txt", 'w')

    for i in range(len(linkler)):
        f.write(linkler[i] + '|')
        f.write(yorumBasiEtiketlemeler[i] + '|')
        f.write(begenildi[i] + '|')
        f.write(bitisTarihleri[i] + '|')
        f.write(cekilisiYapaninTakipEttikleriniTakipEtList[i] + '|')
        f.write(cekilisiYapaninTakipEttikleriniTakipEttinMi[i])
        f.write("\n")

    f.close()
    time.sleep(randomSleepTime)


bot.closeBrowser()


