
"""Lesson 1.7: Smart Model Router"""

# 1. Get input from the user
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# 2. Set estimated prices per 1,000 input tokens
# These are practice rates, not live provider prices.
code_price = 0.003
chat_price = 0.0002

# 3. Choose a model
if task == "private":
    model = "Local model (Ollama)"
    cost = 0.0

elif task == "code":
    model = "Strong coding model"
    cost = tokens / 1000 * code_price

elif task == "chat":
    model = "Small cloud model"
    cost = tokens / 1000 * chat_price

else:
    model = "Unknown task"
    cost = 0.0

# 4. Check the request length
if tokens > 4000:
    warning = "Warning: Consider shortening this request."
else:
    warning = "Request length is fine."

# 5. Display the result
print("=" * 40)
print(f"Selected model: {model}")
print(warning)
print(f"Estimated input cost: ${cost:.2f}")
