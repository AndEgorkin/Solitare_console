from copy import deepcopy
from random import randint


def intro():
    print('****************')
    print('*              *')
    print('*   SOLITARE   *')
    print('*              *')
    print('****************')
    print('By Andrei Egorkin (AKA Kuprisel)')
    print()
    #input('Press Enter to start!')

def generate_kol(): #kol is deck 
    kol=[]
   
    for i in range(52): 
        uniq=False
        while not uniq:
            el=[randint(1,4),randint(1,13),False]
            if el not in kol:
                uniq=True
        kol.append(el)
    return kol
def spl_into(kol): #s1-7 is main field w1-7 is 4 spaces above t1 and t2 is the flip cards arrays 
    s1=kol[0]
    kol[2][2]=True
    s2=kol[1:3]
    kol[5][2]=True
    s3=kol[3:6]
    kol[9][2]=True
    s4=kol[6:10]
    kol[14][2]=True
    s5=kol[10:15]
    kol[20][2]=True
    s6=kol[15:21]
    kol[27][2]=True
    s7=kol[21:28]
    t1=kol[28:]
    
    t2=[]
    w1=[]
    w2=[]
    w3=[]
    w4=[]
    return t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4
def adpt(kol):
    if kol==[]:
        return ['--']
    if isinstance(kol[0], int):
        kol = [kol]
    for i in range(len(kol)):

        if kol[i][2]==False:
            kol[i][0]='X'
            kol[i][1]='X'
        else:
            kol[i][1]=str(kol[i][1])
            if kol[i][1]=='11':
                kol[i][1]='J'
            elif kol[i][1]=='12':
                kol[i][1]='Q'
            elif kol[i][1]=='13':
                kol[i][1]='K'
            elif kol[i][1]=='10':
                kol[i][1]='T'
            elif kol[i][1]=='1':
                kol[i][1]='A'
            if kol[i][0]==1:
                kol[i][0]='♠'
            elif kol[i][0]==2:
                kol[i][0]="\033[31m♥\033[0m"
            elif kol[i][0]==3:
                kol[i][0]="\033[31m♦\033[0m"
            elif kol[i][0]==4:
                kol[i][0]='♣'
        kol[i]=kol[i][:2]
    return kol
def cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4):
    
    t1 = adpt(deepcopy(t1))
    t2 = adpt(deepcopy(t2))
    s1 = adpt(deepcopy(s1))
    s2 = adpt(deepcopy(s2))
    s3 = adpt(deepcopy(s3))
    s4 = adpt(deepcopy(s4))
    s5 = adpt(deepcopy(s5))
    s6 = adpt(deepcopy(s6))
    s7 = adpt(deepcopy(s7))
    w1 = adpt(deepcopy(w1))
    w2 = adpt(deepcopy(w2))
    w3 = adpt(deepcopy(w3))
    w4 = adpt(deepcopy(w4))
        
    print(f"0 {''.join(map(str, t1[-1]))} {''.join(map(str, t2[-1]))}    {''.join(map(str, w1[-1]))} {''.join(map(str, w2[-1]))} {''.join(map(str, w3[-1]))} {''.join(map(str, w4[-1]))}")
    print('  1  2  3  4  5  6  7     ')
    
    def add_ms(kl,s1,s2,s3,s4,s5,s6,s7):
        for i in range(max(len(s1),len(s2),len(s3),len(s4),len(s5),len(s6),len(s7))-len(kl)):
            kl.append(['-','-'])
        return kl
    s1=add_ms(s1,s1,s2,s3,s4,s5,s6,s7)
    s2=add_ms(s2,s1,s2,s3,s4,s5,s6,s7)
    s3=add_ms(s3,s1,s2,s3,s4,s5,s6,s7)
    s4=add_ms(s4,s1,s2,s3,s4,s5,s6,s7)
    s5=add_ms(s5,s1,s2,s3,s4,s5,s6,s7)
    s6=add_ms(s6,s1,s2,s3,s4,s5,s6,s7)
    s7=add_ms(s7,s1,s2,s3,s4,s5,s6,s7)
    
    for i in range(len(s1)):
        print(f'{1 if i==0 else ' '} {''.join(map(str, s1[i]))} {''.join(map(str, s2[i]))} {''.join(map(str, s3[i]))} {''.join(map(str, s4[i]))} {''.join(map(str, s5[i]))} {''.join(map(str, s6[i]))} {''.join(map(str, s7[i]))}')
def FlipCard(t1,t2):
    if len(t1)>=1:
        t2.append(t1[-1])
        del t1[-1]
    else:
        t1=t2[::-1]
        t2.clear()
    return t1,t2

