# -*- coding: utf-8 -*-

import socket ,select, time, os 
from random import *

################################			 VARIABLE

sync="888"
syn=sync.encode() 						
i=0
tours=1
hote= ''
port= '12800'
lr=[]
li=[]
lloup=[]
autre=[]
llpu_vote=[]
joeur=[]
clients=[]
j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12="j1","j2","j3","j4","j5","j6","j7","j8","j9","j10","j11","j12"
l6  = [j1,j2,j3,j4,j5,j6]
l7  = [j1,j2,j3,j4,j5,j6,j7]
l8  = [j1,j2,j3,j4,j5,j6,j7,j8]
l9  = [j1,j2,j3,j4,j5,j6,j7,j8,j9]
l10 = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10]
l11 = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11]
l12 = [j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12]
carte_obli=["loup garou","loup garou","voyante","villageois","villageois","villageois"]
n         =["cupidon","chasseur","sorciere","voleur","villageois","villageois"]
con=0
mortlist=[]
nbjc =0
votedesloups=""
vi=[]
####################################### global
global clients
global nbjc
global mortlist
global votedesloups
global vi
###############################              def

def nuit():
    for i in range(nbjc):
        if vi[i]==1:
            time.sleep(0.5)
            co_client=clients[i]
            co_client.send(b"7")
            aa=co_client.recv(1024)
def jour():
    for i in range(nbjc):
        if vi[i]==1:
            time.sleep(0.5)
            co_client=clients[i]
            co_client.send(b"8")
            aa=co_client.recv(1024)
def leplusvoter(lv):
    b={}
    for i in lv:
        b[str(i)]=b.setdefault(str(i),0)+1.
     
    c=b.items()
    v=[]
    w=0
    for e in c:
        if e[1]>w:
            w=e[1]
            v=[e[0]]
        elif e[1]==w:
            v.append(e[0])
     
    if 1==len(v):
        return v[0]
    else:
        a=(choice(v))
        return a
def loup(lloup):
    for i in range(2):
        if vi[i]==1:
            a=lloup[i]
            co_client=clients[a]
            co_client.send(b"6")
    for i in range(2):
        if vi[i]==1:
            a=lloup[i]
            co_client=clients[a]
            reponce=co_client.recv(1024)
            vote=reponce.decode()
            print(vote)
            llpu_vote.append(vote)
    a = leplusvoter(llpu_vote)
    return a
def cup(cup1,cup2):
    exc="cupidon" in li
    if exc==True:    
        if vi[cup1]==0 or vi[cup2]==0:
            vi[cup1]=0 ; vi[cup2]=0
def voyante(li,lr):
    te=li.index("voyante")
    if vi[te]==1:
        co_client=clients[te]
        co_client.send(b"5")            ###########voyante
        voy=co_client.recv(1024)
        voy=voy.decode()
        voy=int(voy)
        voi=lr[voy]
        voi2=voi.encode()
        co_client.send(voi2)
def fintest(nbj,lloup,autre):
    a=1
    b=0
    testloup=0
    testautre=0
    for i in range(1):
        if vi[lloup[i]]==0:
            testloup +=1
    for i in range(nbj-2):
        if vi[autre[i]]==0:
            testautre +=1
    if testloup==2:
        finvill(nbj,clients)
        return b
    elif testautre==(nbj-2):
        finloup(nbj,clients)
        return b
    else:
        testautre=0
        testloup=0
        return a
def finloup():
    for i in range(nbjc):
        co_client=clients[i]
        co_client.send(b"16")
        aa=co_client.recv(1024)
        co_client.send(b"404")
def finvill():
    for i in range(nbjc):
        co_client=clients[i]
        co_client.send(b"15")
        aa=co_client.recv(1024)
        co_client.send(b"404")
def village():
    lv=[]
    for i in range(nbjc):
        co_client=clients[i]
        co_client.send(b"14")
    for i in range(nbjc):
        co_client=clients[i]
        co_client.send(syn)
        v=co_client.recv(1024)
        votevillage=v.decode()
        lv.append(votevillage)
    a=leplusvoter(lv)
    mortlist.append(a)
