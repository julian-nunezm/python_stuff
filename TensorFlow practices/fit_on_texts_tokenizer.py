#https://machinelearningmastery.com/prepare-text-data-deep-learning-keras/

from tensorflow.keras.preprocessing.text import Tokenizer
from pprint import pprint
# define 5 documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!']
# create the tokenizer
t = Tokenizer()
# fit the tokenizer on the documents
t.fit_on_texts(docs)

# summarize what was learned
pprint(t.word_counts)
pprint(t.document_count)
pprint(t.word_index)
pprint(t.word_docs)

# integer encode documents
encoded_docs = t.texts_to_matrix(docs, mode='count')
print(encoded_docs)
