import tkinter as tk
def is_valid_credit_card(number):

    number = ''.join(c for c in number if c.isdigit())

    if (len(number) not in (13, 15, 16, 19)) or (
            not (number.startswith('4') or
                  (number.startswith('51') or number.startswith('52') or number.startswith('53') or number.startswith('54') or number.startswith('55')) and len(number) == 16 or
                  number.startswith('60') or number.startswith('64') or number.startswith('65') and len(number) in (16, 19) or
                  (number.startswith('34') or number.startswith('37')) and len(number) == 15)):
        return False

    checksum = 0
    is_second = False
    for i, digit in enumerate(reversed(number)):
        digit = int(digit)
        if is_second:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        checksum += digit
        is_second = not is_second

    return checksum % 10 == 0

def validate_card_number():
    number = card_number_entry.get()
    if is_valid_credit_card(number):
        result_label.config(text="Valid credit card number")
    else:
        result_label.config(text="Invalid credit card number")

root = tk.Tk()
root.title("Credit Card Validator")

card_number_label = tk.Label(root, text="Enter credit card number:")
card_number_label.pack()

card_number_entry = tk.Entry(root, width=50)
card_number_entry.pack()

validate_button = tk.Button(root, text="Validate", command=validate_card_number)
validate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
