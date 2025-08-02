# file-watcher 🕵️‍♂️👀

A simple and flexible CLI tool written in Python that watches a directory for file changes and runs a command automatically — perfect for automation and development workflows.

---

## ✨ Features

- Watch any directory for file changes (recursively)
- Run any custom shell command when a change happens
- Ignore files/folders using a `.watcherignore` file
- Easy to use CLI (powered by `typer`)
- Lightweight and cross-platform

---

## 🚀 Installation

```bash
clone project
cd file-watcher
uv tool install .
```

## :( Uninstallation

```bash
uv tool uninstall file-watcher
```
## How can i use it
```bash
file-watcher --command "type your command here"
```

## Run in backgroud?
```
touch .watcherignore
```

add watcher.log to .watcherignore file

```
nohup file-watcher --command "your command" > watcher.log 2>&1 &
```

## Kill backgroud proccess
```bash
killall file-watcher
```
