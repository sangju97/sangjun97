
data = input('1회차/2회차/3회차/4회차/5회차/6회차/7회차/8회차/9회차/10회차/11회차/12회차/13회차/14회차/15회차 점수를 입력해주세요.')

mid=int(input('중간고사 성적은?'))
fin=int(input('기말고사 성적은?'))


print(data.split())
a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 ,a14, a15 = map(int,data.split())



sum_s=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15 #합계 
avg = sum_s/15     #평균=합계/15

avv = avg * 0.4    #비중 40%
bb = mid * 0.3     #비중 30%
cc = fin * 0.3     #비중 30%

score = avv + bb + cc
if 100 >= score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
elif score < 60:
    grade = "F"





print(' %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | %3d | 평균값  %6.2f | 비중  %6.2f |'
      %(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,sum_s, avg,avv))


print('과제 평균(40%)' ,avv, '중간 평균(30%)' , bb, '중간 평균(30%)' , cc,  '총합 :',avv+bb+cc)

print("등급은" + grade + "입니다.")







