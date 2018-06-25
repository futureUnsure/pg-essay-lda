What does Paul Graham write about?
==================================

- Background:
Paul Graham is probably one of the most influential technology pundit of our times. And this is not just because of ViaWeb or YC, but also because of his exemplary writing on everything related to Computer Science, Technology and its impact on society in general. His essays are legendary, and his style of succinct delivery of ideas keeps everyone wanting for more. So when I learned about some of the more advanced things that are possible using NLP toolkits, I thought why not apply them to his essays to find out what he writes about the most!

Initially, I thought of training a skip gram word2vec to generate PG specific embeddings, but then I proceeded to carry out topic modeling. Word algebra just isn't that much fun after a certain point of time. The training data is actually quite small as well.

- Methodology:
    - I scraped his website for articles, barring the chapters specific to Lisp. (We all know that would be #1 topic anyway)
    - I then run a spaCy pipeline on the essays to clean the data: removing time/date, whitespaces, stop words, lemmatizing, the usual drill. I went through spaCy documentation to find out the APIs.
    - After that, I create a dictionary consisting of the cleaned essays, build a corpus out of them using bag-of-words model, and then input the corpus into the LDA modeler , all thanks to the gensim API.


- Results:
I have summarized the topics as output by the LDA algorithm the best I could (Keywords output in brackets next to my summary)
Feel free to summarize them as you see fit by examining the output yourself!

    The top 10(in order) topics are:

1. Startups/Founders (Duh)
2. Wealth/Money
3. ? (Good, time, know, hapless, better)
4. Technology-behind-the-scenes (Design, Language, Software, Programmers, Hackers)
5. Money-behind-the-scenes (Investors, Money, VC, Angel, Deal, Good, Round)
6. Negativity (Mean, Meanness, Patents)
7. Things-in-life-other-than-technology (Kids, School, Parents, Adults)
8. US/Spam/Laws? (America, American, Spam, Countries, Japanese, Laws)
9. ? (Computers, Subject, Fred, Graham)
10. Silicon Valley vs Boston? (Silicon, Valley, Boston, Nerds)
