# ACGI Private Hash Intersection demo

    # get US city information
    wget https://goo.gl/qVgiYp
    cut -d, qVgiYp -f2 > cities.txt

    # generate two files with random personal identifiable information in the format required by NIH now
    python generateRandomPii.py randomPii.csv
    python generateRandomPii.py randomPii2.csv

    # make hashes for them
    hashBirthInfo.py randomPii2.csv randomPiiHashed2.csv
    hashBirthInfo.py randomPii.csv randomPiiHashed.csv

    # create some overlap in these files so we have something to find
    tail -n10 randomPiiHashed.csv >> randomPiiHashed2.csv 
    cut -d, -f12 randomPiiHashed.csv | grep -v PIIHASH > hashes1.txt
    cut -d, -f12 randomPiiHashed2.csv | grep -v PIIHASH > hashes2.txt
    
    # install PSI-OT, follow instructions from here:
    https://github.com/encryptogroup/PSI

    # now compare the two files:

    # run this on one machine (server)
    demo.exe -r 0 -p 3 -f ../hashBirth/hashes1.txt -a 132.249.245.79
    # run this on the another machine (client)
    time ./demo.exe -r 1 -p 3 -f hashes2.txt -a 132.249.245.79

    # set intersection will get printed to stdout
