#!/bin/python3

import math
import os
import random
import re
import sys

def matchingStrings(stringList, queries):
    # Count the occurrences of each string in stringList
    count_dict = {}
    for string in stringList:
        count_dict[string] = count_dict.get(string, 0) + 1

    # Prepare the result based on the queries
    results = []
    for query in queries:
        results.append(count_dict.get(query, 0))

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
