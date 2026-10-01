import csv
import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    # የቢቢሲ ዜና ድረ-ገጽ ሊንክ
    url = "https://bbc.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    print("መረጃ ከመስመር ላይ እየተሰበሰበ ነው...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # የዜና ርዕሶችን መፈለጊያ (HTML tags)
        headlines = soup.find_all(['h2', 'h3'])
        
        # የኤክሴል ፋይል መክፈቻ
        with open('bbc_news_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['No', 'News Headline']) # የአምድ ስሞች
            
            count = 1
            saved_titles = set()
            
            for headline in headlines:
                title = headline.get_text().strip()
                # አጫጭርና ተደጋጋሚ ርዕሶችን ለማስቀረት
                if title and len(title) > 20 and title not in saved_titles:
                    writer.writerow([count, title])
                    saved_titles.add(title)
                    count += 1
                    
        print(f"በአጠቃላይ {count-1} ዜናዎች ተሰብስበው 'bbc_news_headlines.csv' በሚል ፋይል ተቀምጠዋል!")
    else:
        print("የድረ-ገጹን መረጃ ማግኘት አልተቻለም። እባክዎ ኢንተርኔትዎን ያረጋግጡ።")

if __name__ == "__main__":
    scrape_bbc_news()
