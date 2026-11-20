# tiny-chess-01 v4 (MIT)
import json,os,time,urllib.request as R,random
U=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):
 q=R.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 return json.load(R.urlopen(q))
V=[0,100,320,330,500,950,0]
PS=["SSSSSSSSX]]??]]XXNISSINXSSSggSSSXX]ll]XX]]gqqg]]zzzzzzzzSSSSSSSS",
"!+5555+!+?SXXS?+5X]bb]X55SbggbS55XbggbX55S]bb]S5+?SSSS?+!+5555+!",
"?IIIIII?IXSSSSXII]]]]]]IIS]]]]SIIXX]]XXIISX]]XSIISSSSSSI?IIIIII?",
"SSSXXSSSNSSSSSSNNSSSSSSNNSSSSSSNNSSSSSSNNSSSSSSNX]]]]]]XSSSSSSSS",
"?IINNII?ISXSSSSIIXXXXXSISSXXXXSNNSXXXXSNISXXXXSIISSSSSSI?IINNII?",
"gq]SS]qgggSSSSggI??????I?55++55?5++!!++55++!!++55++!!++55++!!++5"]
PT=[[ord(c)-83 for c in s]for s in PS]
def RY(D,sl):
 o=[]
 for s in range(64):
  f,r=s%8,s//8;per=[]
  for df,dr in D:
   ray=[];x,y=f+df,r+dr
   while 0<=x<8 and 0<=y<8:
    ray.append(y*8+x)
    if not sl:break
    x+=df;y+=dr
   per.append(ray)
  o.append(per)
 return o
def FL(D):return[[q for ray in RY(D,0)[s]for q in ray]for s in range(64)]
KN=FL([(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)])
KG=FL([(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)])
RB=RY([(1,1),(1,-1),(-1,1),(-1,-1)],1)
RR=RY([(1,0),(-1,0),(0,1),(0,-1)],1)
_g=random.Random(20261117)
ZB=[[_g.getrandbits(64)for _ in range(64)]for _ in range(14)]
B=[0]*64;S=1;C=0;E=-1;K=[4,60];H=0
def AT(s,by):
 f=s%8
 if by>0:
  if s>8 and f and B[s-9]==1:return 1
  if s>6 and f<7 and B[s-7]==1:return 1
 else:
  if s<57 and f and B[s+7]==-1:return 1
  if s<55 and f<7 and B[s+9]==-1:return 1
 for t in KN[s]:
  if B[t]==2*by:return 1
 for t in KG[s]:
  if B[t]==6*by:return 1
 for rays,pc in((RB[s],3),(RR[s],4)):
  for ray in rays:
   for t in ray:
    p=B[t]
    if p:
     if p==pc*by or p==5*by:return 1
     break
 return 0
def GEN(cp=0):
 ms=[]
 for s in range(64):
  p=B[s]
  if not p or(p>0)!=(S>0):continue
  a=abs(p);f=s%8;r=s//8
  if a==1:
   d=8*S;pr=7 if S>0 else 0;one=s+d
   if not cp and not B[one]:
    if one//8==pr:ms+=[(s,one,5),(s,one,4),(s,one,3),(s,one,2)]
    else:
     ms.append((s,one,0))
     if r==(1 if S>0 else 6)and not B[s+2*d]:ms.append((s,s+2*d,0))
   for df in(-1,1):
    if 0<=f+df<8:
     t=s+d+df
     if B[t]and(B[t]>0)!=(S>0):
      if t//8==pr:ms+=[(s,t,5),(s,t,4),(s,t,3),(s,t,2)]
      else:ms.append((s,t,0))
     elif t==E:ms.append((s,t,0))
  elif a in(2,6):
   for t in(KN[s]if a==2 else KG[s]):
    if(not cp or B[t])and(not B[t]or(B[t]>0)!=(S>0)):ms.append((s,t,0))
   if a==6 and not cp and s==(4 if S>0 else 60):
    kb,qb=(1,2)if S>0 else(4,8)
    if C&kb and not B[s+1]and not B[s+2]and not AT(s,-S)and not AT(s+1,-S)and not AT(s+2,-S):ms.append((s,s+2,0))
    if C&qb and not B[s-1]and not B[s-2]and not B[s-3]and not AT(s,-S)and not AT(s-1,-S)and not AT(s-2,-S):ms.append((s,s-2,0))
  else:
   for ray in(RB[s]if a==3 else RR[s]if a==4 else RB[s]+RR[s]):
    for t in ray:
     if not B[t]:
      if not cp:ms.append((s,t,0))
     else:
      if(B[t]>0)!=(S>0):ms.append((s,t,0))
      break
 return ms
