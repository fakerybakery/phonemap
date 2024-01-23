# Adapted from https://github.com/sidharthrajaram/StyleTTS2/blob/main/src/styletts2/phoneme.py

from .phonemap import BasePhonemizer
from gruut import sentences
from collections.abc import Iterable


class GruutPhonemizer(BasePhonemizer):
    """
    Gruut phonemizer
    """
    def __init__(self, language='en'):
        if language.lower().strip() == 'en': language = 'en-us'
        self.language = language
    def phonemize(self, text, **kwargs):
        phonemized = []
        for sent in sentences(text, lang=self.language, **kwargs):
            for word in sent:
                if isinstance(word.phonemes, Iterable):
                    phonemized.append(''.join(word.phonemes))
                elif isinstance(word.phonemes, str):
                    phonemized.append(word.phonemes)
        phonemized_text = ' '.join(phonemized)
        return phonemized_text