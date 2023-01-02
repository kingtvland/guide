# # BOT_TOKEN = '5880981869:AAGrRMEyP-Ty_KjwmjFOTh_qw5-VMiYvp2o'

# # Replace these with your own values
# api_id = 1909484
# api_hash = 'cc35d89e519babd93edee46b5292ab10'
# TOKEN = '5880981869:AAGrRMEyP-Ty_KjwmjFOTh_qw5-VMiYvp2o'
# destination_channel_username = 'NETFLY'
import os
import telegram
TOKEN = '5880981869:AAGrRMEyP-Ty_KjwmjFOTh_qw5-VMiYvp2o'
#
# Replace TOKEN with your bot's API token
bot = telegram.Bot(token=TOKEN)

# Replace CHAT_ID with the chat ID of the private channel where you want to forward the MKV files
CHAT_ID = '-1001507128390'

# Replace WEBHOOK_URL with the URL of your webhook
WEBHOOK_URL = WEBHOOK_URL

# Set the webhook for the bot
bot.set_webhook(WEBHOOK_URL)

def search_for_mkv_files():
    # Get a list of chats that the bot is a member of
    chats = bot.get_chats()
    for chat in chats:
        # Check if the chat is a group
        if chat.type == 'group':
            # Get a list of messages from the group
            messages = bot.get_history(chat_id=chat.id)
            for message in messages:
                # Check if the message has a file attached
                if message.document:
                    # Check if the file is an MKV file
                    if message.document.mime_type == 'video/x-matroska':
                        # Forward the message to the private channel
                        bot.forward_message(chat_id=CHAT_ID, from_chat_id=chat.id, message_id=message.message_id)

def join_group(update, context):
    # Get the group invite link from the command arguments
    invite_link = context.args[0]

    # Use the join_chat method to join the group
    bot.join_chat(invite_link)

def main():
    # Set up the webhook handler
    update_queue = telegram.ext.Queue()
    updater = telegram.ext.Dispatcher(bot, update_queue)

    # Add a command handler for the "/search" command
    updater.add_handler(telegram.ext.CommandHandler("search", search_for_mkv_files))

    # Add a command handler for the "/join" command
    updater.add_handler(telegram.ext.CommandHandler("join", join_group))

    # Start the webhook server
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.set_webhook(WEBHOOK_URL + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
