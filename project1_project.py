import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler ,filters
import cv2

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('imagetelegram.jpg','rb'),caption='✅تصویر مورد نظر شما ارسال شد')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="hii")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("good")

async def bot1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        text=update.message.text
        print(text)

        if text=="hello":
             
         await update.message.reply_text("bot1 is started")
       
async def ax1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(update.message)
    photo=await update.message.photo[-1].get_file()
    await photo.download_to_drive('image1.jpg')

    #await update.message.reply_text("عکس شما دریافت شد")
    img1=cv2.imread('image1.jpg')
    face_model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    face=face_model.detectMultiScale(gray)
    x=face[0][0]
    y=face[0][1]
    x2=x+face[0][2]
    y2=y+face[0][3]
    out1=cv2.rectangle(img1,(x,y),(x2,y2),(0,250,0),3)
    cv2.imwrite('imagetelegram.jpg', out1)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('imagetelegram.jpg','rb'),caption='✅تصویر مورد نظر شما ارسال شد')

    



    


#if __name__ == '__main__':
application = ApplicationBuilder().token('6513183712:AAHGJ502RF5a2yT4etFrpfOUblYxYjMUDSU').build()
    
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
start_handler = CommandHandler('test', test)
application.add_handler(start_handler)

new_handler=MessageHandler(filters=filters.TEXT, callback=bot1 )
application.add_handler(new_handler)

ax1_handler=MessageHandler(filters=filters.PHOTO, callback=ax1 )
application.add_handler(ax1_handler)

    
    
application.run_polling()