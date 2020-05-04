import nltk
import joblib
import re
import numpy as np

nltk.download('stopwords')
from nltk.corpus import stopwords

# Paths for all resources for the bot.
RESOURCE_PATH = {
    'INTENT_RECOGNIZER': 'data/intent_recognizer.pkl',
    'TAG_CLASSIFIER': 'data/tag_classifier.pkl',
    'TFIDF_VECTORIZER': 'data/tfidf_vectorizer.pkl',
    'THREAD_EMBEDDINGS_FOLDER': 'data/thread_embeddings_by_tags',
    'WORD_EMBEDDINGS': 'data/ss_embeddings.tsv',
}


def text_prepare(text):
    """
    Performs tokenization and simple preprocessing.
    """

    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()


def load_embeddings(embeddings_path):
    """
    Loads pre-trained word embeddings from tsv file.

    Args:
      embeddings_path - path to the embeddings file.

    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """

    with open(embeddings_path) as f:
        embeddings = {key: np.array(values, dtype=np.float32) for key, *values in (line.split() for line in f)}
    
    embeddings_dim = len(next(iter(embeddings.values())))
    return embeddings, embeddings_dim


def question_to_vec(question, embeddings, dim):
    """
    Transforms a string to an embedding by averaging word embeddings.
    """

    embedded = np.array([embeddings[word] for word in question.split() if word in embeddings])
    return embedded.mean(axis=0) if len(embedded) > 0 else np.zeros(dim)

def unpickle_file(filename):
    """
    Returns the result of unpickling the file content.
    """
    with open(filename, 'rb') as f:
        return joblib.load(f)