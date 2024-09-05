import time

def epicgames_colect(page):
    page.goto('https://store.epicgames.com/pt-BR/') 
    time.sleep(5)
    page.locator("div[class='css-cdosd6']").scroll_into_view_if_needed()
    time.sleep(5)
    page.locator("div[class='css-cdosd6']>section[class='css-2u323']").screenshot(path='jogos.png')
    time.sleep(5)
    jogos = page.query_selector_all("div[class='css-cdosd6']>section[class='css-2u323']>div[class='css-1myhtyb']>div[class='css-17st2kc']>div>div>div>a[class='css-g3jcms']")
    lista = []
    for jogo in jogos:
        jogo = jogo.get_attribute('href')
        lista.append(f'https://store.epicgames.com{jogo}')
    