import undetected_chromedriver as uc
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://nowsecure.nl')
html = driver.page_source
soup = bs(html, 'html.parser')
with open("./output.html", "w") as file:
  file.write(str(soup))
print("teste")
driver.save_screenshot('./nowsecure.png')
