from datetime import datetime as dt


def log_msg(msg):
    if msg.guild is None:
        print(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{msg.author} @ DM: {msg.content}")
        with open(f"./logs/{dt.now().strftime('%Y-%m-%d')}", 'w') as f:
            f.write(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{msg.author} @ {msg.channel.type.recipient}DM: {msg.content}")
    else:
        print(
            f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{msg.author} @ {msg.guild}(#{msg.channel}): {msg.content}")
        with open(f"./logs/{dt.now().strftime('%Y-%m-%d')}", 'w') as f:
            f.write(f"[{dt.now().strftime('%Y-%m-%d %H:%M:%S')}]{msg.author} @ DM: {msg.content}")


def log(msg):
    with open(f"./logs/{dt.now().strftime('%Y-%m-%d')}", 'w') as f:
        f.write('a')
