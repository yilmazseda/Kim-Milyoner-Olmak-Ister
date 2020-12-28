#kodların işleyişini kısa süreli durdurmak için
from time import sleep
#rastgele sayı üretmek için
from random import randint
from os import system
#şifre girerkken karakterin gözükmesini sağlar
from getpass import getpass
import time
import operator
import sys
import re
import random

print("""
        ***********************
        KİM MİLYONER OLMAK İSTER YARIŞMASINA HOŞGELDİNİZ!! :)
        OYUNA BAŞLAMAK İSTİYORSANIZ:1
        SORU EKLEMEK İSTİYORSANIZ:2
        SKOR TABLOSUNA GİTMEK İSTİYORSANIZ:3
        ÇIKIŞ YAPMAK İSTİYORSANIZ:4
        ************************ """)
menuChoice1 = int(input(">>> "))
#ekranı temizleme
system("cls,clear;clear")

if(menuChoice1 == 1):
    name = input("Lütfen Adınızı Giriniz:\n")
    system("cls,clear;clear")
    #dosya acımı
    file = open("questions.txt","r")
    questions = file.readlines()
    #dosya kapama
    file.close()

    #sorular dizisini saydırma
    say=0
    for question in questions:
        say += 1
    i=0
    #para ödülü
    class Stack(list):
        def push(self,items):
            self.append(items)
        def isEmpty(self):
            return not self
    s=Stack()
    s.push(1000000)
    s.push(250000)
    s.push(70000)
    s.push(50000)
    s.push(7500)
    s.push(5000)
    s.push(3000)
    s.push(2000)
    s.push(1000)
    s.push(500)

    score = 0
    fail = ""
    #klasördeki 10 soruyu sormasını belirttik

    while(i<=10):
        i +=1
        """
        1.Satır-Soru
        2.Satır-A şıkkı
        3.Satır-B şıkkı
        4.Satır-C şıkkı
        5.satır-D şıkkı
        6.satır-Dogru cevap
        soru seçimi"""
        questionnumber = (randint(0, (int(say / 6) - 1)) * 6)

        system("cls,clear;clear")
        print(fail)
        print(30 * "#" + "\n")
        print(" Soru " + str(i) + "\n   " + str(questions[questionnumber]))
        aOption = questions[questionnumber + 1]
        print(" A)", aOption)
        bOption = questions[questionnumber + 2]
        print(" B)", bOption)
        cOption = questions[questionnumber + 3]
        print(" C)", cOption)
        dOption = questions[questionnumber + 4]
        print(" D)", dOption)
        answer = questions[questionnumber + 5]

        while True:
            kAnswer=input("Cevabınızı Giriniz:[A,B,C,D şeklinde]\n>>> ")
            #büyük harf girildiyse küçültür
            #kAnswer=kAnswer.lower()
            lastDecision=input("Son Kararınız Mı?(Evet:E,Hayır:H)\n>>> ")
            #büyük harf girildiyse küçültülür
            lastDecision=lastDecision.lower()
            if (lastDecision == 'e'):
                break
            elif (lastDecision == 'h'):
                continue
            else:
                print(" Yanlış Karar! ")
        if(kAnswer == answer[:1]):
          score = float(s[i-2])
          print("Doğru Cevap!!"+str(s[i-2])+"TL kazandın,\n bakiye "+str(score))
          print(30*"#"+"\n\n")
          print("  Devam Etmek İstiyor Musun? \n")
          print("  1 -> Evet!!")
          print("  2 -> Hayır...")
          menum = int(input(">>> "))
          print(30 * "#" + "\n")
          if (menum == 2):
           print(30 * "#" + "\n")
           print(" Yarışmadan %0.4f TL kazandın, Tebrikler %s !" % (score, name.upper()))
           print(30 * "#" + "\n")
           break
        else:
            i = 10
            print(30 * "#" + "\n")
            print("  Yanlış Cevap !!!\n Oyun Bitti :(")
            print("  %s, Yarışmadan %d TL kazandın, !" % (name.upper(),score / 2))
            print(30 * "#" + "\n")
            break
elif(menuChoice1==2):
    opt = ["Q: ", "a: ", "b: ", "c: ", "d: ", "Correct Option: "]
    qt = []
    quest = {}


    class m:
        count = 0

        def __init__(self, q, a, b, c, d, corrans):

            self.q = q
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.corrans = corrans
            m.count = m.count + 1

        def add(self):
            quest[m.count] = [self.q, self.a, self.b, self.c, self.d, self.corrans]

        def show(self):

            for i in quest:
                k = 0
                print("Question {}".format(i))
                for j in quest[i]:
                    print('{} {}'.format(opt[k], j))
                    k += 1
                print('\n')

        def quiz(self):
            corrcount = 0
            s = random.sample(range(1, m.count + 1), m.count)
            totque = int(input("Enter the no. of questions needed: "))
            for i in range(1, totque + 1):
                print("Soru {}".format(i))
                q1 = quest[s[i - 1]]
                print('{}\nA: {}\nB: {}\nC: {}\nD: {}'.format(q1[0], q1[1], q1[2], q1[3], q1[4]))
                choice = input("Doğru Cevabı Girin: ")

                if choice == q1[5]:
                    corrcount = corrcount + 1
            print("Toplam Puanınız {}/{}".format(corrcount, totque))


    while True:

        print("1.Soru Ekle\n2.Soruyu Göster\n3.Çıkış")
        a = int(input("Seçiminizi Girin: "))
        if a == 1:

            quest1 = input("Soru:")
            a = input("A şıkkı: ")
            b = input("B şıkkı: ")
            c = input("C şıkkı: ")
            d = input("D şıkkı: ")
            corans = input("Doğru Cevabı Girin: ")
            obj1 = m(quest1, a, b, c, d, corans)
            obj1.add()
        elif a==3:
            print("Oyundan Çıkış Yapıldı!")
            exit()

elif(menuChoice1==4):
    print("Oyundan Çıkış Yapıldı!")
    exit()

