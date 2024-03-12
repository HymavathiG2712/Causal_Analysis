# Words_Important_for_Prediction_to_get_flipped

**Data Collection and Preparation:**

Gathered diverse datasets including Causenet, MedCaus, FinCausal, ADE, and WikiMedia.
Converted JSON and TXT files to CSV format for standardized data handling.
Performed initial data exploration to understand the structure and content of the datasets.

**Data Preprocessing:**

Implemented data preprocessing techniques to clean and prepare the data for analysis.
Utilized Spacy for stopword removal to eliminate irrelevant words.
Ensured data consistency and uniformity across all datasets.

**Data Splitting:**

Split the dataset into training and testing sets with a 70-30 ratio.
Obtained 1.2 lakh sentences for training, with 84k sentences for training and 39k for testing.

**Model Development:**

Developed a causal sentence prediction model based on a Walsh Hadamard BILSTM algorithm.
Configured the model architecture to effectively learn causal relationships from textual data.

**Model Evaluation:**

Evaluated the model's performance on the testing set to measure its predictive accuracy.
Calculated metrics such as precision, recall, and F1-score to assess model performance comprehensively.

**Experimentation and Analysis:**

Selected a subset of 500 correctly predicted sentences, focusing on explicit causal relationships.
Conducted experiments by randomly masking words in the selected sentences to observe the impact on predictions.
Investigated the effect of removing causal verbs from explicit sentences on prediction accuracy.
Utilized Spacy for part-of-speech (POS) tagging and analyzed the impact of removing sentences containing verbs on classifier performance.

**Feature Importance Analysis:**

Employed gradient feature-based importance to identify tokens significantly influencing prediction outcomes.
Identified top importance scores for tokens and their corresponding POS tags from each sentence.
Analyzed the results to gain insights into the key features driving the model's predictions.

**Documentation and Reporting:**

Documented the entire project including data preprocessing steps, model development, and analysis techniques.
Generated reports summarizing the findings, insights, and recommendations.




**Extra Information about the Project:**

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

