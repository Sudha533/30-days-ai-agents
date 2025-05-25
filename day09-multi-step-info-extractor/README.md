
# 🔍 Multi-Step Info Extractor (Day 09 Challenge)

This Python project is part of the AI aGENT Challenge (Day 09). It uses **LangChain**, **OpenAI**, and **SerpAPI** to search the internet and extract structured information (in JSON format) about:

- 👤 People  
- 🏢 Companies  
- 🎬 Movies

---

## 🚀 How It Works

### Step-by-Step Flow:

1. **User enters a topic**  
   Example: `"Elon Musk"` or `"Tesla"` or `"The Matrix"`

2. **Searches the Web**  
   The program uses SerpAPI to get the top 3 search snippets from Google.

3. **Extracts Information**  
   The OpenAI model reads the search result and identifies if it's about a:
   - Person (name, birth info, achievements)
   - Company (industry, key people, products)
   - Movie (director, cast, genre)

4. **Returns Clean JSON Output**  
   The extracted data is returned in a neatly formatted JSON.

---

## 🧠 Example Queries

Try these:
- `Albert Einstein`
- `Microsoft`
- `Inception`

---

## 🛠️ Requirements

Install these libraries:

```bash
pip install openai langchain python-dotenv serpapi
```

---

## 🔐 Setup `.env` File

Create a `.env` file in the same folder as your script and add:

```env
OPENAI_API_KEY=your-openai-api-key
SERPAPI_API_KEY=your-serpapi-key
```

---

## 🧾 Sample JSON Output

```json
{
  "type": "person",
  "full_name": "Elon Musk",
  "birth": {
    "year": "1971",
    "place": "Pretoria, South Africa"
  },
  "fields": ["Technology", "Entrepreneurship"],
  "achievements": [
    {
      "title": "Founded SpaceX",
      "year": "2002"
    },
    {
      "title": "CEO of Tesla",
      "year": "2008"
    }
  ]
}
```

---

## 📁 Project Files

| File         | Purpose                          |
|--------------|----------------------------------|
| `day09_multi_step_info_extractor.py`    | The main script to run the app   |
| `.env`       | Stores API keys securely         |
| `README.md`  | This file (how-to guide)         |

---

## 🧑‍💻 How to Run

```bash
python day09_multi_step_info_extractor.py
```

Then enter a search topic when prompted.

To exit, type:

```bash
exit
```

---

## 🧼 Clean & Reusable Design

- Modular functions: `serpapi_search()` and `dynamic_info_extractor()`
- Uses LangChain's `PromptTemplate` to dynamically extract info
- Prints pretty JSON output to the terminal

---

## 📦 Technologies Used

| Tool       | Purpose                             |
|------------|-------------------------------------|
| OpenAI     | Text generation & understanding     |
| LangChain  | Build prompt chains easily          |
| SerpAPI    | Search Google & extract info        |
| Python     | Core programming language           |

---

## 🙋‍♀️ Want More?

You can extend this to support:
- 📚 Books
- 🎤 Events
- 📱 Apps

---

## 💡 Author Notes

This challenge helped me practice:
- Prompt engineering
- Multi-step logic
- Real-world API integration

---

