# write your code here
import pandas as pd

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.term = False
        self.label = None
        self.feature = None
        self.value = None

    def set_split(self, feature, value):
        self.feature = feature
        self.value = value

    def set_term(self, label):
        self.term = True
        self.label = label


class DecisionTree:
    def __init__(self, min_samples=1):
        self.root = None
        self.min_samples = min_samples

    def _gini_impurity(self, labels):
        tot_samples = len(labels)
        if tot_samples == 0:
            return 0

        class_count = {}
        for label in labels:
            class_count[label] = class_count.get(label, 0) + 1

        gini = 1.0
        for count in class_count.values():
            prob = count / tot_samples
            gini -= prob ** 2

        return gini

    def _weighted_gini(self, node1, node2):
        tot_samples = len(node1) + len(node2)
        if tot_samples == 0:
            return 0

        gini_node1 = self._gini_impurity(node1)
        gini_node2 = self._gini_impurity(node2)

        weighted = (len(node1) / tot_samples) * gini_node1 + (len(node2) / tot_samples) * gini_node2

        return round(weighted, 5)

    def _find_best_split(self, data, target):
        min_gini = float('inf')
        best_feature = None
        best_value = None
        best_left_idx = []
        best_right_idx = []

        for feature in data.columns:
            unique_values = data[feature].unique()
            for value in unique_values:
                left_idx = data.index[data[feature] == value].tolist()
                right_idx = data.index[data[feature] != value].tolist()

                left_node = target[left_idx]
                right_node = target[right_idx]

                weighted = self._weighted_gini(left_node, right_node)

                if weighted < min_gini:
                    min_gini = weighted
                    best_feature = feature
                    best_value = value
                    best_left_idx = left_idx
                    best_right_idx = right_idx

        return min_gini, best_feature, best_value, best_left_idx, best_right_idx

    def _recursive_split(self, node, data, target):
        """Recursively split data into decision tree nodes."""
        if len(data) < self.min_samples or self._gini_impurity(target) == 0 or (data.nunique() == 1).all():
            label = target.mode()[0]
            node.set_term(label)
            return

        min_gini, best_feature, best_value, best_left_idx, best_right_idx = self._find_best_split(data, target)

        if best_feature is None:
            label = target.mode()[0]
            node.set_term(label)
            return

        # Assign split condition to the node
        node.set_split(best_feature, best_value)

        # Debug tree structure
        # print(f"Splitting on feature {best_feature} with value {best_value}")

        # Create left child
        left_data = data.loc[best_left_idx]
        left_target = target.loc[best_left_idx]
        node.left = Node()
        self._recursive_split(node.left, left_data, left_target)

        # Create right child
        right_data = data.loc[best_right_idx]
        right_target = target.loc[best_right_idx]
        node.right = Node()
        self._recursive_split(node.right, right_data, right_target)

    def fit(self, data, target):
        self.root = Node()
        self._recursive_split(self.root, data, target)

    def _predict_sample(self, node, sample):
        """Recursively predict the label for a single sample."""
        # If this is a terminal (leaf) node, return the prediction.
        if node.term:
            print(f"   Predicted label: {node.label}")
            return node.label

        # Log the feature and sample value
        sample_value = sample[node.feature]
        print(f"   Considering decision rule on feature {node.feature} with value {sample_value}")

        # Go to the left child first if condition is met
        if sample_value == node.value:
            return self._predict_sample(node.left, sample)  # Explore left first
        else:
            return self._predict_sample(node.right, sample)  # Explore right otherwise

    def predict(self, data):
        """Predict labels for a set of new observations."""
        predictions = []
        for i, sample in data.iterrows():
            print(f"Prediction for sample # {i}")
            predictions.append(self._predict_sample(self.root, sample))
        return predictions

train_path, test_path = input().split()
train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)
target = train_data['Survived']
features = train_data.drop(['Survived', 'Unnamed: 0'], axis=1)

tree = DecisionTree(min_samples=1)
tree.fit(features, target)

test_features = test_data.drop(['Unnamed: 0'], axis=1)
predictions = tree.predict(test_features)
