

#(x,y) position is for sprite sheet location of each card
class symbol:
    def __init__(self,name,x,y):
        self.Name=name
        self.X=x
        self.Y=y

n=symbol("n",0,0)
wa=symbol("wa",80,0)
ra=symbol("ra",160,0)
ya=symbol("ya",240,0)
ma=symbol("ma",320,0)
ha=symbol("ha",400,0)
na=symbol("na",480,0)
ta=symbol("ta",560,0)
sa=symbol("sa",640,0)
ka=symbol("ka",720,0)
a=symbol("a",785,0)

wi=symbol("wi",80,120)
ri=symbol("ri",160,120)
mi=symbol("mi",320,120)
hi=symbol("hi",400,120)
ni=symbol("ni",480,120)
chi=symbol("chi",560,120)
shi=symbol("shi",640,120)
ki=symbol("ki",720,120)
i=symbol("i",785,120)

ru=symbol("ru",160,230)
yu=symbol("yu",240,230)
mu=symbol("mu",320,230)
fu=symbol("fu",400,230)
nu=symbol("nu",480,230)
tsu=symbol("tsu",560,230)
su=symbol("su",640,230)
ku=symbol("ku",720,230)
u=symbol("u",785,230)


we=symbol("we",80,340)
re=symbol("re",160,340)
me=symbol("me",320,340)
he=symbol("he",400,340)
ne=symbol("ne",480,340)
te=symbol("te",560,340)
se=symbol("se",640,340)
ke=symbol("ke",720,340)
e=symbol("e",785,340)

wo=symbol("wo",80,450)
ro=symbol("ro",160,450)
yo=symbol("yo",240,450)
mo=symbol("mo",320,450)
ho=symbol("ho",400,450)
no=symbol("no",480,450)
to=symbol("to",560,450)
so=symbol("so",640,450)
ko=symbol("ko",720,450)
o=symbol("o",785,450)


#create full deck of flash cards
deck=[n,wa,ra,ya,ma,ha,na,ta,sa,ka,a,
      wi,ri,mi,hi,ni,chi,shi,ki,i,
      ru,yu,mu,fu,nu,tsu,su,ku,u,
      we,re,me,he,ne,te,se,ke,e,
      wo,ro,yo,mo,ho,no,to,so,ko,o]


