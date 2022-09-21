import csv
f = open("test.csv", "w+")
writer = csv.writer(f)
writer.writerow(['id', 'name', 'email'])
writer.writerow([100, 'Ronald', 'ronald@comp.com'])