##################### Hacker Rank Problem Solving (Basic) Test Question. #####################

# Find the maximum vowels a substring of a given string of length of a given length can have. #

def func(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    maxv=[]
    for i in range(0, len(s)):
        substring=''
        vowelcount = 0
        if i<=len(s)-k:
            for j in range(i, i+k):
                substring += s[j]
            for i in substring:
                if i in vowels:
                    vowelcount+=1
            if len(maxv)==0:
                maxv.append({'substring': substring, 'vowelcount': vowelcount})
            elif maxv[len(maxv)-1]['vowelcount']==vowelcount:
                maxv.append({'substring': substring, 'vowelcount': vowelcount})
            elif maxv[len(maxv)-1]['vowelcount']<vowelcount:
                maxv=[{'substring': substring, 'vowelcount': vowelcount}]                
    if maxv[len(maxv)-1]['vowelcount']>0:
        return maxv[0]

print(func('abhiina', 3))