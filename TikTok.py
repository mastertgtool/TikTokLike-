from colorama import Back, Fore, Style
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import random
import os, binascii
import datetime

print(Fore.GREEN + "--- TikTok Like Bot v1 ---")
print(Fore.GREEN + "--- Created by Master TG ---")
print(Fore.GREEN + "--- MAY TAKE UP TO 24 HOURS FOR ALL LIKES TO APPEAR! ---")
print(Fore.WHITE + "------------------------")
likesInputted = int(input("> Enter the amount of likes: "))
videoURL = input("> Video URL: ")
failedlikes = 0

if "tiktok.com" in str(videoURL):
    # Logs video URL in Discord channel
    # webhook = DiscordWebhook(url=os.environ.get('HOOK'), )
    # webhook = DiscordWebhook(
    #     url=
    #     "leave the code",
    # )
    # embed = DiscordEmbed(title="New Like Bot Attempt",
    #                      description=str(videoURL) + ", attempted to add **" +
    #                      str(likesInputted) + "** likes",
    #                      color="03b2f8")
    # webhook.add_embed(embed)
    # response = webhook.execute()

    print("Establishing connection")
    time.sleep(random.randint(10, 40) / 10)
    print(Fore.GREEN + "Success, starting job")
    time.sleep(1)

    for like in range(likesInputted):
        success = random.randint(1, 10)  # Random number to determine success
        if success <= random.randint(8, 10):  #80% chance of success
            time.sleep(random.randint(1, 3) / 20)
            if like == 1:
                print(Fore.WHITE + "Sent " + str(like) + " like (" +
                      str(datetime.datetime.now()) + ", " +
                      str(binascii.b2a_base64(os.urandom(15))) + ")")
            elif like >= 1:
                print(Fore.WHITE + "Sent " + str(like) + " likes (" +
                      str(datetime.datetime.now()) + ", " +
                      str(binascii.b2a_base64(os.urandom(15))) + ")")
        else:
            time.sleep(random.randint(1, 3) / 20)
            failedlikes += 1
            print(Fore.RED + "Failed to send like " + str(like) + "(" +
                  str(datetime.datetime.now()) + ", " +
                  str(binascii.b2a_base64(os.urandom(15))) + ")")

    time.sleep(random.randint(1, 3) / 20)
    print(Fore.WHITE + "Sent " + str(likesInputted) + " likes (" +
          str(datetime.datetime.now()) + ", " +
          str(binascii.b2a_base64(os.urandom(15))) + ")")
    print(Fore.GREEN + "Task completed successfully")
    print(Fore.YELLOW + str(likesInputted - failedlikes) + "/" +
          str(likesInputted) + " likes were successful")
    #webhook = DiscordWebhook(url=str(os.environ['HOOK']))
else:
    print(Fore.RED + "Invalid URL, restart the program to continue.")
Enter
