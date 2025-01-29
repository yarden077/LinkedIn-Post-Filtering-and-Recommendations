# LinkedIn Post Filtering and Recommendation System  
![Poster]()

## 📌 Project Overview  
This project introduces an AI-driven filtering feature for LinkedIn posts, classifying them into three distinct labels. Users can personalize their feeds by selecting preferred topics while excluding unwanted content. Additionally, our system analyzes LinkedIn user profiles to suggest the most relevant posts based on their professional interests.  

## 🎯 Motivation  
LinkedIn feeds can become cluttered with diverse content, from job postings and career achievements to general discussions and personal experiences. Our primary use case is job hunting, so we aimed to develop a filtering system that prioritizes job-related posts, enhancing user experience and making feeds more relevant.  

## 📊 Data Collection & Integration  
- **LinkedIn Data**: Sourced from BrightData, including company posts and user profiles (about section, certifications, education, job positions, authored posts, and courses).  
- **Reddit Data**: Scraped 19,925 posts using Selenium, cleaned to 8,726 posts from 11 subreddits (e.g., AI, Career Advice, Job Posting).  
- **Integration**: We linked LinkedIn posts with the most similar Reddit posts using cosine similarity, leveraging subreddit topics for classification.  

## 🔍 Data Processing & Analysis  
- **Feature Selection**: Focused on LinkedIn post titles and bodies for classification; user profiles (education, certifications, etc.) for recommendations.  
- **Visualizations**: Analyzed word frequencies in LinkedIn posts and created a word cloud from company "About" sections to guide subreddit selection.  

## 🤖 AI Methodologies  
1. **Reddit Post Tagging**: Used subreddit categories, pre-existing post labels, and a word detection dictionary (expanded with ChatGPT).  
2. **Embedding & Similarity Matching**: Applied `UniversalSentenceEncoder` to embed posts and calculated cosine similarity to assign labels.  
3. **Refining Labels**: Used `DeBERTa-Zero-Shot-Classification` to refine post labels, selecting the most relevant three.  
4. **User-Post Recommendations**: Created user embeddings from profile data and matched them with post embeddings to recommend the most relevant content.  

## 📈 Evaluation & Results  
- Lacking pre-labeled data, we manually evaluated results and compared them with ChatGPT-generated labels, concluding our method performed better.  
- Example case: A senior developer received relevant tags like "career_advice" but also less useful ones like "job_posting."  
- Analysis of assigned labels confirmed that job-related and discussion-based tags were most prevalent.  

## 🚧 Challenges & Limitations  
- **LLMs Performance Issues**: Models like LLaMA and Spark NLP underperformed, leading us to pivot to Reddit-based categorization.  
- **Lack of Explicit User Engagement Data**: Used cosine similarity to bridge the gap between user profiles and post categories.  

## ✅ Conclusion  
Our system successfully classifies LinkedIn posts and provides relevant recommendations by integrating LinkedIn and Reddit data. Overcoming challenges with LLMs and data limitations, we demonstrated how diverse data sources and AI techniques can enhance content filtering and recommendation.  

---  

## 📂 Project Structure  
```plaintext
📦 LinkedIn-Post-Filtering  
├── 📂 data/                     # Datasets and processed files  
├── 📂 models/                   # Trained models and embeddings  
├── 📂 notebooks/                # Jupyter Notebooks for data analysis  
├── 📂 scripts/                  # Python scripts for preprocessing & model training  
├── 📜 Project.ipynb             # Main Jupyter Notebook  
├── 📜 requirements.txt          # Dependencies list  
└── 📜 README.md                 # Project documentation  
```  

## 🚀 Installation & Usage  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/LinkedIn-Post-Filtering.git  
cd LinkedIn-Post-Filtering  
```  

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt  
```  

### 3️⃣ Run the Jupyter Notebook  
```bash
jupyter notebook Project.ipynb  
```  

## 👥 Contributors  
- **Maor ZLk** - [[GitHub Profile](https://github.com/MaorZLk)]
- **Yuval Komar** - [[GitHub Profile](https://github.com/yuvalkomar)]
- 
- **Other Contributors**  

## 📜 References  
- [ChatGPT](https://chatgpt.com)  
- [LinkedIn](https://www.linkedin.com/)  
- [Spark NLP](https://sparknlp.org/2020/04/17/tfhub_use.html)  
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)  
- [Hugging Face DeBERTa](https://huggingface.co/DeBERTa-Zero-Shot-Classification)  
