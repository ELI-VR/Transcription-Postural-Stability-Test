import pandas as pd
dic_data={
    'id':[1,2,3,4,5,6,7,8,9,10],
    'Hybrid_0':[
        'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, '
    ],
    'Hybrid_1':['classifying documents to information extraction. Analyzing movie review is one of the classic examples',
                'classifying documents to information extraction. Analyzing movie review is one of the classic examples',
                'classifying documents to information extraction. Analyzing movie review is one of the classic examples',
                'classifying documents to information extraction. Analyzing movie review is one of the classic examples',
                'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
                'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
                'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
                'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
                'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
                'Text mining also referred to as text analytics. Text mining is a process of exploring sizeable textual data and find patterns.'],
    'Hybrid_2':['Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.' #here

    ],
    'Hybrid_3':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.'



    ],
    'Hybrid_4':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.'

    ],
    'FirstPerson_0':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.'

    ],
    'FirstPerson_1':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.'

    ],
    'FirstPerson_2':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',

    ],
    'FirstPerson_3':[
'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Text Mining process the text itself, while NLP process with the underlying metadata. ',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
                'Finding frequency counts of words, length of the sentence, presence/absence of specific words is known as text mining',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.',
'to demonstrate a simple NLP Bag-of-words model, on movie reviews.'

    ],
    'FirstPerson_4':[
'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, '
    ],
    'Blob_0':[
'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, '
    ],
    'Blob_1':[
'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, '
    ],
    'Blob_2':[
'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, '
    ],
    'Blob_3':[
'Text communication is one of the most popular forms of day to day conversion. We chat, message,',
        'tweet, share status, email, write blogs, share opinion and feedback in our daily routine. All of these activities are generating text in a significant amount, which is unstructured in nature. ',
        'I this area of the online marketplace and social media, It is essential to analyze vast quantities of data, to understand peoples opinion.',
        'NLP enables the computer to interact with humans in a natural manner. It helps the computer to understand the human language and derive meaning from it.',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ',
        'NLP is applicable in several problematic from speech recognition, language translation, ' #here
    ],
    'Blob_4':[
        'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ],
    'Bodiless_0':[
'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ],
    'Bodiless_1':[
'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ],
    'Bodiless_2':[
'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ],
    'Bodiless_3':[
'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ],
    'Bodiless_4':[
'NLTK is a powerful Python package that provides a set of diverse natural languages algorithms. ',
        'It is free, opensource, easy to use, large community, and well documented. NLTK consists of the most common algorithms such as tokenizing, part-of-speech tagging, stemming, ',
        'sentiment analysis, topic segmentation, and named entity recognition.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'NLTK helps the computer to analysis, preprocess, and understand the written text.',
        'Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. '
    ]}


for key,value in dic_data.items():
    print(len(value))
df = pd.DataFrame.from_dict(dic_data)
df.to_csv('/home/yesid/Desktop/transcription.csv', index=False)