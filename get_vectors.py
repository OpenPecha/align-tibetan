import sys

from sentence_transformers import SentenceTransformer
import numpy as np

filename = sys.argv[1]
number_of_overlays = int(sys.argv[2]) + 1 # +1 because we want to include the original sentence

def process_file(filename):
    model_path = "buddhist-nlp/bod-eng-similarity"
    model = SentenceTransformer(model_path)

    model.max_seq_length = 500
    file = open(filename,'r')

    sentences = [line.rstrip('\n').strip() for line in file]
    sentences_overlay = []

    for x in range(len(sentences)):
        val = number_of_overlays
        if (len(sentences) - x) < val:
            val = (len(sentences) - x) + 1
        for i in range(1,val):
            sentences_overlay.append(' '.join(sentences[x:x+i]))
    overlay_string = "\n".join(sentences_overlay)
    vectors = np.array(model.encode(sentences_overlay,show_progress_bar=False))
    print("LEN SENTENCES",len(sentences_overlay))
    print("LEN VECTORS",len(vectors))
    with open(sys.argv[1] + "_overlay", "w") as text_file:
        text_file.write(overlay_string)

    np.save(sys.argv[1] + "_vectors",vectors)

process_file(filename)

