import csv
f = open("test.csv", "w+")
B = csv.writer(f)
B.writerow(['id', 'name', 'email'])
B.writerow([100, 'Ronald', 'ronald@comp.com'])