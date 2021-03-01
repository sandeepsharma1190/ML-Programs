# NLP

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# to check, what is inside a file
print (os.listdir(nltk.data.find('corpora')))

# how to open a fields of a file
nltk.corpus.gutenberg.fileids()

hemlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')

for word in hemlet[:500]:
    print (word, sep=';', end = ' ')

paragraph ='Ahead of U.S. President Donald Trump’s visit to India, some of the key deliverables from the trip, as well as the outcomes that may not be delivered after his meeting with Prime Minister Narendra Modi on Tuesday, are coming into view. The larger question remains as to whether the bonhomie between the two, who will be meeting for the fifth time in eight months, will also spur the bilateral relationship towards broader outcomes, with expectations centred at bilateral strategic ties, trade and energy relations as well as cooperation on India’s regional environment. On the strategic front, India and the U.S. are expected to take forward military cooperation and defence purchases totalling about $3 billion. Mr. Trump has cast a cloud over the possibility of a trade deal being announced, but is expected to bring U.S. Trade Representative Robert Lighthizer to give a last push towards the trade package being discussed for nearly two years. Both sides have lowered expectations of any major deal coming through, given that differences remain over a range of tariffs from both sides; market access for U.S. products; and India’s demand that the U.S. restore its GSP (Generalised System of Preferences) status. However, it would be a setback if some sort of announcement on trade is not made. A failure to do so would denote the second missed opportunity since Commerce Minister Piyush Goyal’s U.S. visit last September. Finally, much of the attention will be taken by India’s regional fault-lines: the Indo-Pacific strategy to the east and Afghanistan’s future to the west. India and the U.S. are expected to upgrade their 2015 joint vision statement on the Indo-Pacific to increase their cooperation on freedom of navigation, particularly with a view to containing China. Meanwhile, the U.S.-Taliban deal is expected to be finalised next week, and the two leaders will discuss India’s role in Afghanistan, given Pakistan’s influence over any future dispensation that includes the Taliban.Any high-level visit, particularly that of a U.S. President to India, is as much about the optics as it is about the outcomes. It is clear that both sides see the joint public rally at Ahmedabad’s Motera Stadium as the centrepiece of the visit, where the leaders hope to attract about 1.25 lakh people in the audience. Despite the Foreign Ministry’s statement to the contrary, the narrative will be political. Mr. Trump will pitch the Motera event as part of his election campaign back home. By choosing Gujarat as the venue, Mr. Modi too is scoring some political points with his home State. As they stand together, the two leaders, who have both been criticised in the last few months for not following democratic norms domestically, will hope to answer their critics with the message that they represent the world’s oldest democracy and the world’s largest one, respectively.'

sentences = nltk.sent_tokenize(paragraph)

word_token = nltk.word_tokenize(paragraph)

# Frequency distribution of all words
from nltk.probability import FreqDist
fdist = FreqDist()

for words in paragraph:
    fdist[words.lower()]+=1
fdist

top_10 = fdist.most_common(10)
top_10
























