from tkinter import *
import ctypes
import random
import tkinter

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title('Typing Speed Test')

root.geometry('1000x400')

root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "sans-serif 20")


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            labelRight.configure(text=labelRight.cget('text')[1:])
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    possibleTexts = [
        'In a certain village lived a farmer and his only son. The SON was a thief who goes about stealing from peoples homes. He continued this wicked lifestyle till the day his cup got filled. He stole heavy some of money from the richest man in their village, that day he didn’t escape successfully as he used to. The farmer involved the police immediately he found out that his money was missing and the police started investigating, and finally they found out that the boy stole the money so they sent him to prison.',
        'After some months, it was time for farming and the farmer was already old and weak and cant dig the ground anymore so the old farmer wrote this letter to his son in prison. "Son, this year I will not plant cassava and yam because I cannot dig the field, I know if you were here you would have helped me. The son was really touched by his father is letter so he thought a plan, and replied his father. Dad do not even think of digging the field because that is where I buried the money I stole. The POLICEMEN on reading this letter went early in the morning and dug the whole field in search of the money but nothing was found.',
        'The son was really touched by his fathers letter so he thought a plan, and replied his father "Dad do not even think of digging the field because that is where I buried the money I stole. The POLICEMEN on reading this letter went early in the morning and dug the whole field in search of the money but nothing was found.',
        'The schoolboy squirmed. Another two minutes? He knew he should stand at attention. The drillmaster cane loomed large."Vindhya Himachal …"He grunted in discomfort. This was unbearable. He considered making a dash; after all he was in the last row. What if the master noticed? The cane loomed again. He gritted his teeth."Tava shubha …"This is it. He cast his eyes around."Jaya he …"He started running."Jaya he …"He was almost there."Jaya he …"The chorus floated from afar. He was already in the toilet, heaving a relieved sigh.',
        'On a windy winter morning, a woman looked out of the window.The only thing she saw, a garden. A smile spread across her face as she spotted Maria, her daughter, in the middle of the garden enjoying the weather. It started drizzling. Maria started dancing joyfully.She tried to wave to her daughter, but her elbow was stuck, her arm hurt, her smile turned upside down. Reality came crashing down as the drizzle turned into a storm. Marias murdered corpse consumed her mind.On a windy winter morning, a woman looked out of the window of her jail cell.',
        'The country was on fire. Communal riots had paralyzed most of the state. Reyaz, with the help of a friend, got a fake identity card--his new name was Rakesh--and booked a ticket to Aligarh. The ticket checker on the train asked for his identification--Reyaz nervously showed the one he had recently procured. He seemed satisfied and Reyaz heaved a sigh of relief.At Aligarh there was none to fear. "Assalamu alaikum," said Reyaz to ward off a group of enraged people. The angriest of them, with bloodshot eyes, approached Reyaz and asked for his identity card.',
        'She peered over the open magazine, and there he was, still staring at her, disconcertingly. For the past 30 minutes, she wouldd endured his irritating attention. Time to call airport security. The burly cop strode in purposefully, with a sleek Alsatian on leash. "Sir, there is been a complaint. I need you to come with me. Quietly, please, he growled. The leather-jacketed man didnt move a muscle. His hands were rock-steady on the trolley handle in front of him. The cop waited for a minute, and then reached out to handcuff the Ray-Ban-wearing guy. The hands were locked in rigor mortis.',
        '"Do you believe in shooting stars?" she asked."Do you?""There is no harm, is there?" She paused. "I wouldd love to sit in the balcony amidst all the flowerpots and watch the busy world go by."He said nothing. She needed no assurance, no promise. She squawked a reply when they asked if she was ready to go back to her room. It would be another 10 minutes before the duty nurse wheeled him away.She had laughed at the last tooth he had lost. He had teased her about the silver hair at the back of her sweater.',
        'Hearing a knock on the door,  she hustled towards it with her  little feet, her lips uncloaking the cutest smile and her voice singing, "Daddy is home!" Her mum, glued to the news channels for the past week, approached the door hesitantly and opened it with trepidation.Two men in military uniform were standing at the doorstep. One of them handed her an envelope with a mournful expression, adding plaintively, "We are sorry, Mrs Bhatt.""Where is my dad, Uncle? He promised well celebrate Diwali together this time," exclaimed the girl. They stared helplessly, with a lump in their throats and moistened eyes.',
        'They met at a cafe, stealing glances at each other while the parents  spoke animatedly.They remained silent throughout, only exchanging shy smiles while ordering snacks at the counter.Returning with the food, he moved to the head of the table to get a good look at her.Noticing his manoeuvre, she smiled down at her coffee, making him beam like a proud schoolboy.When the two families parted at the end of the meeting, he rushed back to the cafe, praying that the girl, who had been at the table behind theirs all afternoon, would still be there.'
    ]
    text = random.choice(possibleTexts).lower()
    splitPoint = 0
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='green')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False
    
    amountWords = len(labelLeft.cget('text').split(' '))
    
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global ResultLabel
    ResultLabel = Label(root, text=f'WPM: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    global ResultButton
    ResultButton = Button(root, text=f'RETRY', bg = 'grey',command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    ResultLabel.destroy()
    ResultButton.destroy()

    resetWritingLabels()

def addSecond():

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    if writeAble:
        root.after(1000, addSecond)

resetWritingLabels()

root.mainloop()