'''import random
n=random.randint(1, 100)
g=int(input('عدد را حدس بزنید:'))
if g>n:
    print('عدد تولید شده کوچک‌تر است')
elif g<n:
    print('عدد تولید شده بزرگ‌تر است')
else:
    print('تبریک! شما برنده شدید')'''


'''import random
while True:
    print('1. سنگ')
    print('2. کاغذ')
    print('3. قیچی')
    u=input('انتخاب کنید:')
    if u=='exit':
        break
    if u not in ['1','2','3']:
        print('ورودی نامعتبر است')
        continue
    c= random.choice(['1','2','3'])
    print('انتخاب کامپیوتر:', c)
    if u==c:
        print('مساوی شدید')
    elif (u=='1' and c=='3') or \
         (u=='2' and c=='1') or \
         (u=='3' and c=='2'):
        print("شما برنده شدید")
    else:
        print("کامپیوتر برنده شد")'''
        
        
'''p=input('رمز عبور را وارد کنید:')
if len(p)>=8 and \
   sum(c.isalpha() for c in p)>=4 and \
   any(c.isupper() for c in p) and \
   any(c.islower() for c in p) and \
   any(c.isdigit() for c in p) and \
   any(not c.isalnum() for c in p):
    print('معتبر')
else:
    print('نامعتبر')'''
    
    
'''t=0
while True:
    n=int(input('یک عدد وارد کنید:'))
    if n==0:
        break
    t+=n
print('مجموع اعداد:',t)'''


'''for i in range(1,6):
    print('*'*i)'''