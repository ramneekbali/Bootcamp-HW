import pandas as pd
import requests
from bs4 import BeautifulSoup
from splinter import Browser

# Get Headlines
def get_mars_headline():
    url = "https://mars.nasa.gov/api/v1/news_items/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    resp = requests.get(url).json()
    first_item = resp.get('items')[0]
    return {"item_title": first_item.get('title'), 
            "item_desc": first_item.get('description')
           }

# get_mars_headline()


# Get featured Image


def get_featured_image():
    executable_path = {'executable_path': '/Users/p2778494/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url_pict = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_pict)
    html = browser.html
    nasa_soup = BeautifulSoup(html, 'html.parser')
    picture = nasa_soup.find("div",{"class":"carousel_items"}).find("article")["style"]
    search_background_pict =picture.split("'")[1]
    featured_pict_url = f'https://www.jpl.nasa.gov{search_background_pict}'
    return{"image":featured_pict_url}

# get_featured_image()



# Get the latest weather

def get_mars_weather():
    executable_path = {'executable_path': '/Users/p2778494/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url_weath = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_weath)
    html_weath = browser.html
    mars_weath = BeautifulSoup(html_weath, 'html.parser')
    weather_tweets = mars_weath.find_all("p",{"class":"TweetTextSize"})[0].text
    return {"weather": weather_tweets}

# get_mars_weather()

    


# Get facts table

def get_mars_facts_table():
    mars_fact_url = 'http://space-facts.com/mars/'
    mars_fact__table =pd.read_html(mars_fact_url)
    table=mars_fact__table[0]
    table.columns = ["Parameter", "Values"]
    formatted =  table.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    return {"html_table_facts": formatted}



    #get_mars_facts_table()


# get images
def mars_hemi_img():
    executable_path = {'executable_path': '/Users/p2778494/Downloads/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    mars = BeautifulSoup(html, 'html.parser')
    base_url ='https://astrogeology.usgs.gov'
    hemisphere_image_urls = []
    urls = mars.find_all("div", class_="item")
    for x in urls:
        img_dic = {}
        header = x.find("h3").text
        next_url = x.find("div", class_="description").a["href"]
        full_url = base_url + next_url
        browser.visit(full_url)
        pic_html = browser.html
        pic_soup = BeautifulSoup(pic_html, 'html.parser')
        url_p = pic_soup.find("img", class_="wide-image")["src"]
        img_dic["title"] = header
        img_dic["img_url"] = base_url + url_p
#         print(img_dic["img_url"])
        hemisphere_image_urls.append(img_dic)
        
    return {"images":hemisphere_image_urls}

# get_mars_facts_table()

def scrape_master():
    print('scraping stuff')
    headline_dict = get_mars_headline()
    Featured_img_dict = get_featured_image()
    weather_dict = get_mars_weather()
    facts_table_dict= get_mars_facts_table()
    mars_img_dict = mars_hemi_img()
    merged_dict = {**headline_dict, **Featured_img_dict, **weather_dict, **facts_table_dict, **mars_img_dict}
    print('done merging')
    # merged dict will be the new data in mongodb
    return merged_dict

