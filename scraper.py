import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/OnePlus-Aquamarine-Speicher-Vierfach-Garantie-Green/dp/B08HJPB9TB/ref=pd_vtp_1?pd_rd_w=VDEK2&pf_rd_p=b82fdab5-714d-44f8-bd2d-596f98bc21e4&pf_rd_r=9SFS53AJKK5Q79ACVHBY&pd_rd_r=e8e930d2-3859-493f-a58c-b4a6a110562e&pd_rd_wg=7THUF&pd_rd_i=B08HJPB9TB&psc=1'


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    price = soup.find(id='priceblock_ourprice').get_text()

    converted_price = float(price[0:3])

    if(converted_price < 594.0):
        send_email()

    print(converted_price)

    print(title.strip())

    if(converted_price > 594.0):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('prajwol.devkota016@gmail.com', 'ipchhugjuipehdsc')

    subject  = 'Price fell down!'

    body = 'Check the Amazon link https://www.amazon.de/OnePlus-Aquamarine-Speicher-Vierfach-Garantie-Green/dp/B08HJPB9TB/ref=pd_vtp_1?pd_rd_w=VDEK2&pf_rd_p=b82fdab5-714d-44f8-bd2d-596f98bc21e4&pf_rd_r=9SFS53AJKK5Q79ACVHBY&pd_rd_r=e8e930d2-3859-493f-a58c-b4a6a110562e&pd_rd_wg=7THUF&pd_rd_i=B08HJPB9TB&psc=1'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'prazool007@gmail.com',
        'prajwol.devkota016@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


check_price()