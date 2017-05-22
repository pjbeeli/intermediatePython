import sys
import bz2 # compression tool

opener = bz2.open

def min():
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(" ".join(sys.arv[2:]))
    f.close()



if __name__ == '__main__':
    main()
    exit(0)