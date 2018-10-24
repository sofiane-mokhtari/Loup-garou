# -*- coding: utf-8 -*-

########################################################## import

import socket, sys, os
from random import *

oss=os.name
if oss=="posix": #windows
        import Tkinter
        from Tkinter import *
else:
        import tkinter
        from tkinter import *

########################################################## varaible

sync="888"
syn=sync.encode()
sauver_sou=0
kill_sou=0

li=[]
lr=[]
deco=0
choix_host=0 ########### choix de l'hote
host0="localhost"
ip = var_ip.get()
pseudo = var_pseudo.get()
port = var_port.get()
re_fentre.destroy()
host3=str(ip)
joeur=[]

########################################################## def


def consigne(te):
        f=Tk()
        l=Label(f,text=te,font="Arial 15")
        l.pack()
        valider=Button(f, text ='Valider',command=f.quit).pack(padx=5, pady=5)
        f.mainloop()
        f.destroy()

def vote(vi,titre,joeur):
        va=88
        while va==88 or va=="":
                fj = Tk()
                l=Label(fj,text=titre,font="Arial 15").pack()
                value = StringVar()
                if vi[0]==1:
                    bj1 = Radiobutton(fj, text=joeur[0], variable=value, value=0).pack()
                if vi[1]==1:
                    bj2 = Radiobutton(fj, text=joeur[1], variable=value, value=1).pack()
                if vi[2]==1:
                    bj3 = Radiobutton(fj, text=joeur[2], variable=value, value=2).pack()
                if vi[3]==1:
                    bj4 = Radiobutton(fj, text=joeur[3], variable=value, value=3).pack()
                if vi[4]==1:
                    bj5 = Radiobutton(fj, text=joeur[4], variable=value, value=4).pack()
                if vi[5]==1:
                    bj6 = Radiobutton(fj, text=joeur[5], variable=value, value=5).pack()
                if vi[6]==1: 
                    bj7 = Radiobutton(fj, text=joeur[6], variable=value, value=6).pack()
                if vi[7]==1:
                    bj8 = Radiobutton(fj, text=joeur[7], variable=value, value=7).pack()
                if vi[8]==1:
                    bj9 = Radiobutton(fj, text=joeur[8], variable=value, value=8).pack()
                if vi[9]==1:
                    bj10 = Radiobutton(fj, text=joeur[9], variable=value, value=9).pack()
                if vi[10]==1:
                    bj11 = Radiobutton(fj, text=joeur[10], variable=value, value=10).pack()
                if vi[11]==1:
                    bj12 = Radiobutton(fj, text=joeur[11], variable=value, value=11).pack()

                bvalider=Button(fj, text ='Valider',command=fj.quit).pack(padx=5, pady=5)
                fj.mainloop()
                va=int(value.get())
                fj.destroy()
        va=str(va)
        return(va)

########################################################## connexion
spp=str(speudo)
sp=spp.encode()
connexion_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_client.connect((host0, 12800))
connexion_client.send(sp)
print("speudo ",spp," envoyer")
########################################################## reçois role

b=connexion_client.recv(1024)
a=b.decode()
print("vous etes",a,)
connexion_client.send(syn)

########################################################## nombre de joeur
nbjj=connexion_client.recv(1024)
nbj=nbjj.decode()
print("il y a ",nbj," joueurs")

connexion_client.send(syn)

########################################################## listes

mun=connexion_client.recv(1024)
mun=int(mun.decode())

connexion_client.send(syn)



nbj=int(nbj)
for i in range(nbj):
        oppo=i+1
        ff=connexion_client.recv(1024)
        fff=ff.decode()
        lr.append(fff)
        connexion_client.send(syn)
        ff=connexion_client.recv(1024)
        fff=ff.decode()
        li.append(fff)
        connexion_client.send(syn)
        pp=connexion_client.recv(1024)
        ppp=pp.decode()
        joeur.append(ppp)
        connexion_client.send(syn)

if a=="loup garou":
        coop=connexion_client.recv(1024)
        coop=coop.decode()
        coop=int(coop)

if nbj==6:
    vi=[1,1,1,1,1,1,0,0,0,0,0,0]
elif nbj==7:
    vi=[1,1,1,1,1,1,1,0,0,0,0,0]
elif nbj==8:
    vi=[1,1,1,1,1,1,1,1,0,0,0,0]
elif nbj==9:
    vi=[1,1,1,1,1,1,1,1,1,0,0,0]
elif nbj==10:
    vi=[1,1,1,1,1,1,1,1,1,1,0,0]
