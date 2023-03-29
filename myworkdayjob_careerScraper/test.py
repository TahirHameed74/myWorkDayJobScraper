from bs4 import BeautifulSoup

html = '<div class="priceText_f71sibe"><span class="size14_f7opyze medium_f1wf24vo priceTextSize_frw9zm9" data-automation-id="price-text">1.65</span></div>'

soup = BeautifulSoup(html, "html.parser")

price_texts = soup.findAll("div",{"class":"priceText_f71sibe"})
price_text = price_texts[0]
a = price_text.span["data-automation-id"]


print(a)
print(price_text.span.text)
print(price_text.span.string)
print(price_text.span.getText())
print(price_text.span.get_text())