# first line: 1
@memory.cache
def evaluate_subset(selected_features):
    """Evaluate the SVM model with the selected features."""
    X_train_subset = X_train[:, selected_features]
    X_test_subset = X_test[:, selected_features]

    clf = SVC(kernel='linear', probability=True, C=1.0)  # Use fixed kernel for speed
    clf.fit(X_train_subset, y_train)
    y_pred = clf.predict(X_test_subset)
    
    return accuracy_score(y_test, y_pred)
