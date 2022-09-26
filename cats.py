from playwright.sync_api import sync_playwright
from math import ceil

def get_cats():
    # Chamando o Playwright.
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

    # Como o site não mostra quantas páginas tem para fazer o looping através dela.
    # Eu fiz esse cálculo para descobrir quantas páginas têm automaticamente para facilitar a manutenção.
        page.goto('https://www.amigurumi.com/Cats/1/')
        page_number = page.title().replace('Cats Amigurumi Patterns', '')
        pages = ceil(int(page_number) / 12)

    # Criando as listas para armazenar os links dos padrões e das imagens.
        links_list = []
        images_list = []

    # Iterando sobre as páginas e fazendo um looping sobre a classe de padrões ".item".
        for ind in range(1, pages + 1):
            page.goto('https://www.amigurumi.com/Cats/' + str(ind))
            cats = page.query_selector_all('.item')

    # Iterando sobre cada lista de ".item" para pegar os atributos onde se encontram os links.
            for i in cats:
                handle = i.query_selector('a')
                img = i.query_selector('a > img')
                links = handle.get_attribute('href')
                images = img.get_attribute('src')

    # Adicionando cada um dos atributos às listas criadas
                links_list.append(links)
                images_list.append(images)

    # Usando o comando dict + zip para juntar as listas e transforma-lás em um dicionário onde a chave é o padrão e o valor a imagem.
        data = dict(zip(links_list, images_list))
    return data