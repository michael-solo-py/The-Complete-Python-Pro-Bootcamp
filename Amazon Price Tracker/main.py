import requests
import smtplib
from bs4 import BeautifulSoup as BS


url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7"}
response = requests.get(url=url, headers=header).text


bs = BS(response, "lxml")
price = bs.find("table", class_="a-lineitem a-align-top").find("span", class_="a-offscreen").text
title = bs.find(id="productTitle").get_text().strip()
price = float(price.split("$")[-1])

if price < 80:
    message = f"{title} is {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as email:
        email.starttls()
        result = email.login("forprogramming23@gmail.com", "")
        email.sendmail(
            from_addr="@gmail.com",
            to_addrs="@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

    print(message)
