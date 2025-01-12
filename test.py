import undetected_chromedriver as uc
import chromedriver_autoinstaller
import requests 
from bs4 import BeautifulSoup as bs

chromedriver_autoinstaller.install()
driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://www.idealista.pt/comprar-casas/porto/ramalde/pagina-1')
html = driver.page_source
soup = bs(html, 'html.parser')
with open("./output.html", "w") as file:
  file.write(str(soup))
print("teste")
driver.save_screenshot('./nowsecure.png')
