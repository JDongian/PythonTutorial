import requests
import json
import re
import numpy as np
import matplotlib.pyplot as plt

word_hist = {}

def add_entries(word_list, word_counts):
    # Iterates over word_list, adding to the counts in word_counts.
    for w in word_list:
        w = w.lower()
        if w in word_counts.keys():
            word_counts[w] += 1
        else:
            word_counts[w] = 1

# URL will take a subreddit name as a string format argument.
url = "http://www.reddit.com/r/%s/new.json"

def get_subreddit_words(subreddit):
    # Grab data using the reddit web API.
    response_raw = requests.get(url % subreddit).content.decode('utf-8')
    # Interpret the data as a JSON object.
    response_json = json.loads(response_raw)
    words_found = []
    # Add all words found in the JSON response to the list words_found.
    for i in range(len(response_json['data']['children'])):
        words_found += re.findall('[\w\d]+',
                response_json['data']['children'][i]['data']['title'])
    return words_found

word_counts_overall = {}
for subreddit in ("circlejerk", "funny"):
    # For each subreddit, add the word frequency count.
    word_list_overall = get_subreddit_words(subreddit)
    add_entries(word_list_overall, word_counts_overall)

# Determine the frequencies for a specific subreddit.
word_counts_sub = {}
add_entries(get_subreddit_words(raw_input("Pick a subreddit: ")), word_counts_sub)
sorted_words_sub = sorted([(k, word_counts_sub[k]) for k in word_counts_sub.keys()],
        key=lambda x: x[1], reverse=True)
words_sub, freq_sub= list(zip(*sorted_words_sub))

# Skip outliers (words occuring less than three times).
freq_sub = [x for x in freq_sub if x > 2]
words_sub = words_sub[:len(freq_sub)]
words_overall = words_sub
freq_overall = [word_counts_overall[w]\
        if (w in word_counts_overall.keys()) else 0\
        for w in words_overall]

ind = np.arange(len(words_overall))     # x-locations for the bar groups
width = 0.35                            # bar width

# Normalize data by converting to percents
sum_sub = sum(freq_sub)
sum_overall = sum(freq_overall)
percentages_sub = [f*100/sum_sub for f in freq_sub]
percentages_overall = [f*100/sum_overall for f in freq_overall]

fig, ax = plt.subplots()
#Plot the overall frequency
rects1 = ax.bar(0.1+ind, percentages_overall, width, color='g')
#Plot the subreddit frequency
rects2 = ax.bar(0.1+ind+width, percentages_sub, width, color='r')

ax.set_ylabel('Percentage of common words')
ax.set_title('Word Frequencies on Reddit')
ax.set_xticks(ind+width*2)
ax.set_xticklabels(words_sub)

ax.legend((rects1[0], rects2[0]), ('Overall', subreddit))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., height+width, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
