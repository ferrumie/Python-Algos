# def fib(n):
#     if n in [0, 1]:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)

# def searchChallenge(strParam):
#     used_brackets = [')', '(', '[', ']']
#     param_bracket = ''
#     for param in strParam:
#         if param in used_brackets:
#             param_bracket += param
   
#     brac = param_bracket.count('[')
#     brace = param_bracket.count(')')
#     total = 0
#     print(brac, brace)
#     if brac and brace:
#         total+=brac-1+brace-1
#         return f'1 {total}'
#     else:
#         return 0


# print(searchChallenge('[wir[rw]rw()'))
    


params = {"d": "200x300"}
print(params.get("d").split("x"))

uri = "/images/products/2021/11/2018447.jpg"

ur = uri.split("/")
print(ur)
resulution = params['d']
ur.insert(-1, resulution)

reworked_uri = "/".join(ur)
print(reworked_uri)