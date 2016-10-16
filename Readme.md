# Python 2 web scripts

### Usage

Start web server

```bash
python fork.py
```

Connect to it from the same machine (different terminal)

```
telnet 127.0.0.1 8080
```

or easy switch between screens using GNU `screen`:

```
screen -S new_screen
```

`C-a d` - exit from created screen

`screen -ls` - show all screens

`screen -r` - return to last screen

### Show forked processes in real time

```
watch "ps ax | grep fork"
```