def mortc(nbjc):
    for i in range(len(mortlist)):
        print("mort n",i," est" ,mortlist[i])
    for e in range(nbjc):
        co_client=clients[e]
        co_client.send(b"10")
        for i in range(len(mortlist)):
            aa=co_client.recv(1024)
            m=int(mortlist[i])
            vi[m]=0
            m=str(m).encode()
            co_client.send(m)
        exxx=cu1 in mortlist
        exx=cu2 in mortlist
        if exx==True:
            mortlist.append(cu1)
        elif exxx==True:
            mortlist.append(cu2)
        nbjc=nbjc-len(mortlist)
        for u in range(len(mortlist)):
            mo=int(mortlist[u])      
            del clients[mo]
def sorciere(li):
    te=li.index("sorciere")
    if vi[te]==1:
        a=votedesloups.encode()
        co_client=clients[te]
        co_client.send(b"17")
        print("envoie du 17")
        aa=co_client.recv(1024)
        co_client.send(a)
        print("vote loup envoyer")
        choixx=co_client.recv(1024)
        print("choix recu")
        choixx=choixx.decode()
        choixx=int(choixx)
        if choixx==12:
            mortlist.append("99")
            mortlist.append(votedesloups)
        elif choixx==13:
            mortlist.append("99")
            mortlist.append("99")
        else:
            mortlist.append(choixx)
            mortlist.append(votedesloups)
def choix_carte(lis,nbj):
    for i in range (nbj-6):
        al=(choice(n))
        lis.append(al)
        al=n.index(al)
        del n[al]
def ass_carte(d,e,nbj):
    for i in range (nbj):
        a=choice(d)
        e[i]=a
        b=d.index(a)
        del d[b]

###############################              connection

nbj=int(input("nombre de joueur ?"))
co_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
co_p.bind(('', 12800))
co_p.listen(5)

for i in range(nbj):
    co_client, inn = co_p.accept()
    print("le joueur ",i," est connecté")
    clients.append(co_client)
print("tout les joueurs sont connecté")

nbjc=len(clients)

##############################               speudo

for i in range(nbjc):
    c=clients[i]
    speudo1=c.recv(1024)
    speudo=speudo1.decode()
    joeur.append(speudo)
    print(joeur[i])

############################                 assignation des cartes


if nbj==6:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l6,nbj) ; li=l6
    jo1,jo2,jo3,jo4,jo5,jo6=li[0],li[1],li[2],li[3],li[4],li[5]
    vi=[1,1,1,1,1,1,0,0,0,0,0,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6]
elif nbj==7:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l7,nbj) ; li=l7
    jo1,jo2,jo3,jo4,jo5,jo6,jo7=li[0],li[1],li[2],li[3],li[4],li[5],li[6]
    vi=[1,1,1,1,1,1,1,0,0,0,0,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7]
elif nbj==8:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l8,nbj) ; li=l8
    jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8=li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7]
    vi=[1,1,1,1,1,1,1,1,0,0,0,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8]
elif nbj==9:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l9,nbj) ; li=l9
    jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9=li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8]
    vi=[1,1,1,1,1,1,1,1,1,0,0,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9]
elif nbj==10:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l10,nbj) ; li=l10
    jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10=li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9]
    vi=[1,1,1,1,1,1,1,1,1,1,0,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10]
elif nbj==11:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l11,nbj) ; li=l11
    jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10,jo11=li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[10]
    vi=[1,1,1,1,1,1,1,1,1,1,1,0]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10,jo11]
elif nbj==12:
    lc=carte_obli ; choix_carte(lc,nbj) ; ass_carte(lc,l12,nbj) ; li=l12
    jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10,jo11,jo12=li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[10],li[11]
    vi=[1,1,1,1,1,1,1,1,1,1,1,1]
    lr=[jo1,jo2,jo3,jo4,jo5,jo6,jo7,jo8,jo9,jo10,jo11,jo12]
    lj=[j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12]

############################                 possition des roles dans les listes

