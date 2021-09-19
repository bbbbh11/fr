import math as m
class frac(object):
    def __init__(frac,a,b):
        if(b==0):
            raise ZeroDivisionError()
        if(a==0):
            frac.a=0
            frac.b=1
            return None
        s=0
        while(a!=int(a)):
            s+=1
            a*=10
        b=b*10**s
        while(b!=int(b)):
            s+=1
            a*=10
            b*=10
        s=m.gcd(int(a),int(b))
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
        return('%d/%d'%(frac.a,frac.b))
class fr(object):
    def __init__(fr,a,b,c):
        #fr(a,b,c)表示a+b/c,一般地,程序会自动化简
        #目前，我们支持取绝对值，四则运算，取余，转化为浮点数或整数，比较运算
        a的整数部分=int(a)
        a=frac(a-a的整数部分,1)
        a+=frac(b,c)
        s=int(a.a/a.b)
        a的整数部分+=s
        a.a-=s*a.b
        a,b,c=a的整数部分,a.a,a.b
        if(a<0 and b>0):
            a+=1
            b-=c
        elif(a>0 and b<0):
            a-=1
            b+=c
        fr.a,fr.b,fr.c=a,b,c
    def __str__(fr):
        if fr.b==0:
            return str(fr.a)
        if(fr.a==0):
            return "%d/%d"%(fr.b,fr.c)
        if(fr.a>0):
            return("%d+%d/%d"%(fr.a,fr.b,fr.c))
        return('%d%d/%d',fr.a,fr.b,fr.c)
    def __add__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return(fr(fr1.a+fr2.a,fr1.b*fr2.c+fr1.c*fr2.b,fr1.c*fr2.c))
    def __eq__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        if(fr1.a!=fr2.a or fr1.b!=fr2.b or fr1.c!=fr2.c):
            return False
        return True
    def __lt__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        if(fr1.a<fr2.a):
            return True
        elif(fr1.b*fr2.c<fr2.b*fr1.c):
            return(True)
        return False
    def __gt__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        if(fr1.a>fr2.a):
            return True
        elif(fr1.b*fr2.c>fr2.b*fr1.c):
            return True
        return False
    def __ge__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        if(fr1.a>=fr2.a):
            return True
        elif(fr1.b*fr2.c>=fr2.b*fr1.c):
            return True
        return False
    def __le__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
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
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return(fr(fr1.a-fr2.a,fr1.b*fr2.c-fr2.b*fr1.c,fr1.c*fr2.c))
    def __mul__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return(fr(fr1.a*fr2.b,fr2.b*fr1.c*(fr1.a+1)+fr1.b*fr2.c*(fr2.a+1),fr1.c*fr2.c))
    def __truediv__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return fr(0,fr2.c*(fr1.a*fr1.c+fr1.b),fr1.c*(fr2.a*fr2.c+fr2.b))
    def __floordiv__(fr1,fr2):
        return(int(fr1/fr2))
    def __mod__(fr1,fr2):
        return(fr1-fr2*int(fr1/fr2))
#这里提供一个将其他类型的数转化为fr类的方法:)
def tofr(n) -> any:
    s=type(n)
    if(s==str):
        try:
            n=float(n)
        except:
            def lf(m):
                if(m!=''):
                    return float(m)
                return 0
            n=n.split('+')
            n[1]=n[1].split('/')
            return fr(lf(n[0]),lf(n[1][0]),lf(n[1][1]))
    if s==fr:
        return n
    return fr(0,n,1)
