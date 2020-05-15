import sys
import re
from collections import OrderedDict
from difflib import get_close_matches
import csv
import statistics
filename=sys.argv[1]

def start_process():
    new_list=[]
    pattern=['AICIXE','AMBKP']
    dic=OrderedDict()
    while True:
        print("Welcome Agent! Which stock you need to process?:-")
        stock_name=input()
        print("Oops! Do you mean ",end=" ")
        var=get_close_matches(stock_name,pattern)
        print(var,end=" ")
        print("? y or n:-")
        answer=input()
        if answer=='y':
            break
    print("From which date you want to start")
    start_date=input()
    d1,m1,y1=start_date.split('-')
    print("Till which date you want to analyze")
    end_date=input()
    d2,m2,y2=end_date.split('-')
    with open(filename) as f:
        reader=csv.reader(f)
        for row in reader:
            if  row[0]  ==  var[0]:
                d,m,y=row[1].split('-')
                if d1 <= d <= d2 and m1 <= m <= m2 and y1 <= y <= y2:
                    new_list.append(float(row[2]))
                    dic[row[1]]=float(row[2])
        len_dic=len(dic)
    f.close()
    minvalue=float("inf")
    maxbenefit=0
    for k, val in dic.items():
        if minvalue > val:
            minvalue=val
            buy_date=k
        if maxbenefit < val - minvalue:
            maxbenefit=val-minvalue
            sell_date=k
    length_list=len(new_list)
    print("\"Here is your result :- \"")
    print("Mean :-",statistics.mean(new_list))
    if length_list > 1:
        print("Std :-",statistics.stdev(new_list))
    else:
        print("Variance requires at least two data points")
    print("Buy Date : " , buy_date)
    if length_list == 1:
        print("Sell Date :",buy_date)
    else:
        print("Sell Date : " ,sell_date)
    print("Profit : ",maxbenefit)

while True:
    start_process()
    print("Do you want to continue? (y or n):-")
    action=input()
    if action=='n':
        break;