for i,e in enumerate(li):
    if e=="loup garou":
        lloup.append(i)
    elif e=="voyante":
        num_voyant=i
        autre.append(i)
    elif e=="soucière":
        num_sorciere=i
        autre.append(i)
    else:
        autre.append(i)


exc="cupidon" in li
ex="voleur" in li

########################                     envoi des rôles

for i in range(nbjc):
    co_client=clients[i]
    role=lr[i]
    role_encoder=role.encode()
    co_client.send(role_encoder)
    synn=co_client.recv(1024)
    nbjj=str(nbj)
    nbjj=nbjj.encode()
    co_client.send(nbjj)
    synn=co_client.recv(1024)
    num=str(i)
    mun=num.encode()
    co_client.send(mun)
    synn=co_client.recv(1024)


    for oopo in range(nbj):
        cc=lr[oopo]
        uu=li[oopo]
        pp=joeur[oopo]
        ccc=cc.encode()
        uuu=uu.encode()
        ppp=pp.encode()
        co_client.send(ccc)
        synn=co_client.recv(1024)
        co_client.send(uuu)
        synn=co_client.recv(1024)
        co_client.send(ppp)
        synn=co_client.recv(1024)

    speudo=joeur[i]
    print("le joueur",speudo,"est ",role,)

for e in lloup:
    co_client=clients[e]
    if con==1:
        llloup =lloup[0]
        llloup = str(llloup)
        llloup=llloup.encode()
        co_client.send(llloup)
    else:
        llloup =lloup[1]
        llloup = str(llloup)
        llloup=llloup.encode()
        co_client.send(llloup)        
        con+=1

########################                     deroulement du jeu

print("nuit")
nuit()

if ex==True:
    te=li.index("voleur")
    co_client=clients[te]
    co_client.send(b"4")
    voll=co_client.recv(1024)                #######voleur
    vol=voll.decode()
    vol=int(vol)
    print("le joueur choisi est le",joeur[vol],)
    li[te]=li[vol] ; li[vol]="villageois"
    co_client=clients[vol]
    co_client.send(b"44")   

if exc==True:
    te=li.index("cupidon")
    co_client=clients[te]
    co_client.send(b"2")                ######vote cupidon
    cup1=co_client.recv(1024)
    cu1=cup1.decode()
    co_client.send(syn)                ######synchro
    cup2=co_client.recv(1024)
    cu2=cup2.decode()  
    cu1=str(cu1)
    cu2=str(cu2)
    repr(cu1)
    cu1=int(cu1)
    repr(cu2)
    cu2=int(cu2)
    print("les joueurs", joeur[cu1]," et ", joeur[cu2],"sont en couple")
    a=cu1
    b=cu2
    a=int(a)
    b=int(b)
    co_client=clients[a]
    a=str(a)
    co_client.send(b"3")
    aa=co_client.recv(1024)
    r=a.encode()
    co_client.send(r)
    co_client=clients[b]
    co_client.send(b"3")
    b=str(b)
    r=b.encode()
    aa=co_client.recv(1024)
    co_client.send(r)


print("vote loup")
votedesloups=loup(lloup)
print(votedesloups)

ex="sorciere" in li
if ex==True:
    print("vote soriciere")
    sorciere(li)
print("voyante")
voyante(li,lr)
print("jour")
jour()
print("vote village")
village()
print("mort")
mortc(nbjc)
print("fin tours")

while tours!=0:
    print("test fin")
    tours =fintest(autre,vi)
    print("nuit")
    nuit()
    print("vote loup")
    votedesloups=loup(lloup)
    ex="sorciere" in li
    if ex==True:
        print("vote soriciere")
        sorciere(li)
    print("voyante")
    voyante(li,lr)
    print("jour")
    jour()
    print("vote village")
    village()
    print("mort")
    mortc(nbjc)
    print("fin tours")
    mortlist=[]

########################                     deconnection

for i in range(nbjc):
    co_client=clients[i]
    print("le joeur",i,"a été deconnecté")
    co_client.close()
co_p.close()