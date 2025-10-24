# 🛍️ Amazon & Jack & Cole Price Alert Script

A Python script that compares the price of a specific product on 

- Amazon UK
- Jackson & Cole’s official website

then sends an email alert when the product price drops below a certain threshold or is cheaper on one of the sites.

# 📋 Features

- Scrapes product titles and prices from:

  - Amazon UK
  
  - Jackson & Cole

- Compares the two prices.

- Sends an email notification when the price is below £100 and identifies the cheaper option.

- Uses environment variables for secure storage of email credentials.

# 🧰 Requirements

Python 3.8 or later

The following Python packages:

``` bash
pip install beautifulsoup4 requests lxml
```

# ⚙️ Setup Instructions

1. Clone or download this repository.

2. Set up environment variables in your terminal or .env file:

```bash
export SEND_EMAIL="your_email@gmail.com"
export RECEIVE_EMAIL="recipient_email@example.com"
export PASSWORD="your_app_password"
```
3. Edit product URLs if needed:

    amazon_product_url = "https://www.amazon.co.uk/..."
    
    jack_cole_url = "https://jacksonandcole.com/products/..."


4. Run the script:
```bash 
python3 main.py
```
# 📧 Email Notification Example

When a price drop is detected, you’ll receive an email like this:

Subject: Price Alert!
The product: 'Ancona 30 Premium Waterproof Rolltop Drybag Backpack'

The price: £89.99!

The purchase link: https://the-actual-website-address-here


# 🔒 Environment Variables Summary
Variable	Description
SEND_EMAIL	Sender Gmail address
RECEIVE_EMAIL	Recipient email address
PASSWORD	App password for sender’s email

# 🧠 How It Works

- Fetches and parses product pages using **requests** and **BeautifulSoup**.

- Extracts price and product title elements.

- Compares the numeric values of both prices.

    If both are under £100, Sends an email with details of the cheaper option.
  
    If neither is under £100, no email is sent.

# ⚠️ Notes

The script is tailored for the Ancona 30 Waterproof Rolltop Drybag Backpack.
**You can update the URLs to monitor any other product**.

HTML structure on product pages can change; if it does, you may need to adjust the selectors in the code.

To avoid being blocked by Amazon, avoid sending too many requests in a short time.

# 🧑‍💻 Author

LegradiK - [GitHub](https://github.com/LegradiK)
