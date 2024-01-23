class BasePhonemizer:
    """
    Base class for phonemizer
    """

    def __init__(self, language=None):
        raise NotImplementedError("Not implemented")
    
    def phonemize(self, **kwargs):
        raise NotImplementedError("Not implemented")