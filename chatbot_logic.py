# Basic chatbot logic for intent detection.
def get_bot_response(user_message):
    message = user_message.lower()
    
    if "mattress" in message:
        return ("You selected Mattress Finder. "
                "Please choose a type: Foam, Spring, Hybrid, or Latex.")
    elif "pillow" in message:
        return ("You selected Pillow Finder. "
                "Please choose a type: Memory Foam, Orthopedic, or Cooling.")
    elif "bedsheet" in message:
        return ("You selected Bedsheet Finder. "
                "Please choose material: Cotton, Silk, or Microfiber.")
    elif "order" in message:
        return ("You selected Order Management. "
                "Would you like to Track, Modify, or Cancel your order?")
    elif "complaint" in message:
        return ("Customer Support: Raise Complaint. "
                "Please provide your order ID and details.")
    elif "sleep" in message:
        return ("Sleep Advice: Would you like tips, expert consultation, or articles?")
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"
