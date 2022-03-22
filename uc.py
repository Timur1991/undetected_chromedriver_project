import undetected_chromedriver
import time
from bs4 import BeautifulSoup
# pip install undetected-chromedriver
# pip install bs4

"""
Обход cloudflare защиты, с помощью undetected_chromedriver
Живой пример сбора данных с обходом защиты cloudflare
По всем возникшим вопросам, можете писать в группу https://vk.com/happython
Ссылка на статью: https://vk.com/@happython-obhod-zaschity-cloudflare
Отзывы, предложения, советы приветствуются.
"""


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find('div', class_='jss170').find_all('div', class_='jss174')
    for block in blocks:
        trader = block.find('div', class_='jss179').text
        rate = block.find('div', class_='jss182 jss180').text.split('₽/BTC')[-1]
        limits = block.find('div', class_='jss183 jss180').get_text(strip=True).split(',')[-1]
        print(f'Продавец: {trader} \nКурс ₽/BTC: {rate} \nЛимиты, ₽: {limits}\n')


def main(url):
    # В browser_executable_path указываем путь к exe файлу браузера Хром
    driver = undetected_chromedriver.Chrome(browser_executable_path=f'C:/Program Files/Google/Chrome/Application/chrome')
    try:
        driver.get(url)
        time.sleep(15)
        # запуск сбора инфы
        get_content(driver.page_source)
        time.sleep(2)
        driver.close()
        driver.quit()
    except Exception as ex:
        print(f'Ошибка: {ex}')
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main('https://bitzlato.com/ru/p2p/')
