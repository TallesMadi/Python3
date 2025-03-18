from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r'C:\\Python3\\Python_Modulos\\aula198\drivers\\msedgedriver.exe'
options = EdgeOptions()
# Exemplo: abrir o navegador em modo headless
# options.add_argument("headless")

# Crie o serviço para o Edge Driver
service = EdgeService(executable_path=edge_driver_path)

# Inicia o navegador Edge
driver = webdriver.Edge(service=service, options=options)

# Acesse uma página
driver.get(r"https://www.google.com")

# Exibe o título da página
print(driver.title)

# elemento = driver.find_element(By.CLASS_NAME, "tagH2")
# if elemento is not None:
#     print('*',elemento.text, '*')

search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "q")
    )
)
search_input.send_keys('Banana')
search_input.send_keys(Keys.ENTER)

results = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, 'search')
    )
)
# links = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.TAG_NAME, 'a')
#     )
# )
# links[0].click()
# Encerra o navegador
input()
driver.quit()