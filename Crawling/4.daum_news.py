import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def get_News(start_date, end_date):
    s_date = start_date.strftime('%Y%m%d')
    e_date = end_date.strftime('%Y%m%d')
    day = end_date - start_date
    result = []
    for i in range(day.days):
        date = start_date + datetime.timedelta(days=i)
        regDate = date.strftime('%Y%m%d')
        url = 'https://news.daum.net/newsbox'
        for j in range(1,6):
            page = j
            response = requests.get(url=url, params={'regDate' : regDate , 'page' : page})
            # print(response.text)
            bs = BeautifulSoup(response.text, 'html.parser')

            
            trs = bs.select('.list_arrange li')
            if len(trs) < 1:
                break
            # print(trs)
            for tr in trs:
                try:
                    # print(tr)
                    # 제목 
                    title = tr.select_one('strong a').text
                    # print(title)
                    # 링크 
                    link = tr.find('a').get('href')
                    # print(link)
                    # 언론사 
                    ancor = tr.select_one('span').text
                    # print(ancor)
                    
                    result.append([regDate, page, title, link, ancor])
                    print(result)
                except:
                    continue
    return result

end = datetime.datetime(2024, 1, 2)
start =  datetime.datetime(2024, 1, 1)
# print((end - start).days)
news = get_News(start, end)

column = ['등록일', '페이지', '제목', '주소', '언론사']
dataframe = pd.DataFrame(news, columns=column)
print(dataframe)
dataframe.to_excel('news.xlsx', sheet_name='다음 뉴스') 