import statistics
import numpy
class Math:

    def __init__(self,ages):
        self.ages=ages

    def cont(self):
        c=self.ages
        m=len(c)
        print(m)

    def sm(self):
        c=self.ages
        m=0
        i=0
        j=len(c)
        while (i<j):
            m=m+c[i]
            i+=1
        print(m)

    def mn(self):
        c=self.ages
        c.sort()
        print(c[0])

    def mx(self):
        c=self.ages
        c.sort()
        print(c[-1])


    def rng(self):
        c=self.ages
        a=max(c)-min(c)
        print(a)

    def meaan(self):
        c=self.ages
        c=self.ages
        m=0
        i=0
        j=len(c)
        while (i<j):
            m=m+c[i]
            i+=1
        v=m/len(c)
        print(v)

    def mdn(self):
        c=self.ages
        c.sort()
        f=len(c)
        if f%2==0:
            m=f/2
            e=(c[f]+c[f+1])/2
            print(e)

        elif f%2!=0:

            c=self.ages
            c.insert(-1,44)
            c.sort()
            f=len(c)
            m=f/2
            o=m+1
            e=c[m]+c[o]
            j=e/2
            print(j)

    def mod(self):
        c=self.ages
        m=0
        f=0
        i=0
        j=len(c)
        while (i<j):
            f=0
            count=0
            while(f<len(c)):
                if c[i]==c[f]:
                   count+=1
                f+=1

            if  count>=4:
                a=[count,c[i]]
                print(a)

    def sst(self):
        c=self.ages
        print(numpy.std(c))

    def vr(self):
        c=self.ages
        print(statistics.variance(c))


ag = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=Math(ag)
data.sm()
data.mn()
data.mx()
data.rng()
data.mdn()
data.mod()
data.meaan()