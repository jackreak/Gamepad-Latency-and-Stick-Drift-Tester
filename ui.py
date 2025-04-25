import tkinter as tk
from tkinter import ttk
import threading
import time

class ControllerTesterUI:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.title("Controller Latency & Drift Tester")
        self.root.geometry("600x500")
        self.controller = controller
        self.drift_testing = False
        self.drift_test_callback = None

        self.label = tk.Label(self.root, text=f"Connected to: {controller.get_name()}", font=("Arial", 14))
        self.label.pack(pady=10)

        self.log = tk.Text(self.root, height=15, state="disabled", bg="#111", fg="#0f0", font=("Consolas", 10))
        self.log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.drift_button = tk.Button(self.root, text="Start Stick Drift Test", command=self.start_drift_test)
        self.drift_button.pack(pady=10)

        self.warning_label = tk.Label(self.root, text="", fg="red", font=("Arial", 12))
        self.warning_label.pack()

        self.progress = ttk.Progressbar(self.root, length=300)
        self.progress.pack(pady=10)

    def add_log_entry(self, text):
        if self.drift_testing:
            return
        self.log.config(state="normal")
        self.log.insert(tk.END, f"{text}\n")
        self.log.yview(tk.END)
        self.log.config(state="disabled")

    def set_drift_test_callback(self, callback):
        self.drift_test_callback = callback

    def start_drift_test(self):
        if not self.drift_testing and self.drift_test_callback:
            threading.Thread(target=self.drift_test_callback, daemon=True).start()

    def prepare_for_drift_test(self):
        self.drift_testing = True
        self.clear_log()
        self.warning_label.config(text="Move joysticks and pull triggers!", fg="black")
        self.run_progress(5, reverse=True)

        self.warning_label.config(text="DO NOT TOUCH YOUR CONTROLLER", fg="red")
        self.run_progress(3)

    def run_progress(self, duration, reverse=False):
        steps = 100
        interval = duration / steps
        for i in range(steps + 1):
            value = (steps - i) if reverse else i
            self.progress["value"] = value
            self.root.update_idletasks()
            time.sleep(interval)

    def end_drift_test(self):
        self.warning_label.config(text="Drift test complete.", fg="green")
        self.drift_testing = False

    def display_drift_report(self, report_lines):
        self.clear_log()
        self.log.config(state="normal")
        for line in report_lines:
            self.log.insert(tk.END, f"{line}\n")
        self.log.yview(tk.END)
        self.log.config(state="disabled")

    def clear_log(self):
        self.log.config(state="normal")
        self.log.delete("1.0", tk.END)
        self.log.config(state="disabled")

    def run(self):
        self.root.mainloop()
