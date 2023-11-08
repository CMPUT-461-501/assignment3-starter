import argparse
import math
from collections import Counter, defaultdict

# Function to read data from a file
def read_data(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]

# Function to train a unigram model
def train_unigram(sequences):
    model = Counter([phoneme for sequence in sequences for phoneme in sequence])
    total_count = sum(model.values())
    for phoneme in model:
        model[phoneme] = (model[phoneme] + 1) / (total_count + len(model))  # Applying Laplace smoothing
    return model

# Function to train a bigram or trigram model
def train_ngram(sequences, n, laplace=False):
    model = defaultdict(Counter)
    for sequence in sequences:
        padded_sequence = ['<s>'] * (n-1) + sequence + ['</s>']
        for i in range(len(padded_sequence) - n + 1):
            context = tuple(padded_sequence[i:i+n-1])
            token = padded_sequence[i+n-1]
            model[context][token] += 1

    # Apply Laplace smoothing if requested
    if laplace:
        vocab_size = len(set(token for sequence in sequences for token in sequence)) + 1  # +1 for unknown token
        for context in model:
            for token in model[context]:
                model[context][token] += 1
            model[context]['<unk>'] = 1
            context_total = sum(model[context].values())
            for token in model[context]:
                model[context][token] /= context_total
    else:
        for context in model:
            context_total = sum(model[context].values())
            for token in model[context]:
                model[context][token] /= context_total

    return model
# Function to compute perplexity
def compute_perplexity(model, sequences, n, laplace=False):
    perplexity = 0
    N = 0
    for sequence in sequences:
        # For unigram models, we do not use context
        if n == 1:
            for token in sequence:
                N += 1
                probability = model.get(token, model.get('<unk>', 0))
                
                # Check for zero probability and assign a very small probability to avoid log(0)
                if probability == 0:
                    probability = 1e-10
                
                perplexity += -math.log(probability)
        else:
            padded_sequence = ['<s>'] * (n-1) + sequence + ['</s>']
            for i in range(len(padded_sequence) - n + 1):
                context = tuple(padded_sequence[i:i+n-1])
                token = padded_sequence[i+n-1]
                N += 1
                probability = model[context][token] if token in model[context] else model[context].get('<unk>', 0)
                
                # Check for zero probability and assign a very small probability to avoid log(0)
                if probability == 0:
                    probability = 1e-10
                
                perplexity += -math.log(probability)
    
    perplexity = math.exp(perplexity / N)
    return perplexity

# Main function to handle command-line arguments and train models
def main():
    parser = argparse.ArgumentParser(description='Train n-gram models and compute perplexity.')
    parser.add_argument('model_type', choices=['unigram', 'bigram', 'trigram'], help='Type of n-gram model')
    parser.add_argument('training_data_path', type=str, help='Path to the training data file')
    parser.add_argument('evaluation_data_path', type=str, help='Path to the evaluation data file')
    parser.add_argument('--laplace', action='store_true', help='Apply Laplace smoothing')
    args = parser.parse_args()

    training_sequences = read_data(args.training_data_path)
    evaluation_sequences = read_data(args.evaluation_data_path)
    n = {'unigram': 1, 'bigram': 2, 'trigram': 3}[args.model_type]

    if args.model_type == 'unigram':
        model = train_unigram(training_sequences)
    else:
        model = train_ngram(training_sequences, n, laplace=args.laplace)

    perplexity = compute_perplexity(model, evaluation_sequences, n, laplace=args.laplace)
    print(f'Perplexity: {perplexity}')

if __name__ == '__main__':
    main()
