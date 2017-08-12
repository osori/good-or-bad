# good-or-bad

This is a rude and judgmental python script that judges, based on the word's Wikipedia article, if a word is good or bad. The criteria of good/badness of each word in the article is defined by the positive/negative sentiment word lists from Opinion Lexicon: Positive & Negative (Hu and Liu, 2004).

## Built with
- [NLTK (Natural Language Toolkit)](https://github.com/nltk/nltk) - a Python library for statistical Natural Language Processing
- [wikipedia](https://pypi.python.org/pypi/wikipedia) - a Python library that makes accessing and parsing Wikipedia data easy

## Examples

    Enter the word: North Korea
    
    [ Result ]
    Baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad 👎 (Score: -36)
    
    Positive score:  52
    Negative score:  109

Our judgmental script tells us that North Korea is baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad. Considering the number of a's our script has written, North Korea must be a horribly bad nation!

Now compare it with this:

    Enter the word: South Korea
    
    [ Result ]
    Goooooooooooood 👍 (Score: 13)
    
    Positive score:  173
    Negative score:  160
    
What do you think? Not bad, right?

Any word, if it's on Wikipedia, can be evaluated with this script. Even people, incidents, and so much more! 

    Enter the word: Donald Trump
    
    [ Result ]
    Baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad 👎 (Score: -49)
    # This guy must be a real douche. He's worse than North Korea!
    
    Positive score:  121
    Negative score:  170
    
## Reference
1. Minqing Hu and Bing Liu. "Mining and summarizing customer reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (KDD-2004, full paper), Seattle, Washington, USA, Aug 22-25, 2004.
