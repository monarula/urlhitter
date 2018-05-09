# author : MohitNarula

from urllib.request import Request, urlopen
import time
from pprint import pprint

url2 = input("\nEnter URL = ")
hit_count = input("\nEnter the integer number of hits = ")

url_response_list = []
time_list = []

def hitter():
    count = 0
    while count < int(hit_count):
        start = time.time()
        req = Request(url2)
        response = urlopen(req)
        end = time.time()
        url_response_list.append(response.reason)
        total_time = end - start
        time_list.append(total_time)
        count +=1

    my_dict = list(zip(url_response_list, time_list))
    print("\nPrinting URL request response & "
          "Time Taken (in seconds) for that Request..\n")
    pprint(my_dict)
    print("\nTotal Time for {} HTTP requests = {} seconds".format(hit_count, sum(time_list)))
hitter()
