# 1. Read Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_dir = "data/"
origional_data = pd.read_csv(data_dir + "spam.csv", encoding = "latin-1")
print(origional_data.head())
print(origional_data.shape)
label = origional_data.v1
data = origional_data.v2
print(label.head())
print(data.head())

############################################################
# 2. Train using model of Naive Bayes
# 80% of data for traning dataset and 20% of data for test dataset
from sklearn.model_selection import train_test_split

data_train, data_test, label_train, label_test = train_test_split(data, 
                                                                  label, 
                                                                  test_size = 0.2, 
                                                                  random_state = 0)

print(data_train.shape, data_test.shape, label_train.shape, label_test.shape)
print(data_train.head())
print(data_test.head())

# Calculate the frequency of word
vectorizer = Vectorizer()
data_train_counts = vectorizer.fit_transform(data_train)
data_test_counts = vectorizer.transform(data_test, vectorizer.vocablary)
print ('Number of all the unique words : ' + str(len(vectorizer.vocablary)))

print("train:")
print(len(data_train_counts))

print("test:")
print(len(data_test_counts))

word_freq = pd.DataFrame({"word": vectorizer.vocablary, "occurrences": np.array(data_train_counts).sum(axis = 0)})
word_freq["frequency"] = word_freq.occurrences / np.sum(word_freq.occurrences)

plt.plot(word_freq.occurrences)
plt.xlabel("index")
plt.ylabel("word occurrences")
plt.show()

word_freq_sort = word_freq.sort_values(by = "occurrences", ascending = False)
word_freq_sort.head()

# Traning begin
bayes = NBayes()
bayes.fit(data_train_counts, label_train.values)
label_pred = bayes.predict(data_test_counts)
print(len(label_pred))

#######################################################
# 3. How is this model: validation
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.cross_validation import cross_val_score

print("accuracy: ", accuracy_score(label_test, label_pred))
print(classification_report(label_test, label_pred))
print(confusion_matrix(label_test, label_pred))
