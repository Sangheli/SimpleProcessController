# by Sangheli a.savel.vic@gmail.com

from subprocess import Popen
import os
import signal
import time

class ProcessHandle():
    commands = []
    processes = []

    def __init__(self,commands):
        self.commands = commands

    def updateCommands(self,commands):
        self.commands = commands

    def make_proc(self,cmd):
        time.sleep(5)
        return Popen(cmd, shell=True,  executable='/bin/bash',preexec_fn=os.setsid)

    def execute(self):
        self.processes = [self.make_proc(cmd) for cmd in self.commands]

    def shutdown(self):
        for p in self.processes:
            os.killpg(os.getpgid(p.pid), signal.SIGTERM)