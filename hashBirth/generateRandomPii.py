# generate a random list of names and cities
from random import *
import sys

outFname = sys.argv[1]
firsts = open("first.txt").read().splitlines()
lasts = open("family.txt").read().splitlines()
cities = open("cities.txt").read().splitlines()
sexes = ["M", "F"]

ofh = open(outFname, "w")
ofh.write("ID,FIRSTNAME,MIDDLENAME,LASTNAME,MOB,DOB,YOB,COB,SEX,SUBJECTHASMIDDLENAME,USEEXISTINGGUID\n")
for i in range(1, 100001):
    row = [str(i), choice(firsts), "", choice(lasts), randrange(1,12), randrange(1,30), randrange(1930,2010), choice(cities), choice(sexes), "N", "N"]
    row = [str(x).upper() for x in row]
    ofh.write(",".join(row))
    ofh.write("\n")
print "wrote", ofh.name
