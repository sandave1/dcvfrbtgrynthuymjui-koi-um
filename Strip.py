from bs4 import BeautifulSoup
import requests ,os
from faker import Faker
import random
faker = Faker()
fake = Faker()
try:
    from getuseragent import UserAgent
except ModuleNotFoundError:

    os.system('pip install getuseragent')
    from getuseragent import UserAgent
    
user_agent = UserAgent('windows').Random()

def Check(P):
    fer = faker.first_name()
    lat = faker.first_name()
    no = faker.first_name().upper()
    mo = faker.first_name().upper()
    name = f"{no} {mo}"
    psw = faker.password()
    hell = ''.join(random.choice('qwaszxcerdfvbtyghnmjkluiop0987654321') for i in range(17))
    domin = random.choice(['@hotmail.com', '@aol.com', '@gmail.com', '@yahoo.com'])
    email = hell + domin

    try:
      n, mm, yy, cvc = map(str.strip, P.split("|"))
    except:
      pass

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
        'dnt': '1',
        'referer': 'https://www.ucanada.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    }

    params = {
        'sharedCustomerIdentifierType': 'undefined',
        'braintreeLibraryVersion': 'braintree/web/2.15.7',
        'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjU1MDgyMDksImp0aSI6IjhlMmM3Y2Y2LWQyODItNDFlNS05YTU3LTA4Y2FjYzNiOTk2NiIsInN1YiI6ImQ1MzVuM2tkNThucHg2aHkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImQ1MzVuM2tkNThucHg2aHkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.CKuulaa0jDs4YLLqrlBHDulE4--mTd0Z0x00-BflEgTTemVDug4NE0TXmR8VMEwlFKfaUd1FzsnXBQPPjJq3Gw',
        'share': 'undefined',
        'creditCard[billingAddress][postalCode]': '10080',
        'creditCard[number]': n,
        'creditCard[cardholderName]': 'dave',
        'creditCard[expirationMonth]': mm,
        'creditCard[expirationYear]': yy,
        'creditCard[cvv]': cvc,
        'creditCard[options][validate]': 'false',
        '_meta[integration]': 'custom',
        '_meta[source]': 'form',
        '_method': 'POST',
        'callback': 'callback_json2cd725ec85764c78858121cdb6cf160f',
    }

    response = requests.get(
        'https://api.braintreegateway.com/merchants/d535n3kd58npx6hy/client_api/v1/payment_methods/credit_cards',
        params=params,
        headers=headers,
    ).text
    try:
        tokenz = response.split('"nonce":"')[1].split('"')[0]
    except:
        pass


    cookies = {
        '.Nop.RecentlyViewedProducts': '1927%2C2178',
        '.Nop.Authentication': 'CfDJ8EHWuELgMsJGndWiDmYn3NWNq1S2myFoSHSY-Kn6YSCPmaIZVi3dAiwF4d8cMlKtNLNFPlxHhHfaKS0gEh9DR2FqqWH7drQbd53FDqfqyXrnos2pPf2sTGG-s-Km4GQ-Yfc6zZ30Iry5YH3KqlUoF7lA2NX-nDp8upe2iH3Q4xetDMUuvzzDasLRGOxRm6kzGgX2zHSjiw4m9704nhAVNZVvHng7lgQFXQzPMg4UvcfVVeAQRsB6atxnBh3vAPLqK-DwRKpqZ4e1suSrGYVB0XyBZofSpn2mKK6D8A2p2qkSlIoQJ-q2V2komXl3slqZuBSqN0xGaLJ2NJaGoZ4wlacvlnbr_ANjl6ytQrEBEfikqLY-ngU2OLlhyh-ww6btA7pGGDCCKjDgVfqoJzURMjwV3jzyoWGFQwewnKz4qFtNqvYPdOcdOwwt92yYtYaKzItk79bzJyDAyz_ssnhHHhyISSmhDOM-_3TcBuWyU8zzgxx9T_2EfynGgl09MU1ToWgrbFXN09MtU56ZaGgvFZDklxUfx3NQ9vQFN-w6oIVpY_kxGYUL-SHGe7TkWEK3XY51Z1bDsrUp27VwQJQWgg613lclY75Wpfr2tsEaNwMK',
        '_gid': 'GA1.2.38224294.1725421724',
        '.Nop.Antiforgery': 'CfDJ8EHWuELgMsJGndWiDmYn3NV6qYBlCkVE0oRqqNZNDvwoy7kWS2nIKppBbtpPCQTUTKko_hdDNQ4n-DJE5LwcRqJoUOcQMfsY4kT6iqoYOM-7tWe7HTvARxCgsSzrNENpfQ6XxNDITGxVmZuuDrDnljQ',
        '_gat_gtag_UA_51641748_2': '1',
        '_ga_X65ZPPEB85': 'GS1.1.1725421724.17.1.1725421794.54.0.0',
        '_ga': 'GA1.1.433138092.1723066068',
        '.Nop.Customer': '2eabf2da-0d47-4636-9571-3895a109e1af',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,tr;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '.Nop.RecentlyViewedProducts=1927%2C2178; .Nop.Authentication=CfDJ8EHWuELgMsJGndWiDmYn3NWNq1S2myFoSHSY-Kn6YSCPmaIZVi3dAiwF4d8cMlKtNLNFPlxHhHfaKS0gEh9DR2FqqWH7drQbd53FDqfqyXrnos2pPf2sTGG-s-Km4GQ-Yfc6zZ30Iry5YH3KqlUoF7lA2NX-nDp8upe2iH3Q4xetDMUuvzzDasLRGOxRm6kzGgX2zHSjiw4m9704nhAVNZVvHng7lgQFXQzPMg4UvcfVVeAQRsB6atxnBh3vAPLqK-DwRKpqZ4e1suSrGYVB0XyBZofSpn2mKK6D8A2p2qkSlIoQJ-q2V2komXl3slqZuBSqN0xGaLJ2NJaGoZ4wlacvlnbr_ANjl6ytQrEBEfikqLY-ngU2OLlhyh-ww6btA7pGGDCCKjDgVfqoJzURMjwV3jzyoWGFQwewnKz4qFtNqvYPdOcdOwwt92yYtYaKzItk79bzJyDAyz_ssnhHHhyISSmhDOM-_3TcBuWyU8zzgxx9T_2EfynGgl09MU1ToWgrbFXN09MtU56ZaGgvFZDklxUfx3NQ9vQFN-w6oIVpY_kxGYUL-SHGe7TkWEK3XY51Z1bDsrUp27VwQJQWgg613lclY75Wpfr2tsEaNwMK; _gid=GA1.2.38224294.1725421724; .Nop.Antiforgery=CfDJ8EHWuELgMsJGndWiDmYn3NV6qYBlCkVE0oRqqNZNDvwoy7kWS2nIKppBbtpPCQTUTKko_hdDNQ4n-DJE5LwcRqJoUOcQMfsY4kT6iqoYOM-7tWe7HTvARxCgsSzrNENpfQ6XxNDITGxVmZuuDrDnljQ; _gat_gtag_UA_51641748_2=1; _ga_X65ZPPEB85=GS1.1.1725421724.17.1.1725421794.54.0.0; _ga=GA1.1.433138092.1723066068; .Nop.Customer=2eabf2da-0d47-4636-9571-3895a109e1af',
        'DNT': '1',
        'Origin': 'https://www.ucanada.com',
        'Referer': 'https://www.ucanada.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '__RequestVerificationToken': 'CfDJ8EHWuELgMsJGndWiDmYn3NW9AtGbVf-AXxlD7RceSQgeQbYkZKEvNW-leZRA9t5I__GuYXEmqwfXhHwalNmUVjmJSv0PZW51OUHAQxqqYWqZ5Tw02rFuQecKa68nYzeZV1zSDACb4hgcqInaI1VjbBlpWV4xjHLdCIFPwOwa7dqfwzM9nueDqW_N84FxYW21fA',
        'billingFirstName': 'dave',
        'billingLastName': 'ali',
        'billingEmail': 'sandavesssx22@gmail.com',
        'billingCompany': 'dave',
        'billingCountry': '1',
        'billingStateProvince': '11',
        'billingCity': 'Kadobunkuro',
        'billingCounty': '',
        'billingAddress1': '234 Ahmed Gambo Saleh Crescent',
        'billingAddress2': '',
        'billingZipPostalCode': '10080',
        'billingPhoneNumber': '',
        'billingFaxNumber': '',
        'billingVatNumber': '',
        'shipToSameAddress': 'true',
        'shippingFirstName': 'dave',
        'shippingLastName': 'ali',
        'shippingEmail': 'sandavesssx22@gmail.com',
        'shippingCompany': 'dave',
        'shippingCountry': '1',
        'shippingStateProvince': '11',
        'shippingCity': 'Kadobunkuro',
        'shippingCounty': '',
        'shippingAddress1': '234 Ahmed Gambo Saleh Crescent',
        'shippingAddress2': '',
        'shippingZipPostalCode': '10080',
        'shippingPhoneNumber': '',
        'shippingFaxNumber': '',
        'shippingmethod': '[object Object]',
        'paymentmethod': '[object Object]',
        'CardholderName': 'dave',
        'CardNumber': n,
        'ExpireMonth': mm,
        'ExpireYear': yy,
        'CardCode': cvc,
        'paymenttoken': tokenz,
        'nextstep': 'Next',
        'itemquantity298545': '1',
    }

    response = requests.post('https://www.ucanada.com/RealOnePageCheckout/ConfirmOrder', cookies=cookies, headers=headers,data=data)
    hh = response.text
    return hh
    	
        