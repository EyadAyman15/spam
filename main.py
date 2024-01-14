import requests
from colorama import Fore, Style, init
import time
from concurrent.futures import ThreadPoolExecutor
import pyperclip

init()

# Welcome message
print(f"{Fore.RED}{Style.BRIGHT}\nProgrammed by: Eyad Ayman\nDiscord: eyad_15{Style.RESET_ALL}")

# allow pasting 
def paste_from_clipboard():
    return pyperclip.paste()

if __name__ == "__main__":
    clipboard_content = paste_from_clipboard()

# Prompt user for number of orders
num_orders = int(input("\nHow many orders do you want?: "))
token = [None] * num_orders
channel_id = [None] * num_orders
message = [None] * num_orders

# Loop through each order
for i in range(num_orders):
    print(f"{Fore.BLUE}{Style.BRIGHT}\nOrder {i + 1}:{Style.RESET_ALL}")

    # Prompt user for token, channel ID, and message
    token[i] = input("Token: ")
    channel_id[i] = input("Id: ")
    message[i] = input("Message: ")

def send_message(order):
    while True:
        payload = {
            'content': message[order]
        }

        header = {
            'authorization': token[order]
        }
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id[order]}/messages", data=payload,
                          headers=header)
        time.sleep(1.5)

        # Check if message was sent successfully
        if r.status_code == 200:
            print(f"{Fore.GREEN}{Style.BRIGHT}Message sent to channel {channel_id[order]}!\n{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{Style.NORMAL}Error. Please check your credentials. 3s break.\n{Style.RESET_ALL}")
            time.sleep(3)

# Send messages endlessly for each order concurrently
with ThreadPoolExecutor(max_workers=num_orders) as executor:
    executor.map(send_message, range(num_orders))