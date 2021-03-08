# I have changed function's name to custom_max not to shadow built-in max
def custom_max(*args):
    if args:
        return max(args)
    else:
        return 'no numbers given'

