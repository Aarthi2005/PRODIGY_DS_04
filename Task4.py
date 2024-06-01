import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\aarth\\OneDrive\\Documents\\twitter_training.csv")

print(data.head())

col_names = ['ID', 'Entity', 'Sentiment', 'Content']
df = pd.read_csv("C:\\Users\\aarth\\OneDrive\\Documents\\twitter_training.csv", names=col_names)

print(data.head())

print(df.isnull().sum())

print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

sentiment= df['Sentiment'].value_counts()
print(sentiment)


plt.figure(figsize=(8, 5))
sentiment.plot(kind='bar', color=['pink', 'lightblue', 'violet', 'orange'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('No of Tweets')
plt.xticks(rotation=0)
plt.show()


brand= df[df['Entity'].str.contains('Facebook', case=False)]
brand_sentiment= brand['Sentiment'].value_counts()
print(brand_sentiment)

plt.figure(figsize=(6, 6))
plt.pie(brand_sentiment, labels=brand_sentiment.index, autopct='%1.1f%%')
plt.title('Sentiment Distribution for Facebook')
plt.show()
     
     
     
     