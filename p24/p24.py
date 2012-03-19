#ten factorial is ~3.6m
#nine factorial is 362880
#one million / nine factorial is ~2.75
#that means the first digit changes twice
#so the first digit must be 2
#1000000 - 2*9! = 274240
#274240/8! ~ 6.8
#that means the second number changed 6 times
#0, 1, 3, 4, 5, 6, 7
#274240 - 6*8! = 32320
#32320/7! ~ 6.4
#0, 1, 3, 4, 5, 6, 8
#32320 - 6 * 7! = 2080
#2080/6! ~ 2.9
#0, 1, 3
#2080 - 6! * 2 = 640
#640/5! ~ 5.3
#0, 1, 4, 5, 6, 9
#640 - 5*5! = 40
#40/4! ~ 1.7
#0, 1
#40 - 4! = 16
#16/3! ~ 2.6
#0, 4, 5
#16 - 2 * 3! = 4
#4/2! = 2
#0, 4, 6
#the fourth permutation of 046 is 460

#so the answer is 2783915460



