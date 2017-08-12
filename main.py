import nltk
import wikipedia

thumbs_up = '👍'
thumbs_down = '👎'


def load_sentiment_data(positive_filename, negative_filename):
	global positive_list, negative_list
	positive_list = open(positive_filename).read().splitlines()
	negative_list = open(negative_filename).read().splitlines()

def getwikitext(title):
	try:
		print('Fetching data from Wikipedia...')
		page = wikipedia.page(title)
		text = page.content
	except wikipedia.exceptions.PageError:
		return 'PageError'

	return text


def sentiment_analysis(topic):
	text = getwikitext(topic)
	if (text == 'PageError'):
		print('No matching document found on Wikipedia. Try another keyword.')
		return

	# tokenize the text
	print('Tokenizing...')
	tokens = nltk.word_tokenize(text)

	token_sentiment_dict = dict()

	print('Analyzing...')
	# look for positive/negative words in the text
	for token in tokens:
	    if (token in positive_list):
	        token_sentiment_dict[token] = 'positive'
	    elif (token in negative_list):
	        token_sentiment_dict[token] = 'negative'

	positive_count = list(token_sentiment_dict.values()).count('positive')
	negative_count = list(token_sentiment_dict.values()).count('negative')

	score_diff = positive_count - negative_count
	score_msg = '(Score: ' + str(score_diff) + ')'

	print ('\n[ Result ]')
	if (score_diff > 0):
	    print ('g' + 'o' * score_diff + 'd', thumbs_up, score_msg)
	elif (score_diff < 0):
	    print ('B' + 'a' * abs(score_diff) + 'd', thumbs_down, score_msg)
	else:
	    print ('Hmm... not sure.')

	print()
	print("Positive score: ", positive_count)
	print("Negative score: ", negative_count)

def main():
	load_sentiment_data('positive-words.txt', 'negative-words.txt')
	topic = input("Enter the word: ")
	sentiment_analysis(topic)

if __name__ == '__main__':
	main()