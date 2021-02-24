import jellyfish


class StringAnalysis:

    def __init__(self, string_stream):
        self.string_stream = string_stream

    def get_most_similar_word(self, word):
        """
        Returns the most similar word on the corpus as measured by the Jaro distance.

        :param word: desired query word.
        :return: the most similar word on the corpus (defined on the class constructor).
        """
        scores = list(map(lambda x: jellyfish.jaro_distance(x, word),
                          self.string_stream))
        max_score = max(zip(scores, range(len(scores))))[1]
        return self.string_stream[max_score]
