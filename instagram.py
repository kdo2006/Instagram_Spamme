from email import message
from instabot import Bot
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Instagram Spammer by K.D.O")
print(ascii_banner)

bot = Bot()

print("Login to your Instagram account to use this Tool")
print("Enter Your UserName:", end=""),
user = (input( ))

print("Enter Your Password:", end=""),
password = (input( ))

bot.login(username=(user), password=(password))

print("Enter Target UserName:", end=""),
Target = (input( ))

print("Enter Massage:", end=""),
Message = (input( ))

print("Enter Amount:", end=""),
amu = (input( ))

for i in range(amu):
    
    bot.send_message((Message), [(Target)])
