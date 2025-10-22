from bs4 import BeautifulSoup
import requests
import smtplib
import os

amazon_product_url = "https://www.amazon.co.uk/Jackson-Cole-Ancona-Waterproof-Backpack/dp/B0CN4PF88F?ref_=ast_sto_dp&th=1"
headers = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/126.0.0.0 Safari/537.36'
}
jack_cole_url = "https://jacksonandcole.com/products/ancona-30-premium-waterproof-rolltop-drybag-backpack"


sender = os.environ["SEND_EMAIL"]
recipient = os.environ["RECEIVE_EMAIL"]
password = os.environ["PASSWORD"]
gmail_smtp = "smtp.gmail.com"
port_num = 587

amazon_response = requests.get(url=amazon_product_url, headers=headers)
soup = BeautifulSoup(amazon_response.text, "lxml")

amazon_product_name = soup.find('span', id="productTitle").getText().strip()
amazon_price = soup.find('span', class_='a-offscreen').getText().split("£")[1]

jack_cole_response = requests.get(url=jack_cole_url, headers=headers)
soup = BeautifulSoup(jack_cole_response.text, "lxml")

jack_cole_product_name = soup.find('div', class_="product__title").find('h1').getText()



try:
    jack_cole_price = soup.find('span', class_='price-item price-item--sale price-item--last').getText().strip()
except FileNotFoundError:
    print(f"Jack & Cole {jack_cole_product_name} is not on sale.")
    pass
else:
    jack_cole_price = jack_cole_price.split()[0].strip("£")


amazon_message = (f"Subject:Price Alert!\n"
           f"The product: '{amazon_product_name}'\n\n"
           f"The price: £{amazon_price}!\n\n"
           f"The purchase link: {amazon_product_url}\n")
jack_cole_message = (f"Subject:Price Alert!\n"
           f"\nThe product: '{jack_cole_product_name}'\n\n"
           f"The price: £{jack_cole_price}\n\n"
           f"The purchase link: {jack_cole_url}\n")

# print(amazon_message)
# print(jack_cole_message)

if float(amazon_price) < 100 and float(jack_cole_price) < 100:
    if float(amazon_price) < float(jack_cole_price):
        with smtplib.SMTP(host=gmail_smtp, port=port_num) as server:
            server.starttls()
            server.login(user=sender, password=password)
            server.sendmail(
                from_addr=sender,
                to_addrs=recipient,
                msg=amazon_message.encode('utf-8')
            )
            print(f"Email has been sent to {recipient}")
    elif float(amazon_price) > float(jack_cole_price):
        with smtplib.SMTP(host=gmail_smtp, port=port_num) as server:
            server.starttls()
            server.login(user=sender, password=password)
            server.sendmail(
                from_addr=sender,
                to_addrs=recipient,
                msg=jack_cole_message.encode('utf-8')
            )
            print(f"Email has been sent to {recipient}")
else:
    pass
