import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os 
#------------------------------------------------------------------------------------------

"""  colors  for   later   use"""

c1 = '#D7FF0E'
c2 = '#faa213'
c3 = '#1e282d'
c6 = '#577e75'

c4 = '#faa21f'
c5 = '#577e75'

c7 = '#1e282d'
c8 = '#faa21f'

# Alternative Chat Colours
'''
c4 = '#4790f9'
c5 = '#00a3cf'

c7 = '#85c0f6'
c8 = '#83e7f2'
'''

#-------------------------------------------------------------------------------------------

"""
getting data from entry of
    'Enter Name' page
"""

def info () :

    global myname
    myname = entry_user.get('1.0' , 'end-1c')
                                                                        
    global chatbot                           
    chatbot = entry_chat.get('1.0' , 'end-1c')
    
    if myname == "" or chatbot == "":
        Label(frame_info , text = "Fill both fields to proceed." , bg = "red" , fg = "white" , font = 'Verdana 11 bold').place( x = 182 , y = 96)
        return 

    entry_user.delete('1.0' , END)
    entry_chat.delete('1.0' , END)

    frame_info.pack_forget ()
    frame_topic.pack ()
    
#------------------------------------------------------------------------------------------

"""
opening files after selection of
        topic in topic selestion
                    page
"""

