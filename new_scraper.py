#%%
# Fontes:
# https://github.com/Asier-Garcia/api-idealista-python/blob/main/main.py --chave
# client_id = 'b9lhgfyr9fkvojhpsl89p3bctizo2fk9'
# client_secret = '8ud8lnorl5K0'
#https://github.com/ADS-UB/rentCoach/blob/4a292373f871e3981868fb09c5db4bee3329c466/update_rentdata.py#L16
#apikey= urllib.parse.quote_plus('kn5fkovg91u9cuzo68pdiiwylgw878o1')
#secret= urllib.parse.quote_plus('AK8NlpBSDmoV')
#https://github.com/JoelDela/Master-Data-Science/blob/48d352661ceffbcf5d64dae5a1e5357e98cf3e40/7.%20Data%20engineering/Extra/Master%201/APIs/authidealista.R#L30
#consumer_key <- "rrry3jb98a7wjs5xbcwsk3u7z2rb9q77"
#consumer_secret <- "OM5tXahuf36x"
#https://github.com/xlasj05/Backoffice/blob/3ad0e293355e40d275dfaecde4df66cc1ed40562/Table21.py#L18
#apikey = '82bzidhyikkdonhpcdr6eoel1beljbgx'  # Replace with your actual API key
#secret = 'IeO2OmRLxf9Z' 
#https://github.com/falba3/harmonia/blob/6db29d3d2df07b9becc6760ac4c122343c9b39df/old/3.py#L11
#apikey = '2zky9zdsmvowg05bx61lsmyvxthkewum'
#secret = 'HtvQmb7FUAzj'
# https://github.com/Fred-Costa/ScraperImobiliario
# https://github.com/Zeimoto
# https://github.com/marnovo/pydealista/blob/master/api-docs/property-search-api-v3_5.pdf -- documentação da API
#%%

#%%
import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    "--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
#driver = webdriver.Chrome(options = chrome_options)


