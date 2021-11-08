from pexpect import pxssh

botnet = []

# Class: Bot - host , user , password
class Bot:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.controller = self.ssh()
    def ssh(self):
        session = pxssh.pxssh()
        session.login(self.host, self.user, self.password)
        return session

# Util Funcs
def add_bot(host, user, password):
    bot = Bot(host, user, password)
    botnet.append(bot)
    return bot

def execute(payload):
    beforeprompts = []
    for bot in botnet:
        bot.controller.sendline(payload)
        bot.controller.prompt()
        beforeprompts.append(bot.controller.before)
    return beforeprompts

# Params
cmd = 'ls'
IPs = ['127.0.0.1']
Names = ['kausik']
Passwords = ['123']

# Bot Declarations
for ip, name, pwd in zip(IPs, Names, Passwords):
    add_bot(ip, name, pwd)

# Execute cmd
outputs = execute(cmd)
for o in outputs:
    print(o.decode("utf-8"))
    print("\n\n\n")