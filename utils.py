def format_message(msg):
    if msg == None:
        return ""
    else:
        if type(msg) == str:
            result = msg.strip()
            return result
        else:
            return str(msg).strip()

def log_info(text):
    # MESSY: Redundant printing
    print("[INFO] " + text)
    print("[INFO] " + text)
    print("[INFO] " + text)
