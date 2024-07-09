import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, script_to_run):
        self.script_to_run = script_to_run
        self.observer = Observer()

    def run(self):
        event_handler = Handler(self.script_to_run)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):

    def __init__(self, script_to_run):
        self.script_to_run = script_to_run

    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'modified':
            # Restart the script
            os.system(f"{sys.executable} {self.script_to_run}")

if __name__ == '__main__':
    script = 'main.py'  # Replace with your Tkinter script
    watcher = Watcher(script)
    watcher.run()
