from dp.phonemizer import Phonemizer
from cached_path import cached_path

class DeepPhonemizer:
    """
    DeepPhonemizer phonemizer
    """

    def __init__(self, language='en'):
        if language.lower().strip() == 'en': language = 'en-us'
        if language.lower().strip() != 'en-us':
            raise NotImplementedError('DeepPhonemizer only supports English')
        self.language = language
        self.ph = Phonemizer.from_checkpoint(cached_path('hf://mrfakename/deep-phonemizer/en_us_cmudict_ipa.pt'))
    
    def phonemize(self, text, **kwargs):
        return self.ph(text, lang=self.language.replace('-', '_'), **kwargs)