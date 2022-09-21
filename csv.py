import csv
f = open("test.csv", "w+")
writer = f.writer()
writer.writerow(['id', 'name', 'email'])
writer.writerow([100, 'Ronald', 'ronald@comp.com'])