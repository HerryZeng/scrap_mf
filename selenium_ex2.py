from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"提效工具 ▾").click()
driver.find_element_by_link_text(u"Git 版本管理").click()
driver.find_element_by_link_text(u"大家说").click()

html = driver.page_source

driver.get_screenshot_as_file("image/screenshot2.png")
driver.close()
print(html[:200])