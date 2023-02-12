import requests
import time
import tkinter as tk
import threading
from tkinter import PhotoImage

#Set timeout and number of bots - THERE IS A 120s COOLDOWN BEFORE YOU CAN WRITE THE NEXT COMMNAND
TIMEOUT= 130

#Number of bots actually depends on your rank in the PHTS server (you can get from 50 to 1000 bots)
BOTS= 100


# ================== TO EDIT:  ===================

#THIS LINK LEADS TO THE 'COMMANDS' ROOM ON THE PHTS SERVER (THIS LINK SHOULD BE THE SAME)
MESSAGES_ID= "https://discord.com/api/v9/channels/959820125912043582/messages"

#HOW TO GET THE AUTHORIZATION TOKEN TUTORIAL IS IN THE /how_to_use/ FOLDER
AUTHORIZATION= ''





# ================= CODE (DONT EDIT) =================

def send_message():
    TTV_USERNAME = username_entry.get()
    payload = {
        'content': f".follow {TTV_USERNAME}"
    }

    header = {
        'authorization': AUTHORIZATION
    }

    def post_request():
        total_bots = 0
        while True:
            total_bots += 1
            # Send API request
            r = requests.post(MESSAGES_ID, data=payload, headers=header)
            # Update console output with Discord and stream information
            infos_output.config(fg='#3D8EFD')
            infos_output.tag_config("value", foreground="cyan")
            infos_output.insert(tk.END, "=== Discord ids ===\n")
            infos_output.insert(tk.END, "Discord link (09.02.23):\n")
            infos_output.insert(tk.END, f"https://discord.gg/phts\n\n", 'value')
            infos_output.insert(tk.END, f"MESSAGES_ID: ")
            infos_output.insert(tk.END, f"{MESSAGES_ID}\n\n", 'value')
            infos_output.insert(tk.END, f"AUTHORIZATION: ")
            infos_output.insert(tk.END, f"{AUTHORIZATION}\n\n", 'value')
            #infos_output.insert(tk.END, "===========================================\n", ('green'))
            infos_output.insert(tk.END, "=== Stream ids ===\n")
            infos_output.insert(tk.END, f"Stream url: ")
            infos_output.insert(tk.END, f"https://www.twitch.tv/{TTV_USERNAME.lower()}\n", 'value')
            infos_output.insert(tk.END, f"TIMEOUT: ")
            infos_output.insert(tk.END, f"{TIMEOUT}\n", 'value')
            infos_output.insert(tk.END, f"NUMBER OF BOTS: ")
            infos_output.insert(tk.END, f"{BOTS}\n", 'value')
            infos_output.insert(tk.END, f"Total bots sent: ")
            infos_output.insert(tk.END, f"{total_bots * BOTS}\n", 'value')
            #infos_output.insert(tk.END, f"CURRENT FOLLOWERS: {curr_followers}\n")
            infos_output.see(tk.END)
            for i in range(TIMEOUT, 0, -1):
                timeout_output.config(fg='#3D8EFD')
                timeout_output.insert(tk.END, str(i) + "...\n")
                timeout_output.see(tk.END)
                time.sleep(1)
    t = threading.Thread(target=post_request)
    t.start()

def end_program():
    root.quit()


#ROOT
root = tk.Tk()
root.title("LOLIBOT V3")


#WINDOW SETUP
username_label = tk.Label(root, text="TTV USERNAME:", bg='black', fg='cyan')
username_entry = tk.Entry(root)

#BUTTONS
send_button = tk.Button(root, text="SEND", command=send_message, bg='black', fg='cyan')
end_button = tk.Button(root, text="END", command=end_program, bg='black', fg='cyan')

#CONSOLE OUTPUT 1
infos_output = tk.Text(root, height=16, width=50, bg='black')

#CONSOLE OUTPUT 2
timeout_output = tk.Text(root, height=4, width=50, bg='black')

#BG IMG
image = PhotoImage(file="lolibotig.png")
background_label2 = tk.Label(root, image=image)
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
background_label2.lower()

#WINDOW PACK
username_label.pack()
username_entry.pack()
send_button.pack()
end_button.pack()
infos_output.pack()
timeout_output.pack()

#RUN
root.geometry("700x500")
root.resizable(False, False)
root.mainloop()