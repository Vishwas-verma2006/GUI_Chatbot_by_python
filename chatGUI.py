from backend import get_response   
import PySimpleGUI as sg

sg.theme("Darkblue3")


USER_COLOR = "#0078D7"
BOT_COLOR = "#3C3C3C"
FONT = ("Segoe UI", 11)


layout = [ [sg.Text("🤖 CHATBOT",font=('Helvicate', 18, "bold"),text_color="blue" ,pad=((5,5),(10,10)),justification='center', expand_x=True )],
           [sg.Multiline(size=(60,15), key= 'chat',disabled=True, autoscroll=True,
            font=FONT,
            background_color="#1E1E1E",
            text_color="white",
            no_scrollbar=False,
            pad=(5, 5)) 
            ],

           [sg.InputText(key="user", size=(45,1),
            font=FONT,
            background_color="#2D2D2D",
            text_color="white",
            border_width=1,
            focus=True), 
            sg.Button("Send",bind_return_key=True), sg.Button("Exit")]
]

win = sg.Window("Chatbot with GUI", layout, finalize=True, element_justification='center' ,resizable=True)

chat_history = ''

while True:
    event ,value = win.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    elif event == "Send":
        message = value['user']
        if message:
            chat_history += f"You: {message}\n"

        win['chat'].update(chat_history + "🤖 Chatbot Typing.... \n")
        win.refresh()

        try:
            bot = get_response(message)
        except Exception as e:
            print(f"Error:- {e}")

        chat_history += f"\nChatbot: {bot}\n\n"
        win['chat'].update(chat_history)
        win['user'].update("")

    else:
        sg.popup("Please enter a prompt !")


