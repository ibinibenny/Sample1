import csv
csv_fn = 'out.csv'
out_csv = csv.writer(open(csv_fn, 'w'))
out_csv.writerow(["name","place","age"])
out_csv.writerows([("jes","pala",22),("john","pala",50)])
out_csv.writerows([("tahir","Petta",34),("tom","ekm",52)])

