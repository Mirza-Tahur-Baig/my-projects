from plyer import notification
import time
from playsound import playsound
def notifyMe(title,message,app_icon):
    notification.notify(
        title = title,
        message = message,
        app_icon = app_icon,
       
        timeout = 10,
    )

if __name__ == '__main__':
    playsound = "piece-of-cake-611.mp3"
    notifyMe("EXERCISE TIME", "Dear User, Start Your Day With Some Exercise",'exercise.ico')
    time.sleep(12)
    notifyMe("TAKE YOUR MEDICINE","Hey User, It's time for your medicine","medicine.ico")
    time.sleep(12)
    notifyMe("GO TO YOUR OFFICE","Hello User, Today you have a meeting in your Office","office.ico")
    