
from colorama import Fore, Back, Style #окрашивает текст, фон так как нам нужно

print(Fore.WHITE + "Это белый текст")
print(Fore.RED + "Это красный текст")
print(Back.YELLOW + "Текст с жёлтым фоном")
print(Style.RESET_ALL + "Снова обычный текст")

# Fore — цвет текста.
#
# Back — цвет фона.
#
# Style.RESET_ALL — сброс стиля обратно к обычному.