#import tkinter as tk

#window = tk.Tk()
#window.title("My ChatBot")
#label = tk.Label(window, text="Hello! I am your ChatBot.")
#label.pack(padx=20, pady=20)
#window.mainloop()

import tkinter as tk

def get_reply(message):
    message = message.lower().strip()

    if message == "bye":
        return "Goodbye!"
    elif message == "hi" or message == "hello":
        return "Hello there!"
    elif "how are you" in message:
        return "I am just code, but I feel great!"
    elif "name" in message:
        return "I am ChatBot!"
    elif "time" in message:
        return "You can check the current time."
    elif "weather" in message:
        return "Please check your weather app."
    elif "joke" in message:
        return "Why did the programmer quit? Because they didn't get arrays!"
    elif "food" in message:
        return "I like talking about delicious food!"
    elif "help" in message:
        return "Ask me about my name, time, weather, jokes, or food."
    elif "thank you" in message:
        return "You're welcome!"
    else:
        return "I am not sure how to answer that yet."


def send_message():
    message = entry.get().strip()

    if message:
        chat_area.insert(tk.END, "You: " + message + "\n")
        reply = get_reply(message)
        chat_area.insert(tk.END, "ChatBot: " + reply + "\n\n")
        entry.delete(0, tk.END)

window = tk.Tk()
window.title("My ChatBot")
window.geometry("500x500")
window.configure(bg="lightblue")

chat_area = tk.Text(window, height=18, width=50,font=("Arial", 11),bg="white")
chat_area.pack(padx=15, pady=15)

entry = tk.Entry(window, width=35,font=("Arial", 12))
entry.pack(padx=10, pady=5)

send_button = tk.Button(
    window,
    text="Send",
    command=send_message
)
send_button.pack(pady=5)

window.mainloop()