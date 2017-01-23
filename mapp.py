import os
import logic
import tailer
for line in tailer.follow(open(sys.getenv('SOURCE_FILE'))):
    call_command = logic.extract_command(line)
    if call_command is not None:
        os.system(call_command)
