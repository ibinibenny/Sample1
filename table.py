import csv

f=open("csvtst.csv","w")

cp=csv.writer(f)
cp.writerow(["name","place","age"])
cp.writerows([("jes","pala",22),("john","pala",50)])

f.close()

