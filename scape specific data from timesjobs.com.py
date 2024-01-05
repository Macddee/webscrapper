from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
def fa():
    pass

    '''
    code samples and examples from beautifulsoup documentation.
    '''

    #searching using a name in the actual text
    #soup.find_all(href=re.compile("elsie"), class_ = "something", id = "something")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]\

    #searching by name of a html element
    #name_soup.find_all(name="email")
    # []

    #finfing classes in partials
    #soup.find_all(class_=re.compile("itl"))
    # [<p class="title"><b>The Dormouse's story</b></p>]

    #finding if the file contains certain strings
    #soup.find_all(string=["Tillie", "Elsie", "Lacie"])
    # [u'Elsie', u'Lacie', u'Tillie']

        #Finding a tag that contains a certain string
    #soup.find_all("a", string="Elsie")
    # [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

    # forcing beautiful soup to stop searching after a certain limit
    #soup.find_all("a", limit=2)

    #Searching in the haerachy of tags
    #soup.find("head").find("title")
    # <title>The Dormouse's story</title>


                #strting from a certain string or tag and going back upwords
    #a_string = soup.find(string="Lacie")
    #a_string
    # u'Lacie'

    #a_string.find_parents("a")
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

    #a_string.find_parent("p")
    # <p class="story">Once upon a time there were three little sisters; and their names were
    #  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    #  and they lived at the bottom of a well.</p>

    #a_string.find_parents("p", class="title")
    # []

    #testing if an attribute exists
    #soup.select('a[href]')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # print("Input an unfamilia skill")
    # unfamiliar_skill = input(">>")
    
html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
date = soup.find_all(True, string=re.compile("Python"))
for da in date:
    print(da)
    print("")
current_jobs = []
for job in jobs:
    date_posted = job.find("span", class_ = "sim-posted").text.strip()
    
    if "few" in date_posted:
        skills = job.find("span", class_ = "srp-skills").text.strip().replace(" ", "")
        if unfamiliar_skill not in skills:
            company_name = job.find("h3", class_ = "joblist-comp-name").text.strip()
            link = job.header.h2.a["href"] # find(["something", "something"])
            
            print(f"{company_name}")
            print(f"{skills}")
            print(f"{date_posted}")
            print(f"{link}\n")

            one_job = {
                "Company": company_name,
                "Skills": skills,
                "Date Posted": date_posted,
                "Link": link,
            }

            current_jobs.append(one_job)


data_frame = pd.DataFrame(current_jobs)
data_frame.to_excel("current_jobs.xlsx")
            