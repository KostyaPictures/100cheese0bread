#############ОБРАБОТКА###############
nxt=1


#БЕЗ 1 прод
def noP1():
    global prod1, cas, nxt
    if cas==1:
        if prod1[-1]=="а" and nxt==1:
            prod1=prod1[:-1]+"ы"
            nxt=0
        if prod1[-1]=="я" and nxt==1:
            prod1=prod1[:-1]+"и"
            nxt=0
    if cas==2:
        if (prod1[-1]=="о" or prod1[-1]=="е") and nxt==1:
            prod1=prod1[:-1]+"а"
            nxt=0
        if prod1[-1]=="й" and nxt==1:
            prod1=prod1[:-1]+"я"
            nxt=0
        if prod1[-1]=="ь" and nxt==1:
            prod1=prod1[:-1]+"я"
            nxt=0
        if nxt==1:
            prod1=prod1+"а"
            nxt=0
    if cas==3:
        if prod1[-1]=="ь" and nxt==1:
            prod1=prod1[:-1]+"а"
            nxt=0

#БЕЗ 2 прод
def noP2():
    global prod2, cas, nxt
    if cas==1:
        if prod2[-1]=="а" and nxt==1:
            prod2=prod2[:-1]+"ы"
            nxt=0
        if prod2[-1]=="я" and nxt==1:
            prod2=prod2[:-1]+"и"
            nxt=0
    if cas==2:
        if (prod2[-1]=="о" or prod2[-1]=="е") and nxt==1:
            prod2=prod2[:-1]+"а"
            nxt=0
        if prod2[-1]=="ь" and nxt==1:
            prod2=prod2[:-1]+"я"
            nxt=0
        if prod2[-1]=="й" and nxt==1:
            prod2=prod2[:-1]+"я"
            nxt=0
        if nxt==1:
            prod2=prod2+"а"
            nxt=0
    if cas==3:
        if prod2[-1]=="ь" and nxt==1:
            prod2=prod2[:-1]+"а"
            nxt=0

#С 1 прод
def yesP1():
    global prod1, cas, nxt
    if cas==1:
        if (prod1[-2]=="й" or prod1[-2]=="ч" or prod1[-2]=="щ" or prod1[-2]=="ш") and nxt==1:
            prod1=prod1[:-1]+"ей"
            nxt=0
        if prod1[-1]=="а" and nxt==1:
            prod1=prod1[:-1]+"ой"
            nxt=0
        if prod1[-1]=="я" and nxt==1:
            prod1=prod1[:-1]+"ей"
            nxt=0
    if cas==2:
        if prod1[-1]=="о" or prod1[-1]=="е" and nxt==1:
            prod1=prod1[:-1]+"ом"
            nxt=0
        if (prod1[-1]=="й" or prod1[-1]=="ч" or prod1[-1]=="щ" or prod1[-1]=="ш") and nxt==1:
            prod1=prod1+"ом"
            nxt=0
        if prod1[-1]=="ь" and nxt==1:
            prod1=prod1[:-1]+"ем"
            nxt=0
        if nxt==1:
            prod1=prod1+"ом"
            nxt=0
    if cas==3:
        if prod1[-1]=="ь" and nxt==1:
            prod1=prod1+"ю"
            nxt=0

#C 2 прод
def yesP2():
    global prod2, cas, nxt
    if cas==1:
        if (prod2[-2]=="й" or prod2[-2]=="ч" or prod2[-2]=="щ" or prod2[-2]=="ш") and nxt==1:
            prod2=prod2[:-1]+"ей"
            nxt=0
        if prod2[-1]=="а" and nxt==1:
            prod2=prod2[:-1]+"ой"
            nxt=0
        if prod2[-1]=="я" and nxt==1:
            prod2=prod2[:-1]+"ей"
            nxt=0
    if cas==2:
        if (prod2[-1]=="о" or prod2[-1]=="е") and nxt==1:
            prod2=prod2[:-1]+"ом"
            nxt=0
        if (prod2[-1]=="й" or prod2[-1]=="ч" or prod2[-1]=="щ" or prod2[-1]=="ш") and nxt==1:
            prod2=prod2+"ом"
            nxt=0
        if prod2[-1]=="ь" and nxt==1:
            prod2=prod2[:-1]+"ем"
            nxt=0
        if nxt==1:
            prod2=prod2+"ом"
            nxt=0
    if cas==3:
        if prod2[-1]=="ь" and nxt==1:
            prod2=prod2+"ю"
            nxt=0



###############ВЫВОД#################

#финальный принт

def without1():
    global prod1,prod2
    print(prod2, "без", prod1)
