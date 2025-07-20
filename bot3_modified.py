import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
USERNAME = "HRO_X"
from gates import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading


import threading
import time
from telebot import types

stopuser = {}
token = "8153463474:AAG5GyDDvReiW1bJggZcNHLlmJ1qopEWM5E"
bot=telebot.TeleBot(token,parse_mode="HTML")


admin='5770036341'

myid = ['5770036341']

admins = ['55770036341','5770036341']


import telebot
from telebot.types import LabeledPrice, ShippingOption, PreCheckoutQuery
from datetime import datetime, timedelta


     










command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == 'Free - Not Subscribed':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Devloper bot ϟ", url=f"https://t.me/@HRO_X")
			keyboard.add(contact_button)
			random_number = random.randint(4, 17)
			photo_url = f'https://t.me/For_Hiro/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''ϟ Welcome Dear -> {name} ϟ
ϟ Youre Not Subscribed in Check World Bot ❌

ϟ For Show Bot Prices Send -> /prices
ϟ Programmer ~ @HRO_X  ''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="ϟ Devloper bot ϟ", url="https://t.me/HRO_X")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(4, 17)
		photo_url = f'https://t.me/For_Hiro/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''ϟ Welcome -> {name} ϟ
- Your Subscription is Active ✅

- For Show check commands Send -> /cmds
- For Check The Combo CC File Send The Combo And Choose The Gate ✅

