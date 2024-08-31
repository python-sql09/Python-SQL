from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Combine all word counts into one dictionary
def aggregate_word_counts(dataset_word_count):
    aggregate_counts = Counter()
    for review in dataset_word_count:
        aggregate_counts.update(review[WORD_COUNT_KEY])
    return aggregate_counts

# Find the top N words
def top_n_words(aggregate_counts, n=10):
    return aggregate_counts.most_common(n)

# Generate word cloud
def generate_word_cloud(aggregate_counts):
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(aggregate_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Example usage
aggregate_counts = aggregate_word_counts(dataset_word_count)
print("Top 10 Words:", top_n_words(aggregate_counts))

# Display Word Cloud
generate_word_cloud(aggregate_counts)