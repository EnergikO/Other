from googletrans import Translator


def translate(src: str, language: str='ru') -> str:
	return Translator().translate(src, dest=language).text

