import sys, getopt
import os
import codecs

from auvsi_suas.client.exceptions import InteropError
from auvsi_suas.client.client import AsyncClient
from auvsi_suas.client.client import Client
import argparse


def main(argv):
    url = str()
    username = str()
    password = str()
    timeout = 10
    max_concurrent = 128
    max_retries = 10

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-ur', dest='url', action='store', default=None, type=str)
    parser.add_argument('-un', dest='username', action='store', default=None, type=str)
    parser.add_argument('-pw', dest='password', action='store', default=None, type=str)
    parser.add_argument('-t', dest='timeout', action='store', default=10, type=int)
    parser.add_argument('-mc', dest='max_concurrent', action='store', default=128, type=int)
    parser.add_argument('-mr', dest='max_retries', action='store', default=10, type=int)
    args = parser.parse_args()

    # check for errors in commandline args
    if args.url is None:
        print("-ur <url> must be included")
        sys.exit()
    if args.username is None:
        print("-un <username> must be included")
    if args.password is None:
        print("-pw <password> must be included")
    if args.timeout < 0:
        print("-t <timeout> must be >= 0")
    if args.max_concurrent < 0:
        print("-t <max_concurrent> must be >= 0")
    if args.max_retries < 0:
        print("-t <max_retries> must be >= 0")

    # init client
    client = Client(args.url, args.username, args.password, args.timeout,
                    args.max_concurrent, args.max_retries)
    testStuff = client.get_mission(1)
    print(testStuff)

if __name__ == "__main__":
    main(sys.argv[1:])
