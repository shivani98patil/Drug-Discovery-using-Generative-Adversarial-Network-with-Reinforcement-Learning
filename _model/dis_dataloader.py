import numpy as np

from re import compile as _Re
"""Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes)
. However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string
 with a byte pattern or vice-versa; similarly, when asking for a substitution, the replacement string must
 be of the same type as both the pattern and the search string.Regular expressions use the backslash
 character ('\') to indicate special forms or to allow special characters to be used without invoking 
 their special meaning. This collides with Python’s usage of the same character for the same purpose in 
 string literals; for example, to match a literal backslash, one might have to write '\\\\' as the pattern
 string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a 
 regular Python string literal. Also, please note that any invalid escape sequences in Python’s usage of
 the backslash in string literals now generate a DeprecationWarning and in the future this will become a 
 SyntaxError. This behaviour will happen even if it is a valid escape sequence for a regular expression."""




def split_unicode_chrs(text):

    _unicode_chr_splitter = _Re('(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)').split
    """complie library is used and we have used split function for the task which is to split the discriminator dada
    split function splits the characters and put it in list.
    ?: , *? and ?P when include those characters are included."""
    return [chr for chr in _unicode_chr_splitter(text) if chr]
""" for return statemnet we are iterating through the list."""





class Dis_dataloader():

    def __init__(self):

        self.vocab_size = 5000



    def load_data_and_labels(self, positive_examples, negative_examples):

        """ we are talking about the generator generated data and actual data """

        x_text = positive_examples + negative_examples



        # Generate labels

        positive_labels = [[0, 1] for _ in positive_examples]

        negative_labels = [[1, 0] for _ in negative_examples]

        y = np.concatenate([positive_labels, negative_labels], 0)



        x_text = np.array(x_text)

        y = np.array(y)

        return [x_text, y]



    def load_train_data(self, positive_file, negative_file):

        """this loads the data in the discriminator by shuffling the data so that discriminator would not find 
        which data is what."""

        # Load and preprocess data

        drug, labels = self.load_data_and_labels(positive_file, negative_file)

        shuffle_indices = np.random.permutation(np.arange(len(labels)))

        x_shuffled = drug[shuffle_indices]

        y_shuffled = labels[shuffle_indices]

        self.sequence_length = 20

        return [x_shuffled, y_shuffled]



    def load_test_data(self, positive_file, test_file):

        test_examples = []

        test_labels = []

        with open(test_file)as fin:

            for line in fin:

                line = line.strip() # Removes starting and end characters.

                line = line.split()

                parse_line = [int(x) for x in line]

                test_examples.append(parse_line)

                test_labels.append([1, 0])



        with open(positive_file)as fin:

            for line in fin:

                line = line.strip()

                line = line.split()

                parse_line = [int(x) for x in line]

                test_examples.append(parse_line)

                test_labels.append([0, 1])



        test_examples = np.array(test_examples)

        test_labels = np.array(test_labels)
        

        shuffle_indices = np.random.permutation(np.arange(len(test_labels)))

        x_dev = test_examples[shuffle_indices]

        y_dev = test_labels[shuffle_indices]



        return [x_dev, y_dev]



    def batch_iter(self, data, batch_size, num_epochs):

        """

        Generates a batch iterator for a dataset.

        """

        data = np.array(list(data))

        data_size = len(data)

        num_batches_per_epoch = int(len(data) / batch_size) + 1

        for epoch in range(num_epochs):

            # Shuffle the data at each epoch

            shuffle_indices = np.random.permutation(np.arange(data_size))

            shuffled_data = data[shuffle_indices]

            for batch_num in range(num_batches_per_epoch):

                start_index = batch_num * batch_size

                end_index = min((batch_num + 1) * batch_size, data_size)
                """ min(iterable, *[, default=obj, key=func])"""

                yield shuffled_data[start_index:end_index]
    """The yield statement suspends function’s execution and sends a value back to the caller,
    but retains enough state to enable function to resume where it is left off. When resumed, 
    the function continues execution immediately after the last yield run. 
    This allows its code to produce a series of values over time, rather than computing them at once and 
    sending them back like a list."""