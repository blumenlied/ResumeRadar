import io
from pdfminer.high_level import extract_text
from cleantext import clean


def cleaner(text):
    return clean(
        "some input",
        fix_unicode=True,  # fix various unicode errors
        to_ascii=True,  # transliterate to closest ASCII representation
        lower=False,  # lowercase text
        no_line_breaks=True,  # fully strip line breaks as opposed to only normalizing them
        no_urls=False,  # replace all URLs with a special token
        no_emails=False,  # replace all email addresses with a special token
        no_phone_numbers=False,  # replace all phone numbers with a special token
        no_numbers=False,  # replace all numbers with a special token
        no_digits=False,  # replace all digits with a special token
        no_currency_symbols=False,  # replace all currency symbols with a special token
        no_punct=False,  # remove punctuations
        lang="en",  # set to 'de' for German special handling
    )


def clean_text(text):
    return clean(text)


def parse(pdf: bytes):
    pdf_file = io.BytesIO(pdf)
    text = extract_text(pdf_file)
    return clean(text)
