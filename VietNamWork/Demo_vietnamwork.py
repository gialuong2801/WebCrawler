import requests
from bs4 import BeautifulSoup
import array as arr

page = requests.get("https://www.vietnamworks.com/marketing-team-leader-thu-nhap-tu-15-20-trieu-1321288-jv/?source=searchResults&searchType=2&placement=1321289&sortBy=date")

soup = BeautifulSoup(page.content,"html.parser")

payload = {
	'userName': 'luongdg.bi9159@st.usth.edu.vn',
	'passWord': 'Conanpro123'
}

job_information = []
requests.post('https://www.vietnamworks.com/marketing-team-leader-thu-nhap-tu-15-20-trieu-1321288-jv/?source=searchResults&searchType=2&placement=1321289&sortBy=date', payload)

name_job = soup.find("h1",{"class":"job-title"}).text
name_company = soup.find("div",{"class","company-name"}).text.replace("\n","")
name_location = soup.find("span",{"class":"company-location"}).text.replace("\n","").strip()
salary = soup.find("span",{"class":"salary"}).text.replace("\n","").strip()
expiry = soup.find("span",{"class":"expriry"})
job_information = [x.get_text() for x in soup.find_all("span", attrs={"class":"content"})]


print(name_job)
print(name_company)
print(name_location)
print(salary)
print(expiry)
print(job_information)
