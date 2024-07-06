from django.shortcuts import render
from google.generativeai import GenerativeModel, configure

configure(api_key="your api key")  
model = GenerativeModel("gemini-1.5-pro")

def index(request):
    return render(request, "index.html")

def ai_response(request):
    if request.method == 'POST':
        user_input = request.POST.get("x")
        print("User Input:", user_input)  
        response = model.generate_content(user_input)
        print("Gemini Response:", response.text)
        return render(request, "index.html", {"response": response.text})
    else:
        return render(request, "index.html")