def without2():
    global prod1,prod2
    print(prod1, "без", prod2)
def with1():
    global prod1,prod2
    if ((prod1[0]=="ш" or prod1[0]=="з" or prod1[0]=="в" or prod1[0]=="р" or prod1[0]=="л" or prod1[0]=="ж" or prod1[0]=="с" or prod1[0]=="м") and (prod1[1]=="ь" or prod1[1]=="ц" or prod1[1]=="к" or prod1[1]=="н" or prod1[1]=="г" or prod1[1]=="ш" or prod1[1]=="щ" or prod1[1]=="з" or prod1[1]=="х" or prod1[1]=="ф" or prod1[1]=="в" or prod1[1]=="п" or prod1[1]=="р" or prod1[1]=="л" or prod1[1]=="д" or prod1[1]=="ж" or prod1[1]=="ч" or prod1[1]=="с" or prod1[1]=="м" or prod1[1]=="т" or prod1[1]=="б")) or prod1[0]=="щ":
        wth="со"
    else:
        wth="с"
    print(prod2, wth, prod1)
def with2():
    global prod1,prod2
    if ((prod2[0]=="ш" or prod2[0]=="з" or prod2[0]=="в" or prod2[0]=="р" or prod2[0]=="л" or prod2[0]=="ж" or prod2[0]=="с" or prod2[0]=="м") and (prod2[1]=="ь" or prod2[1]=="ц" or prod2[1]=="к" or prod2[1]=="н" or prod2[1]=="г" or prod2[1]=="ш" or prod2[1]=="щ" or prod2[1]=="з" or prod2[1]=="х" or prod2[1]=="ф" or prod2[1]=="в" or prod2[1]=="п" or prod2[1]=="р" or prod2[1]=="л" or prod2[1]=="д" or prod2[1]=="ж" or prod2[1]=="ч" or prod2[1]=="с" or prod2[1]=="м" or prod2[1]=="т" or prod2[1]=="б")) or prod2[0]=="щ":
        wth="со"
    else:
        wth="с"
    print(prod1, wth, prod2)
def f5050():
    global prod1,prod2
    print(prod1,prod2,sep="-")





#########################################################
#########################################################

pril1=True
pril2=True


#запрос 1 продукта
while pril1:
    print("введите первый продукт:")
    prod1=input()
    if prod1[-2:]=="ой" or prod1[-2:]=="ый" or prod1[-2:]=="ий" or prod1[-2:]=="ая" or prod1[-2:]=="яя" or prod1[-2:]=="ое" or prod1[-2:]=="ее" or prod1[-2:]=="ые" or prod1[-2:]=="ие":
        pril1=True
        print('Программа не может воспринимать существительные, имеющие склонения как у прилагательных, например "отбивная" или "мороженое". Нажмите Enter для продолжения')
        enter=input()
    else:
        pril1=False



#запрос доли первого продука
frac1=-1
while frac1>100 or frac1<0:
    print("доля первого продукта в процентах:")
    frac1=int(input())
    if frac1>100 or frac1<0:
        print("Проценты не могут быть больше 100 или меньше 0.")


#высчет доли второго продукта
frac2=100-frac1

qon=""
qonALOT=""
cnt=0
cntALOT=0
sex1=0
sex2=0

if frac1<50:
    if prod1[-1]=="ь":
        while qon!="нет" and qon!="да":
            if cnt>0 and (qon!="нет" or qon!="да"):
                print('введите только "да" или "нет"')
                qon=input()
            if cnt==0:
                print('слово',prod1,'женского рода? (да/нет)')
                qon=input()
                cnt+=1
            if qon=="да":
                cas=3
                sex1=1
            if qon=="нет":
                cas=2
                sex1=1
        if frac1==0:
            noP1()
        if frac1<50 and frac1>0:
            yesP1()
    if prod1[-1]=="а" or prod1[-1]=="я" or prod1[-1]=="и" or prod1[-1]=="ы":
        while qonALOT!="да" or qonALOT!="нет":
            if cntALOT==0:
                print("Это множественное число? (да/нет)")
                qonALOT=input()
                cntALOT+=1
            if cntALOT>0 and qonALOT!="да" and qonALOT!="нет":
                print('введите только "да" или "нет"')
                qonALOT=input()
            if qonALOT=="да":
               print("К сожалению, программа не может воспринимать множественное числа из-за проблемы с определением рода. Напишите другое существительное.\nВведите первый продукт:")
               prod1=input()
               break
            if qonALOT=="нет":
                break



