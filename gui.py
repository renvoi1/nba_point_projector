import tkinter as tk
import json
from datetime import timedelta

# Load JSON data
import tkinter.font as tkFont

# Create Tkinter root window
root = tk.Tk()
root.title("NBA Player Statistics Viewer")
formatted_data = ""

# Button to trigger the text retrieval

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a Text widget
text_widget = tk.Text(root, wrap="word", width=50, height=20, font=('Arial', 28))
text_widget.pack(padx=10, pady=10)

# Function to format milliseconds into "X days, HH:MM:SS"
def format_duration(milliseconds):
    try:
        # Convert milliseconds to seconds
        total_seconds = int(milliseconds) // 1000
        duration = timedelta(seconds=total_seconds)
        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if days > 0:
            return f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"
        else:
            return f"{hours:02}:{minutes:02}:{seconds:02}"
    except Exception as e:
        # Print the error and return the original value for debugging
        print(f"Error converting {milliseconds}: {e}")
        return f"Unrecognized format: {milliseconds}"

# Format JSON as key-value pairs with timestamp conversion


def print_stats():
    formatted_data = ""
    with open("player_stats.json", "r") as file:
        data = json.load(file)
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (str)):  # Likely to be a duration in milliseconds
                value = format_duration(value)
            formatted_data += f"{key}: {value}\n"
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, (int, float)):  # Likely to be a duration in milliseconds
                        value = format_duration(value)
                    formatted_data += f"{key}: {value}\n"
                formatted_data += "\n"  # Add a blank line between items
            else:
                formatted_data += f"{item}\n"
    # Insert formatted data into the Text widget
    text_widget.insert("1.0", formatted_data)

    # Disable editing (optional)
    text_widget.config(state="disabled")

def get_text():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    guy = entry.get()  # Get the text from the Entry widget
    from pointprojector import grab_stats
    grab_stats(guy2=guy)
    print_stats()
    text_widget.config(state=tk.DISABLED)

    
    

button = tk.Button(root, text="Retrieve Player Statistics", command=get_text)
button.pack(pady=10)

root.mainloop()