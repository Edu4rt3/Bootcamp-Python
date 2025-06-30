from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

def get_price(element):
    try:
        price = element.find_element(By.CLASS_NAME, "price").text
        return int(price.replace(",", ""))
    except:
        return float('inf')  # Não tem preço visível

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Espera o carregamento inicial
sleep(3)

# Seleciona idioma
try:
    lang_btn = driver.find_element(By.ID, "langSelect-EN")
    lang_btn.click()
    sleep(3)
except NoSuchElementException:
    pass

# Espera o jogo carregar
sleep(2)

# Tempo de execução
wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

# Loop principal
while True:
    try:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
    except Exception as e:
        print(f"Erro ao clicar no cookie: {e}")

    if time() > timeout:
        try:
            # Total de cookies disponíveis
            cookies_element = driver.find_element(By.ID, "cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Buscar todos os produtos habilitados
            products = driver.find_elements(By.CSS_SELECTOR, "div.product.unlocked.enabled")

            best_product = None
            best_price = 0

            for product in products:
                price = get_price(product)
                if price <= cookie_count and price > best_price:
                    best_product = product
                    best_price = price

            if best_product:
                best_product.click()
                print(f"Comprou: {best_product.get_attribute('id')} por {best_price} cookies")

        except Exception as e:
            print(f"Erro ao tentar comprar: {e}")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, "cookies")
            print(f"Resultado final: {cookies_element.text}")
        except NoSuchElementException:
            print("Não foi possível obter cookies finais.")
        break

    sleep(0.01)
