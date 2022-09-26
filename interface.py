from tkinter import *
from playwright.sync_api import sync_playwright
from math import ceil

count = 0
def plus_upd():
    global count
    count += + 1
    page_count.configure(text='Pattern : ' + str(count))
def my_upd():
    global count
    page_count.configure(text = 'Pattern : ' + str(count))
def less_upd():
    global count
    if count == 0:
        count = 0
    else:
        count -= 1
    page_count.configure(text = 'Pattern : ' + str(count))

def get_cats():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.amigurumi.com/Cats/1/')
        page_number = page.title().replace('Cats Amigurumi Patterns', '')
        pages = ceil(int(page_number) / 12)
        links_list = []
        images_list = []
        for ind in range(1, pages + 1):
            page.goto('https://www.amigurumi.com/Cats/' + str(ind))
            cats = page.query_selector_all('.item')
            for i in cats:
                handle = i.query_selector('a')
                img = i.query_selector('a > img')
                links = handle.get_attribute('href')
                images = img.get_attribute('src')
                links_list.append(links)
                images_list.append(images)
        data = dict(zip(links_list, images_list))

    cat_response["text"] = list(data)[count]
    cat_img_response["text"] = list(data.values())[count]

def get_dogs():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.amigurumi.com/Dogs/1/')
        page_number = page.title().replace('Dogs Amigurumi Patterns', '')
        pages = ceil(int(page_number) / 12)
        links_list = []
        images_list = []
        for x in range(1, pages + 1):
            page.goto('https://www.amigurumi.com/Dogs/' + str(x))
            dogs = page.query_selector_all('.item')
            for i in dogs:
                handle = i.query_selector('a')
                img = i.query_selector('a > img')
                links = handle.get_attribute('href')
                images = img.get_attribute('src')
                links_list.append(links)
                images_list.append(images)
        data = dict(zip(links_list, images_list))

    dog_response["text"] = list(data)[count]
    dog_img_response["text"] = list(data.values())[count]


window = Tk()
window.title('Amigurumi Blog')
window.configure(bg = "grey")

paragraph = Label(window, text='Would you like to see Cats or Dogs Patterns?', font = 'Arial 20')
paragraph.grid(column=0, row = 0, padx=10, pady=15)


cat_button = Button(window, text='Cats', font = 'Arial 15', command = get_cats)
cat_button.grid(column=0, row =3, padx=40, pady=15)
cat_response = Label(window, text = "", font = 'Arial 10')
cat_response.configure(bg = 'grey')
cat_response.grid(column = 0, row = 4, padx=50, pady=10)
cat_img_response = Label(window, text = "", font = 'Arial 10')
cat_img_response.configure(bg = 'grey')
cat_img_response.grid(column = 0, row = 5, padx=50, pady=10)

page_count = Button(window, text='Pattern', font = 'Arial 15', command = my_upd)
page_count.grid(column = 1, row = 6, padx = 10, pady = 15)
less_count = Button(window, text='-', font = 'Arial 15', command = less_upd)
less_count.grid(column = 0, row = 6, padx = 10, pady = 15)
plus_count = Button(window, text='+', font = 'Arial 15', command = plus_upd)
plus_count.grid(column = 2, row = 6, padx = 10, pady = 15)

dog_button = Button(window, text='Dogs', font = 'Arial 15', command = get_dogs)
dog_button.grid(column = 0, row = 8, padx=40, pady=15)
dog_response = Label(window, text = "", font = 'Arial 10')
dog_response.configure(bg = 'grey')
dog_response.grid(column = 0, row = 9, padx=40, pady=10)
dog_img_response = Label(window, text = "", font = 'Arial 10')
dog_img_response.configure(bg = 'grey')
dog_img_response.grid(column = 0, row =10, padx=50, pady=10)

exit_button = Button(window, text="Exit", font = 'Arial 15', command=exit)
exit_button.grid(column = 2, row = 0 , padx = 10, pady = 10)

window.mainloop()