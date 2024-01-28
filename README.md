# Words_Important_for_Prediction_to_get_flipped

Data has been collected from 4 different websites.
1. FinCausal Dataset - https://github.com/yseop/YseopLab/blob/develop/FNP_2020_FinCausal/data/practice/fnp2020-fincausal2-task1.csv
2. ADE: https://huggingface.co/datasets/ade_corpus_v2?library=true
3. https://causenet.org/ : causenet precision
4. Wikimedia data
5. Medcaus: https://github.com/farhadmfar/ace/blob/main/MedCaus/MedCaus.txt

Preprocessed the unstructure data into proper csv format.
( The datasets were of JSON format Converted from JSON to CSV)

Splitted the data into 70-30 ratio.

Built the Walsh Hadamard Transform Model.

Evaluated the Test data and noted correctly predicted.

Took a subset of correctly predicted sentences and masked 20% of the words to the test data.

For those sentences where prediction got flipped -> noted those sentences and highlighted the words which were masked

Basically the task is which words are important in making the prediction getting flipped.
