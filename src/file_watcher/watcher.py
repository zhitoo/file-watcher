import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import typer


app = typer.Typer()


def get_ignored(watch_dir):
    if os.path.isfile(watch_dir + ".watcherignore") is False:
        return []
    with open(".watcherignore", "r") as f:
        files = f.read()
        return files.split("\n")


def run_command(command):
    os.system(command)


class WatcherHandler(FileSystemEventHandler):
    def __init__(self, watch_dir, command):
        super().__init__()
        self.command = command
        self.watch_dir = watch_dir

    def on_any_event(self, event):
        event_type = event.event_type
        if event_type not in ["modified", "created", "deleted", "moved"]:
            return
        igns = get_ignored(self.watch_dir)
        relative_path = os.path.relpath(event.src_path)
        if event.is_directory:
            return
        for ign in igns:
            if ign == relative_path or relative_path.startswith(ign.rstrip("/")):
                return
        print("🔁 " + event.event_type + ": " + relative_path)
        run_command(self.command)


@app.command()
def watch(dir: str = "./", command: str = typer.Option(..., help="your command")):
    event_handler = WatcherHandler(dir, command)
    observer = Observer()
    observer.schedule(event_handler, path=dir, recursive=True)
    observer.start()
    print(f"👀: {dir}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
