from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load the iris dataset
iris = datasets.load_iris()
X = iris['data']
y = iris['target']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a Gaussian naive Bayes classifier
classifier = GaussianNB()

# Train the classifier on the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = classifier.predict(X_test)

# Calculate the accuracy of the predictions
accuracy = sum(predictions == y_test) / len(y_test)
print(f'Accuracy: {accuracy:.2f}')
