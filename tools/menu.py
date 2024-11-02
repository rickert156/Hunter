RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


def menu():
    menu = f"""Меню Hunter

    {BLUE}[1]{RESET} {GREEN}DuckDuckGo{RESET}\t{BLUE}[2]{RESET} {GREEN }Operator 1{RESET}
    {BLUE}[3]{RESET} {GREEN}Operator 2{RESET}\t{BLUE}[4]{RESET} {GREEN}Operator 3{RESET}
    
    {YELLOW}[x]{RESET} {GREEN}Config{RESET}
    
    {RED}Для вывода конфига нажми '10'{RESET}
    """
    print(menu)



