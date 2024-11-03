import re
import json
  # Example usage
example_text = """This is a sample text. It contains multiple sentences! And even more? Yes, that's right. The quick brown fox jumps over the lazy dog. This sentence is for testing purposes! It contains various punctuation marks, such as commas, semicolons, and colons. Can you split it into meaningful sentences?

Let's add another paragraph here. Integer nec eros vitae justo tincidunt placerat a ut ex. Suspendisse potenti. Vivamus condimentum suscipit lorem at volutpat. Sed et risus nec ipsum tempus aliquam. Phasellus sodales, lectus eget fermentum sollicitudin, nisi nunc commodo nunc, vel posuere orci justo nec velit. Donec venenatis nisi vitae ligula bibendum, vitae hendrerit ligula pulvinar.

"Life is what happens when you're busy making other plans." - John Lennon. This famous quote highlights the unpredictability of life. It's often true, isn't it? Sometimes we meticulously plan our days, only to have unexpected events change everything!
"""

def split_into_sentences(text:str):
    # (?<!\w\.\w.) - Negative lookbehind assertion that ensures that the match is not preceded by a word character, a period, and a word character.
    # (?<![A-Z][a-z]\.) - Negative lookbehind assertion that ensures that the match is not preceded by an uppercase letter, a lowercase letter, and a period.
    # (?<=\.|\?) - Positive lookbehind assertion that ensures that the match is preceded by a period, an exclamation mark or a question mark.
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(pattern, text)
    return sentences

def split_text_into_paragraphs_and_sentences(text: str):
  paragraphs = text.strip().split('\n\n')
  return [split_into_sentences(paragraph) for paragraph in paragraphs]

print(json.dumps(split_text_into_paragraphs_and_sentences(example_text), indent=4))