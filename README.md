**Task Overview**

Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands.

**Data Description**

The dataset used in the code appears to be Twitter data, likely containing tweets along with associated metadata such as IDs, entities, sentiment labels, and content.

**Output**

1.Display of Data: The script prints the first few rows of the dataset to provide an overview of the data structure.

2.Data Cleaning:

    Renaming Columns: The script renames columns to more descriptive names (ID, Entity, Sentiment, Content).
  
    Handling Missing Values: It checks for missing values in the DataFrame (df) using isnull().sum() and reports the count of missing values for each column.
  
    Handling Duplicates: It checks for duplicated rows in the DataFrame (df) using duplicated().sum() and removes duplicates using drop_duplicates(inplace=True).
  
3.Sentiment Analysis:

    Sentiment Distribution: The script analyzes the sentiment distribution of the tweets and prints the counts of tweets for each sentiment label.
    
    Sentiment Visualization: It visualizes the sentiment distribution using a bar chart (plt.bar) with sentiment labels on the x-axis and the number of tweets on the y-axis.
    
4.Brand-specific Analysis:

    Filtering Tweets by Brand: It filters tweets related to a specific brand (e.g., Facebook) from the DataFrame.
    
    Brand Sentiment Distribution: It analyzes the sentiment distribution of the filtered tweets for the specific brand and prints the counts of tweets for each sentiment label.
    
    Brand Sentiment Visualization: It visualizes the sentiment distribution for the specific brand using a pie chart (plt.pie) with sentiment labels as wedges and the percentage of tweets for each sentiment label.

**Knowledge Gained**

1.Data Preprocessing: Understanding how to handle missing values and duplicated rows in the dataset to ensure data quality.

2.Data Visualization: Learning how to visualize the sentiment distribution of tweets using bar charts and pie charts to gain insights into public opinion.

3.Brand-specific Analysis: Understanding how to filter data based on specific criteria (e.g., brand name) and analyze sentiment distribution for a subset of data.
