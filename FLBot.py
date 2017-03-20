from tkinter import *
from selenium import webdriver
import time

def URLGen(model, sku):
	URL = "http://www.footlocker.com/product/model:" + str(model) +"/sku:" + str(sku)
	return URL

def URLFind(product, colorway):
	browser = webdriver.Chrome() 
	browser.get("http://www.footlocker.com/release-dates/")

	content = browser.find_elements_by_css_selector('div.day')
	
	print(len(content))
	for i in range(0, len(content), 1):

		if content[i].find_element_by_class_name('colorway').text == colorway:
			mod = content[i].get_attribute("data-modelnumber")
			sku = content[i].get_attribute("data-skunumber")
			rlu = URLGen(mod, sku)
			print(rlu)
			return rlu

def run_bot(event):
	model = mod.get()
	size = sz.get()
	color = col.get()
	link = URLFind(model, color)
	site = webdriver.Chrome()
	site.get(link)
	site.find_element_by_id('pdp_size_select_mask').click()
	sizeList = site.find_element_by_id('size_selection_list')
	time.sleep(1)
	sizeList.find_element_by_xpath('//*[@title="Size ' + size + '"]').click()
	site.find_element_by_id('pdp_addtocart_button').click()
	time.sleep(1)
	site.get('http://www.footlocker.com/shoppingcart')

root = Tk()
root.title("Sneaker Bot")
modelLabel = Label(root, text="Model")
modelLabel.grid(row=0, column=0)
mod = Entry(root)
mod.grid(row=1, column=0, padx=6)
colorLabel = Label(root, text="Color")
colorLabel.grid(row=2, column=0)
col = Entry(root)
col.grid(row=3, column=0)
sizeLabel = Label(root, text="Size (ex: 08.0)")
sizeLabel.grid(row=4, column=0)
sz = Entry(root)
sz.grid(row=5, column=0)
go = Button(root, text="Go")
go.grid(row=6, column=0)
go.bind("<Button-1>", run_bot)
root.mainloop()
