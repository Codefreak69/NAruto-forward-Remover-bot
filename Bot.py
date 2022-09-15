from telegram.ext import Filters,Updater,MessageHandler,CommandHandler
import os


#Bot Token

token = "5719383526:AAETSEbKSYAQr3dXgYrArBWaLX5KadCUOaM"


#Start Message
def start_text(u,c):
    u.message.reply_text("StartMsg")

#Help Message
def help_text(u,c):
    u.message.reply_text("HelpTxt")


#Send document from user
def frwrd_file(u,c):
    u.message.reply_document(u.message.document.file_id)

#Send video from user
def frwrd_media(u,c):
    u.message.reply_video(u.message.video.file_id)

#Send photo from user
def frwrd_photo(u,c):
    u.message.reply_photo(u.message.photo[-1].file_id)

#Send text from user
def frwrd_text(u,c):
    u.message.reply_text(u.message.text)

#Send sticker from user
def frwrd_sticker(u,c):
    u.message.reply_sticker(u.message.sticker.file_id)

#Send voice from user
def frwrd_voice(u,c):
    u.message.reply_voice(u.message.voice.file_id)


updater = Updater(token,use_context=True)
dp = updater.dispatcher


#Filtering Commands

dp.add_handler(CommandHandler('start',start_text))

dp.add_handler(CommandHandler('help',help_text))



#Filtering Files
dp.add_handler(MessageHandler(Filters.document,frwrd_file))

#Filtering Media
dp.add_handler(MessageHandler(Filters.video,frwrd_media))

#Filtering Photos
dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

#Filtering Text
dp.add_handler(MessageHandler(Filters.text,frwrd_text))

#Filltering Stickers
dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

#Filtering Voice
dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))

updater.start_polling()

updater.idle()


