from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# (a) Download and load MNIST dataset
print("Loading MNIST dataset...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target.astype(int)
print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features each")

# (b) Preprocess: normalise pixel values (0-255 → 0-1)
X = X / 255.0

# Split into training and test sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train a Multi-Layer Perceptron classifier
print("Training classifier... (this takes ~2 min)")
clf = MLPClassifier(
    hidden_layer_sizes=(128, 64),
    max_iter=20,
    random_state=42,
    verbose=True
)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualise some predictions
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"True: {y_test[i]}  Pred: {y_pred[i]}")
    ax.axis('off')
plt.suptitle("MNIST Digit Predictions (Task 1)")
plt.tight_layout()
plt.savefig("mnist_predictions.png")
plt.show()