def topic_1():
    global no_topic
    no_topic = 1
    
    global top
    top = 'addmission1.txt'

    global a
    a = open( top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()    

    topic = 'Addmission'
    label_topic.config(text = topic)

    refresh_screen()
    
def topic_2():
    global no_topic
    no_topic = 2


    global top
    top = 'Academic.txt'
    a = open(top , 'r')


    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()

    topic = ' Academic  '
    label_topic.config(text = topic)

    refresh_screen()
            
def topic_3():
    global no_topic
    no_topic = 3

    global top
    top = 'eaxmination.txt'
    a = open(top , 'r')

    global doc
    doc = a.readlines()

    frame_topic.pack_forget ()
    frame_chat.pack()

    topic = 'Examination'
    label_topic.config(text = topic)

    refresh_screen()


#----------------------------------------------------------------------------------------------------------

"""
functions for writing in files
        for writing in files in chat screen

"""

def write_ans () :

    enter1 = entry_feed.get('1.0' , END)

    b.write(enter1)
    b.close()

    window.destroy()

    """           
        Reopening of files after
           changes are saved
    """

    if no_topic == 1 :
        topic_1()
    
    elif no_topic == 2 :
        topic_2()          
    
    elif no_topic == 3 :
        topic_3()
    
    
def feed_answer () :

    """
a seperate window for writing answer
            on file

    """

    global window
    window=Tk()

    frame_root = Frame(window , bg = c1)
    frame_root.pack()
                                                                                            
    label = Label (frame_root , text = 'Enter the answer of Question here ...' , bg = c1 , fg = 'white' )
    label.pack()

    global entry_feed
    entry_feed = Text (frame_root , height = 3 , width = 30 , fg = 'white' , bg = c2)
    entry_feed.bind ('<Return>' , write_ans)
    entry_feed.pack()

    button = Button (frame_root , text = 'Add answer' , command  = write_ans , bg = c3 , fg = 'white' )
    button.pack()
    
def write_file () :

    """
opening file for appending in
exsisting  files

    """

    global b
    b = open ( top , 'a')
    
    b.write(chat_raw)
    b.write('\n')

    button_write.place_forget()
    feed_answer ()

#----------------------------------------------------------------------------------------------

def refresh_screen () :

    for widget in frame_chats.winfo_children():
        widget.destroy()

    button_write.place_forget()
    label_space = Label (frame_chats , bg = c1 ,  text = '')
    label_space.pack()

#------------------------------------------------------------------------------------------

def submit() :

    """
function for producing response of
        request of user

    """

    button_write.place_forget ()
    global chat_raw
    chat_raw = entry.get('1.0' , 'end-1c')
                        
    entry.delete('1.0' , END)
    
    chat = chat_raw.lower()
    chat = chat.replace(' ','')

    global label_request
    label_request = Label(frame_chats ,text=chat_raw , bg = c4 , fg= c7  , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')
    
    label_request.pack(anchor = 'w')   
    
    global answer
    
    if chat == 'groupmembers' or chat == 'group' or chat=='whocreatedyou?' or chat == 'groupmember' :
          answer = "SUMIT KUMAR  \nANURAG KUMAR   \nNITIN CHAUHAN  \nISHAN"

    elif chat == "what'smyname?" or chat == "whatsmyname?" or chat == "whatismyname?" or chat == "whatsmyname" or chat == 'myname?' or chat =='myname' :
          answer = myname

    elif chat == "what'syourname?" or chat == "whatisyourname?" or chat == "whatsyourname?" or chat == "whatsyourname" or chat == 'yourname?' or chat =='yourname' :
          answer = chatbot

    elif chat == 'bye' or chat == 'goodbye' or chat == 'exit' or chat == 'close' or chat == 'end' :
          answer = 'Bye'
    elif chat == 'hi' or chat == 'Hi' or chat == 'hellow' or chat == 'hello' or chat == 'hey' :
          answer ='hi '+ myname+' !'+'\n !! Ask your quarry !!'

    else:
        i = 0
        j = 0
        for lines in doc:
            stats = lines [:-1]
            stats = stats.lower()
            stat = stats.replace(' ','')
            i += 1
            if stat == chat :
                answer = doc[i]
                break
            else:
                 j += 1
                 
        if i == j :
            
            answer = "I don't understand.........please teach me ! "
            button_write.place(x=430,y=3)

    get_response()
        
def get_response() :

    global label_response
    label_response = Label(frame_chats ,text= answer ,bg= c5 , fg = c8 , justify = LEFT , wraplength = 300, font = 'Verdana 10 bold')

    label_response.pack(anchor = 'e')

    if answer ==  'Bye':
        root.destroy()


#------------------------------------------------------------------------------------------------------------------

"""

moving from one page to another
    by help of button

"""

def welcome_to_info ():
    frame_welcome.pack_forget ()
    frame_info.pack ()
    
def info_to_topic ():
    frame_info.pack_forget ()
    frame_topic.pack ()

def topic_to_chat ():
    frame_topic.pack_forget ()
    frame_chat.pack()

def chat_to_topic ():
    frame_chat.pack_forget ()
    frame_topic.pack ()

def topic_to_info ():
    frame_topic.pack_forget ()
    frame_info.pack ()

def info_to_welcome ():
    frame_info.pack_forget ()
    frame_welcome.pack ()

#-----------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
"""
calling constructor to make window

"""

root = Tk ()  

#----------------------------------------------------------------------------------------------------

"""  images used in window  """

back = PhotoImage(file = 'arrow_behind.png')

front = PhotoImage(file = 'arrow_ahead.png')

exitt = PhotoImage(file = 'exit.png')

screen_1 = PhotoImage(file = 'image_5.png')

submit_img = PhotoImage(file = 'image_8.png')

#---------------------------------------------------------------------------------------------------------------------

"""     WELCOME FRAME    """
"""    first frame containing time date and welcome messages """

frame_welcome = Frame (root , bg ='#EBECE1' , height = '670' , width = '550')
frame_welcome.pack_propagate(0)
frame_welcome.pack()  


imageframe=Frame(frame_welcome, bg ='green' , height = '270' , width = '250')
imageframe.place(x=150,y=100)

file = 'chatbot.png'

image = Image.open(file)

zoom = 0.4

#multiple image size by zoom
pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
label = Label(imageframe, image=img)
label.image = img
label.pack()
  
welcome = Label (frame_welcome , text = '!Welcome!' , font = "Vardana 50 bold" , bg = 'black' , fg = "white")
welcome.place(x = 110 , y = 400)

welcome_chatbot = Label (frame_welcome , text = '--College Enquiry ChatBot-- ' , font = "Helvetica 20 bold" , bg ='#FAE078' , fg ='#990000')
welcome_chatbot.place(x = 105 , y =50)
button_front = Button (frame_welcome , image = front , relief = "flat" , bg = c1 , bd = "3px solid black" , command = welcome_to_info ).place(x=250 , y=500)



"""     INFO FRAME   """
"""     frame of entering names    """

frame_info = Frame (root , bg = 'gray' , height = '670' , width = '550')
frame_info.pack_propagate(0)

spacer1 = Label(frame_info , bg = c1)
spacer1.pack()

spacer2 = Label(frame_info , bg = c1)
spacer2.pack()

label_sub = Label (frame_info ,text = "Enter Information" , bg = "light blue" , fg = "black" , font = 'Verdana 20 bold')
label_sub.pack()
                            
user_name = Label (frame_info , text = 'Enter your name : ' , bg = 'black' , fg = 'yellow' , font = 'Ariel 15 bold')
user_name.place(x = 80,y=130)

entry_user = Text (frame_info , bg ="white", fg = "black" , height ='1'  , width ='40' , font = 'Ariel 15 ')
entry_user.focus()
entry_user.place(x = 80 , y = 170)

chatbot_name = Label (frame_info , text = 'Give Chatbot a Name : ' , bg = 'black' , fg = 'yellow' , font = 'Ariel 15 bold')
chatbot_name.place(x = 80 , y = 220)

entry_chat = Text (frame_info , bg ="white", fg = "black" , height ='1'  , width ='40' , font = 'Ariel 15')
entry_chat.place(x = 80 , y = 260)

button_1 = Button (frame_info , text ='submit' , font = 'Vardana 10 bold' , bg = 'green' , fg = 'white' , command = info )
button_1.place(x = 470 , y = 330)

button_back = Button (frame_info , image =  back , relief = "flat" , bg = 'light yellow' , command = info_to_welcome).place(x=10 , y = 10)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root.title("chatterbot") 
"""     TOPIC FRAME   """
""""   frame for topic selection     """

frame_topic = Frame (root , bg = c1 , height = '670' , width = '550')
frame_topic.pack_propagate(0)
                            
spacer3 = Label(frame_topic , bg = c1)
spacer3.pack()

spacer4 = Label(frame_topic , bg = c1)
spacer4.pack()

select_label = Label (frame_topic , text = "Select Topic" , bg = 'red' , fg = "white" , font = 'Ariel 20 bold ')
select_label.pack()

spacer5 = Label(frame_topic , bg = c1)
spacer5.pack()

option_1 = Label (frame_topic , text = '1- Addmission' , font = 'Verdana 15 bold' ,bg = 'black' , fg= c2)
option_1.place(x = 30 , y = 120)

button_opt_1 = Button (frame_topic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 ,command = topic_1)
button_opt_1.place(x = 350 , y = 120)

option_2 = Label (frame_topic , text = '2- Academic' , font = 'Verdana 15 bold' ,bg = 'black' , fg= c2)
option_2.place(x = 30 , y = 160)

button_opt_2 = Button (frame_topic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 , command = topic_2)
button_opt_2.place(x = 350 , y = 160)

option_3 = Label (frame_topic , text = '3-  Eaxmination ' , font = 'Verdana 15 bold' ,bg = 'black' , fg= c2)
option_3.place(x=30 , y = 200)

button_opt_3 = Button (frame_topic , text = 'Proceed' , image = front , relief = "flat" , bg = c1 , command = topic_3)
button_opt_3.place(x = 350 , y = 200)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""         CHAT FRAME   """
""""       main chat screen   """

frame_chat = Frame (root , bg = 'light green' , height = '670' , width = '550')
frame_chat.pack_propagate(0)

frame_top = Frame( frame_chat , bg = c3 , height = '100' , width = '550')
frame_top.pack()

label_topic = Label ( frame_top , bg = c3 , fg = 'white' , font = 'Verdana 20 bold ')
label_topic.pack(pady = '40')

frame_spacer = Frame( frame_top , bg = c2 , height = "10" , width = "550" )
frame_spacer.pack()

bottom_frame = Frame (frame_chat , bg = c2 , height = '100' , width = '550')
bottom_frame.pack_propagate(0)
bottom_frame.pack(side = BOTTOM)

button = Button (bottom_frame , image = submit_img , relief = "flat", font = 'Vardana 10 bold' , bg = c3 , command = submit )
button.place(x = 410 , y = 27)
                                   
entry = Text (bottom_frame , bg = "white" , fg = c6 , height = '5'  , width ='45' , font  ='Verdana 10')
entry.bind ('<Return>' , submit)
entry.place(x = 30, y = 10)

frame_chats = Frame (frame_chat , bg = 'light green' , height = '450' , width = '500' )
frame_chats.pack_propagate (0)
frame_chats.pack()


label_space = Label(frame_chats , bg =  'light green').pack()

button_refresh = Button (frame_chat , bg = c3 , fg = c2 ,  text = 'refresh' , font = 'Vardana 10 bold' ,  command =refresh_screen)
button_refresh.place(x = 440 , y = 80)

button_write = Button (bottom_frame , text = 'write' ,bg = c3 ,fg = c2 , font = 'Vardana 8' ,  command = write_file )

button_back = Button (frame_chat , image = back , relief = "flat" , bg = c3 , command = chat_to_topic).place(x=10 , y = 10)
button_front = Button (frame_chat , image = exitt , relief = "flat" , bg = c3 , command = root.destroy ).place(x=440 , y = 10)

#-----------------------------------------------------------------------------------------------------------

root.mainloop ()
"""    END OF CODE   """
