# Adapted from https://github.com/Kyubyong/g2p/issues/29#issuecomment-1841937554

from .phonemap import BasePhonemizer
from gruut import sentences
from collections.abc import Iterable
from g2p_en import G2p
import string

phonemap = {
    '<pad>': '<pad>',
    '<unk>': '<unk>',
    '<s>': '<s>',
    '</s>': '</s>',
    'AA0': 'ɑ',
    'AA1': 'ˈɑː',
    'AA2': 'ˌɑ',
    'AE0': 'æ',
    'AE1': 'ˈæ',
    'AE2': 'ˌæ',
    'AH0': 'ə',
    'AH1': 'ˈʌ',
    'AH2': 'ˌʌ',
    'AO0': 'ɔ',
    'AO1': 'ˈɔː',
    'AO2': 'ˌɔ',
    'AW0': 'aʊ',
    'AW1': 'ˈaʊ',
    'AW2': 'ˌaʊ',
    'AY0': 'aɪ',
    'AY1': 'ˈaɪ',
    'AY2': 'ˌaɪ',
    'B': 'b',
    'CH': 'tʃ',
    'D': 'd',
    'DH': 'ð',
    'EH0': 'ɛ',
    'EH1': 'ˈɛ',
    'EH2': 'ˌɛ',
    'ER0': 'ɚ',
    'ER1': 'ˈɚ',
    'ER2': 'ˌɚ',
    'EY0': 'eɪ',
    'EY1': 'ˈeɪ',
    'EY2': 'ˌeɪ',
    'F': 'f',
    'G': 'g',
    'HH': 'h',
    'IH0': 'ɪ',
    'IH1': 'ˈɪ',
    'IH2': 'ˌɪ',
    'IY0': 'i',
    'IY1': 'ˈiː',
    'IY2': 'ˌi',
    'JH': 'dʒ',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'NG': 'ŋ',
    'OW0': 'oʊ',
    'OW1': 'ˈoʊ',
    'OW2': 'ˌoʊ',
    'OY0': 'ɔɪ',
    'OY1': 'ˈɔɪ',
    'OY2': 'ˌɔɪ',
    'P': 'p',
    'R': 'ɹ',
    'S': 's',
    'SH': 'ʃ',
    'T': 't',
    'TH': 'θ',
    'UH0': 'ʊ',
    'UH1': 'ˈʊ',
    'UH2': 'ˌʊ',
    'UW': 'uː',
    'UW0': 'u',
    'UW1': 'ˈuː',
    'UW2': 'ˌu',
    'V': 'v',
    'W': 'w',
    'Y': 'j',
    'Z': 'z',
    'ZH': 'ʒ',
}

class G2PPhonemizer(BasePhonemizer):
    """
    G2P EN phonemizer
    """
    def __init__(self, language='en'):
        if language.lower().strip() == 'en': language = 'en-us'
        if language.lower().strip() != 'en-us':
            raise NotImplementedError('G2PPhonemizer only supports English')
        self.language = language
        self.g2p = G2p()
    def phonemize(self, text, punctuation=True, **kwargs):
        phones = self.g2p(text, **kwargs)
        result = ''
        for phone in phones:
            if phone in phonemap:
                result += phonemap[phone]
            else:
                result += phone
        if not punctuation:
            for p in string.punctuation:
                result = result.replace(p, '')
        return result.strip()