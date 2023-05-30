import tkinter as tk
from tkinter import filedialog
import log_analyzer
from tkinter import messagebox
from datetime import datetime


class LogViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Log Browser")
        self.geometry("1000x600")

        self.logList = []
        self.logRawList = []
        self.selectedLog = None
        self.LIST_const = []
        self.LIST_RAW_const = []

        # create the widgets
        self.fileFrame = tk.Frame(self)
        self.logFrame = tk.Frame(self)
        self.detailFrame = tk.Frame(self)

        self.loadBtn = tk.Button(self.fileFrame, text="Load File", command=self.load_file)


        self.logListbox = tk.Listbox(self.logFrame)
        self.logListbox.bind("<<ListboxSelect>>", self.mouse_click)

        self.filterStartLabel = tk.Label(self.fileFrame, text="From")
        self.filterStartEntry = tk.Entry(self.fileFrame)
        self.filterEndLabel = tk.Label(self.fileFrame, text="To")
        self.filterEndEntry = tk.Entry(self.fileFrame)
        self.filterBtn = tk.Button(self.fileFrame, text="Filter Logs", command=self.filter_logs)



        self.host = tk.Label(self.detailFrame, text="Remote host: -")
        self.date = tk.Label(self.detailFrame,text="Date: -")
        self.code = tk.Label(self.detailFrame, text="Status code: -")
        self.size = tk.Label(self.detailFrame, text="Size: -")
        self.path = tk.Label(self.detailFrame, text="Path: -")




        self.logListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.prevBtn = tk.Button(self.logFrame, text="Previous", command=self.prev_log, state=tk.DISABLED)
        self.nextBtn = tk.Button(self.logFrame, text="Next", command=self.next_log, state=tk.DISABLED)

        # grid the widgets
        self.fileFrame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.logFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=(30, 30))
        self.detailFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.loadBtn.pack(side=tk.LEFT, padx=10)
        self.filterStartLabel.pack(side=tk.LEFT, padx=10)
        self.filterStartEntry.pack(side=tk.LEFT, padx=10)
        self.filterEndLabel.pack(side=tk.LEFT, padx=10)
        self.filterEndEntry.pack(side=tk.LEFT, padx=10)
        self.filterBtn.pack(side=tk.LEFT, padx=10)



        self.host.pack(side=tk.TOP, pady=(200, 0))
        self.date.pack(side=tk.TOP)
        self.code.pack(side=tk.TOP)
        self.size.pack(side=tk.TOP)
        self.path.pack(side=tk.TOP)



        self.logListbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.prevBtn.pack(side=tk.LEFT, padx=(40, 0), pady=(20, 0))
        self.nextBtn.pack(side=tk.RIGHT, padx=(0, 40), pady=(20, 0))

    def load_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.logList = log_analyzer.analyze_log(filename)
            self.logRawList = log_analyzer.read_log(filename)
            self.show_logs()
            self.LIST_const = log_analyzer.analyze_log(filename)
            self.LIST_RAW_const = log_analyzer.read_log(filename)

    def show_logs(self):
        self.logListbox.delete(0, tk.END)
        for log in self.logRawList:
            self.logListbox.insert(tk.END, f"{log[:50]}...")

        self.selectedLog = None
        self.prevBtn.config(state=tk.DISABLED)
        if len(self.logList) > 0:
            self.logListbox.selection_set(0)
            self.nextBtn.config(state=tk.NORMAL)

    def show_detail(self, event=None):
        if len(self.logList) == 0:
            self.prevBtn.config(state=tk.DISABLED)
            self.nextBtn.config(state=tk.DISABLED)
            return
        self.host.config(text=f"Remote host: {self.selectedLog['host']}")
        self.date.config(text=f"Date: {self.selectedLog['datetime']}")
        self.code.config(text=f"Status Code: {self.selectedLog['code']}")
        self.size.config(text=f"Size: {self.selectedLog['size']}")
        self.path.config(text=f"Path: {self.selectedLog['path']}")

    def mouse_click(self, event):
        selected_item = self.logListbox.curselection()
        if not selected_item:
            return
        index = int(selected_item[0])
        self.selectedLog = self.logList[index]
        self.show_detail()

    def filter_logs(self):
        self.logList = self.LIST_const
        self.logRawList = self.LIST_RAW_const
        start_time = self.filterStartEntry.get()
        end_time = self.filterEndEntry.get()

        if not start_time or not end_time:
            messagebox.showwarning("Filter Logs", "Both start and end times are required")
            return

        try:
            start_time = datetime.strptime(start_time, "%Y-%m-%d")
            end_time = datetime.strptime(end_time, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Filter Logs", "Invalid date/time format. Use YYYY-MM-DD")
            return

        filtered_logs = []
        filtered_raw = []
        i = 0
        for log in self.logList:
            log_time = log['datetime']
            if start_time <= log_time <= end_time:
                filtered_logs.append(log)
                filtered_raw.append(self.logRawList[i])
            i += 1

        self.logList = filtered_logs
        self.logRawList = filtered_raw
        self.show_logs()

    def prev_log(self):
        if not self.logListbox.curselection():
            return

        index = self.logListbox.curselection()[0]
        self.logListbox.selection_clear(index)
        self.logListbox.selection_set(index - 1)
        self.selectedLog = self.logList[index - 1]
        self.logListbox.activate(index - 1)
        self.show_detail()

        if index - 1 == 0:
            self.prevBtn.config(state=tk.DISABLED)
        self.nextBtn.config(state=tk.NORMAL)

    def next_log(self):
        if not self.logListbox.curselection():
            return

        index = self.logListbox.curselection()[0]
        if index < len(self.logList) - 1:
            self.logListbox.selection_clear(index)
            self.logListbox.selection_set(index + 1)
            self.selectedLog = self.logList[index + 1]
            self.show_detail()

            if index + 1 == len(self.logList) - 1:
                self.nextBtn.config(state=tk.DISABLED)
            self.prevBtn.config(state=tk.NORMAL)


    def run_app(self):
        self.mainloop()


if __name__ == '__main__':
    app = LogViewer()
    app.run_app()