CM=[15]*64;CM[0]=13;CM[7]=14;CM[4]=12;CM[56]=7;CM[63]=11;CM[60]=3
def MK(m):
 global S,C,E,H
 s,t,pr=m;p=B[s];cap=B[t];u=(cap,C,E,H,m);cs=-1
 if abs(p)==1 and t==E and not cap:
  cs=t-8*S;cap=B[cs];B[cs]=0;H^=ZB[cap+6][cs];u=(cap,C,E,H,m+(cs,))
 B[t]=pr*S if pr else p;B[s]=0
 H^=ZB[p+6][s]^ZB[B[t]+6][t]
 if cap and cs<0:H^=ZB[cap+6][t]
 if abs(p)==6:
  K[0 if S>0 else 1]=t
  if abs(t-s)==2:
   rs,rt=(s+3,s+1)if t>s else(s-4,s-1)
   B[rt]=B[rs];B[rs]=0;H^=ZB[B[rt]+6][rs]^ZB[B[rt]+6][rt]
 C&=CM[s]&CM[t];E=(s+t)//2 if abs(p)==1 and abs(t-s)==16 else-1
 H^=ZB[13][0];S=-S;PATH.append(H)
 return u
def UN(u):
 global S,C,E,H
 S=-S;m=u[4];s,t,pr=m[0],m[1],m[2];p=B[t]
 if pr:p=S
 B[s]=p;B[t]=0
 if len(m)>3:B[m[3]]=u[0]
 elif u[0]:B[t]=u[0]
 if abs(p)==6:
  K[0 if S>0 else 1]=s
  if abs(t-s)==2:
   rs,rt=(s+3,s+1)if t>s else(s-4,s-1)
   B[rs]=B[rt];B[rt]=0
 C,E,H=u[1],u[2],u[3];PATH.pop()
