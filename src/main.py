from function import *

test = sort_data(completed_operation(open_file('operations.json')))
for t in test:
    # print(t)
    print(f'{date_format(t['date'])} {t['description']}')
    if t.get('from') == None and "Счет" in t.get('to'):
        print(f"-> Счет {hide_account_number(t.get('to'))}")
    elif "Счет" in t.get('from') and "Счет" in t.get('to'):
        print(f"Счет {hide_account_number(t.get('from'))} -> Счет {hide_account_number(t.get('to'))}")
    elif "Счет" in t.get('to'):
        cart = t.get('from').split()[:-1]
        print(f"{" ".join(cart)} {hide_cart_number(t.get('from'))} -> "
              f"Счет {hide_account_number(t.get('to'))}")
    else:
        cart_from = t.get('from').split()[:-1]
        cart_to = t.get('to').split()[:-1]
        print(f"{" ".join(cart_from)} {hide_cart_number(t.get('from'))} -> "
              f"Счет {" ".join(cart_to)} {hide_cart_number(t.get('to'))}")
    print(f"{t['operationAmount']['amount']} {t['operationAmount']['currency']['name']}\n")
