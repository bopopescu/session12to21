import requests
from bs4 import BeautifulSoup # External Library for Parsing HTML Data

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

years = soup.find_all( "span",class_="secondaryInfo")

sal = []

for year in years:
    # print(tag.text)
    # print("------")

    data = year.text
    # c=int(data)
    sal.append(data)
print(sal)
print(type(sal[0]))
#
# for movie in movies:
#     print(movie)
#     print("*******")

rates= soup.find_all("td", class_="ratingColumn imdbRating")
rating=[]
for rate in rates:
    d=rate.text
    rating.append(d.strip())
print(type(rating[0]))
# for r in rating:
#     print(r)
#     print("___________________________________")


# print(sal)

import matplotlib.pyplot as plt
# plt.plot(movies,rating)
# plt.show()
# sal.sort()
saal=sal[0:10]
#
ra=rating[0:10]
# print(saal)
# print(ra)
plt.plot(sal,ra)
plt.show()

# dic=dict(zip(saal,ra))
#
# print(dic)
# for i, key in enumerate(dic):
#     plt.pie(key, dic[key])
# plt.show()
#
# plt.plot(saal,ra)
# plt.show()
