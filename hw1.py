import calendar
import time


print('2021년 달력 출력')
print( calendar.calendar(2021) )

year = int(input('년도 입력 : '))
month = int(input('월 입력 : '))
day = int(input('일 입력 : '))

print()
print(calendar.month(year, month))

weekdays = ['월', '화', '수', '목', '금', '토', '일']
print( '%d년 %d월 %d일 %s요일' %(year, month, day, weekdays[calendar.weekday(year, month, day)]) )

curTime = time.time()
print()
print(' 현재 날짜와 시간 출력')
tm1 = time.localtime(curTime)
print( time.strftime('%m/%d/%Y %H:%M:%S', tm1) )

time.sleep(5)

after5Time = time.time()
print()
print(' 5초 후 ....')
tm2 = time.localtime(after5Time)
print('{:04d}년 {:d}월 {:d}일'.format(tm2.tm_year, tm2.tm_mon, tm2.tm_mday))
print('{:02d}시 {:d}분 {:02d}초'.format(tm2.tm_hour, tm2.tm_min, tm2.tm_sec))
