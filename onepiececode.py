#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import gdown
import urllib.request
import os

class FirstGuiApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.label1 = tk.Label(self.toplevel1)
        self.label1.configure(font="{ariel} 20 {bold}", text="ONE PIECE")
        self.label1.grid(column=0, row=0)
        self.control = tk.Frame(self.toplevel1)
        self.episode = tk.Label(self.control)
        self.episode.configure(text="from episode")
        self.episode.grid(column=0, row=0)
        self.label3 = tk.Label(self.control)
        self.label3.configure(text="to episode\n")
        self.label3.grid(column=0, row=1)
        self.FROM_EPISODE = tk.Entry(self.control)
        self.FROM_EPISODE.grid(column=1, row=0)
        self.TO_EPISODE = tk.Entry(self.control)
        self.TO_EPISODE.grid(column=1, row=1)
        self.label4 = tk.Label(self.control)
        self.label4.configure(text="Select download directory")
        self.label4.grid(column=0, row=2)
        self.path_chooser_button = tk.Button(self.control, text="Browse", command=self.choose_directory)
        self.path_chooser_button.grid(column=1, row=2)
        self.file_path_label = tk.Label(self.control, text="")
        self.file_path_label.grid(column=2, row=2)
        self.control.configure(height=200, width=200)
        self.control.grid(column=0, row=1)
        self.download = tk.Button(self.toplevel1)
        self.download.configure(compound="top", justify="left", text="download\n")
        self.download.grid(column=0, row=3)
        self.download.configure(command=self.on_press_start_download)
        self.combobox1 = ttk.Combobox(self.toplevel1)
        self.combobox1.configure(values=["one piece", "dragon ball Z", "dragon ball GT"])
        self.combobox1.grid(column=0, row=2)
        self.label2 = ttk.Label(self.toplevel1)
        self.label2.configure(
            text="one piece 1-1000\ndragon ball z 1-291\ndragon ball gt 1-64"
        )
        self.label2.grid(column=0, row=4)
        self.toplevel1.configure(background="#ff4642", cursor="pirate")
        self.toplevel1.geometry("800x600")
        self.toplevel1.resizable(True, True)
        self.toplevel1.title("one piece bot")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def on_press_start_download(self):
        try:
            to = int(self.TO_EPISODE.get())
            fro = int(self.FROM_EPISODE.get())
            out = self.file_path_label["text"]
            sidra = self.combobox1.get()
            temp_url = "https://animeisrael.website/watch/fulllink/xx/fulllinkxx-*.php"
            if sidra == "one piece":
                temp_url = temp_url.replace('xx', "op")
            elif sidra == "dragon ball Z":
                temp_url = temp_url.replace('xx', "dbz")
            else:
                temp_url = temp_url.replace('xx', "dbgt")
            for i in range(fro, to + 1):
                url = temp_url.replace('*', str(i))
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                html = str(urllib.request.urlopen(req).read())
                templine = '<iframe class="embed-responsive-item" scrolling="no" src="https://drive.google.com/file/d/'
                stringstart = html.find(templine)
                stringend = stringstart + len(templine)
                id = html[stringend:stringend + 33]
                output = os.path.join(out, f'{sidra}_{i}.mp4')
                gdown.download(id=id, output=output, quiet=False, use_cookies=False)
            tk.messagebox.showinfo("Download Complete", "Episodes downloaded successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def choose_directory(self):
        directory = filedialog.askdirectory()
        self.file_path_label["text"] = directory


if __name__ == "__main__":
    app = FirstGuiApp()
    app.run()
