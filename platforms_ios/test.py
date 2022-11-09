import re
texto = "xcz xzcxc São Paulo e Espaço czxcx zxcz"
print(re.escape(texto))

term = re.compile(r"São")
match = term.search(texto, re.IGNORECASE)
if match.group():
    texto = re.sub(match.group(), f" Início {match.group()} Fim", texto)
print(match.group())
print(texto)