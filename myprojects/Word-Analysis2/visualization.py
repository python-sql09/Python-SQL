import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plots
import matplotlib.pyplot as plt

def visualize_word_frequencies(word_frequencies):
    #words, counts = zip(*word_frequencies.items())
    words = list(word_frequencies.keys())
    counts = list(word_frequencies.values())
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)  # Create the bar plot
    plt.xlabel('Words')      # Set the x-axis label
    plt.ylabel('Frequency')   # Set the y-axis label
    plt.title('Word Frequencies')  # Set the plot title
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()        # Adjust layout for better fit
    
    # Save the plot instead of showing it
    plt.savefig('/home/linuxdeepa/python-sql09/Python-SQL/myprojects/Word-Analysis2/word_frequencies.png')  # Save the figure
    plt.close()  # Close the plot to free up memory