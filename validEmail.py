import xml.etree.ElementTree as elemTree
from validate_email import validate_email
import re
import argparse
import arrow

def makeargpaser():
    parser = argparse.ArgumentParser(description='Check the valid credentials')
    parser.add_argument('-t', '--target path', dest='path',
                        help='target file path', required=True, type=str)
    parser.add_argument('-l', '--limit', dest='limit',
                        help='count limit', required=True, type=int)
    parser.add_argument('-o', '--target name', dest='oname',
                        help='target name', required=True, type=str)

    return parser

def validID(ID):
    is_valid = validate_email(ID)

    return is_valid

def main(options):
    target = options.path
    limit = options.limit
    output = options.oname

    file = open(target, "r")

    raw_index = 1
    file_index = 1

    dataList = file.readlines()

    todayDate = arrow.now().format('YYYY-MM-DD_')

    for data in dataList:
        ID = data.split(",")[0]
        check = validID(ID)
        if check == True:
            result = todayDate + output + "_" + str(file_index) + ".csv"

            if raw_index < limit + 1:
                file_ = open(result, "a")

                raw_index = raw_index + 1
                file_.write(data)
                continue

            if raw_index >= limit + 1:
                file_index = file_index + 1
                raw_index = 1
                continue

        if check != True:
            continue

if __name__ == "__main__":
    p = makeargpaser()
    opts = p.parse_args()
    main(opts)
