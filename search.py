import csv
from collections import Counter

things = []

start = input('Start with row: ')
start = start-1

finish = ''

try:
  finish = input('End after row: ')
except:
  finish = 100000000

with open('list.csv') as raw:
    reader = csv.reader(raw)
    for row in reader:
        item = row
        things.append(item);

sliced_things = things[start:finish]

flat_things = [item for sublist in sliced_things for item in sublist]

final = Counter(flat_things)

print " "

for key,value in final.items():
    print key + ": " + str(value)

print " "
