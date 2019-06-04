# Sentence-Compression-through-Deletion-using-Stacked-LSTM
A techniques which help to summarizes the information, we used the google compressed dataset for performing this task.
We designed a model for sentence compression through deletion using the concept of Stacked LSTM. We introduce a simple model, which help to summarizes the text information into meaningful compressed sentence with minimal to no information loss. we evaluate the model both the automatic and human evaluation techniques.Automatic evaluation consists of calculation of BleU score and Rouge-4 score. whereas for human evaluation we taken informativeness and grammatically correct of the compressed sentences. the state of the art model has stated the compression ratio of 0.40. we calculated the compression ratio as follows:


Compression Ratio is defined as No. of words in compressed sentences to the No. of words in original sentences * 100


# Result
The results are coming to be quite state of the art:\
Compression ratio: 0.41 [5_win_model] \
Compression ratio: 0.37 [3_win_model]

# Requirement 
Python 3.0+\
Keras \
numpy \
pandas \
json \
glove [GloVe: Global Vector reprsentation of words] 

# Download Links
[glove] http://nlp.stanford.edu/data/glove.840B.300d.zip 

[datset_Original]: http://tiny.cc/0pss7y \
[dataset_compressed]: https://drive.google.com/open?id=0B7FKpaFOwrQ4MXhlaHplbTdTRVdpYmJ2bjlvVWhUNGUxalJ3
