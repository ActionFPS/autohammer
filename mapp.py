import os
import logic
import tailer
sf = os.getenv('SOURCE_FILE')
assert sf != None, "Set SOURCE_FILE env"
for line in tailer.follow(open(sf)):
    call_command = logic.extract_command(line)
    if call_command is not None:
        os.system(call_command)
