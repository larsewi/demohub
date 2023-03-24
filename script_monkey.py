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

@call_maybe(5)
def monkey_cron():
    commands = [
        ["chown", "script_monkey", "/etc/cron.allow"],
        ["chgrp", "script_monkey", "/etc/cron.allow"],
        ["chmod", "0777", "/etc/cron.allow"],
        ["chown", "script_monkey", "/etc/crontab"],
        ["chgrp", "script_monkey", "/etc/crontab"],
        ["chmod", "0777", "/etc/crontab"],
        ["chown", "script_monkey", "/etc/cron.d"],
        ["chgrp", "script_monkey", "/etc/cron.d"],
        ["chmod", "0777", "/etc/cron.d"],
        ["chown", "script_monkey", "/etc/cron.hourly"],
        ["chgrp", "script_monkey", "/etc/cron.hourly"],
        ["chmod", "0777", "/etc/cron.hourly"],
        ["chown", "script_monkey", "/etc/cron.daily"],
        ["chgrp", "script_monkey", "/etc/cron.daily"],
        ["chmod", "0777", "/etc/cron.daily"],
        ["chown", "script_monkey", "/etc/cron.weekly"],
        ["chgrp", "script_monkey", "/etc/cron.weekly"],
        ["chmod", "0777", "/etc/cron.weekly"],
        ["chown", "script_monkey", "/etc/cron.monthly"],
        ["chgrp", "script_monkey", "/etc/cron.monthly"],
        ["chmod", "0777", "/etc/cron.monthly"],
    ]
    commands = list(filter(lambda x: os.path.exists(x[2]), commands))
    random.shuffle(commands)
    command = commands[0]
    print("Running command '%s'" % " ".join(command))
    subprocess.run(command)


@call_maybe(5)
def monkey_encrypt_method():
    filename = "/etc/login.defs"
    sha512 = "ENCRYPT_METHOD SHA512"
    sha256 = "ENCRYPT_METHOD SHA256"

    if not os.path.exists(filename):
        return

    contents = ""
    with open(filename, "r") as f:
        contents = f.read()

    if (sha512 in contents):
        print(f"Replacing '{sha512}' with '{sha256}' in file '{filename}'")
        with open(filename, "w") as f:
            f.write(contents.replace(sha512, sha256))

@call_maybe(5)
def monkey_dotrhosts():
    filename = "/home/script_monkey/.rhosts"
    print(f"Touching file '{filename}'")
    with open(filename, "w"):
        pass


@call_maybe(5)
def monkey_prelinking():
    prelink_not_yes = ["PRELINKING=no", "PRELINKING=unknown"]
    prelink_yes = "PRELINKING=yes"
    filenames = ["/etc/default/prelink", "/etc/sysconfig/prelink"]

    for filename in filenames:
        if not os.path.exists(filename):
            continue

        contents = ""
        with open(filename, "r") as f:
            contents = f.read()

        for not_yes in prelink_not_yes:
            if not_yes in contents:
                with open(filename, "w") as f:
                    print(f"Replacing '{not_yes}' with '{prelink_yes}' in file '{filename}'")
                    f.write(contents.replace(not_yes, prelink_yes))


@call_maybe(5)
def monkey_files():
    filenames = ["/tmp/virus", "/tmp/rootkit", "/tmp/worm", "/tmp/reverse_shell"]
    random.shuffle(filenames)
    filename = filenames[0]
    print(f"Creating file '{filename}'")
    with open(filename, "w") as f:
        f.write("You have been pwned!")


@call_maybe(5)
def monkey_aslr():
    command = ["sysctl", "-w", "kernel.randomize_va_space=0"]
    print("Running command '%s'" % " ".join(command))
    subprocess.run(command)


@call_maybe(5)
def monkey_etc_issue():
    commands = [
        ["chown", "script_monkey", "/etc/issue"],
        ["chgrp", "script_monkey", "/etc/issue"],
        ["chmod", "0777", "/etc/issue"],
    ]
    random.shuffle(commands)
    command = commands[0]
    print("Running command '%s'" % " ".join(command))
    subprocess.run(command)


if __name__ == "__main__":
    monkey_cron()
    monkey_encrypt_method()
    monkey_dotrhosts()
    monkey_prelinking()
    monkey_files()
    monkey_aslr()
    monkey_etc_issue()
