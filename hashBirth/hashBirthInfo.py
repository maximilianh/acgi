#!/usr/bin/env python2.7

import logging, sys, optparse
from collections import defaultdict
from os.path import join, basename, dirname, isfile
import hashlib

# ==== functions =====
    
def parseArgs():
    " setup logging, parse command line arguments and options. -h shows auto-generated help page "
    parser = optparse.OptionParser("""usage: %prog [options] filename - given a .csv file with certain columns about a person's birth certificate info, create a copy of the file adding salted SHA1 hashes of the info. 
    Should this add a fixed entry such that an overlap can always be found, to make sure the salt and protocols work across steward servers?
    
    columns are:
    ID, - Ignored.
    FIRSTNAME - first name
    MIDDLENAME - middle name
    LASTNAME - last/family name
    MOB - month of birth
    DOB - day of birth
    YOB - year of birth
    COB - city of birth, no province, country or state added
    SEX - M or F
    SUBJECTHASMIDDLENAME - YES or NO
    USEEXISTINGGUID - ignored
    
    Download template from: http://ndar.nih.gov/ndarpublicweb/Documents/guid_sample_template.csv
    """)

    parser.add_option("-d", "--debug", dest="debug", action="store_true", help="show debug messages")
    #parser.add_option("-f", "--file", dest="file", action="store", help="run on file") 
    #parser.add_option("", "--test", dest="test", action="store_true", help="do something") 
    (options, args) = parser.parse_args()

    if args==[]:
        parser.print_help()
        exit(1)

    if options.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    return args, options

def parseRows(infname):
    " return the rows of a csv file a tuple with 9 fields"
    # XX add more validations!! check date, month, YES/NO etc, 
    for line in open(infname):
        line = line.rstrip("\r\n")
        if line.startswith("ID,"):
            assert(line=="ID,FIRSTNAME,MIDDLENAME,LASTNAME,MOB,DOB,YOB,COB,SEX,SUBJECTHASMIDDLENAME,USEEXISTINGGUID")
            continue
        if line.startswith("#"):
            continue
        fields = line.rstrip("\n").split(",")
        assert(len(fields)==11)
        row = []
        row.append(fields[0])
        row.append(fields[1])
        row.append(fields[2])
        row.append(fields[3])
        row.append(str(int(fields[4])))
        row.append(str(int(fields[5])))
        row.append(str(int(fields[6])))
        row.append(fields[7])
        row.append(fields[8])
        row.append(fields[9])
        row.append(fields[10])
        assert(len(row)==11)
        yield row

# ----------- main --------------
def main():
    sha = hashlib.sha1()

    args, options = parseArgs()
    salt = "7YrGdpd4ycrAG4LmCTkb"

    inFname, outFname = args
    ofh = open(outFname, "w")
    ofh.write("ID,FIRSTNAME,MIDDLENAME,LASTNAME,MOB,DOB,YOB,COB,SEX,SUBJECTHASMIDDLENAME,USEEXISTINGGUID,PIIHASH\n")
    for row in parseRows(inFname):
        row = [x.upper() for x in row]
        inStr = ",".join(row[1:10])
        inStr += ","+salt
        piiHash =  hashlib.sha1(inStr).hexdigest()
        row.append(piiHash)
        ofh.write(",".join(row))
        ofh.write("\n")

main()
