from bs4 import BeautifulSoup
import os
import requests
import csv

csvAcc=open('Accepted.csv','w')
csvWrg=open('Accepted.csv','w')
csv_writer=csv.writer(csvAcc)
csv_writer.writerow(['ProblemName','ProblemLink'])

username=input("What is your username:???")
mainurl=f'https://codeforces.com/submissions/{username}'
url=requests.get(mainurl).text
soup = BeautifulSoup(url,'lxml')
pagelist=soup.find_all('span',class_='page-index')
totalpages= int(pagelist[len(pagelist)-1]['pageindex'])

# print(totalpages)

table= soup.find_all('table',class_='status-frame-datatable')
for pagenum in range(1,totalpages+1):
    urlhere = mainurl+"/page/"+str(pagenum)
    souphere= BeautifulSoup(urlhere,'lxml')
    rows= table.find_all('tr',class_="highlighted-row")
    for row in rows:
        cols=row.find_all('td')
        verdict_col=cols[5]
        verdict=verdict_col.find('span',class_="submissionVerdictWrapper")['submissionverdict']
        if(verdict=="OK"):
            continue
        else:
            continue
 

