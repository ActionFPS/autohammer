import re
from logic import *
import pytest
input = ("Jan 23 01:28:07 [185.11.146.154] client Mr.HydeMOM called a vote: ban"
    " player Mr.Hyde, reason: STOP_USE_HACKS_MY_SON_OF_A_BITCHHHHHHHHHHHHHHHHHHHHHH"
    "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

def test_itworks():
    assert(extract_spam_match(input) == '185.11.146.154')

def test_cmd():
    assert(extract_command(input) == "iptables -I INPUT -s 185.11.146.154 -j DROP")
