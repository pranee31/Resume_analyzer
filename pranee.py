import google.generativeai as genai

genai.configure(api_key="AIzaSyDfg9F5EYMlUzvTwYeq-UQiaqQVJVeEx4g")
model = model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content("Hello Gemini!")
print(response.text)
