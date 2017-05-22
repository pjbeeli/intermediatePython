import sys
import gzip  # compression tool

opener = gzip.open


def min():
    f = gzip.open(sys.argv[1], mode='wt')
    f.write(" ".join(sys.arv[2:]))
    f.close()


if __name__ == '__main__':
    main()
    exit(0)