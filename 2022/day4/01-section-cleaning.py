from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

areas = [x.split(',') for x in data]

count_overlaps = 0
for area in areas:
   x1, y1 = area[0].split('-')
   x2, y2 = area[1].split('-')

   x1 = int(x1)
   y1 = int(y1)
   x2 = int(x2)
   y2 = int(y2)

   if x1 == x2 and y2 == y1:
       count_overlaps += 1
       continue

   firstIsLonger = True

   if abs(y2 - x2) > (y1 - x1):
       firstIsLonger = False

   if firstIsLonger:
       if x1 <= x2 and y1 >= y2:
          count_overlaps += 1
   else:
       if x2 <= x1 and y2 >= y1:
          count_overlaps += 1

     
print(count_overlaps)