def MoveCard(Mfrom,Mto,clm,toclm,st,am):
    if len(Mfrom)<1:return Mfrom,Mto
    if Mfrom[-am][0]==1 or Mfrom[-am][0]==4: ColourFlag2=True
    else: ColourFlag2=False
    if len(Mto)==0: ColourFlag1=not(ColourFlag2)
    else:
        if Mto[-1][0]==1 or Mto[-1][0]==4: ColourFlag1=True
        else: ColourFlag1=False
    if st:
        if len(Mto)==0 and Mfrom[-am][1]!=13: return Mfrom,Mto
        if ((len(Mto)==0) or ((ColourFlag1 ^ ColourFlag2) and Mfrom[-am][1]+1==Mto[-1][1])) and Mfrom[-am][2]:
            Mto.extend(Mfrom[-am:])
            del Mfrom[-am:]
        else:
            return Mfrom,Mto
    else:
        if len(Mto)==0 and Mfrom[-am][1]!=1: return Mfrom,Mto
        if (len(Mto)==0) or (((Mto[-1][0]==Mfrom[-am][0]) and Mfrom[-am][1]-1==Mto[-1][1]) and Mfrom[-am][2]):
            Mto.extend(Mfrom[-am:])
            del Mfrom[-am:]
        else:
            return Mfrom,Mto
    return Mfrom,Mto

def main():
    intro()
    kol=generate_kol()
    t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4=spl_into(kol)
    s = [s1, s2, s3, s4, s5, s6, s7]
    w = [w1, w2, w3, w4]
    while True:
        print()
        for i in range(len(s)):
            if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
        for i in range(len(w)):
            if len(w[i])==3 and (w[i][2]==True or w[i][2]==False): w[i][:] = [w[i].copy()]
        if len(t2)==3 and (t2[2] == True or t2[2] == False): t2 = [t2]
        if len(t1)==3 and (t1[2] == True or t1[2] == False): t1 = [t1]
        for i in range(len(s)):
            if len(s[i])>=1:s[i][-1][2]=True
        cout(kol,t1,t2,s[0],s[1],s[2],s[3],s[4],s[5],s[6],w[0],w[1],w[2],w[3])
        print('Enter what colum,row do you move? (e.x. "5 1")')
        while True: 
            try: clm,row=map(int,input().split());break; #clm is colum
            except ValueError: continue
        if clm==1 and row==0:
            t1,t2=FlipCard(t1,t2)
            if len(t1)>=1: t1[-1][2]=False
            if len(t2)>=1: t2[-1][2]=True
        elif clm==0 and row==0:
            break        
        else: 
            print('Enter where do you move? (e.x. "5 1")')
            while True:
                try: toclm, torow=map(int,input().split());break; 
                except ValueError: continue

            for i in range(len(s)):
                if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
            if row==0 and clm==2 and torow!=0:
                if toclm not in range(1,8): continue
                toclm-=1
                am=1
                t2,s[toclm]=MoveCard(t2,s[toclm],clm,toclm,True,am)
            elif row==0 and torow==0 and clm==2:
                if toclm not in range(4,8): continue
                toclm-=4
                if len(t2)==0:continue
                am=1
                t2,w[toclm]=MoveCard(t2,w[toclm],clm,toclm,False,am)
            elif torow==0 and row==0: continue
            elif torow==0:
                if toclm not in range(4,8): continue
                if clm not in range(1,8): continue
                toclm-=4
                clm-=1
                am=1
                s[clm],w[toclm]=MoveCard(s[clm],w[toclm],clm,toclm,False,am)
            elif row==0:
                if toclm not in range(1,8): continue
                if clm not in range(4,8): continue
                toclm-=1
                clm-=4
                am=1
                w[clm],s[toclm]=MoveCard(w[clm],s[toclm],clm,toclm,True,am)
            else:
                if toclm not in range(1,8): continue
                if clm not in range(1,8): continue
                toclm-=1
                clm-=1
                am=input('How many cards would you like to take:')
                try:
                    am=int(am)
                except:
                    continue
                if am>len(s[clm]) or am<=0:continue
                s[clm],s[toclm]=MoveCard(s[clm],s[toclm],clm,toclm,True,am)

        if len(w1)+len(w2)+len(w3)+len(w4)==52:
            break   
    if len(w1)+len(w2)+len(w3)+len(w4)==52:
        print('You won!') 
    else:
        print('Thanks for playing!')

if __name__=='__main__':
    main()
