class Solution:
    def nearestPalindromic(self, n: str) -> str:
        y=int(n)
        x=len(n)
        ls,mid=[10**(x)+1,10**(x)-1,10**(x-1)+1,10**(x-1)-1],x//2
        if x%2==1:
            e=int(n[:mid+1])
            ls.append(int(n[:mid]+n[mid]+(n[:mid][::-1])))
            ls.append(int(str(e+1)+(str(e+1)[::-1][1:])))
            ls.append(int(str(e-1)+(str(e-1)[::-1][1:])))
        else:
            e=int(n[:mid])
            ls.append(int(n[:mid]+(n[:mid][::-1])))
            ls.append(int(str(e+1)+(str(e+1)[::-1])))
            ls.append(int(str(e-1)+(str(e-1)[::-1])))
        diff=float(inf)
        j=0
        for i in range(len(ls)):
            s=abs(ls[i]-y)
            if s<diff and s!=0:
                diff=s
                j=i
            if s==diff and ls[i]<ls[j]:
                j=i
        return str(ls[j])