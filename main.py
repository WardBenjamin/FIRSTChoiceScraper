from bs4 import BeautifulSoup
import urllib.request


class Product:
    def __init__(self, name, sku, url, price, max_quantity):
        self.name = name
        self.sku = sku
        self.price = price
        self.max_quantity = max_quantity
        self.url = url

    def __str__(self):
        return "Product <%s>, %s" % (sku, name)

    def csv_format(self):
        return "%s, %s, %s, %s, %s,\n" % (self.sku, self.name, self.url, self.price, self.max_quantity)


if __name__ == '__main__':

    # We can either read directly from the remote FIRST Choice website, or use the local copy. If you want to read from
    # the remote, uncomment that line and comment the local line.

    # Website method
    # r = urllib.request.urlopen('https://firstchoicebyandymark.com/everything').read()

    # Local copy method
    r = open('firstchoicebyandymark_everything.html')

    soup = BeautifulSoup(r, 'html.parser')

    products = {}

    for product_item in soup.find_all('div', {'class': 'product-item'}):

        # Get title elements (url, name, sku)
        title_div = product_item.find('h2', {'class': 'product-title'})

        url = 'https://firstchoicebyandymark.com' + (title_div.find('a').get('href'))

        # Text contains both name and SKU, so separate them out
        text = title_div.find('a').getText()
        name = text[:-11]  # Strip " (fcxx-xxx)"
        sku = text[-10:][:-1][1:]  # Get "(fcxx-xxx)", then strip leading and following parenthesis

        # Get price elements (price, max quantity if applicable)
        price_div = product_item.find('div', {'class': 'prices'})

        price = price_div.find('span', {'class': 'actual-price'}).getText()[:-14]  # Strip " FIRST Credits"

        # If the item has a maximum quantity, get it. Otherwise will contain None.
        max_qty = price_div.find('span', {'class': 'maxqty'})
        if max_qty:
            max_qty = max_qty.getText()[18:]  # Strip "Max Qty Per Team: "

        products[sku] = Product(name, sku, url, price, max_qty)

    with open('firstchoice.csv', 'w') as file:
        file.write('SKU, Name, URL, Price (FIRST Credits), Max Qty Per Team,\n')
        for product in products.values():
            file.write(product.csv_format())


