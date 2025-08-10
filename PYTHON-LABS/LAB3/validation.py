def is_valid_email(email):
    return "@" in email


def is_valid_phone(phone):
    return phone.startswith("01") and len(phone) == 11 and phone.isdigit()


def is_valid_number(text):
    return text.isdigit()


def is_valid_date(date):
    # هنا ممكن نضيف تحقق بالتاريخ لو عايز بعدين
    return len(date) == 10 and date[4] == "-" and date[7] == "-"