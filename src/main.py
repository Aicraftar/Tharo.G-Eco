# main.py

import torch
from torch import optim
from src.models.model import SimpleNeuralNetwork
from src.utils.helpers import get_data_loaders, save_model, load_model
import json
from config.hyperparameters import hyperparams

def train_model():
    """Train the neural network model."""
    # Initialize the model, loss function, and optimizer
    input_dim = 4
    hidden_dim = 10
    output_dim = 3
    model = SimpleNeuralNetwork(input_dim, hidden_dim, output_dim)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=hyperparams['learning_rate'])
    
    # Get data loaders
    train_loader, test_loader = get_data_loaders(hyperparams['batch_size'])
    
    # Training loop
    num_epochs = hyperparams['num_epochs']
    for epoch in range(num_epochs):
        running_loss = 0.0
        for i, (inputs, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        epoch_loss = running_loss / len(train_loader)
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')
        logger.info(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')
    
    # Save the model
    save_model(model, 'models/checkpoints/final_model.pth')

def main():
    train_model()

if __name__ == "__main__":
    main()