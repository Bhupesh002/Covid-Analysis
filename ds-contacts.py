

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries):
    # Write your code here
    a=[]
    res=[]
    for i in queries:
        if('add' in i):
            str=i.split()
            a.append(str[1])
        if('find' in i):
            c=0
            r=i.split()
            for j in a:
                if(r[2] in j):
                    c+=1 
                res.append(c)    
    return res        
if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w') """

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

   """  fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close() """
