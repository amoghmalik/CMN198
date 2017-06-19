import sqlite3
import csv

#onn = sqlite3.connect(":memory:")
conn = sqlite3.connect('dataTest.db')

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS unicom()""")

csvFile = "twitterREsult.csv"
csvFile.encode('utf-8')

with open(csvFile) as f:
	reader = csv.reader(f)
	for field in reader:
		cu.execute("INSERT INTO unicom VALUES (?,?,?,?);", field)

conn.commit()
conn.close()