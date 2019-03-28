import argparse, operator
from nltk import word_tokenize, FreqDist

parser = argparse.ArgumentParser(description='Reads a text and give us analysis')
parser.add_argument("filename", help="takes file name as argument", type=str)
parser.add_argument("--top", help="shows top words and counts", type=int)
parser.add_argument("--to-lower", help="processes the text as lower case", action = "store_true")

def open_text(file_path, lower):
    
    tokenised = []
    
    with open(file_path, "r", encoding="utf-8") as text:
        if lower == True:

            for line in text:
                tokenised += word_tokenize(line.lower())
        else:
            for line in text:
                tokenised += word_tokenize(line)
        
    return tokenised

def text_stats(list_tokens, topn):
    corpus_freqs = dict(FreqDist(list_tokens))
    sorted_x = sorted(corpus_freqs.items(), key=operator.itemgetter(1), reverse=True)
    for i in sorted_x[:topn]:
        print(i[1], "", str(i[0]))

args = parser.parse_args()



if __name__ == "__main__":
    if args.to_lower:
        lower = True
    else:
        lower = False

    if args.top:
        n = args.top
    else:
        pass
        n = 10

    test_file = open_text(args.filename, lower)
    text_stats(test_file, n)
    