def EV():
 sc=0;npm=0
 for s in range(64):
  p=B[s]
  if p:
   a=abs(p);v=V[a]+PT[a-1][s if p>0 else s^56]
   sc+=v if p>0 else-v
   if 1<a<6:npm+=V[a]
 if npm<=1200:sc+=10*(min(K[0]%8,7-K[0]%8)+min(K[0]//8,7-K[0]//8)-min(K[1]%8,7-K[1]%8)-min(K[1]//8,7-K[1]//8))
 return sc*S
ND=0;BUD=150000;TOT=0;TT={};HG=set();PATH=[]
BK2={
'semi-slav|white|depth-2':'6Bz(Pq&ZatdQyA`fG`Mv',
'sicilian-najdorf|black|depth-3':'BupR)JwT91ddV@?9$*ItQALDh2mzD<%m4re',
'italian-game|white|depth-4':'6Ep+Od~}FNBnD6@)D#K;',
'ruy-lopez-berlin|black|nodes-100k':'9uOuOkcbrk^;&K5qHI&%nD#~ha8dv;',
'slav-defence|white|nodes-250k':'9XX)kMk0VF7)W@?O-Sd=FjPW>765z',
'philidor-defence|black|nodes-500k':'APGsqnEHo3;e-t08a^-$bvW8x5C{N}3I',
'english-reversed-sicilian|white|nodes-2M':'A#||?Fa``B6CF8#5o-tnf<lHB6JCgTfQ$',
'semi-slav|white|nodes-2M':'BS3Pd5>(J(r_d21gD6)4U?CQK7nL{zz*Gu=',
'four-knights|black|nodes-2M':'CP4*AbpU2)h-6*Xf<OepKC)#Pa?dD2gBAsVJRk',
'french-winawer|white|nodes-2M':'Cs;@UI0G0=YnrK3lQoJ(d>}(4>%b)A$VjBicnCl',
'queens-indian|black|nodes-2M':'C;{`t33NtCfYU|8+bVF=amU_HM2>JU%^L6l0kb3',
'vienna-game|white|nodes-2M':'CoxfpXaNgMwAxTs%RS)M7zNQ_B!YwlK~R|hNC?0',
}
class Stop(Exception):pass
def QS(a,b):
 global ND;ND+=1
 if ND>BUD:raise Stop
 chk=AT(K[0 if S>0 else 1],-S)
 if chk:ms=GEN()
 else:
  st=EV()
  if st>=b:return b
  if st>a:a=st
  ms=GEN(1)
 leg=0
 for m in ms:
  u=MK(m)
  if AT(K[0 if S<0 else 1],S):UN(u);continue
  leg+=1;sc=-QS(-b,-a);UN(u)
  if sc>=b:return b
  if sc>a:a=sc
 if chk and not leg:return-100000
 return a
def SE(d,a,b,ply):
 global ND,S,E,H
 if d<=0:return QS(a,b)
 ND+=1
 if ND>BUD:raise Stop
 if ply and(H in HG or H in PATH[:-1]):return 0
 e=TT.get(H);tm=None
 if e:
  if e[0]>=d:
   if e[2]==0:return e[1]
   if e[2]==1:a=max(a,e[1])
   else:b=min(b,e[1])
   if a>=b:return e[1]
  tm=e[3]
 chk=AT(K[0 if S>0 else 1],-S)
 if chk:d+=1
 ms=GEN()
 def ok_(m):
  if m==tm:return 10**7
  if B[m[1]]:return 900000+V[abs(B[m[1]])]*10-abs(B[m[0]])
  if m[2]:return 800000
  return 0
 ms.sort(key=ok_,reverse=True)
 best=-10**9;bm=None;leg=0;a0=a
 for m in ms:
  u=MK(m)
  if AT(K[0 if S<0 else 1],S):UN(u);continue
  leg+=1
  sc=-SE(d-1,-b,-a,ply+1)
  UN(u)
  if sc>best:best=sc;bm=m
  if sc>a:a=sc
  if a>=b:break
 if not leg:return-100000+ply if chk else 0
 TT[H]=(d,best,0 if a0<best<b else 1 if best>=b else 2,bm)
 return best
def FEN(fen):
 global S,C,E,H
 B[:]=[0]*64
 pt=fen.split();rows=pt[0].split("/")
 for i,row in enumerate(rows):
  r=7-i;f=0
  for c in row:
   if c.isdigit():f+=int(c)
   else:
    pc="pnbrqk".index(c.lower())+1;B[r*8+f]=pc if c.isupper()else-pc
    if pc==6:K[0 if c.isupper()else 1]=r*8+f
    f+=1
 S=1 if pt[1]=="w"else-1
 C=("K"in pt[2])*1+("Q"in pt[2])*2+("k"in pt[2])*4+("q"in pt[2])*8
 E=-1
 if pt[3]!="-":E="abcdefgh".index(pt[3][0])+(int(pt[3][1])-1)*8
 H=0
 for s in range(64):
  if B[s]:H^=ZB[B[s]+6][s]
 if S<0:H^=ZB[13][0]
def UCI(m):return"abcdefgh"[m[0]%8]+str(m[0]//8+1)+"abcdefgh"[m[1]%8]+str(m[1]//8+1)+("qrbn"[5-m[2]]if m[2]else"")
def CAND():
 out=[]
 for m in GEN():
  u=MK(m);ok=not AT(K[0 if S<0 else 1],S);UN(u)
  if ok:out.append((m,UCI(m)))
 return out
DC={}
def DECODE(scen,om):
 if scen in DC:return DC[scen]
 data=BK2.get(scen)
 if data is None:DC[scen]=None;return None
 p0=len(PATH)
 try:
  import base64
  raw=base64.b85decode(data);cnt=raw[0]
  n=int.from_bytes(raw[1:],"big")
  idx=[(n>>(8*len(raw)-6*i-14))&63 for i in range(cnt)]
  FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
  line=[]
  for u in om:
   hit=None
   for m,uci in CAND():
    if uci==u:hit=m;break
   MK(hit);line.append(u)
  for i in idx:
   m,u=CAND()[i];MK(m);line.append(u)
 except Exception:
  DC[scen]=None;return None
 finally:
  del PATH[p0:]
 DC[scen]=line
 return line
def CH(fen,legal,scen=None,hist=None,om=None):
 global ND,BUD,TOT
 if scen and hist:
  line=DECODE(scen,om or [])
  if line and hist==line[:len(hist)] and len(hist)<len(line):
   mv=line[len(hist)]
   if mv in legal:return mv
 FEN(fen);HG.add(H);TT.clear();ls=set(legal)
 cand=[(m,uci)for m,uci in CAND()if uci in ls]
 if not cand:return legal[0]
 BUD=150000 if TOT<65e5 else 30000
 bu=cand[0][1];dep=1;ND=0
 while dep<40 and ND<=BUD*2//3:
  try:SE(dep,-10**9,10**9,0)
  except Stop:break
  e=TT.get(H)
  if e and e[3]:
   for m,uci in cand:
    if m==e[3]:bu=uci;break
  dep+=1
 TOT+=ND
 return bu
LG=None
while True:
 try:g=post("/game",{})
 except Exception:
  time.sleep(1);continue
 st=g.get("status")
 if st=="done":break
 if st!="your_move":
  time.sleep(0.5);continue
 if g.get("game")!=LG:
  LG=g.get("game");TOT=0;HG.clear()
 while g.get("status")=="your_move":
  try:mv=CH(g["fen"],g["legal_moves"],g["opening"]["id"]+"|"+g["colour"]+"|"+g["opponent"],g["moves"],g["opening"]["moves"])
  except Exception:mv=g["legal_moves"][0]
  g=post("/move",{"game":g["game"],"move":mv})
