#修复了一些问题
import math as m
def g(n):
        if n==int(n):
            return 0
        n=str(n)
        return len(n)-n.find('.')-1
class frac(object):
    def __init__(frac,a,b):
        if(b==0):
            raise ZeroDivisionError()
        if(a==0):
            frac.a=0
            frac.b=1
            return None
        s=max(g(a),g(b))
        a,b=a*10**s,b*10**s
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
    def __init__(fr,a,b,c,isint=0):
        #fr(a,b,c)表示a+b/c,一般地,程序会自动化简
        #目前，我们支持取绝对值，四则运算，取余，转化为浮点数或整数，比较运算
        if(isint):
            if(c<0):
                b=-b
                c=-c
            s=b//c
            a=a+s
            b=b-s*c
            c=c
            s=m.gcd(int(b),int(c))
            b,c=b//s,c//s
        else:
            a的整数部分=int(a)
            a=frac(a,1)
            a.a-=a.b*a的整数部分
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
    def __repr__(fr):
        if fr.b==0:
            return str(fr.a)
        if(fr.a==0):
            return "%d/%d"%(fr.b,fr.c)
        if(fr.a>0):
            return("%d+%d/%d"%(fr.a,fr.b,fr.c))
        return('%d%d/%d'%(fr.a,fr.b,fr.c))
    def __add__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return(fr(fr1.a+fr2.a,fr1.b*fr2.c+fr1.c*fr2.b,fr1.c*fr2.c,1))
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
        return(fr(fr1.a-fr2.a,fr1.b*fr2.c-fr2.b*fr1.c,fr1.c*fr2.c,1))
    def __mul__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return(fr(fr1.a*fr2.b,fr2.b*fr1.c*(fr1.a+1)+fr1.b*fr2.c*(fr2.a+1),fr1.c*fr2.c,1))
    def __truediv__(fr1,fr2):
        if(type(fr1)!=fr):
            fr1=fr(0,fr1,1)
        if(type(fr2)!=fr):
            fr2=fr(0,fr2,1)
        return fr(0,fr2.c*(fr1.a*fr1.c+fr1.b),fr1.c*(fr2.a*fr2.c+fr2.b,1))
    def __floordiv__(fr1,fr2):
        return(int(fr1/fr2))
    def __mod__(fr1,fr2):
        return(fr1-fr2*int(fr1/fr2))
