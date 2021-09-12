import math as m
def g(n):
    #返回n的小数位数，去掉末尾的0
    if(int(n)==n):
        return(0)
    n=str(n)
    while(n[-1]=='0'):
        n=n[0:-1]
    s=len(n)
    for i in range(s):
        if(n[i]=='.'):
            return(s-i-1)
class frac(object):
    def __init__(frac,a,b):
        if(b==0):
            raise ZeroDivisionError()
        if(a==0):
            frac.a=0
            frac.b=1
            return None
        s=10**max(g(a),g(b))
        a=int(a*s)
        b=int(b*s)
        s=m.gcd(a,b)
        a/=s
        b/=s
        if(b<0):
            a=-a
            b=-b
        frac.a=a
        frac.b=b
    def __add__(frac1,frac2):
        return(frac(frac1.a*frac2.b+frac1.b*frac2.a,frac1.b*frac2.b))
    def __repr__(frac):
        return("%d/%d"%(frac.a,frac.b))
def tofrac(n):
    if(type(n)==frac):
        return(n)
    return(frac(n,1))
class fr(object):
    def __init__(fr,a,b,c,skip=False):
        #fr(a,b,c)表示a+b/c,一般地,程序会自动化简;若skip为True,则跳过化简环节
        #目前，我们支持取绝对值，四则运算，取余，转化为浮点数或整数，比较运算
        if(skip):
            fr.a,fr.b,fr.c=a,b,c
            return(None)
        a的整数部分=int(a)
        a的小数位数=g(a)
        a的小数部分=int((a-a的整数部分)*10**a的小数位数)/10**a的小数位数
        分数部分=frac(a的小数部分,1)+frac(b,c)
        a=int(分数部分.a/分数部分.b)
        c=分数部分.b
        b=分数部分.a-a*c
        a+=a的整数部分
        if(a<0 and b>0):
            a+=1
            b-=c
        elif(a>0 and b<0):
            a-=1
            b+=c
        fr.a,fr.b,fr.c=a,b,c
    def __repr__(fr):
        return('fr(%d,%d,%d)'%(fr.a,fr.b,fr.c))
    def __add__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        return(fr(fr1.a+fr2.a,fr1.b*fr2.c+fr1.c*fr2.b,fr1.c*fr2.c))
    def __eq__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        if(fr1.a!=fr2.a or fr1.b!=fr2.b or fr1.c!=fr2.c):
            return False
        return True
    def __lt__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        if(fr1.a<fr2.a):
            return True
        elif(fr1.b*fr2.c<fr2.b*fr1.c):
            return(True)
        return False
    def __gt__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        if(fr1.a>fr2.a):
            return True
        elif(fr1.b*fr2.c>fr2.b*fr1.c):
            return True
        return False
    def __ge__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        if(fr1.a>=fr2.a):
            return True
        elif(fr1.b*fr2.c>=fr2.b*fr1.c):
            return True
        return False
    def __le__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        if(fr1.a<=fr2.a):
            return True
        elif fr1.b*fr2.c<=fr2.b*fr1.c:
            return(True)
        return False
    def __int__(fr):
        return fr.a
    def __float__(fr):
        return fr.a+fr.b/fr.c
    def __abs__(fr):
        if(fr.b<0):
            return(fr(-fr.a,-fr.b,fr.c))
        return fr
    def __sub__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        return(fr(fr1.a-fr2.a,fr1.b*fr2.c-fr2.b*fr1.c,fr1.c*fr2.c))
    def __mul__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        return(fr(fr1.a*fr2.b,fr2.b*fr1.c*(fr1.a+1)+fr1.b*fr2.c*(fr2.a+1),fr1.c*fr2.c))
    def __truediv__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=tofrac(fr1)
            s=int(fr1.a/fr1.b)
            fr1=fr(s,fr1.a-s*fr1.b,fr1.b,True)
        if(type(fr2)!=fr):
            fr2=tofrac(fr2)
            s=int(fr2.a/fr2.b)
            fr2=fr(s,fr2.a-s*fr2.b,fr2.b,True)
        return fr(0,fr2.c*(fr1.a*fr1.c+fr1.b),fr1.c*(fr2.a*fr2.c+fr2.b))
    def __floordiv__(fr1,fr2):
        return(int(fr1/fr2))
    def __mod__(fr1,fr2):
        return(fr1-fr2*int(fr1/fr2))
#这里提供一个将其他类型的数转化为fr类的方法:)
def tofr(n):
    s=type(n)
    if s==fr:
        return n
    elif s==frac:
        return fr(0,n.a,n.b)
    return fr(0,n,1)
