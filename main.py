import pygame
import threading
import time
from ui import ControllerTesterUI
from drift_detection import DriftDetector

# Initialize Pygame
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected.")
    pygame.quit()
    exit()

controller = pygame.joystick.Joystick(0)
controller.init()

ui = ControllerTesterUI(controller)
drift_detector = DriftDetector(controller, ui)

def input_loop():
    last_input_time = None
    start_time = time.time()

    while True:
        pygame.event.pump()

        # Button presses only
        for i in range(controller.get_numbuttons()):
            if controller.get_button(i):
                now = time.time()
                latency = (now - start_time) * 1000
                between_inputs = (now - last_input_time) * 1000 if last_input_time else 0
                last_input_time = now
                ui.add_log_entry(f"Button {i} pressed — {latency:.2f} ms since start, {between_inputs:.2f} ms since last")
                start_time = now
                time.sleep(0.1)

        # Skip axis movement logging during latency mode
        time.sleep(0.01)

def run_drift_test():
    ui.prepare_for_drift_test()
    drift_detector.perform_test()
    ui.end_drift_test()

threading.Thread(target=input_loop, daemon=True).start()
ui.set_drift_test_callback(run_drift_test)
ui.run()
