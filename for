#반복문(for)

#5번 python을 출력

for x in [1,2,3,4,5]:
    print('python',x)

for x in ['a','b','c']:
    print(x)

for x in ('python','c','java'):
    print(x,'사용 가능')

#구구단 출력
dan=int(input('단수는?'))
for x in range(1,20):
    print(dan,'*',x,'=',dan*x)
