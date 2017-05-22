import os
import codecs
import sys
import spacy
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from parsedatetime import Calendar
from pprint import pprint

spacy_model = spacy.load('en')
cal_parser = Calendar()

dataset_path = "./dataset-3/"
assert(os.access(dataset_path, os.F_OK))

essay_files = [dataset_path + essay_file for dir_name, sub_dirs, files in \
        os.walk(dataset_path) for essay_file in files ]


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

def pipeline(essays):

    res = []
    for doc in spacy_model.pipe(essays, batch_size=50, n_threads=4):
        f0 = doc
        #f0 = lemmatize(doc)
        #print(f0.text)
        f1 = remove_time_date(f0)
        #print(f1.text)
        f2 = remove_numeric_data(f1)
        #print(f2.text)
        f3 = remove_single_character_tokens(f2)
        #print(f3.text)
        f4 = remove_internet_refs(f3)
        #print(f4.text)
        f5 = remove_whitespaces(f4)
        #print(f5.text)
        f6 = remove_stop_words(f5)
        #print(f6.text)
        res.append([f6.text])

    return res

def main():

    essays = [codecs.open(essay_file,
            encoding="utf-8", errors='replace').read().lower()
            for essay_file in essay_files]

    clean_essays = pipeline(essays)

    dictionary = Dictionary(clean_essays)

    corpus = [dictionary.doc2bow(essay) for essay in clean_essays]

    #??
    temp = dictionary[0]
    id2word = dictionary.id2token

    print("No. of unique tokens {}".format(len(dictionary)))
    print("No. of documents {}".format(len(corpus)))

    model = LdaModel(corpus=corpus, id2word=id2word,\
            chunksize=10, alpha='auto', eta='auto', iterations=400,\
            num_topics=10, passes=20, eval_every=None)

    top_topics = model.top_topics(corpus, num_words=20)
    pprint(top_topics)

main()
