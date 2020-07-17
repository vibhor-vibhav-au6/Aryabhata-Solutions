class Solution:
    def dayOfYear(self, date: str) -> int:
        arr = date.split('-')
        y=int(arr[0])
        m=int(arr[1])
        d=int(arr[2])
        
        if m == 1: return d
        
        # calender = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        calender = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        # A year is leap year if the following conditions are satisfied:
        # 1.Year is multiple of 400.
        #or
        # 2.Year is multiple of 4 and not multiple of 100.
        
        if ((y%4 == 0) and (y%100) != 0) or (y%400 == 0):
            calender[2] = 29
            
        for i in range(1,m):
            d = d + calender[i]

        return d