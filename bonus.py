(lambda i:i['main'](i))({'d':{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000},'f':lambda x,s:sum(-x['d'][u] if x['d'][u]<x['d'][v] else x['d'][u] for (u,v) in zip(s[:-1],s[1:]))+x['d'][s[-1]],'main':lambda x:print(x['f'](x,input()))})
# stdin/stdout
# "It just works" - Todd Howard
