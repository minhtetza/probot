import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '7336963132:AAGc7mn2T6-MF7H-hWcBvRVQu-lu27B1Rbw'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=6191863486 
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
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/bkddgfsa/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="😈 𝗝𝗢𝗜𝗡 🎉", url="https://t.me/CHITNGE54")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/bkddgfsa/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝐂𝐥𝐢𝐜𝐤 /cmds 𝐓𝐨 𝐕𝐢𝐞𝐰 𝐓𝐡𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐎𝐞 𝐒𝐞𝐧𝐭 𝐓𝐡𝐞 𝐓𝐱𝐓 𝐅𝐢𝐥𝐞 𝐀𝐧𝐝 𝐈 𝐖𝐢𝐥𝐥 𝐂𝐡𝐞𝐜𝐤 𝐈𝐭''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"💥 {BL} 💳",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗮𝗿𝗴𝗲 3$ ✅ <code>/chk</code> 𝗻𝗯|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 

𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗮𝗿𝗴𝗲  <code>/sex</code> 𝗻𝗯|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝐘𝐨𝐮 𝐂𝐚𝐧𝐧𝐨𝐭 𝐔𝐬𝐞 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐘𝐨𝐮𝐫 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐄𝐱𝐩𝐢𝐫𝐞𝐝 🥲</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🎉 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗖𝗵𝗮𝗿𝗴𝗲 💵",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"🎉 𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗮𝗿𝗴𝗲 3$💵",callback_data='sq')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝐂𝐡𝐨𝐨𝐬𝐞 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐔𝐬𝐞',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Stripe Charge 💵'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('Unknown')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('Unknown')
					try:
						country=(data['country']['name'])
					except:
						country=('Unknown')
					try:
						brand=(data['scheme'])
					except:
						brand=('Unknown')
					try:
						card_type=(data['type'])
					except:
						card_type=('Unknown')
					try:
						url=(data['bank']['url'])
					except:
						url=('Unknown')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"⚆ 𝐒𝐓𝐀𝐓𝐔𝐒 : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"⚆ 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ : [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"⚆ 𝐂𝐂𝐍 ☑️ :             [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"⌧ 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ : [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"⌧ 𝐂𝐕𝐕 🟢 :             [ {riskk} ] •", callback_data='x')
                                        if "success" in last or 'Stripe Error: Your card number is incorrect.' in last or 'Stripe Error: Your card insufficient funds' in last or 'Stripe Error: Your card does not support this type of purchase' in last or 'Thank you ' in last or 'Stripe Error: Your cars security code is incorrect.' in last or '3d' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(20)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Stripe Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "V2 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('Unknown')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('Unknown')
					try:
						country=(data['country']['name'])
					except:
						country=('Unknown')
					try:
						brand=(data['scheme'])
					except:
						brand=('Unknown')
					try:
						card_type=(data['type'])
					except:
						card_type=('Unknown')
					try:
						url=(data['bank']['url'])
					except:
						url=('Unknown')
					
					start_time = time.time()
					try:
						last = str(Tele2(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"⚆ 𝐒𝐓𝐀𝐓𝐔𝐒 : {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"⚆ 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ : [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"⚆ 𝐂𝐂𝐍 ☑️ :             [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"⌧ 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ : [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"⌧ 𝐂𝐕𝐕 🟢 :              [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"⌧ 𝐓𝐎𝐓𝐀𝐋 🎉 :    [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ ⌧ 𝐒𝐓𝐎𝐏 🚫 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐖𝐡𝐢𝐥𝐞 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬 𝐀𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐀𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a>''', reply_markup=mes)
					
					msg=f'''<b>
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code></a>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge 3$</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code> SUCCESS 🟢</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
					if "success" in last or 'Stripe Error: Your card number is incorrect.' in last or 'Stripe Error: The card insufficient funds' in last or 'Stripe Error: Your card does not support this type of purchase' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(20)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_sex(message):
	gate='Stripe Charge 3$'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝐘𝐨𝐮 𝐂𝐚𝐧𝐧𝐨𝐭 𝐔𝐬𝐞 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐘𝐨𝐮𝐫 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐄𝐱𝐩𝐢𝐫𝐞𝐝 🥲</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐬𝐮𝐫𝐞 𝐲𝐨𝐮 𝐞𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝 𝐝𝐞𝐭𝐚𝐢𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐨𝐫𝐫𝐞𝐜𝐭 𝐟𝐨𝐫𝐦𝐚𝐭:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele2(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟	</a>		
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>{gate}</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>SUCCESSFUL 🟢</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
	msgd=f'''
-𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
┏━━━━━━━⍟	
┃𝐂𝐂: <code>{cc}</code>
┗━━━━━━━━━━━⊛
-𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Stripe Charge 3$</code>		
-𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code> Card Was Declined 🚫</code>

-𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
-𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
-𝐁𝐚𝐧𝐤: <code>{bank}</code>

-𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
-𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
-𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
	if "Thank you for your message." in last or 'Stripe Error: Your card number is incorrect.' in last or 'Stripe Error: insufficient funds' in last or 'success' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_sex(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>TOME VIP 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='TOME-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]
𝗕𝗢𝗧 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 @GSIXTEAM_BOT</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sex') or message.text.lower().startswith('/sex'))
def respond_to_sex(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>Hi Buddy {name}
𝐓𝐡𝐞 𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐚𝐥𝐥𝐨𝐰𝐬 𝐲𝐨𝐮 𝐭𝐨 𝐮𝐬𝐞 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐭𝐨𝐨𝐥𝐬 𝐚𝐧𝐝 𝐩𝐨𝐫𝐭𝐚𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐥𝐢𝐦𝐢𝐭𝐬
𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞
━━━━
𝐕𝐈𝐏 𝐩𝐥𝐚𝐧 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐩𝐫𝐢𝐜𝐞𝐬:

3𝐝𝐚𝐲𝐬 = . 5$
𝐖𝐞𝐞𝐤 =   9$
𝐌𝐨𝐧𝐭𝐡 = 19$
𝐁𝐎𝐘 𝐁𝐘 <a href='t.me/Ownerxxxxx'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a></b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="♻️ 𝐎𝐰𝐧𝐞𝐫  😈", url="https://t.me/Ownerxxxxx")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝐘𝐨𝐮 𝐂𝐚𝐧𝐧𝐨𝐭 𝐔𝐬𝐞 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐘𝐨𝐮𝐫 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐄𝐱𝐩𝐢𝐫𝐞𝐝 🥲</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐬𝐮𝐫𝐞 𝐲𝐨𝐮 𝐞𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐜𝐚𝐫𝐝 𝐝𝐞𝐭𝐚𝐢𝐥𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐜𝐨𝐫𝐫𝐞𝐜𝐭 𝐟𝐨𝐫𝐦𝐚𝐭:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele2(cc))
	except Exception as e:
		last='Close Cmds Now 🚫'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟	</a>		
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Charge</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
	msgd=f'''
<a href='t.me/Approved_Raven'>-</a> 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟	</a>		
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Charge</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
	if 'Approved ✅' in last or 'Approved ✅! CVV' in last or 'Approved ✅! Live' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("The bot has been activated.")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"An error occurred:: {e}")
