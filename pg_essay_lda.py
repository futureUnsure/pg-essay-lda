import codecs
import sys
import spacy
import gensim
from parsedatetime import Calendar

spacy_model = spacy.load('en')
cal_parser = Calendar()

def remove_time_date(doc):
    
    return spacy_model(' '.join([word.text for word in doc if cal_parser.nlp(word.text) is None]))

def remove_numeric_data(doc):

    return spacy_model(' '.join([word.text for word in doc if not word.like_num]))

def remove_single_character_tokens(doc):

    return spacy_model(' '.join([word.text for word in doc if len(word) > 1]))

def remove_internet_refs(doc):

    return spacy_model(' '.join([word.text for word in doc if not (word.like_url or word.like_email)]))

def remove_whitespaces(doc):

    return spacy_model(' '.join([word.text for word in doc if not word.is_space]))

def remove_stop_words(doc):

    return spacy_model(' '.join([word.text for word in doc if not word.is_stop]))

def lemmatize(doc):

    return spacy_model(' '.join([word.lemma_ for word in doc if (word.lemma and word.lemma_ != "-PRON-")]))

def main():
    sample_pg_doc = codecs.open("./dataset-3/13sentences.txt",
            encoding=sys.stdout.encoding, errors='replace').read().lower()

    f0 = lemmatize(spacy_model(sample_pg_doc))
    print(f0.text)
    f1 = remove_time_date(spacy_model(sample_pg_doc))
    print(f1.text)
    f2 = remove_numeric_data(f1)
    print(f2.text)
    f3 = remove_single_character_tokens(f2)
    print(f3.text)
    f4 = remove_internet_refs(f3)
    print(f4.text)
    f5 = remove_whitespaces(f4)
    print(f5.text)
    f6 = remove_stop_words(f5)
    print(f6.text)


main()