headers_imoveis = {
    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "acccept-encoding": "gzip, deflate, br",
    "accept-language": 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
    "cache-control": "max-age=0",
    "dnt": "1",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest":"document",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "cookie": """_cb=i0oszBCGTuEDQdmxN; _chartbeat2=.1701789608305.1732570084517.0000000000000001.CJvMQFCk81c1mMCgNwSpbPr_tS6.1; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1qbHlmYWgyfG0zeGpodDUyIn0%3D; _pcid=%7B%22browserId%22%3A%22m3xjht4zujoryusy%22%2C%22_t%22%3A%22mjlyfamw%7Cm3xjhtaw%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbAFaoAngDNC-AB4AffgGYpggBZEpIAL5A; _tt_enable_cookie=1; _ttp=p4SMKtf5lmh5zHMawG9zCabu44l.tt.1; _fbp=fb.1.1732570084953.667120816833566162; userUUID=64e41627-6742-408f-bafc-17fddc32ebc4; _hjSessionUser_1676782=eyJpZCI6ImUzZDRjNzExLTA2ZTYtNTczZC1hZDM4LTdmMjc0YzgyZjI1MCIsImNyZWF0ZWQiOjE3MzMxNjI5NTA5MzksImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; _last_search=officialZone; _gcl_au=1.1.796023751.1733162970; askToSaveAlertPopUp=true; pbw=%24b%3d16999%3b%24o%3d11100%3b%24sw%3d1920%3b%24sh%3d1200; TestIfCookieP=ok; pid=7491099310567318900; utag_main__prevCompleteClickName=; galleryHasBeenBoosted=true; lcsrd=2025-01-09T13:30:05.7961482Z; SESSION=833e67124e689ac0~4d1459a0-c434-4cd3-a197-be5f76c1b31b; contact4d1459a0-c434-4cd3-a197-be5f76c1b31b="{'maxNumberContactsAllow':10}"; utag_main__sn=7; utag_main_ses_id=1736530611014%3Bexp-session; utag_main__ss=0%3Bexp-session; utag_main__prevTsUrl=https%3A%2F%2Fwww.idealista.pt%2Fcomprar-casas%2Fcampanha%2Fantas-estadio-do-dragao%2F%3Bexp-1736534215434; utag_main__prevTsReferrer=%3Bexp-1736534215434; utag_main__prevTsSource=Direct traffic%3Bexp-1736534215434; utag_main__prevTsCampaign=organicTrafficByTm%3Bexp-1736534215434; utag_main__prevTsProvider=%3Bexp-1736534215434; _clck=k187g7%7C2%7Cfsg%7C0%7C1790; _hjSession_1676782=eyJpZCI6IjE1ZjcwNWNiLWI3NjEtNDcwOC1iNDZkLWVhNjk0MTBkZjFkZiIsImMiOjE3MzY1MzA2MTYyNzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; send4d1459a0-c434-4cd3-a197-be5f76c1b31b="{}"; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222026-01-10T17%3A40%3A15.352Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22uGIMVxJjICuHIBwBMBtG%22%2C%22expiryDate%22%3A%222026-01-10T17%3A40%3A15.360Z%22%7D; cto_bundle=7cUkq191YlB4MzY0R1U5djVzZWp1d0prWUlSemFRVFJIYlJtYkUwWjRIZlVTRm9SUUhJSFlXMGhoZmZKU1lITFl4WFI1bTZBb3NmeDU2N2NuRnFSQzR6ZTFPb2tjTXJpSERYNlJpSzNxWmllcEkxanhxWUYyRjY0UlBLMGZCZ2pwbU5tOG5oRDFaS3N4OG4wRWhNYjZtYyUyQkc4ZGNqekRZVFNKMzRjelB3dDE1Q2FueHdtUUpqdzVBclNqZXY5YWdJSkRud3o5VU1TZTJpdTZXYSUyRkdmZW9LRUJ2cGVtRG5haVZKNnAxayUyRk42UzZkSjFubThkMSUyQkdyYU5QUUFzS0oxejdieEdKMXl6cmhEVFFKZlNwdDBhYVFudVk3SGZVdnVNRVFKVFdjNEV3Z3ZSRUh4eUJXcTFEcjhXd0lXY1pPR1kzOCUyRnM; smc="{}"; cookieSearch-1="/comprar-casas/campanha/antas-estadio-do-dragao/:1736532667214"; utag_main__pn=9%3Bexp-session; utag_main__se=26%3Bexp-session; utag_main__st=1736534469114%3Bexp-session; utag_main__prevCompletePageName=005-idealista/portal > portal > viewResults%3Bexp-1736536269373; utag_main__prevLevel2=005-idealista/portal%3Bexp-1736536269373; _uetsid=3a9e4670cdf611efa6c563cda4fabfab; _uetvid=85aad78078ee11eea6244bc7a063d4cb; _clsk=u8vhve%7C1736532670511%7C16%7C0%7Cn.clarity.ms%2Fcollect; datadome=V_OqyYshU_tj2zKaGTr3NCRRf1llObKBmfN0e0FiVMi9pNapSuB6cjbMZLqsV9U5mzRZDY2EgXnfTaFQcF0K8p0_ZZuCul5tjx7RcCRd~VTC5cYLeokpgtVTy1BpSoIs"""
    #"cookie": """_cb=i0oszBCGTuEDQdmxN; _chartbeat2=.1701789608305.1732570084517.0000000000000001.CJvMQFCk81c1mMCgNwSpbPr_tS6.1; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1qbHlmYWgyfG0zeGpodDUyIn0%3D; _pcid=%7B%22browserId%22%3A%22m3xjht4zujoryusy%22%2C%22_t%22%3A%22mjlyfamw%7Cm3xjhtaw%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbAFaoAngDNC-AB4AffgGYpggBZEpIAL5A; _tt_enable_cookie=1; _ttp=p4SMKtf5lmh5zHMawG9zCabu44l.tt.1; _fbp=fb.1.1732570084953.667120816833566162; userUUID=64e41627-6742-408f-bafc-17fddc32ebc4; _hjSessionUser_1676782=eyJpZCI6ImUzZDRjNzExLTA2ZTYtNTczZC1hZDM4LTdmMjc0YzgyZjI1MCIsImNyZWF0ZWQiOjE3MzMxNjI5NTA5MzksImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; _last_search=officialZone; _gcl_au=1.1.796023751.1733162970; askToSaveAlertPopUp=true; pbw=%24b%3d16999%3b%24o%3d11100%3b%24sw%3d1920%3b%24sh%3d1200; TestIfCookieP=ok; pid=7491099310567318900; utag_main__prevCompleteClickName=; galleryHasBeenBoosted=true; lcsrd=2025-01-09T13:30:05.7961482Z; SESSION=833e67124e689ac0~4d1459a0-c434-4cd3-a197-be5f76c1b31b; contact4d1459a0-c434-4cd3-a197-be5f76c1b31b="{'maxNumberContactsAllow':10}"; utag_main__sn=7; utag_main_ses_id=1736530611014%3Bexp-session; utag_main__ss=0%3Bexp-session; utag_main__prevTsUrl=https%3A%2F%2Fwww.idealista.pt%2Fcomprar-casas%2Fcampanha%2Fantas-estadio-do-dragao%2F%3Bexp-1736534215434; utag_main__prevTsReferrer=%3Bexp-1736534215434; utag_main__prevTsSource=Direct traffic%3Bexp-1736534215434; utag_main__prevTsCampaign=organicTrafficByTm%3Bexp-1736534215434; utag_main__prevTsProvider=%3Bexp-1736534215434; _clck=k187g7%7C2%7Cfsg%7C0%7C1790; _hjSession_1676782=eyJpZCI6IjE1ZjcwNWNiLWI3NjEtNDcwOC1iNDZkLWVhNjk0MTBkZjFkZiIsImMiOjE3MzY1MzA2MTYyNzYsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; send4d1459a0-c434-4cd3-a197-be5f76c1b31b="{}"; smc="{}"; cookieSearch-1="/comprar-casas/campanha/antas-estadio-do-dragao/:1736532667214"; utag_main__pn=10%3Bexp-session; utag_main__se=28%3Bexp-session; utag_main__st=1736534860597%3Bexp-session; utag_main__prevCompletePageName=005-idealista/portal > portal > viewAdDetail%3Bexp-1736536660615; utag_main__prevLevel2=005-idealista/portal%3Bexp-1736536660615; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222026-01-10T18%3A17%3A40.776Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22uGIMVxJjICuHIBwBMBtG%22%2C%22expiryDate%22%3A%222026-01-10T18%3A17%3A40.779Z%22%7D; _uetsid=3a9e4670cdf611efa6c563cda4fabfab; _uetvid=85aad78078ee11eea6244bc7a063d4cb; cto_bundle=a2TvaV91YlB4MzY0R1U5djVzZWp1d0prWUlUdjQ2R1BQdzdDUSUyRkEzRjY4NjRTdmxOa2Q1VEJRVkNXNEhHakRYVFdGVnJ5RzZxeDV3aFJ0V1BFS3JtTmclMkI4b1lYYThOZFp5NGFWQ3c4c2s3VWxEYnJnTGYlMkZYM0hxd3BoNUJESHpNd0VlQWpiaGhQUWVPaHRXU2RHYjVRTTB0bGVTZ25vSVhvY3dVRXh6ZUolMkJaNndLcU5ZQmZPRlNueXhnVEpDJTJCVHpEbmJSeCUyRk51a1RRSU02M0g1ZmRNeEElMkJNbVUlMkJSYUF4akR2ZHdiZUgySVZzdW9ZM3FkRXE1cVk5eUwxVGZPUXgxZSUyRmE4eWZhZzNJOTFNb3RxYWVTZk1mJTJGb2tWN3BEZWhaakJ5NGZpalpNYnJYVzhDMnVQWThST0JIdU5WazZZWDJOcHZo; datadome=6kMmBoqgnaDy8H2Q1PMx~oACZ1_DPrdIL_PMsYdrff4xTwjVscUuZ_fMX2JkW3Dw3a2sN8R1IEBWBFjZjjrBaGwapTniB4nbx2SXEOhcUgJwt26wE2yug_tnazX5Hj8B; _clsk=u8vhve%7C1736534159807%7C18%7C0%7Cn.clarity.ms%2Fcollect"""
}
# url = 'https://www.idealista.com/venta-viviendas/sevilla/los-remedios/asuncion-adolfo-suarez/'
# browser.get(url)
# browser.implicitly_wait(10)
# browser.find_element("xpath", "//*[@id='didomi-notice-agree-button']").click()
# html=browser.page_source
# soup = bs(html,'html.parser')
# soup
# listings = soup.find_all("a",{"class":"item-link"})
# for listing in listings:
#     print(listing.text)
#     print(listing.get('href'))

url_bairros = ["paranhos","bonfim","ramalde","campanha",
               "monte-dos-burgos-carvalhido",
               "aldoar-foz-do-douro-nevogilde",
               "lordelo-do-ouro-e-massarelos",
               "cedofeita-santo-ildefonso-se-miragaia-sao-nicolau-vitoria"]
import datetime
dia_semana = datetime.datetime.now().strftime('%A')
print(f'Dia da semana: {dia_semana}')
if dia_semana == 'Friday':
    bairros = ["paranhos"]
elif dia_semana == 'Saturday':
    bairros = ["bonfim","campanha"]
elif dia_semana == 'Sunday':
    bairros = ["ramalde"]
elif dia_semana == 'Monday':
    bairros = ["cedofeita-santo-ildefonso-se-miragaia-sao-nicolau-vitoria"] 
elif dia_semana == 'Tuesday':
    bairros = ["monte-dos-burgos-carvalhido"]
elif dia_semana == 'Wednesday':
    bairros = ["aldoar-foz-do-douro-nevogilde"]
elif dia_semana == 'Thursday':
    bairros = ["lordelo-do-ouro-e-massarelos"]
print(f'Bairros: {bairros}')
#%%

#%%
# browser = uc.Chrome()
# anuncios = []
# paginas =["https://www.idealista.pt/comprar-casas/porto/paranhos/pagina-1","https://www.idealista.pt/comprar-casas/porto/paranhos/pagina-2"]

# for i in range(59,62):
#     url = f"https://www.idealista.pt/comprar-casas/porto/paranhos/pagina-{i}"
#     browser.get(url)
#     if i == 1:
#         browser.implicitly_wait(10)
#         browser.find_element("xpath", "//*[@id='didomi-notice-agree-button']").click()
#     html=browser.page_source
#     soup = bs(html,'html.parser')
#     page_number = int(soup.find('main',{'class':"listing-items"}).find('div',{"class":"pagination"}).find("li",{"class":"selected"}).text)
#     print(f'Pagina {i}')
#     print(f'Pagina atual: {page_number}')
#     if page_number == (i):
#         print('Tudo certo, continuar')
#         listings = soup.find_all("a",{"class":"item-link"})
#         print(f'Total de anuncios: {len(listings)}')
#         for listing in listings:
#             print(listing.text)
#             print(listing.get('href'))
#             texto = listing.text
#             link = listing.get('href')
#             anuncios.append([texto,link,page_number])

#             # Random sleep timer between 2 and 5 seconds
#             sleep_time = random.uniform(2, 5)
#             print(f"Aguardando {sleep_time:.2f} segundos antes de continuar...")
#             time.sleep(sleep_time)
#     else:
#         print('Algo deu errado, parar')
#         break

#%%

#%%
browser = uc.Chrome(options = chrome_options)
#headless=True,use_subprocess=False
anuncios = []
for bairro in bairros:
    print(f'Analisando bairro: {bairro}')
    i = 1
    print(bairro)
    while True:  # Run indefinitely until the final page is reached
        url = f"https://www.idealista.pt/comprar-casas/porto/{bairro}/pagina-{i}"
        print(url)
        browser.get(url)
        
        if i == 1:
            browser.implicitly_wait(10)
            browser.find_element("xpath", "//*[@id='didomi-notice-agree-button']").click()
        
        html = browser.page_source
        soup = bs(html, 'html.parser')
        
        # Extract current page number
        page_number = int(soup.find('main', {'class': "listing-items"})
                        .find('div', {"class": "pagination"})
                        .find("li", {"class": "selected"}).text)
        
        print(f'Pagina {i}')
        print(f'Pagina atual: {page_number}')
        
        if page_number == i: 
            #print(f'Tudo certo, continuar')
            listings = soup.find_all("a", {"class": "item-link"})
            print(f'Total de anuncios: {len(listings)}')
            
            for listing in listings:
                texto = listing.text
                link = listing.get('href')
                anuncios.append([texto, link, page_number,bairro])
            
            # Random sleep timer between 2 and 5 seconds
            sleep_time = random.uniform(2, 10)
            print(f"Aguardando {sleep_time:.2f} segundos antes de continuar...")
            time.sleep(sleep_time)
            
            i += 1  # Go to the next page
        else:
            print(f'Algo deu errado no bairro {bairro}, parar')
            break
browser.quit()
#%%

#%%
# browser = uc.Chrome()
# i = 1
# anuncios = []
# while True:  # Run indefinitely until the final page is reached
#     url = f"https://www.idealista.pt/comprar-casas/porto/paranhos/pagina-{i}"
#     browser.get(url)
    
#     if i == 1:
#         browser.implicitly_wait(10)
#         browser.find_element("xpath", "//*[@id='didomi-notice-agree-button']").click()
    
#     html = browser.page_source
#     soup = bs(html, 'html.parser')
    
#     # Extract current page number
#     page_number = int(soup.find('main', {'class': "listing-items"})
#                       .find('div', {"class": "pagination"})
#                       .find("li", {"class": "selected"}).text)
    
#     print(f'Pagina {i}')
#     print(f'Pagina atual: {page_number}')
    
#     if page_number == i: 
#         print('Tudo certo, continuar')
#         listings = soup.find_all("a", {"class": "item-link"})
#         print(f'Total de anuncios: {len(listings)}')
        
#         for listing in listings:
#             texto = listing.text
#             link = listing.get('href')
#             anuncios.append([texto, link, page_number])
        
#         # Random sleep timer between 2 and 5 seconds
#         sleep_time = random.uniform(2, 10)
#         print(f"Aguardando {sleep_time:.2f} segundos antes de continuar...")
#         time.sleep(sleep_time)
        
#         i += 1  # Go to the next page
#     else:
#         print('Algo deu errado, parar')
#         break
# browser.quit()
#%%

#%%
df_anuncios = pd.DataFrame(anuncios,columns=["descricao","link","pagina"])
#%%

#%%
def get_infos_imovel(id_imovel,headers,scraping_source= 'live'):
    print("Imóvel: "+id_imovel)
    if scraping_source == 'live':
        url_imovel = f'https://www.idealista.pt/imovel/{id_imovel}/'
    elif scraping_source == 'cache':
        url_imovel = f'https://webcache.googleusercontent.com/search?q=cache:https%3A%2F%2Fwww%2Eidealista%2Ept%2Fimovel%2F{id_imovel}%2F'
    #print(url_imovel)
    
    try:
        r = requests.get(url_imovel,headers=headers,verify=False)
        soup = bs(r.text,"html.parser")
  
        titulo = soup.find("span",{"class":"main-info__title-main"}).text
        local = soup.find("span",{"class":"main-info__title-minor"}).text
        preco = soup.find("span",{"class":"txt-bold"}).text
        features = soup.find("section",{"id":"details"}).find("div",{"class":"details-property"})
        c1 = features.find("div",{"class":"details-property-feature-one"})
        c2 = features.find("div",{"class":"details-property-feature-two"})
        descricao = soup.find("div",{"class":"adCommentsLanguage"}).text
        #c3 = c2.find_all("div",{"class":"details-property_features"})
        localizacao= soup.find("div",{"id":"headerMap"})
        data_atualizacao = soup.find("p",{"class":"stats-text"})
        cert_text = c2.find("span", {"class": "icon-energy-c-16"})
        certificado = None
        #try:
        #    certificado = cert_text.get('title')
        #except Exception as e:
        #    certificado = None
        #    print(f"An error occurred: {e}")
        if cert_text is not None:
            certificado = cert_text.get('title')
        #certificado = c2.find("span",{"class":"icon-energy-c-16"}).get('title')

        data = {
            'id_imovel': [id_imovel] ,
            'Title': [titulo] if titulo else None,
            'Local': [local] if local else None,
            'Price (€)': [preco] if preco else None,
            'Certificado Energético': [certificado] if certificado else None,
            'Características': [", ".join([caract.text for caract in c1.find_all("li")])] if c1 else None,
            'Características 2': [", ".join([caract.text for caract in c2.find_all("li")])] if c2 else None,
            'Endereco': [", ".join([caract.text.replace('\n','') for caract in localizacao.find_all("li")])] if localizacao else None,
            'Descricao': [descricao] if descricao else None
        }
        df = pd.DataFrame(data)
    except Exception as e:
        sleep_time = random.uniform(15,60)
        time.sleep(sleep_time)
        print(f"An error occurred: {e}")
        return None
    
    return df

df_imoveis = []
for i,row in df_anuncios.iterrows():
    try:
        print(i)
        if i % 20 == 0:
            sleep_time = random.uniform(15,60)
            time.sleep(sleep_time)
        id_anuncio = row["link"].replace("/imovel/","").replace("/","")
        if id_anuncio.isnumeric():
            aux=get_infos_imovel(id_anuncio,headers_imoveis)
            if aux is not None:
                df_imoveis.append(aux)
                sleep_time = random.uniform(2, 10)
                time.sleep(sleep_time)
        else:
            print(f"Skipping non-numeric ID: {id_anuncio}")
            continue
    except Exception as e:
        print(f"An unexpected error occurred in the loop at index {i}: {e}")
        continue  # Continue to the next iteration even if an error occurs
#id_imovel= "33828101"

#%%

#%%
df = pd.concat(df_imoveis,ignore_index=True)
today = datetime.datetime.now().strftime("%Y%m%d")
filename = f'{os.getcwd()}/{today}_imoveis_{"_".join(bairros)}.csv'
df.to_csv(filename,encoding='utf-8-sig',index=False)
#%%
