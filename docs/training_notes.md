# Training Details

## Training Data
- The TharoGEco model was trained on a diverse corpus of text from various sources, including books, articles, and websites.
- The training data is filtered to ensure high-quality and relevance.

## Training Configuration
- **Batch size:** 4096 tokens per batch.
- **Learning rate:** Adam optimizer with learning rate 1e-4.
- **Training steps:** 500,000 iterations.
- **Hardware:** Trained on multiple A100 GPUs for parallel computation.

## Evaluation Metrics
- **Perplexity:** Measures how well the model predicts unseen data.
- **BLEU Score:** Evaluates the quality of generated text compared to reference texts.