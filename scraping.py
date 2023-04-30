import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector

driver = uc.Chrome()
domain = 'https://www.legifrance.gouv.fr'
start_url = f'{domain}/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchType=ALL&nature=ORDONNANCE&nature=DECRET&nature=ARRETE&etatArticle=VIGUEUR&etatArticle=ABROGE_DIFF&etatTexte=VIGUEUR&etatTexte=ABROGE_DIFF&typeRecherche=date&dateVersion=18%2F04%2F2023&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=1&tab_selection=lawarticledecree#lois'

def get_page(url, by_method, by_selector, timeout=10):
    driver.get(url)
    wait = WebDriverWait(driver, timeout)
    elem = wait.until(EC.presence_of_element_located((by_method, by_selector)))
    return Selector(text=driver.page_source)

next_page = 1
while(next_page):
    response = get_page(start_url, By.CLASS_NAME, "result-item")
    urls = response.css('.title-result-item a::attr("href")').getall()
    for url in urls:
        response = get_page(f'{domain}{url}', By.CLASS_NAME, "page-content")
        item = extract_item(response)
        process_item(item)
        break
    break

def extract_item(response):
    return {}

def process_item(item):
    pass