ϟ - Programmer • @HRO_X ''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='Free - Not Subscribed'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"ϟ {BL} ϟ",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text='''
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 1
[ϟ] Format: /chk card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 2
[ϟ] Format: /cc card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 3
[ϟ] Format: /b3 card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 4
[ϟ] Format: /sa card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Charge 0.50$
[ϟ] Format: /ba card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: BIN Info Lookup
[ϟ] Format: /bin BIN
[ϟ] Condition: ON! ✅
[ϟ] Type: Free For All ✅
━━━━━━━━━━━━━━━━━━━
ϟ - We will adding More Gates....
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
		if BL == 'Free - Not Subscribed':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - Hiro", url=f"https://t.me/@HRO_X")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''ϟ Welcome Dear » {name}
- Youre Not Subscribed in BOT ❌

• For Show Bot Priced Send /prices
- Programmer ~ @HRO_X ''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - Hiro", url=f"https://t.me/@HRO_X")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>• Welcome Dear » {name}
- Youre Not Subscribed in BOT ❌

• For Show Bot Priced Send /prices
- Programmer ~ @HRO_X </b>''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Devloper - Hiro ϟ", url=f"https://t.me/@HRO_X")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text='''ϟ Your Subscription has Expired • لاتستطيع استخدام البوت لانه انتهى اشتراكك 
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = 'Free - Not Subscribed'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"ϟ Braintree Auth 1 ϟ",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"ϟ Braintree Auth 2 ϟ️",callback_data='br2')
		b3 = types.InlineKeyboardButton(text=f"ϟ Braintree Auth 3 ϟ️",callback_data='br3')
		sa = types.InlineKeyboardButton(text=f"ϟ Braintree Auth 4 ϟ️",callback_data='br4')
		m = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		d = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		keyboard.add(contact_button)
		keyboard.add(sw)
		keyboard.add(b3)
		keyboard.add(sa)
		keyboard.add(m)
		keyboard.add(d)
		bot.reply_to(message, text=f'ϟ Chose The Gateway You Want to use from Bellow ',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
			
			
			
			

	
	
	
	
def dato(zh):
 
 

 
 
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
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
		print(e)
		return 'No info'
	
	
	







import threading
import time
from telebot import types

MAX_LINES = 10000
stopuser = {}  
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True

check_enabled_ch1 = True






@bot.message_handler(commands=['onb1'])
def enable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb1'])
def disable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')








@bot.message_handler(commands=['onb2'])
def enable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb2'])
def disable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')





@bot.message_handler(commands=['onb3'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb3'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        

        
        
@bot.message_handler(commands=['onb4'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
@bot.message_handler(commands=['offb4'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        
        
        
@bot.message_handler(commands=['onch1'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
@bot.message_handler(commands=['offch1'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        
        
        





from telebot import types

check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True
check_enabled_ch1 = True

MAX_LINES = 10000

@bot.message_handler(commands=['gate'])
def show_menu(message):
    if str(message.from_user.id) in admins:
        markup = types.InlineKeyboardMarkup(row_width=1)
        toggle_br1 = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        toggle_br2 = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        toggle_br3 = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        toggle_br4 = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        toggle_ch1 = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        
        br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({toggle_br1})", callback_data='toggle_br1')
        br2_button = types.InlineKeyboardButton(f"Braintree Auth 2 ({toggle_br2})", callback_data='toggle_br2')
        br3_button = types.InlineKeyboardButton(f"Braintree Auth 3 ({toggle_br3})", callback_data='toggle_br3')
        br4_button = types.InlineKeyboardButton(f"Braintree Auth 4 ({toggle_br4})", callback_data='toggle_br4')
        ch1_button = types.InlineKeyboardButton(f"Braintree Charge 1 ({toggle_ch1})", callback_data='toggle_ch1')
        limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
        
        markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'You are not the owner 🤍')

@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_') or call.data == 'set_limits')
def handle_toggle(call):
    global check_enabled_br1, check_enabled_br2, check_enabled_br3, check_enabled_br4, check_enabled_ch1, MAX_LINES
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == 'toggle_br1':
        check_enabled_br1 = not check_enabled_br1
        status = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 1 is now {status}.")
    elif call.data == 'toggle_br2':
        check_enabled_br2 = not check_enabled_br2
        status = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 2 is now {status}.")
    elif call.data == 'toggle_br3':
        check_enabled_br3 = not check_enabled_br3
        status = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 3 is now {status}.")
    elif call.data == 'toggle_br4':
        check_enabled_br4 = not check_enabled_br4
        status = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 4 is now {status}.")
    elif call.data == 'toggle_ch1':
        check_enabled_ch1 = not check_enabled_ch1
        status = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Charge 1 is now {status}.")
    elif call.data == 'set_limits':
        
        bot.send_message(chat_id, "Please enter the new limit value for Gate limits as /set_limit 1500")

    
    markup = typesطط.InlineKeyboardMarkup(row_width=1)
    br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({'Enable✅' if check_enabled_br1 else 'Disable❌'})", callback_data='toggle_br1')
    br2_button = types.InlineKeyboardButton(f"Braintree Auth 2 ({'Enable✅' if check_enabled_br2 else 'Disable❌'})", callback_data='toggle_br2')
    br3_button = types.InlineKeyboardButton(f"Braintree Auth 3 ({'Enable✅' if check_enabled_br3 else 'Disable❌'})", callback_data='toggle_br3')
    br4_button = types.InlineKeyboardButton(f"Braintree Auth 4 ({'Enable✅' if check_enabled_br4 else 'Disable❌'})", callback_data='toggle_br4')
    ch1_button = types.InlineKeyboardButton(f"Braintree Charge 1 ({'Enable✅' if check_enabled_ch1 else 'Disable❌'})", callback_data='toggle_ch1')
    limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
    markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    global MAX_LINES
    try:
        
        if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            new_limit = int(message.text.split()[1])
            MAX_LINES = new_limit
            bot.reply_to(message, f"Gate limit has been set to {MAX_LINES}.")
            
            
            show_menu(message)
        else:
            bot.reply_to(message, "Please use the correct format: /set_limit 1500.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        print(f"Error: {e}")











import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  
check_enabled = True 

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br1:  
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  
    def my_function():
        gate = 'Braintree Auth 1'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @HRO_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @HRO_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
	
	
	
	
	
	



	

	
	
	
	
	
	
	


import threading
import time
from telebot import types

MAX_LINES = 10000
stopuser = {}  
check_enabled_br2 = True  

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 2 Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br2:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  
    def my_function():
        gate = 'Braintree Auth 2'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele2(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @HRO_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @HRO_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
	
	
	












	











import threading
import time
from telebot import types

MAX_LINES = 10000
stopuser = {}  
check_enabled_br3 = True  
@bot.message_handler(commands=['offb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 3 Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br3')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br3:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return

    def my_function():
        gate = 'Braintree Auth 3'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'
                        return

                    start_time = time.time()
                    try:
                        last = str(Tele3(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time

                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @HRO_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @HRO_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')









import threading
import time
from telebot import types

    







	
	
	
	
	
	
	
	
	
	
	
import threading
import time
from telebot import types

MAX_LINES = 10000
stopuser = {}  
check_enabled_br4 = True  
@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = False
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br4')
def menu_callbactok(call):
    id = str(call.from_user.id)

    if not check_enabled_br4:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  
    def my_function():
        gate = 'Braintree Auth 4'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)
        
        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)
                
                
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  
                    return
                
                stopuser[id] = {'status': 'start'}
                
                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  
                        return
                    start_time = time.time()
                    try:
                        last = str(notauto(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    
                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @HRO_X </b>''', 
                        reply_markup=mes)
                    
                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''
                    
                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1
                    
                    time.sleep(15)
        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')
        
        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @HRO_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
    


	






























import json
from datetime import datetime, timedelta


def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)]['plan']
        timer = json_data[str(user_id)]['timer']
        if user_plan != 'Free - Not Subscribed':
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  
                    return True
            except Exception as e:
                return False
    return False










import time
from datetime import datetime, timedelta


command_usage = {}

check_enabled_br1 = True

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vhk(message):
    global check_enabled_br1
    user_id = message.chat.id
    current_time = datetime.now()

    
    if not check_enabled_br1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.chk ', '').replace('/chk ', '')
        gate='Braintree Auth 1'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Auth 1

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Auth 1

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        cvc = f'''<b>• Cvv Card ☑️        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @HRO_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed HiroChk BOT !❌

Your ID : {message.chat.id}
Programmer - @HRO_X''')




















import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br2 = True

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def respond_to_vhk(message):
    global check_enabled_br2
    user_id = message.chat.id
    current_time = datetime.now()

    
    if not check_enabled_br2:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.cc ', '').replace('/cc ', '')
        gate = 'Braintree Auth 2'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele2(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Auth 2

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Auth 2

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        cvc = f'''<b>• Cvv Card ☑️        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @HRO_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed HiroChk BOT !❌

Your ID : {message.chat.id}
Programmer - @HRO_X''')











import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br3 = True

@bot.message_handler(commands=['offb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.b3') or message.text.lower().startswith('/b3'))
def respond_to_vhk(message):
    global check_enabled_br3
    user_id = message.chat.id
    current_time = datetime.now()

    
    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.b3 ', '').replace('/b3 ', '')
        gate='Braintree Auth 3'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele3(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{c}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Auth 3

{str(dato(c[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{c}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Auth 3

{str(dato(c[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        cvc = f'''<b>• Cvv Card ☑️        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(c[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @HRO_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed HiroChk BOT !❌

Your ID : {message.chat.id}
Programmer - @HRO_X''')












import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br4 = True

@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sa') or message.text.lower().startswith('/sa'))
def respond_to_vhk(message):
    global check_enabled_br4
    user_id = message.chat.id
    current_time = datetime.now()
    
    
    if not check_enabled_br4:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.sa ', '').replace('/sa ', '')
        gate='Braintree Auth 4'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(notauto(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Auth 4

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Auth 4

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        cvc = f'''<b>• Cvv Card ☑️        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @HRO_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed HiroChk BOT !❌

Your ID : {message.chat.id}
Programmer - @HRO_X''')






























































from datetime import datetime, timedelta


last_command_usage = {}


check_enabled_ch1 = True

@bot.message_handler(commands=['offch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = False
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(commands=['onch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = True
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.ba') or message.text.lower().startswith('/ba'))
def respond_to_vhk(message):
    global check_enabled_ch1
    user_id = message.chat.id
    current_time = datetime.now()

    
    if not check_enabled_ch1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    
    if user_id in last_command_usage:
        time_diff = (current_time - last_command_usage[user_id]).seconds
        if time_diff < 30:  
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return

    
    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        cc = message.text.replace('.ba ', '').replace('/ba ', '')
        gate = 'ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele4(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> ʙʀᴀɪɴᴛʀᴇᴇ ᴄʜᴀʀɢᴇ 𝟶.𝟻𝟶 $

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @HRO_X⚡</b>'''

        cvc = f'''<b>• Cvv Card ☑️        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @HRO_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed HiroChk BOT !❌

Your ID : {message.chat.id}
Programmer - @HRO_X''')


















@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>ϟ BIN Info Lookup  🔍
	
ϟ - BIN -></b> <code>{cc}</code>

<b>{str(dato(cc[:6]))}</b>''')










import json
import threading
from datetime import datetime
import time




def get_user_info(user_id):
    try:
        chat = bot.get_chat(user_id)
        user_name = chat.first_name
        user_username = chat.username
        return user_name, user_username
    except Exception as e:
        m = (f"Error retrieving user info for ID {user_id}: {e}")
        return 'Unknown', 'Unknown'

def notify_admins(user_id, user_data):
    user_name, user_username = get_user_info(user_id)
    message = f'''- Subscription Expired Notification 🕒

• User ID: {user_id}
• User Name: {user_name}
• Username: @{user_username}
• Plan: {user_data.get('plan', 'Free - Not Subscribed')}
• Expiration Date: {user_data.get('timer', 'N/A')}
'''
    for admin_id in myid:
        bot.send_message(admin_id, message)

def notify_user(user_id):
    try:
        bot.send_message(user_id, "Your Subscription Has Expired.")
    except Exception as e:
        m = (f"Error notifying user {user_id}: {e}")

def update_subscription_status():
    try:
        
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        current_time = datetime.now()
        updated = False  

        for user_id, user_data in json_data.items():
            timer_str = user_data.get('timer', None)
            if timer_str:
                try:
                    expiration_time = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                    
                    if current_time > expiration_time:
                        user_data['plan'] = 'Free - Not Subscribed'
                        del user_data['timer']  
                        updated = True
                        
                        notify_admins(user_id, user_data)
                        
                        notify_user(user_id)
                except ValueError:
                    m = (f"Date format error for user {user_id} with date {timer_str}")
        
        if updated:
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = ("Subscription status updated.")
    
    except Exception as e:
        mm = (f"Error updating subscription status: {e}")

def schedule_check():
    while True:
        update_subscription_status()
        time.sleep(1)  
check_thread = threading.Thread(target=schedule_check)
check_thread.start()















import json
from datetime import datetime, timedelta


def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)].get('plan', 'Free - Not Subscribed')
        timer = json_data[str(user_id)].get('timer', None)
        if user_plan != 'Free - Not Subscribed' and timer:
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  
                    return True
            except Exception as e:
                print(f"Error parsing date for user {user_id}: {e}")
                return False
    return False
    
    
    



@bot.message_handler(commands=['kil'])
def qwwe(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            idd = message.from_user.id
            mes = message.text.replace("/kil ", "")
            bot.send_message(idd, mes)

            
            with open('data.json', 'r') as file:
                json_data = json.load(file)

            for user_id, details in json_data.items():
                if check_user_plan(user_id):
                    try:
                        mp += 1
                        bot.send_message(user_id, text=mes)
                    except Exception as e:
                        erop += 1
                        print(f"Error sending message to user {user_id}: {e}")

            bot.reply_to(message, f'''- Hello Hiro
• Done Send - {mp}
• Bad Send - {erop}''')
        except Exception as err:
            bot.reply_to(message, f'- Was An error : {err}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")












@bot.message_handler(commands=["tot"])
def adode(message):
    if str(message.from_user.id) in myid:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        vip_count = 0
        for user_id, details in json_data.items():
            user_plan = details.get('plan', 'Free - Not Subscribed')
            timer = details.get('timer', None)
            if user_plan != 'Free - Not Subscribed' and timer:
                try:
                    date_str = timer.split('.')[0]
                    provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    current_time = datetime.now()
                    if current_time - provided_time <= timedelta(hours=0):  
                        vip_count += 1
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")

        bot.reply_to(message, f'- Total VIP Subscribers: {vip_count}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")











import json
from datetime import datetime

@bot.message_handler(commands=['sh'])
def show_vip_subscribers(message):
    if str(message.chat.id) in myid:
        user_id = message.text.replace("/sh", "")
        try:
            with open('data.json', 'r') as file:
                json_data = json.load(file)
        except Exception as e:
            bot.send_message(message.chat.id, f'- Error reading data file: {e}')
            return

        total_subscribers = 0
        subscriber_details = []

        for user_id, user_data in json_data.items():
            plan = user_data.get('plan', 'NO PLAN')
            if plan == 'VIP Subscribed':
                timer = user_data.get('timer', 'NO EXPIRATION DATE')
                if timer != 'NO EXPIRATION DATE':
                    try:
                        expiration_date = datetime.strptime(timer, "%Y-%m-%d %H:%M")
                        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M")
                    except ValueError:
                        expiration_date_str = 'INVALID DATE FORMAT'
                else:
                    expiration_date_str = 'NO EXPIRATION DATE'
                
                
                try:
                    chat = bot.get_chat(user_id)
                    user_name = chat.first_name
                    user_username = chat.username
                    if user_name:
                        user_display = f"Name: {user_name}\nUsername: @{user_username}" if user_username else f"Name: {user_name}\nUsername: Not Available"
                    else:
                        
                        continue
                except Exception as e:
                    
                    continue
                
                subscriber_details.append(f'''• User ID: {user_id}
{user_display}
• Plan: {plan}
• Expiration Date: {expiration_date_str}
━━━━━━━━━━━━━━━━━━━━━━
''')

                total_subscribers += 1

        if subscriber_details:
            details_message = "\n".join(subscriber_details)
            bot.send_message(message.chat.id, f'''- VIP Subscriber Details ✅💫

{details_message} - Total VIP Subscribers -> {total_subscribers} ✅
''')
        else:
            bot.send_message(message.chat.id, '- No VIP subscribers found.')











import json
from datetime import datetime

def remove_subscription(user_id):
    try:
        
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
            
            json_data[user_id]['plan'] = 'Free - Not Subscribed'
            del json_data[user_id]['timer']  
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = (f"Subscription for user {user_id} has been set to FREE.")
        else:
            mm= (f"User ID {user_id} not found in data.json.")
    
    except Exception as e:
        m = (f"Error removing subscription for user {user_id}: {e}")

@bot.message_handler(commands=['dele'])
def qwwem(message):
    if str(message.chat.id) in admins:
        user_id = message.text.replace("/dele ", "")
        
        
        remove_subscription(user_id)
        
        try:
            chat = bot.get_chat(user_id)
            frs = chat.first_name
            use = chat.username
            bot.send_message(message.chat.id, f'''- Done ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}

- IS Removed From Subscribers ✅''')
        except Exception as e:
            bot.send_message(message.chat.id, f'''- UnSuccessful Removal ❌

• User might not have opened your bot.

- Error -> {e}''')
    else:
        bot.send_message(message.chat.id, "You do not have permission to execute this command.")















@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or 'NoUsername'  
    response_message = f'''🌟 Welcome » {user_first_name}
🆔 ID » <code>{user_id}</code>
📛 Name » {user_first_name}
🧑 Username » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')



	
	
	







@bot.message_handler(commands=["menu"])
def adodre(message):
	if str(message.chat.id) in myid:
		bot.reply_to(message,'''- Welcome My Boss ♡
- Start Check Bot ¦ /start
- Add New Subscriber ¦ /add + ID
- Total Bot Users ¦ /tot
- Send Msg Forr All ¦ /kil + msg
- Delete A Subsc ¦ /dele + ID
- Show Sub's ID's ¦ /sh
- Stop And Start The Gate's /gate
------------------------------------
• Programmer ¦ @HRO_X
• Channel ¦ @Soon....''')





	
	
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.prices') or message.text.lower().startswith('/prices'))
def respondn_to_vhk(message):
 bot.reply_to(message,'- you can donate to bot owner from this command:  /donate') 












import json
import threading
from datetime import datetime, timedelta
import random
import string


@bot.message_handler(commands=["code"])
def generate_code(message):
    def my_function():
        id = message.from_user.id
        if not str(id) in myid:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            
            characters = string.ascii_uppercase + string.digits
            pas = 'HiroChk-' + '2024' +'-' + ''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            expiration_time = current_time + timedelta(hours=h)
            plan = 'VIP Subscribed'
            expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
            
            new_data = {
                pas: {
                    "plan": plan,
                    "timer": expiration_time_str
                }
            }
            
            existing_data.update(new_data)
            
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            
            msg = f'''<b>ϟ Check World Code
ϟ Expire in -> {expiration_time_str}
ϟ Code -> <code>{pas}</code>
            
ϟ For redeem The Code Use /redeem code</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f'<b>ERROR : {e}</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            
            re = message.text.split(' ')[1]
            
            
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            
            
            if re in json_data:
                timer = json_data[re].get('timer', 'Unknown')
                typ = json_data[re].get('plan', 'Free - Not Subscribed')

                
                json_data[str(message.from_user.id)] = {
                    'timer': timer,
                    'plan': typ
                }
                
                
                del json_data[re]
                
                
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=2, ensure_ascii=False)

                msg = f'''<b>ϟ Check World VIP Subscribtion Done ✅
ϟ Expires in -> {timer}</b>'''
                bot.reply_to(message, msg, parse_mode="HTML")
            else:
                bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")

        except KeyError as e:
            print(f'KeyError: {e}')
            bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '<b>There was an error processing your request. Please try again later.</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


@bot.message_handler(commands=['add'])
def add_subscription(message):
    def my_function():
        try:
            chid = message.chat.id
            command_text = message.text.replace('/add ', '')
            user_id, duration_hours = command_text.split()
            duration_hours = int(duration_hours)
            
            if str(message.chat.id) in myid:
                current_time = datetime.now()
                expiration_time = current_time + timedelta(hours=duration_hours)
                expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
                plan = 'VIP Subscribed'
                
                
                with open('data.json', 'r') as json_file:
                    existing_data = json.load(json_file)
                
                
                existing_data[user_id] = {
                    'timer': expiration_time_str,
                    'plan': plan
                }
                
                
                with open('data.json', 'w') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                
                
                try:
                    chat = bot.get_chat(user_id)
                    frs = chat.first_name
                    use = chat.username
                    user_display = f"Name: {frs}\nUsername: @{use}" if use else f"Name: {frs}\nUsername: Not Available"
                except Exception as e:
                    user_display = f"Name: Unknown\nUsername: Unknown"
                
                bot.send_message(chid, f'''- Done Add -> <code>{user_id}</code> 

• Subscription Duration -> {duration_hours} hours
• {user_display}
- Added to Subscribers List ✅''')
            else:
                bot.send_message(chid, ' - Unauthorized Access !!!!')
        except Exception as e:
            bot.reply_to(message, f'- Was An Error -> {e}')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()











def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
		continue