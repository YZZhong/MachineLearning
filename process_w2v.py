# SST-1:   max_length :52
# SST-2:   max_length :52
# Subj:    max_length :106
# TREC:    max_length :33
# Qbclaims:max_length :63  average_length:16

import numpy as np
import gensim
import cPickle
import io


# def w2v(data_word, max_length):#data_word is a txt with sentence
#     w2v_model = gensim.models.KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin', binary=True)
#     vocab = w2v_model.vocab
#     text_np = None
#     with io.open(data_word, 'r', encoding='utf-8') as f1:
#         batch_data = []
#         lines = f1.readlines()
#         for sample_i in range(len(lines)):
#             text_arr = np.zeros((max_length, 300))
#             for word_j in range(len(lines[sample_i].split())):
#                 if lines[sample_i].split()[word_j] in vocab:
#                     text_arr[word_j] = np.reshape(w2v_model[lines[sample_i].split()[word_j]], [1, 300])
#                 else:
#                     text_arr[word_j] = np.reshape(w2v_model['UNK'], [1, 300])
#             batch_data.append(text_arr)
#         text_np = np.array(batch_data)
#         print "Sample nums:",len(lines)
#    return text_np


def process_to_string(data_word):#data_word is a txt with sentence
    text_np = None
    with io.open(data_word, 'r', encoding='utf-8') as f1:
        batch_data = []
        lines = f1.readlines()
        for sample_i in range(len(lines)):
            text_arr = []
            for word_j in range(len(lines[sample_i].split())):
                text_arr.append(lines[sample_i].split()[word_j])
            batch_data.append(text_arr)
        text_np = np.array(batch_data)
        print "Sample nums:",len(lines)
    return text_np

#process txt to ndarry


def process_to_ndarry(filename):#filename is a txt with labels or length
    text_np = None
    with io.open(filename, 'r', encoding='utf-8') as f2:
        lines = f2.readlines()
        data_arr = []
        for sample_i in range(len(lines)):
            data_arr.append(int(lines[sample_i].split()[-1]))
        print data_arr
        text_np = np.array(data_arr)
    return text_np


if __name__ == '__main__':
    sentence_file = 'video_train_word.txt'
    labels_file = 'video_train_label.txt'
    length_file = 'video_train_length.txt'
    #max_length = 1084
    word_list = process_to_string(sentence_file) #word_list = w2v(sentence_file, max_length)
    label_list = process_to_ndarry(labels_file)
    length_list = process_to_ndarry(length_file)
    cPickle.dump([word_list, label_list, length_list], open('video_train.p', 'w'))
    all_data = cPickle.load(open('video_train.p', "r"))
    print all_data[0].shape  # text
    print all_data[1].shape  # label
    print all_data[2].shape  # length
    print all_data[1]
