# Senternce-Compression-through-Deletion-using-Stacked-LSTM
A techniques which help to summarizes the information, we used the google compressed dataset for performing this task.
We designed a model for sentence compression through deletion using the concept of Stacked LSTM. We introduce a simple model, which help to summarizes the text information into meaningful compressed sentence with minimal to no information loss. we evaluate the model both the automatic and human evaluation techniques.
Automatic evaluation consists of calculation of BleU score and Rouge-4 score. whereas for human evaluation we taken inforamtiveness and grammatically correctness of the compressed sentences. the state of the art model has stated the compression ratio of 0.42. we calculated the compression ratio as follows:

Compression Ratio = #of words in compressed sentences / #no of words in original sentences * 100


# Result
The results are coming to be quite state of the art:
Compression ratio: 0.41 [5_win_model]
Compression ratio: 0.29 [3_win_model]


# Contributors
please feel free for the contribution in the model.

# Requirement 
Python 3.0+
Keras
numpy
pandas
json
glove [Glove: Global Vector reprsentation of words] 
{Chris Manning and Richard Socher}- Stanford University Pre-trained model



