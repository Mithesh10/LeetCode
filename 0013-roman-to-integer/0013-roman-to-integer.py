class Solution(object):
    def romanToInt(self, s):
        if len(s)>0 and len(s)<16:
            n,c=0,''
            for i in s:
                if i=='I':
                    n+=1
                    c='I'
                elif i=='V':
                    if c=='I':
                        c=''
                        n+=3
                    else:
                        n+=5
                elif i=='X':
                    if c=='I':
                        c='X'
                        n+=8
                    else:
                        c='X'
                        n+=10
                elif i=='L':
                    if c=='X':
                        c=''
                        n+=30
                    else:
                        n+=50
                elif i=='C':
                    if c=='X':
                        c='C'
                        n+=80
                    else:
                        c='C'
                        n+=100
                elif i=='D':
                    if c=='C':
                        c=''
                        n+=300
                    else:
                        n+=500
                elif i=='M':
                    if c=='C':
                        c=''
                        n+=800
                    else:
                        n+=1000
                else:
                    return
            return n