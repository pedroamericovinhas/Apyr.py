from datetime import datetime as dt


def logga(msg):
    date = f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]"
    server = f"{msg.guild} (#{msg.channel})" if msg.guild else f"{msg.channel.recipient} DM"
    attachment = f"[{msg.attachments[0].url}]" if msg.attachments else ''
    try:
        with open(f"./logs/{dt.now().strftime('%Y-%m-%dlog.txt')}", 'a', encoding="utf-8") as f:
            f.write(f"{date} {msg.author} @ {server}: {msg.content} {attachment}\n")
    except FileNotFoundError:
        with open(f"./logs/{dt.now().strftime('%Y-%m-%dlog.txt')}", 'w', encoding="utf-8") as f:
            f.write(f"{date} {msg.author} @ {server}: {msg.content} {attachment}\n")
