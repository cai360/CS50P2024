import cowsay
import sys

# beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
# 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex',
# 'turkey', 'turtle', 'tux'

try:
    cowsay.turkey("hello, " + sys.argv[1])
except EOFError:
    pass
