import codecs
import sys
import spacy
import gensim
from parsedatetime import Calendar

spacy_model = spacy.load('en')
cal_parser = Calendar()

def remove_time_date(doc):
    
    return spacy_model(' '.join([word.text for word in doc if cal_parser.nlp(word.text) is None]))

def main():
    sample_pg_doc = codecs.open("./dataset-3/13sentences.txt",
            encoding=sys.stdout.encoding, errors='replace').read()
    f1 = remove_time_date(spacy_model(sample_pg_doc))
    print(f1.text)

main()
