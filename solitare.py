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

def generate_kol():
    kol=[]
   
    for i in range(52):
        uniq=False
        while not uniq:
            el=[randint(1,4),randint(1,13),False]
            if el not in kol:
                uniq=True
        kol.append(el)
    return kol
def spl_into(kol):
    kol[0][2]=True
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
def DTypeFlipFlop(t1,t2):
    if len(t1)>=1:
        t2.append(t1[-1])
        del t1[-1]
    else:
        t1=t2[::-1]
        t2.clear()
    return t1,t2

def main():
    intro()
    kol=generate_kol()
    t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4=spl_into(kol)
    
    cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4)
    
    while True:
        print('Enter what colum,row do you move& (e.x. "5 5")')
        while True: 
            try: clm,row=map(int,input().split());break; 
            except ValueError: continue
        if clm==1 and row==0:
            t1,t2=DTypeFlipFlop(t1,t2)
            if len(t1)>=1: t1[-1][2]=False
            if len(t2)>=1: t2[-1][2]=True        
            
        else: 
            print('Enter where do you move? (e.x. "5 5")')
            while True:
                try: toclm, torow=map(int,input().split());break; 
                except ValueError: continue
            
            s = [s1, s2, s3, s4, s5, s6, s7]
            w = [w1, w2, w3, w4]
            for i in range(len(s)):
                if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
            if row==0 and clm==2 and torow!=0:
                toclm-=1
                if len(t2)==0:
                    cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4)
                    continue
                am=1
                if len(t2)==3 and (t2[2] == True or t2[2] == False): t2 = [t2]
                if len(s[toclm])>=1:
                    if s[toclm][-1][0]==1 or s[toclm][-1][0]==4: InternalPointerVariable=True
                    else: InternalPointerVariable=False
                else:InternalPointerVariable=False
                if t2[-am][0]==1 or t2[-am][0]==4: GlobalConstantValue=True
                else: GlobalConstantValue=False
                if len(s[toclm])==0: InternalPointerVariable=not(GlobalConstantValue)
                if clm>=1 and ((len(s[toclm])==0 and t2[-am][1]==13) or ((InternalPointerVariable ^ GlobalConstantValue) and t2[-am][1]+1==s[toclm][-1][1])):
                    s[toclm].extend(t2[-am:])
                    del t2[-am:]
            elif row==0 and torow==0 and clm==2:
                toclm-=4
                if len(t2)==0:
                    cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4)
                    continue
                am=1
                if len(t2)==3 and (t2[2] == True or t2[2] == False): t2 = [t2]
                if len(w[toclm])>=1:
                    if w[toclm][-1][0]==1 or w[toclm][-1][0]==4: InternalPointerVariable=True
                    else: InternalPointerVariable=False
                else:InternalPointerVariable=False
                if t2[-am][0]==1 or t2[-am][0]==4: GlobalConstantValue=True
                else: GlobalConstantValue=False
                if len(w[toclm])==0: InternalPointerVariable=not(GlobalConstantValue)
                if clm>=1 and ((len(w[toclm])==0 and t2[-1][1]==1) or ((w[toclm][-1][0]==t2[-am][0]) and t2[-am][1]-1==w[toclm][-1][1])):
                    w[toclm].extend(t2[-am:])
                    del t2[-am:]
            elif torow==0:
                toclm-=4
                clm-=1
                am=1
                for i in range(len(s)):
                    if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
                for i in range(len(w)):
                    if len(w[i])==3 and (w[i][2]==True or w[i][2]==False): w[i][:] = [w[i].copy()]
                if len(w[toclm])>=1:
                    if w[toclm][-1][0]==1 or w[toclm][-1][0]==4: InternalPointerVariable=True
                    else: InternalPointerVariable=False
                else:InternalPointerVariable=False
                
                if s[clm][-am][0]==1 or s[clm][-am][0]==4: GlobalConstantValue=True
                else: GlobalConstantValue=False
                if len(w[toclm])==0: InternalPointerVariable=not(GlobalConstantValue)
                if clm>=0 and ((len(w[toclm])==0 and s[clm][-1][1]==1) or ((w[toclm][-1][0]==s[clm][-am][0]) and s[clm][-am][1]-1==w[toclm][-1][1])):
                    w[toclm].extend(s[clm][-am:])
                    del s[clm][-am:]
            elif row==0:
                toclm-=1
                clm-=4
                am=1
                for i in range(len(s)):
                    if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
                for i in range(len(w)):
                    if len(w[i])==3 and (w[i][2]==True or w[i][2]==False): w[i][:] = [w[i].copy()]
                if len(s[toclm])>=1:
                    if s[toclm][-1][0]==1 or s[toclm][-1][0]==4: InternalPointerVariable=True
                    else: InternalPointerVariable=False
                else:InternalPointerVariable=False
                if w[clm][-am][0]==1 or w[clm][-am][0]==4: GlobalConstantValue=True
                else: GlobalConstantValue=False
                if len(s[toclm])==0: InternalPointerVariable=not(GlobalConstantValue)
                if clm>=0 and ((len(s[toclm])==0 and w[clm][-am][1]==13) or ((InternalPointerVariable ^ GlobalConstantValue) and w[clm][-am][1]+1==s[toclm][-1][1])):
                    s[toclm].extend(w[clm][-am:])
                    del w[clm][-am:]
            else:
                toclm-=1
                clm-=1
                am=int(input('How many cards would you like to take:'))
                for i in range(len(s)):
                    if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
                if len(s[toclm])>=1:
                    if s[toclm][-1][0]==1 or s[toclm][-1][0]==4: InternalPointerVariable=True
                    else: InternalPointerVariable=False
                else:InternalPointerVariable=False
                if s[clm][-am][0]==1 or s[clm][-am][0]==4: GlobalConstantValue=True
                else: GlobalConstantValue=False
                if len(s[toclm])==0: InternalPointerVariable=not(GlobalConstantValue)
                if clm>=0 and ((len(s[toclm])==0 and s[clm][-am][1]==13) or ((InternalPointerVariable ^ GlobalConstantValue) and s[clm][-am][1]+1==s[toclm][-1][1])) and s[clm][-am][2]:
                    s[toclm].extend(s[clm][-am:])
                    del s[clm][-am:]
                else:
                    #nt(1)
                    pass
                #else:cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4);continue
                for i in range(len(s)):
                    if len(s[i])==3 and (s[i][2]==True or s[i][2]==False): s[i][:] = [s[i].copy()]
                    #print(i)
            for i in range(len(s)):
                if len(s[i])>=1:s[i][-1][2]=True
        if len(w1)+len(w2)+len(w3)+len(w4)==52:
            break
        cout(kol,t1,t2,s1,s2,s3,s4,s5,s6,s7,w1,w2,w3,w4)
    print('GG')




if __name__=='__main__':
    main()
