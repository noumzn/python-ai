
"""Lesson 1.5: AI Model Profile Card and cost estimate."""

# AI model profile
model_name = "gemma3:1b"
context_window = 32768
price_per_1k_tokens = 0.5
runs_locally = True


print("--- AI Model Profile Card ---")
print(f"Model: {model_name} | Type: {type(model_name)}")
print(f"Context window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR | Type: {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} | Type: {type(runs_locally)}")

tokens_used = int(input("Tokens used in one chat: "))

cost = tokens_used / 1000 * price_per_1k_tokens

print(f"Estimated cost per chat: {round(cost, 2)} PKR")

chats_per_day = int(input("Chats per day: "))
monthly_cost = cost * chats_per_day * 30

print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")
