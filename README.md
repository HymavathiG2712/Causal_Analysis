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

Took a subset of 500 sentences which are solely explicit from the test data.

ran the classifier on explicit dataset to see the prediction- everything were predicted as 1

in the next run the causal markers were removed from the explicit sentences to see if the predictions gets flipped to 0.

but that didn't happen most of the sentences are still predicted as 1 even though the causal markers are removed.

20% of masking has been done on the explicit sentences and whatever words have been removed/masked has been noted.

note all the words into a excel sheet and then did parts of speech to know how much % each category is?

removed just the verbs which are being calculated from parts of speech and took the sentences.

now ran the classifier again for sentences with no verbs in it.

Built a Classifier and try to get the gradient feature based importance for each input feature of the sentence.

try to do part of speech for each of this sentence and get the top two words maximum scores and top two words scores.

