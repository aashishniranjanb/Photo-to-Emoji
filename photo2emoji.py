# Input: { "caption": "a man drinking coffee at the beach" }
def transform(inputs):
    caption = inputs["caption"].lower()
    keyword_emoji = {
        "dog": "🐶", "cat": "🐱", "coffee": "☕", "beach": "🏖️", 
        "laptop": "💻", "phone": "📱", "tree": "🌳", "car": "🚗",
        "food": "🍲", "person": "🧍", "baby": "👶", "bike": "🚴"
    }
    output = []
    for word in caption.split():
        word = word.strip(",.")
        if word in keyword_emoji and word not in output:
            output.append(keyword_emoji[word])
        if len(output) == 3:
            break
    return {"emojis": " ".join(output) if output else "🤖"}
