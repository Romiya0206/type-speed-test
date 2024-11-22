
# window.mainloop()
import tkinter as tk
import math

word_count= 0
wrong_word_count = 0
char_count= 0
restart_button = None

def highlight_next_word(event=None):
    global current_word_index, word_count, char_count, wrong_word_count
    current_word_index += 1

    words = text.get("1.0", "end-1c").split()

    if current_word_index < len(words):
        text.tag_remove("highlight", "1.0", tk.END)
        start_index = f"1.0 + {sum(len(word) + 1 for word in words[:current_word_index])} chars"
        end_index = f"{start_index} + {len(words[current_word_index])} chars"
        text.tag_add("highlight", start_index, end_index)
        text.tag_config("highlight", background="yellow")

        if words[current_word_index-1] == input.get().split(" ")[0]:

            word_count += 1
            char_count += len(words[current_word_index-1])
        else:
            wrong_word_count += 1
            char_count += len(input.get())

        word_input.delete(0, tk.END)
        word_input.insert(0, word_count)

        wrong_input.delete(0, tk.END)
        wrong_input.insert(0, wrong_word_count)

        char_input.delete(0, tk.END)
        char_input.insert(0, char_count)

    if current_word_index == len(words):
        pass

def clear_text(event=None):
    input.delete(0, tk.END)
    input.focus_set()


def combined_function(event=None):
    highlight_next_word()
    clear_text()


def timer(count= 20):
    global restart_button
    word_index = 0
    words = text.get("1.0", "end-1c").split()[0]

    if current_word_index == 0:
        start_index = f"1.0 + {sum(len(word) + 1 for word in words[:word_index])} chars"
        end_index = f"{start_index} + {len(words)} chars"
        text.tag_add("highlight", start_index, end_index)
        text.tag_config("highlight", background="yellow")


    time_in_mins = math.floor(count/60)
    time_in_sec= count % 60
    if time_in_sec < 10:
        time_in_sec = f"0{time_in_sec}"
    time_label.config(text=f"{time_in_mins}:{time_in_sec}")

    if count > 0:
        root.after(1000, timer, count-1)

    else:
        time_label.config(text="Time's Up!")
        input.config(state=tk.DISABLED)
        button.config(state=tk.DISABLED)
        show_restart_button()

def show_restart_button():
    global restart_button
    restart_button = tk.Button(root, text="Start Again", command=start_again, font=("roboto", 10, "bold"))
    restart_button.grid(column=2, columnspan=2, row=6)

def start_again():
    global current_word_index, word_count, wrong_word_count, char_count, restart_button

    current_word_index = 0
    word_count = 0
    wrong_word_count = 0
    char_count = 0

    word_input.delete(0, tk.END)
    wrong_input.delete(0, tk.END)
    char_input.delete(0, tk.END)

    restart_button.config(state=tk.DISABLED)
    input.config(state=tk.NORMAL)
    button.config(state=tk.NORMAL)

    time_label.config(text="00:00")

    words = text.get("1.0", "end-1c").split()
    text.tag_remove("highlight", "1.0", tk.END)
    start_index = "1.0"
    end_index = f"{start_index} + {len(words[0])} chars"
    text.tag_add("highlight", start_index, end_index)
    text.tag_config("highlight", background="yellow")

    input.delete(0, tk.END)
    input.focus_set()

    timer(20)

# Initialize the main window
root = tk.Tk()
root.config(padx=30, pady=30)
root.title("Highlight Words")


# Create Timer Label
time_label = tk.Label(root, text="00:00", font=("roboto", 25, "bold"))
time_label.grid(column=0, columnspan=6, row=0)

# Create word count label
word_label = tk.Label(root, text="Correct Words:", padx=10, pady=10)
word_label.grid(column=0, row=1)

word_input = tk.Entry(root)
word_input.grid(column=1, row=1)


wrong_label = tk.Label(root, text="Wrong Words:", padx=10, pady=10)
wrong_label.grid(column=2, row=1)

wrong_input = tk.Entry(root)
wrong_input.grid(column=3, row=1)

char_label = tk.Label(root, text="Character Count:", padx=10, pady=10)
char_label.grid(column=4, row=1)

char_input = tk.Entry(root)
char_input.grid(column=5, row=1)

# Create a Text widget
text = tk.Text(root, wrap="word", padx=10, pady=10)
text.grid(column= 0, columnspan= 6, row=2)
text.insert("1.0", "Technology has revolutionized the way we live, work, and communicate. Over the past few decades, advancements in digital tools and the internet have connected people across the globe in ways that were once unimaginable. From remote work to online education, the possibilities are endless. However, with these opportunities come challenges, such as the need for digital literacy and concerns over privacy and cybersecurity. As we continue to innovate, it's crucial that we balance the benefits of technology with the responsibility of ensuring it is used ethically and inclusively for the greater good.")

# Initialize the current word index
current_word_index = 0

# Create a Entry Box
input = tk.Entry(root, width=80)
input.grid(column=0, columnspan=6, row=3)
input.focus_set()

# Create a Button to trigger the highlight function
button = tk.Button(root, text="Start", command=timer, font=("roboto", 10, "bold"))
button.grid(column=2, columnspan= 2, row=4)


# Using space bar to call the function
root.bind("<space>", combined_function)

# Run the Tkinter event loop
root.mainloop()