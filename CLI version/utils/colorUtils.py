from colorama import Fore, Style, init
init(autoreset= True)

def colorText(text, resultType):
    if resultType == 'win':
        return (f"{Fore.GREEN}{text}{Style.RESET_ALL}")
    elif resultType == 'lose':
        return (f"{Fore.RED}{text}{Style.RESET_ALL}")
    elif resultType == 'tie':
        return (f"{Fore.YELLOW}{text}{Style.RESET_ALL}")
    elif resultType == 'info':
        return (f"{Fore.CYAN}{text}{Style.RESET_ALL}")
    else:
        return text
