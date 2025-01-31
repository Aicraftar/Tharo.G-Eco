# Model Architecture

The model implemented in this project is a simple feedforward neural network designed for classification tasks. Here's an overview of its structure:

## Neural Network Structure
- **Input Layer**: Accepts input features (4 dimensions for Iris dataset).
- **Hidden Layer**: A single hidden layer with 10 neurons using ReLU activation.
- **Output Layer**: Outputs probabilities for each class (3 classes for Iris dataset).

## Activation Functions
- **ReLU (Rectified Linear Unit)**: Used in the hidden layer to introduce non-linearity.
- **Softmax**: Applied in the output layer to convert logits to probabilities.

This architecture is suitable for small to medium-sized datasets and classification tasks with a limited number of classes. The network can be easily extended by adding more layers or units if needed for more complex problems.

