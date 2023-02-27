import os
import random
import subprocess

def call_maybe(probability):
    def decorator(func):
        def inner(*args, **kwargs):
            if random.randrange(0, 100) < probability:
                return func(*args, **kwargs)
            return None
        return inner
    return decorator

@call_maybe(100)
def monkey_cron():
    commands = [
        ["chown", "nobody", "/etc/cron.allow"],
        ["chgrp", "nobody", "/etc/cron.allow"],
        ["chmod", "0777", "/etc/cron.allow"],
        ["chown", "nobody", "/etc/crontab"],
        ["chgrp", "nobody", "/etc/crontab"],
        ["chmod", "0777", "/etc/crontab"],
        ["chown", "nobody", "/etc/cron.d"],
        ["chgrp", "nobody", "/etc/cron.d"],
        ["chmod", "0777", "/etc/cron.d"],
        ["chown", "nobody", "/etc/cron.hourly"],
        ["chgrp", "nobody", "/etc/cron.hourly"],
        ["chmod", "0777", "/etc/cron.hourly"],
        ["chown", "nobody", "/etc/cron.daily"],
        ["chgrp", "nobody", "/etc/cron.daily"],
        ["chmod", "0777", "/etc/cron.daily"],
        ["chown", "nobody", "/etc/cron.weekly"],
        ["chgrp", "nobody", "/etc/cron.weekly"],
        ["chmod", "0777", "/etc/cron.weekly"],
        ["chown", "nobody", "/etc/cron.monthly"],
        ["chgrp", "nobody", "/etc/cron.monthly"],
        ["chmod", "0777", "/etc/cron.monthly"],
    ]
    commands = list(filter(lambda x: os.path.exists(x[2]), commands))
    commands = random.sample(commands, random.randrange(0, len(commands)))
    for command in commands:
        subprocess.run(command)


if __name__ == "__main__":
    monkey_cron()
