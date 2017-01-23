import re
ip_command = "iptables -I INPUT -s %s -j DROP"

def extract_spam_match(message):
    if "STOP_USE" in message:
        rr = re.search('\[([^\[]+)\]', message)
        if rr is not None:
            return rr.group(1)

def extract_command(message):
    r = extract_spam_match(message)
    if r is not None:
        return ip_command % r
