# stock-trend-prediction
use the twitter bag of words i.e #APPL and use it to learn the stock trends ( from yahoo and financial data). Based on the learnt model predict the stock trends from the twitter data using pandas, tensorflow
How it works?
Step 1. Collect historical tweets about companies using twitter API based on hashtag. Ex #Apple
Step 2. Calculate the scores if its negative or positive using sentimental analysis for each tweet
Step 3. Train the model using the tweets score for the day and stock price on that partcular day. Tweets score will be independent variable & Stock price will be dependent.
Step 4. Predict and test the accuracy of each model.

What's being done?
Part 1:
Step 1. We collect tweets using the twitter API  based on APPl hashtag for a week.
Step 2. Get stock data for the week.
Step 3. Tain the model and predict

Result : As the data is too little to predict anything we couldn't get proper results. We coudn't collect more data due to the limitations of twitter API.
Part 2:
Step 1. We found a prepared dataset of Apple stock prices with tweets.
Step 2. Process the dataset.
Step 3. Tain different models and predict using each model and compare accuracy scores.