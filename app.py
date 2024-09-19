from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Mock data for hospitals in cities (e.g., Kolkata, Delhi)
hospitals_data = {
    "kolkata": {
        "govt_hospital": ["Kolkata Medical College", "Seth Sukhlal Karnani Memorial Hospital", "R.G. Kar Medical College"],
        "private_hospital": ["Apollo Gleneagles Hospital", "Fortis Hospital", "AMRI Hospital"],
        "diagnostic_centre": ["Thyrocare Kolkata", "Dr Lal PathLabs", "Suraksha Diagnostics"],
        "nursing_home": ["Nightingale Nursing Home", "Woodlands Nursing Home", "Belle Vue Clinic"]
    },
    "delhi": {
        "govt_hospital": ["AIIMS Delhi", "Safdarjung Hospital", "Lok Nayak Hospital"],
        "private_hospital": ["Max Super Speciality Hospital", "BLK Super Speciality Hospital", "Fortis Escorts"],
        "diagnostic_centre": ["SRL Diagnostics", "Dr Lal PathLabs", "Thyrocare"],
        "nursing_home": ["Moolchand Nursing Home", "Holy Family Nursing Home", "Sitaram Bhartia Nursing Home"]
    }
}

greetings_responses = [
    "Hi there! I'm your friendly assistant. How can I help you today?",
    "Hello! Need some help finding hospitals or healthcare services? Just ask!",
    "Hey! I'm here to make your search for hospital services easy and quick."
]

small_talk_responses = {
    "how are you": ["I'm just a bot, but I'm here to help you with hospital information! How can I assist you today?", "I'm doing great! How can I assist you with our hospital services?"],
    "who are you": ["I'm HealthSync, your assistant for all things hospital-related. How can I help you today?", "I'm your chatbot guide for finding hospital services. Let me know what you need!"],
    "what can you do": ["I can help you find hospitals, book appointments, and more! What can I assist you with today?", "I can help you with hospital details, emergency services, and more. Just ask!"]
}

off_topic_responses = [
    "That sounds interesting! While I can't help with that topic, I'm here to assist with hospital services. How can I help you?",
    "Wow, that's cool! But my expertise is in hospital services. Need help finding a hospital or booking an appointment?",
    "Interesting topic! Let’s get back to hospitals. How can I assist you with finding the right one?"
]

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if any(greeting in user_input for greeting in ["hello", "hi", "hey", "greetings"]):
        return {
            "response": random.choice(greetings_responses),
            "buttons": [
                {"title": "Find Hospitals", "action": "find_hospitals"},
                {"title": "Book an Appointment", "action": "book_appointment"},
                {"title": "Emergency Services", "action": "emergency_services"}
            ]
        }

    for key, responses in small_talk_responses.items():
        if key in user_input:
            return {
                "response": random.choice(responses),
                "buttons": [
                    {"title": "Find Hospitals", "action": "find_hospitals"},
                    {"title": "Book an Appointment", "action": "book_appointment"},
                    {"title": "Emergency Services", "action": "emergency_services"}
                ]
            }
    
    if "real-time bed analysis" in user_input:
        return {
            "response": "You can view the real-time bed analysis here: [Real-Time Bed Analysis](app://real-time-bed-analysis)",
            "buttons": []
        }
    
    if "emergency" in user_input:
        return {
            "response": "Access emergency services here: [Emergency Services](app://emergency)",
            "buttons": []
        }
    
    if "appointment" in user_input:
        return {
            "response": "You can book an appointment here: [Book Appointment](app://appointment_booking)",
            "buttons": []
        }
    
    if "city" in user_input or "cities" in user_input:
        return {
            "response": "Our app currently supports Kolkata, Delhi, and Bangalore. Which city would you like to explore?",
            "buttons": [
                {"title": "Kolkata", "action": "explore_kolkata"},
                {"title": "Delhi", "action": "explore_delhi"},
                {"title": "Bangalore", "action": "explore_bangalore"}
            ]
        }

    if "kolkata" in user_input:
        if "govt hospital" in user_input or "government hospital" in user_input:
            return {
                "response": f"Here are some government hospitals in Kolkata: {', '.join(hospitals_data['kolkata']['govt_hospital'])}. Would you like to know about Private Hospitals, Diagnostic Centres, or Nursing Homes in Kolkata?",
                "buttons": [
                    {"title": "Private Hospitals", "action": "kolkata_private_hospitals"},
                    {"title": "Diagnostic Centres", "action": "kolkata_diagnostic_centres"},
                    {"title": "Nursing Homes", "action": "kolkata_nursing_homes"}
                ]
            }

    return {
        "response": "I'm here to help you navigate our app. Please ask about specific services or sections.",
        "buttons": []
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
