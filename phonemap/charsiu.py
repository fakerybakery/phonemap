from transformers import T5ForConditionalGeneration, AutoTokenizer

class CharsiuPhonemizer:
    """
    Charsiu phonemizer
    """

    def __init__(self, language='en'):
        if (language == 'en' or language == 'en_us'): language = 'eng-us'
        self.language = language
        self.model = T5ForConditionalGeneration.from_pretrained('charsiu/g2p_multilingual_byT5_tiny_16_layers_100')
        self.tokenizer = AutoTokenizer.from_pretrained('google/byt5-small')

    
    def phonemize(self, text, **kwargs):
        t = f'<{self.language}>: ' + text
        out = self.tokenizer([t], padding=True,add_special_tokens=False, return_tensors='pt')
        preds = self.model.generate(**out, num_beams=1, max_length=1024)
        phones = self.tokenizer.batch_decode(preds.tolist(),skip_special_tokens=True)
        return ' '.join(phones)