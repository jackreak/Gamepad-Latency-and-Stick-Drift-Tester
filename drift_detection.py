import time

class DriftDetector:
    def __init__(self, controller, ui):
        self.controller = controller
        self.ui = ui

    def perform_test(self):
        observations = {i: [] for i in range(self.controller.get_numaxes())}

        # Observe for 3 seconds (UI already told them not to touch)
        start = time.time()
        while time.time() - start < 3:
            for i in observations:
                val = self.controller.get_axis(i)
                observations[i].append(val)
            time.sleep(0.01)

        report = []
        for axis, values in observations.items():
            avg = sum(map(abs, values)) / len(values)
            if avg > 0.1:
                report.append(f"❌ Axis {axis} (Stick/Trigger) — Drift detected! (Avg: {avg:.3f})")
            else:
                report.append(f"✅ Axis {axis} (Stick/Trigger) — No significant drift (Avg: {avg:.3f})")

        self.ui.display_drift_report(report)