elif nbj==11:
    vi=[1,1,1,1,1,1,1,1,1,1,1,0]
elif nbj==12:
    vi=[1,1,1,1,1,1,1,1,1,1,1,1]

vi[mun]=0
nbb=lr.index(a)
bouvle=0

while bouvle==0:
        ordre = connexion_client.recv(1024)
        o=ordre.decode()
        print("l'ordre est",o," et il est en cours")
        o=int(o)

        if o==2: ##cupidon
            ti="choissez le couple"
            votee= int(vote(vi,ti,joeur))
            vi[votee]=0
            fjj = Tk()
            l=Label(fjj,text=ti,font="Arial 15").pack()
            value = StringVar()
            if vi[0]==1:
                bj1 = Radiobutton(fjj, text=joeur[0], variable=value, value=0).pack()
            if vi[1]==1:
                bj2 = Radiobutton(fjj, text=joeur[1], variable=value, value=1).pack()
            if vi[2]==1:
                bj3 = Radiobutton(fjj, text=joeur[2], variable=value, value=2).pack()
            if vi[3]==1:
                bj4 = Radiobutton(fjj, text=joeur[3], variable=value, value=3).pack()
            if vi[4]==1:
                bj5 = Radiobutton(fjj, text=joeur[4], variable=value, value=4).pack()
            if vi[5]==1:
                bj6 = Radiobutton(fjj, text=joeur[5], variable=value, value=5).pack()
            if vi[6]==1:
                bj7 = Radiobutton(fjj, text=joeur[6], variable=value, value=6).pack()
            if vi[7]==1:
                bj8 = Radiobutton(fjj, text=joeur[7], variable=value, value=7).pack()
            if vi[8]==1:
                bj9 = Radiobutton(fjj, text=joeur[8], variable=value, value=8).pack()
            if vi[9]==1:
                bj10 = Radiobutton(fjj, text=joeur[9], variable=value, value=9).pack()
            if vi[10]==1:
                bj11 = Radiobutton(fjj, text=joeur[10], variable=value, value=10).pack()
            if vi[11]==1:
                bj12 = Radiobutton(fjj, text=joeur[11], variable=value, value=11).pack()

                                            

                    
            bvalider=Button(fjj, text ='Valider',command=fjj.quit).pack(padx=5, pady=5)
            fjj.mainloop()
            va=int(value.get())
            fjj.destroy()
            
            vi[votee]=1
            votee2=str(va)
            votee=str(votee)
            voteee=votee.encode()
            voteee2=votee2.encode()
            connexion_client.send(voteee)
            aa=connexion_client.recv(1024)
            connexion_client.send(voteee2)
        elif o==3: ## choisi comme couple
            connexion_client.send(sync)
            aaa=connexion_client.recv(1024)
            cup1=aaa.decode()
            cup1=int(cup1)
            couple=joeur[cup1]
            te="vous etes en couple avec "+couple
            consigne(te)
        elif o==4: ## voleur
            ti="choissez qui volez"
            k=vote(vi,ti,joeur)
            k=str(k)
            f=k.encode()
            connexion_client.send(f)
            k=int(k)
            li[nbb]=li[k]
            li[k]="villageois"
            te="vous etes maintenant "+li[nbb]
            consigne(te)
        elif o==44:
            te="vous vous etes fait voler votre carte vous etes maintenant villageois"
            li[nbb]="villageois"
            consigne(te)
        elif o==5: ##voyante
            if a=="voyante":
                    ti="choissir qui vous voulez voir"
                    voyantevote=vote(vi,ti,joeur)
                    votevoyante=voyantevote.encode()
                    connexion_client.send(votevoyante)
                    votevoyante=connexion_client.recv(1024)
                    voyantevote=votevoyante.decode()
                    consigne(voyantevote)
        elif o==6: ##vote loup
            if a=="loup garou":
                    if vi[coop]==1:
                            vi[coop]=0
                            coopd=0
                    ti="choissiez qui vous voulez tuer"
                    llouuup=vote(vi,ti,joeur)
                    llouuup=str(llouuup)
                    ll=llouuup.encode()
                    connexion_client.send(ll)
                    if vi[coopd]==0:
                            vi[coop]=1
                            coopd=1
        elif o==7: ##nuit
            te="bonne nuit"
            consigne(te)
            connexion_client.send(syn)
        elif o==8: ##jour
            te="reveillez vous c'est le matin"
            consigne(te)
            connexion_client.send(syn)
        elif o==10: ## 1 mort
            mort=[]
            connexion_client.send(syn)
            m1=connexion_client.recv(1024)
            connexion_client.send(syn)
            m2=connexion_client.recv(1024)
            connexion_client.send(syn)
            m3=connexion_client.recv(1024)
            m1=mort.append(int(connexion_client.decode(m1)))
            m2=mort.append(int(connexion_client.decode(m2)))
            m3=mort.append(int(connexion_client.decode(m3)))
            exc=mun in mort
            excc=cup1 in mort
            for i in range(nbj):
                vi[i]=0
                if exc==True:
                    consigne("vous etes mort")
                    bouvle=1
                elif excc==True:
                    te="la personne qui était dans votre coeur est mort(e), le chagrin est tel que vous vous suicidez"
                    consigne(te)
                    bouvle=1
        elif o==14: ## vote village
            ti="votez pour qui tuer"
            cote_vill=vote(vi,ti,joeur)
            vii=cote_vill.encode()
            rien=connexion_client.recv(1024)
            connexion_client.send(vii)
        elif o==15: ##village gagner
            if a=="loup garou":
                    te="vous avez gagnez"
                    consigne(te)    
            elif a!="loup garou":        
                    te="vous avez perdu"
                    consigne(te)
        elif o==16: ##loup gagner
            if a=="loup garou":
                    te="vous avez perdu"
                    consigne(te)
            else:
                    te="vous avez gagnez"
                    consigne(te)
        elif o==17: ##soucière
            connexion_client.send(syn)
            print("1")
            t=connexion_client.recv(1024)
            print("vote luup recu")
            ttt=t.decode()
            ttt=int(ttt)
            vi[ttt]=0
            print(ttt)
            tt="sauver le joeur " + joeur[ttt]
            va=88
            while va==88 or va=="":
                    fj = Tk()
                    fj.title("sorciere")
                    value = StringVar()
                    if kill_sou==0 and sauver_sou==0:
                        if sauver_sou==0:
                            sauver = Radiobutton(fj, text=tt, variable=value, value=13).pack()
                        if kill_sou==0:
			                if vi[0]==1:
			                    bj1 = Radiobutton(fj, text=joeur[0], variable=value, value=0).pack()
			                if vi[1]==1:
			                    bj2 = Radiobutton(fj, text=joeur[1], variable=value, value=1).pack()
			                if vi[2]==1:
			                    bj3 = Radiobutton(fj, text=joeur[2], variable=value, value=2).pack()
			                if vi[3]==1:
			                    bj4 = Radiobutton(fj, text=joeur[3], variable=value, value=3).pack()
			                if vi[4]==1:
			                    bj5 = Radiobutton(fj, text=joeur[4], variable=value, value=4).pack()
			                if vi[5]==1:
			                    bj6 = Radiobutton(fj, text=joeur[5], variable=value, value=5).pack()
			                if vi[6]==1:
			                    bj7 = Radiobutton(fj, text=joeur[6], variable=value, value=6).pack()
			                if vi[7]==1:
			                    bj8 = Radiobutton(fj, text=joeur[7], variable=value, value=7).pack()
			                if vi[8]==1:
			                    bj9 = Radiobutton(fj, text=joeur[8], variable=value, value=8).pack()
			                if vi[9]==1:
			                    bj10 = Radiobutton(fj, text=joeur[9], variable=value, value=9).pack()
			                if vi[10]==1:
			                    bj11 = Radiobutton(fj, text=joeur[10], variable=value, value=10).pack()
			                if vi[11]==1:
			                    bj12 = Radiobutton(fj, text=joeur[11], variable=value, value=11).pack()

                        rien = Radiobutton(fj, text="rien faire", variable=value, value=12).pack()
                        bvalider=Button(fj, text ='Valider',command=fj.quit).pack(padx=5, pady=5)
                        fj.mainloop()
                        va=int(value.get())
                        ttt=int(ttt)
                        vi[ttt]=1
                        fj.destroy()
                    else:
                        va=12
            if va==13:
                    va=str(va)
                    va=va.encode()
                    sauver_sou +=1
                    connexion_client.send(va)
            elif va==1 or va==2 or va==3 or va==4 or va==5 or va==6 or va==7 or va==8 or va==9 or va==10 or va==11 or va==0:
                    kill_sou +=1
                    va=str(va)
                    va=va.encode()
                    connexion_client.send(va)
            elif va==12:
                    va=str(va)
                    va=va.encode()
                    connexion_client.send(va)
        elif o==888:
            print("888 recu")
        elif o==404:
            deco=1
            bouvle=1

while deco==0:
    rr=connexion_client.recv(1024)
    r=rr.decode()
    if r==404:
            deco=1

connexion_client.close()
