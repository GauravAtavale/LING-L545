## Q1. Why should we split punctuation from the token it goes with ?
Tokenization is the process of breaking a stream of text into individual tokens, which are the basic units of meaning in a language. These tokens can be words, numbers, symbols, or other elements that make up the text. Tokenization is typically done by splitting the text on whitespace and punctuations. 
Here are the reasons why we should split punctuation from the token it goes with?

a) By separating punctuation from the tokens, it is easier to consistently apply processing steps to the text. For example, if you want to lowercase all the words in a text, it is easier to do so if the punctuation is already separated from the words.
b) Splitting punctuation from the tokens can make the text easier to read and understand.
c) It becomes easier to make use of NLP libraries and tools if we separate punctuations from tokens

## Q2. Should abbreviations with space in them be written as a single token or two tokens?
How about numerals like 134 000 ?
I think it depends on the context and the specific NLP task we are working on. In some cases, it may be more appropriate to treat abbreviations with spaces as a single token, while in other cases, it may be better to treat them as two separate tokens.
In the case of ‘134 000’, it should be considered as a single token.

## Q3. If you have a case suffix following punctuation, how should it be tokenised ?
I think they have to be treated as two tokens in such cases. By treating case suffixes as separate tokens, we can accurately capture the meaning and structure of the text. Also, this can help in POS tagging.

## Q4. Should contractions and clitics be a single token or two (or more) tokens ?
Examples of Contraction words are can't (for ‘cannot’), won't (for ‘will not’), and it's (for it is). Examples of clitics in English include ‘ve’ (for have), and ‘re’ (for ‘are’). They can be tokenized into two or more tokens depending on the context. 
