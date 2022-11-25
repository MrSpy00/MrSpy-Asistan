from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
import webbrowser
import psutil
from plyer import notification
import time
import pywhatkit as k
import feedparser


r = sr.Recognizer()

    
def record(ask=False):
    playsound("dosyalar/DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice
    
    
def ingrecord(ask=False):
    playsound("c:\\Users\\PC\\OneDrive\\Masaüstü\\MrSpy_Asistan\\dosyalar/DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice
    
 
    
def almrecord(ask=False):
    playsound(r"c:\\Users\\PC\\OneDrive\\Masaüstü\\MrSpy_Asistan\\dosyalar/DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="de-DE")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice
    


def response(voice):
    if "merhaba" in voice:
        sozler = ["Sanada merhaba",
                "Merhabalar nasılsınız",
                "Merhaba hoşgeldin",
                "I have boyfriend",
                
        ]
        secim = choice(sozler)

        speak(secim)
        
    if "selam" in voice or "selamlar" in voice or "Selam" in voice or "Selamlar" in voice:
        sozler = ["Sana da selam",
                "Selam nasılsın",
                "Merhabalar selam",
                "Selam",
                
        ]
        secim = choice(sozler)

        speak(secim)
        
    if "Selamün aleyküm" in voice or "Selamünaleyküm" in voice or "selamün aleykün" in voice or "selamünaleyküm" in voice:
        sozler = ["Aleyküm selam nasılsın",
                "As nasılsın ",
                "Ve aleykümesselam nasılsınız efendim",
                "Aleyküm selam",
                
        ]
        secim = choice(sozler)

        speak(secim)
        
    if "hoşbuldum" in voice or "hoş buldum" in voice or "Hoş buldum" in voice or "Hoşbuldum" in voice:
        sozler = ["Naber ne var ne yok",
                "Youtube'da bişiler izlemek ister misin",
                "Google'da bişiler aratmak ister misin",
                "Nasılsın",
                
        ]
        secim = choice(sozler)

        speak(secim)    
        
    if "naber" in voice or "ne haber" in voice:
        sozler = ["senden naber",
                "benden bi haber senden naber",
                "ne naber",     
        ]
        secim = choice(sozler)
        speak(secim)
        
    if "beni duyuyor musun" in voice:
        sozler = ["evet seni duyuyorum",
                "evet",
                "tabii ki seni duyuyorum",
                "Anlayamadım, şakaydı seni duyuyorum hahahaha",
                "buna cevap verdiğime göre",
                "buna cevap veriyorsam seni duymuyorum demektir",
                "sence duyuyor muyum",
                "seni duymamı ister misin",
                "bilmem duyuyor muyum",     
        ]
        secim = choice(sozler)
        speak(secim)
        
    if "nasılsın" in voice:
        sozler = ["iyilik benden ya sen",
                "iyi ben peki ya sen",
                "iyi olduğumu duyarsan sevinicek misin",
                "Sağolasın iyiyim sen nasılsın",       
        ]
        secim = choice(sozler)
        speak(secim)
        
    if "youtube aç" in voice:
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        sozler = ["Youtube ana sayfası açıldı",
                "Al sana youtube",
                "İyi seyirler dilerim",
                "sen you ben tube, hahahaha",       
        ]
        secim = choice(sozler)
        speak(secim)
        
    if "google aç" in voice:
        url = "https://www.google.com/"
        webbrowser.get().open(url)    
        speak("Buyrun google ana sayfası")
    if "çeviriyi aç" in voice:
        url = "https://translate.google.com/?hl=tr"
        webbrowser.get().open(url)    
        speak("Çeviri açıldı. İyi çeviriler")
    if "github aç" in voice or "githabı aç" in voice or "git hap aç" in voice or "habı aç" in voice or "git hava aç" in voice or "git hat aç" in voice:
        url = "https://github.com"
        webbrowser.get().open(url)    
        speak("Github açıldı. Kolay gelsin")
    if "türk siber tayfa sayfası" in voice or "türk siber tayfa" in voice or "türk siber ekibi" in voice: # Asistanın en rahat anladığı kelimeler bunlardı :D
        url = "https://www.turkhackteam.org/"
        webbrowser.get().open(url)   
        speak("Türk siber tayfa resmi sayfası")
    if "mp3 çevirici aç" in voice or "mp3 çevirici" in voice:
        url = "https://flvconverter.org/"
        webbrowser.get().open(url)
        speak("Al sana mp3 çevirici")
    if "mp4 çevirici aç" in voice or "mp4 çevirici" in voice:
        url = "https://en.y2mate.is/"
        webbrowser.get().open(url) 
        speak("İşte mp4 çevirici")
        
    # OYUNLAR  
        
    if "oyun 1 başlat" in voice or "human fall başlat" in voice:
        os.startfile("steam://run/477160")
        speak("Human Fall Flat Başlatılıyor.")
    if "oyun 2 başlat" in voice or "just cause 2 başlat" in voice:
        os.startfile("steam://run/8190")
        speak("Just Cause 2 Başlatılıyor.")
    if "oyun 3 başlat" in voice or "Left 4 Dead 2 başlat" in voice or "l4d2 başlat" in voice or "l4d 2" in voice:
        os.startfile("steam://run/550")
        speak("Left 4 Dead 2  Başlatılıyor.")
    if "oyun 4 başlat" in voice or "geometry dash başlat" in voice or "geometri ders başlat" in voice or "geometri ders passat" in voice or "geometri test başlat" in voice or "geometri test passat" in voice:
        os.startfile("steam://run/322170")
    if "oyun 5 başlat" in voice or "gta 5 başlat" in voice or "gta v başlat" in voice or "gta v passat" in voice or "gta 5 passat" in voice:
        os.startfile("steam://run/271590")
    
    
    # OYUNLAR
    
    if "hesap makinesi" in voice or "makineyi aç" in voice or " hesp makinesini aç" in voice or "hesap makinesini çalıştır" in voice or " hesap makinesini başlat" in voice:
        os.startfile("dosyalar\hes_mak.exe") # Asistan için yaptığım mini hesap makinesi 
  
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "bu gün nasılsın" in voice:
        speak("İyiyim teşekkürler sen nasılsın?")
    if "iyiyim" in voice:
        speak("Hep iyi ol")
    if "kötüyüm" in voice:
        speak("Buna üzüldüm")
    if "görüşürüz" in voice or "bay bay" in voice or "kapan" in voice or "baybay" in voice:
        speak("görüşürüz")
        os.system("TASKKILL /F /IM MrSpy_Asistan.py")
        
    if "söylediğim her şeyi not et" in voice:
        speak("Dosya ismi ne olsun?")
        txtfile = record() + ".txt"
        speak("Hangi dilde kayıt istiyorsun?")
        dil = record()
        dil = dil.lower()
        if "türkçe" in dil:
            speak("Söylemeye başlayabilirsin.")
            while True:
                thetxt = record()
                if "not yazmayı bitir" in thetxt:
                    speak("Not tutma işlemi sonlandırıldı.")
                    f.close()
                    os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
                f = open("notlar/"+txtfile, "a", encoding="utf-8")
                f.writelines(thetxt+" ")
        if "almanca" in dil:
            speak("Söylemeye başlayabilirsin.")
            while True:
                thetxt = almrecord()
                if "not yazmayı bitir" in thetxt:
                    speak("Not tutma işlemi sonlandırıldı.")
                    f.close()
                    os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
                f = open("notlar/"+txtfile, "a", encoding="utf-8")
                f.writelines(thetxt)
        if "ingilizce" in dil:
            speak("Söylemeye başlayabilirsin.")
            while True:
                thetxt = ingrecord()
                if "not yazmayı bitir" in thetxt:
                    speak("Not tutma işlemi sonlandırıldı.")
                    f.close()
                    os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
                f = open("notlar/"+txtfile, "a", encoding="utf-8")
                f.writelines(thetxt)


    if "not al" in voice:
        speak("Dosya ismi ne olsun?")
        txtfile = record() + ".txt"
        speak("Ne not tutmamı istersin?")
        thetxt = record()
        f = open("notlar/"+txtfile, "w", encoding="utf-8")
        f.writelines(thetxt)
        f.close()
        speak("İstediğin notu aldım")
        
    if "not oku" in voice:
        speak("Hangi dosyayı okim")
        txtfile = record() + ".txt"
        notes = os.listdir(r"notlar/")
        icermek = notes.__contains__(txtfile)
        if icermek:
            speak(record() + ".txt")
            speak("İstediğin notu okudum")
        else:
            speak("silmek istediğin dosya mevcut değil.")
    
    if "not sil" in voice:
        speak("Hangi notu sileyim?")
        txtfile = record() + ".txt"
        notes = os.listdir(r"notlar/")
        icermek = notes.__contains__(txtfile)
        if icermek:
            os.remove(r"notlar/" + txtfile)
            speak("İstediğin notu sildim.")
        else:
            speak("silmek istediğin dosya mevcut değil.")
        
    if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice or "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)
        

    if "saat kaç" in voice or "zamanı söyle" in "saati söyle" in voice or "saat durumu" in voice or "zaman durumu" in voice:
        clock = datetime.now().strftime("%H:%M:%S")
        speak(clock)
        print("MrSpy - "+datetime.now().strftime('%H:%M:%S'))
        
    if "tarih" in voice or "tarihi söyle" in voice or "bugünün tarihi ne" in voice or "bugün takvimde ne zaman" in voice or "gün ay yılı söyle" in voice or "tarihi gün ay yıl olarak söyle" in voice:
        date = datetime.now().strftime("%D %B %Y")
        speak("Tarih " + date)
        
    if "yıl ay günü söyle" in voice or "tarihi yıl ay gün olarak söyle" in voice:
        date = datetime.now().strftime("%Y % B %D")
        speak("Tarih " + date)
        
    if "ayı söyle" in voice or "hangi aydayız" in voice or " şuan hangi aydayız" in voice or "aylardan hangisindeyiz" in voice or "şuan bulunduğumuz ay hangisi" in voice:
        date = datetime.now().strftime("%B")
        speak(date + "Ayındayız")
    
    if "hangi yıldayız" in voice or "yılı söyle" in voice or "kaç yılındayız" in voice:
        date = datetime.now().strftime("%Y")
        speak(date + "Yılındayız")
        

    if "pil kaç" in voice or "şarj kaç" in voice or "pil durumu" in voice or "batarya durumu" in voice or "şarj durumu" in voice:
        pil = psutil.sensors_battery()
        yuzde = pil.percent
        speak(f"Kalan pil: yüzde{yuzde}")

    if "bilgisayarı yeniden başlat" in voice or "bilgisayar yeniden başlat" in voice or "pc reset" in voice:
        speak("Bilgisayarı yeniden başlatma mı ister misin?")
        onay = record()
        onay = onay.lower()
        if "evet" in onay:
            speak("Sistem yeniden başlatılıyor")
            os.system("shutdown /r /t 2")
            os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
        if "hayır" in onay:
            speak("İşlem iptal edildi")
            print("MrSpy - İşlem iptal edildi")
            
    if 'güle güle' in voice or "bye bye" in voice or "kapan" in voice or "kendini kapat" in voice or "görüşmek üzere" in voice or "bye" in voice or "hizmetlerin içn sağol" in voice or "bay" in voice or "hizmetlerin için sağ ol" in voice:
        speak('görüşürüz')
        print('MrSpy  = Görüşürüz')
        exit()

    if "googleda ara" in voice or "google'da ara" in voice or "google'da arama yap" in voice or "googleda arama yap" in voice:
        speak("Googleda ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak(search + "İşte google sonuçları")
        
    if "wikipedia'da ara" in voice or "wikipediada ara" in voice or "wikipedia da ara" in voice:
        speak("Wikipedia da ne aramamı istersin?")
        search = record()
        url = "https://tr.wikipedia.org/w/index.php?go=Go&search={}".format(search)
        webbrowser.get().open(url)
        speak(search + "işte sonuçlar")
        
    if "gizli arama da ara" in voice or "özel arama da ara" in voice or "gizli serviste ara" in voice or "özel bilgilerde ara" in voice:
        speak("Shodan da ne aramamı istersin?")
        search = record()
        url = "https://www.shodan.io/search?query={}".format(search)
        webbrowser.get().open(url)
        speak("İşte Shodan sonuçları")    

    if "githubda ara" in voice or "proje ara" in voice or "gethabda ara" in voice or "code ara" in voice or "kod ara" in voice or "git hatta arama yap" in voice or "git hatta ara" in voice:
        speak("Githab da ne aramamı istersin?")
        search = record()
        url = "https://github.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İşte githab sonuçları.") #Sesli asistan bazı yerlerde düzgün okuyamadığı için github yerine githab yazılmıştır.

    if "youtubeda ara" in voice or "youtube ara" in voice or "youtube'da ara" in voice:
        speak("Youtubeda ne aramamı istersin?")
        search = record()
        url = "https://youtube.com/search?q={}".format(search)
        webbrowser.get().open(url)
        sozler = ["İşte arama sonuçları",
                "Al sana youtube aramanın sonuçları",
                (search + "Demek bunu aradın"),
                ("İşte" + search + "aramasının sonuçları bunlar"),
                ("Bunlar" + search + "aramasının sonuçları"),       
        ]
        secim = choice(sozler)
        speak(secim)

        
    if "hava durumu" in voice or "hava durumuna bak" in voice or "hava durumunu söyle" in voice or "hava tahminleri" in voice or "hava tahminlerine bak" in voice or "bugün kaç derece" in voice or "hava kaç derece" in voice or "hava tahminini söyle" in voice or "hava tahmini" in voice or "hava tahminine bak" in voice:
        speak("Hangi ilin hava durumunu öğrenmek istiyorsun")
        search1 = record()
        print("İl: " + search1)
        speak("Peki hangi ilçe")
        search2 = record()
        print("İlçe: " + search2)
        url = ("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={}&ilce={}").format(search1,search2)
        webbrowser.get().open(url)
        sozler = ["İşte hava durumu sonuçları",
                "Hava durumu böyle",
                ("İşte" + search1 + search2 + "için hava durumu"),
                (search1 + search2 + "için hava bu şekilde"),
                ("Bu" + search1 + search2 + "için hava durumu"),       
        ]
        secim = choice(sozler)
        speak(secim)

         
    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "discord" in runApp:
            os.startfile(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\helpers\\Discord.lnk")
            speak("Discordu açtım.")
            os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
        elif "visual studio code" in runApp:
            os.startfile(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\Yazilim\\Visual Studio Code.lnk")
            speak("Visual Studio Code'yi açtım.")
            os.system("TASKKILL /F /IM MrSpy_Asistan.exe")
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")

    if "mesaj yolla" in voice or "mesaj gönder" in voice or "mesaj at" in voice:
        speak("Kime mesaj yollamak istiyorsunuz?")
        saat = datetime.now().strftime("%H")
        dk = datetime.now().strftime("%M")
        user = record()
        user = user.lower()
        if "anne" in user:
            speak("Ne mesaj yollamak istiyorsun?")
            mesaj = record()
            if mesaj:
                speak(f"Annenize {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1235",mesaj, int(saat),int(dk))
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
        
        elif "baba" in user:
            speak("Ne mesaj yollamak istiyorsunuz?")
            mesaj = record()
            if mesaj:
                speak(f"Babanıza {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1234567890",mesaj, int(saat),int(dk) + 1)
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
        
        elif "arkadaş" in user:
            speak("Ne mesaj yollamak istiyorsunuz?")
            mesaj = record()
            if mesaj:
                speak(f"Arkadaşınıza {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1234567890",mesaj, int(saat),int(dk) + 1)
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
        else:
            speak("Bu kişi kişilerde yok.")
            
    if "müzik aç" in voice:
        music = os.listdir(r"C:\Users\K_ADI\Music")
        music = random.choice(music)
        os.startfile(rf"C:\Users\K_ADI\Music\{music}")
        speak("Senin için bir müzik açtım.")
        print("MrSpy - Müzik açıldı")
        
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "Cevap.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



# Uyanma       
        
print("Merhabalar ben MrSpy, kişisel asistanınız bugün size nasıl yardımcı olabilirim.")
speak("Merhabalar ben Mistırsıpay, size nasıl yardımcı olabilirim") # Asistan MrSpy gibi yazıları düzgün okuyamadığı için böyle yazmak zorunda kalındı.

time.sleep(1)
while 1:
    voice= record()
    print(voice)
    response(voice)

# Uyanma