#запрос 2 продукта
while pril2:
    print("введите второй продукт:")
    prod2=input()
    if prod2[-2:]=="ой" or prod2[-2:]=="ый" or prod2[-2:]=="ий" or prod2[-2:]=="ая" or prod2[-2:]=="яя" or prod2[-2:]=="ое" or prod2[-2:]=="ее" or prod1[-2:]=="ые" or prod1[-2:]=="ие":
        pril2=True
        print('Программа не может воспринимать существительные, имеющие склонения как у прилагательных, например "отбивная" или "мороженое". Нажмите Enter для продолжения')
        enter=input()
    else:
        pril2=False




if frac2<50:
    if prod2[-1]=="ь":
        while qon!="нет" and qon!="да":
            if cnt>0 and (qon!="нет" or qon!="да"):
                print('введите только "да" или "нет"')
                qon=input()
            if cnt==0:
                print('слово',prod2,'женского рода? (да/нет)')
                qon=input()
                cnt+=1
            if qon=="да":
                cas=3
                sex2=1
            if qon=="нет":
                cas=2
                sex2=1
        if frac2==0:
            noP2()
        if frac2<50 and frac2>0:
            yesP2()
    if prod2[-1]=="а" or prod2[-1]=="я" or prod2[-1]=="и" or prod2[-1]=="ы":
        while qonALOT!="да" or qonALOT!="нет":
            if cntALOT==0:
                print("Это множественное число? (да/нет)")
                qonALOT=input()
                cntALOT+=1
            if cntALOT>0 and qonALOT!="да" and qonALOT!="нет":
                print('введите только "да" или "нет"')
                qonALOT=input()
            if qonALOT=="да":
                print("К сожалению, программа не может воспринимать множественное числа из-за проблемы с определением рода. Напишите другое существительное.\nВведите второй продукт:")
                prod2=input()
                break
            if qonALOT=="нет":
                break





#############ПРОВЕРКА################


#склонения для продукта 1
cas=0
if (frac1<50 or frac1==0) and cas==0 and sex1==0:
    if prod1[-1]=="а" or prod1[-1]=="я":
        #1 склонение
        cas=1
        print(cas)
    if prod1[-1]=="й" or prod1[-1]=="о" or prod1[-1]=="е":
        #2 склонение
        cas=2
    if prod1[-1]=="ь":
        #3 склонение
        cas=3
    if prod1=="колибри" or prod1=="кенгуру" or prod1=="шоссе" or prod1=="фламинго" or prod1=="пони" or prod1=="шимпанзе" or prod1=="какао" or prod1=="кофе" or prod1=="домино" or prod1=="алоэ" or prod1=="радио" or prod1=="кино" or prod1=="такси" or prod1=="метро" or prod1=="купе" or prod1=="пальто" or prod1=="кашне" or prod1=="кафе" or prod1=="трюмо" or prod1=="манто" or prod1=="какаду" or prod1=="драже" or prod1=="пари" or prod1=="интервью" or prod1=="рагу" or prod1=="жюри" or prod1=="пианино" or prod1=="фойе" or prod1=="пюре" or prod1=="бюро" or prod1=="ателье" or prod1=="манго":
        cas=0
    else:
        #2 склонение
        if cas!=1:
            cas=2

#склонения для второго продукта
if (frac2<50 or frac2==0) and cas==0 and sex2==0:
    if prod2[-1]=="а" or prod2[-1]=="я":
        #1 склонение
        cas=1
    if prod2[-1]=="й" or prod2[-1]=="о" or prod2[-1]=="е":
        #2 склонение
        cas=2
    if prod2[-1]=="ь":
        #3 склонение
        cas=3
    if prod1=="колибри" or prod1=="кенгуру" or prod1=="шоссе" or prod1=="фламинго" or prod1=="пони" or prod1=="шимпанзе" or prod1=="какао" or prod1=="кофе" or prod1=="домино" or prod1=="алоэ" or prod1=="радио" or prod1=="кино" or prod1=="такси" or prod1=="метро" or prod1=="купе" or prod1=="пальто" or prod1=="кашне" or prod1=="кафе" or prod1=="трюмо" or prod1=="манто" or prod1=="какаду" or prod1=="драже" or prod1=="пари" or prod1=="интервью" or prod1=="рагу" or prod1=="жюри" or prod1=="пианино" or prod1=="фойе" or prod1=="пюре" or prod1=="бюро" or prod1=="ателье":
        cas=0
    else:
        #2 склонение
        if cas!=1:
            cas=2

#Финальная проверка перед принтом/менеджер действий
if frac1==0:
    noP1()
    without1()
if frac2==0:
    noP2()
    without2()
if frac1<50 and frac1>0:
    yesP1()
    with1()
if frac2<50 and frac2>0:
    yesP2()
    with2()
if frac1==50:
    f5050()