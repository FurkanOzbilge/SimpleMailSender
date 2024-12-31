import tkinter as tk
import time
import smtplib
from email.message import EmailMessage

# -------------------------
EmailSender_EMail="example@gmail.com"
EmailSender_Email_password="mypassword123"
# -------------------------

window = tk.Tk()
window.geometry("800x600")
window.resizable(False,False)
window.title("SimpleMailSender")
window.iconbitmap("mail.ico")

def SendEmail(subject, msg, mail):
    msg = EmailMessage()
    msg.set_content(subject)
    msg['subject'] = subject
    msg['to'] = mail

    user = EmailSender_EMail
    msg['from'] = user
    password = EmailSender_Email_password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def ButtonCommand():
    mail = MailReceiver()
    content = ContentReceiver()
    subject = SubjectReceiver()
    ReplyBox = tk.Label(window, background="black", font=("Arial", 12, "bold"), fg="white", text="")
    if mail != "" and content != "" and len(content) >= 1:
        SendEmail(subject, content, mail)
        ReplyBox.config(background="#73fc03", text="Email Sent Successfully!")
        window.after(3000, lambda: ReplyBox.destroy())
    else:
        ReplyBox.config(background="red", text="Email Failed to Send!")
        window.after(3000, lambda: ReplyBox.destroy())

    ReplyBox.place(x=10, y=330)

def MailReceiver():
    mail = entry_mailAddress.get()
    return mail   

def ContentReceiver():
    content = text_area.get("1.0","end-1c")
    return content

def SubjectReceiver():
    subject = entry_Subject.get()
    return subject   

# Entry Label
entry_label = tk.Label(window, text="Mail Address", fg="black", font=("Arial", 15))
entry_label.place(x=10,y=15)

# Entry 
entry_mailAddress = tk.Entry(window, borderwidth=2, width=28, font=("Arial", 14)) 
entry_mailAddress.place(x=10, y=40)  

# Subject Label
entry_label = tk.Label(window, text="Subject", fg="black", font=("Arial", 15))
entry_label.place(x=10,y=70)

# Subject
entry_Subject = tk.Entry(window, borderwidth=2, width=28, font=("Arial", 14))
entry_Subject.place(x=10, y=95)  

# Button widget
button = tk.Button(window, text="Send", command=ButtonCommand, background="#0384fc", font=("Arial", 12, "bold"), fg="white",)
button.place(x=350, y=50, width=75, height=40)  

# Text widget
text_area = tk.Text(window, height=10, width=50, font=("Arial", 12), borderwidth=2)
text_area.place(x=10, y=140) 

window.mainloop()
