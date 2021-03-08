# I have changed function's name to custom_max not to shadow built-in max
def custom_max(*args):
    return max(args) if args else 'no numbers given'


