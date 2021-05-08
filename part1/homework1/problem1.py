import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="The given text", type=str)
parser.add_argument("first_word", help="First word", type=str)
parser.add_argument("second_word", help="Second word", type=str)

args = parser.parse_args()

replaced_text = args.text.replace(args.first_word, args.second_word)
print(replaced_text)