def gui_func():

    import tkinter as tk
    import json
    from datetime import timedelta

    # Load JSON data
    with open("player_stats.json", "r") as file:
        data = json.load(file)

    # Create Tkinter root window
    root = tk.Tk()
    root.title("Readable JSON Viewer")

    # Create a Text widget
    text_widget = tk.Text(root, wrap="word", width=50, height=20)
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
    formatted_data = ""

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

    root.mainloop()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    gui_func()