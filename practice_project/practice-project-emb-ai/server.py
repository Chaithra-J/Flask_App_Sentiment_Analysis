''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request #Import Flask, render_template, request from the flask pramework package : TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer #Import the sentiment_analyzer function from the package created: TODO

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    test_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(test_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return 'Invalid input! try again'
    else:
        return 'The given text has been identified as {} with a score {}' .format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run(host="0.0.0", port=5000)