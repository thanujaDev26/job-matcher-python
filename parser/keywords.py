import yake

def extract_keywords(text: str):
    kw_extractor = yake.KeywordExtractor(lan="en", n=1, top=10)
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, score in keywords]
