# src/utils/helpers.py

import torch
from torch.utils.data import DataLoader
import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

logging.basicConfig(filename='logs/training.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data():
    """Load the Iris dataset and split into training and test sets."""
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def normalize_data(X_train, X_test):
    """Normalize the data using mean and standard deviation."""
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    X_train_norm = (X_train - mean) / std
    X_test_norm = (X_test - mean) / std
    return X_train_norm, X_test_norm

def get_data_loaders(batch_size):
    """Return DataLoaders for training and test data."""
    X_train, X_test, y_train, y_test = load_data()
    X_train_norm, X_test_norm = normalize_data(X_train, X_test)
    
    train_dataset = torch.utils.data.TensorDataset(torch.FloatTensor(X_train_norm), torch.LongTensor(y_train))
    test_dataset = torch.utils.data.TensorDataset(torch.FloatTensor(X_test_norm), torch.LongTensor(y_test))
    
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader

def save_model(model, path):
    """Save the model to the specified path."""
    torch.save(model.state_dict(), path)
    logger.info(f"Model saved at {path}")

def load_model(model, path):
    """Load the model from the specified path."""
    model.load_state_dict(torch.load(path))
    model.eval()
    logger.info(f"Model loaded from {path}")