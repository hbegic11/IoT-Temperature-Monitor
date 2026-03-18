import serial
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "OVDJE_STAVI_SVOJ_TOKEN"
CHAT_ID = 0  # Ovdje upišite svoj Chat ID

# Inicijalizacija Arduina
try:
    arduino = serial.Serial('COM9', 9600, timeout=1)
except Exception as e:
    print(f"Greška: Ne mogu otvoriti COM9 port! ({e})")

trenutna_temp = 0.0
upozorenje_poslano = False

async def temp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Odgovara na /temp koristeći zadnju očitanu vrijednost."""
    await update.message.reply_text(f"🌡 Trenutna temperatura: {trenutna_temp:.1f} °C")

async def check_temperature_job(context: ContextTypes.DEFAULT_TYPE):
    """Funkcija koju JobQueue pokreće periodično."""
    global trenutna_temp, upozorenje_poslano
    
    try:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode().strip()
            if line:
                trenutna_temp = float(line)
                print(f"Trenutna temperatura: {trenutna_temp:.1f} °C")

                
                if trenutna_temp > 25.0:
                    if not upozorenje_poslano:
                        await context.bot.send_message(chat_id=CHAT_ID, 
                                                     text=f"⚠ Upozorenje! Temperatura je {trenutna_temp:.1f} °C")
                        upozorenje_poslano = True
                else:
                    upozorenje_poslano = False
    except Exception as e:
        print(f"Greška u čitanju senzora: {e}")

def main():
    # Build aplikacije
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("temp", temp_command))

    job_queue = app.job_queue
    job_queue.run_repeating(check_temperature_job, interval=1.0, first=1.0)

    print("Bot je pokrenut! Čekam podatke s Arduina...")
    
    app.run_polling()

if __name__ == "__main__":
    main()