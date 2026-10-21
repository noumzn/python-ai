"""AI Front Desk for Sweet Crumbs bakery.

Answers common questions with free rules, gives exact price quotes
(discount + delivery) with Python maths, builds AI-ready prompts for
everything else (private questions -> local model), and ends with a
session report the owner can act on.
"""

# Constants in UPPER_CASE: the owner can change a price here, not in the logic
BOT_NAME = "Sweet Crumbs Desk"
BUSINESS = "Sweet Crumbs bakery"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
BULK_MIN_QTY = 10
BULK_DISCOUNT_PERCENT = 10
CLOUD_PRICE_PER_1K = 0.1  # example PKR per 1,000 tokens
LOCAL_MODEL = "llama3.2"
MAX_QUESTION_CHARS = 150

# Header and name (asked once, before the loop)
print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")
customer_name = input(f"{BOT_NAME}: What is your name?   ").strip().title()
if customer_name == "":
    customer_name = "Customer"

# Session counters
messages = 0
answered_by_rules = 0
unanswered = 0
quotes = 0
quoted_value = 0
total_ai_cost = 0.0
complaints = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()

    # Empty input: ask again, and do not count it as a message
    if message == "":
        print(f"{BOT_NAME}: Please type a question, /quote or bye.")
        continue

    messages += 1
    # Padding with spaces lets us match the whole word " late " so that
    # "chocolate" does not trigger the complaint rule by accident
    padded = " " + message + " "

    if message == "bye":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        answered_by_rules += 1
        break

    # Complaint rule FIRST: an unhappy customer must always reach a human,
    # even if the same message also contains another keyword
    elif "refund" in message or "complaint" in message or " late " in padded:
        print(f"{BOT_NAME}: Sorry about that. A manager will call you within 1 hour.")
        answered_by_rules += 1
        complaints += 1

    elif message == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()
        qty_text = input(f"{BOT_NAME}: How many? ").strip()

        # isdigit() before int() so letters cannot crash the program
        if not qty_text.isdigit() or int(qty_text) < 1:
            print(f"{BOT_NAME}: Please enter a whole number of 1 or more.")
            continue
        quantity = int(qty_text)

        if item == "cupcake":
            unit_price = 250
        elif item == "brownie":
            unit_price = 300
        elif item == "chocolate cake":
            unit_price = 1500
        else:
            unit_price = 0

        if unit_price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
        else:
            subtotal = unit_price * quantity
            if quantity >= BULK_MIN_QTY:
                discount = subtotal * BULK_DISCOUNT_PERCENT // 100
            else:
                discount = 0
            # Delivery is judged AFTER the discount: the customer only
            # pays for what is left, so that is what must reach the limit
            after_discount = subtotal - discount
            if after_discount >= FREE_DELIVERY_LIMIT:
                delivery = 0
            else:
                delivery = DELIVERY_FEE
            total = after_discount + delivery

            print(f"{BOT_NAME}: {quantity} x {item} = {subtotal:,} PKR")
            print(f"     Discount: -{discount:,} PKR | Delivery: {delivery:,} PKR")
            print(f"     Total: {total:,} PKR")
            quotes += 1
            quoted_value += total

    # Greetings use == / startswith, never "in": "hi" hides inside "which"
    elif message == "hi" or message.startswith("hi ") or message.startswith("hello") or message.startswith("salam"):
        print(f"{BOT_NAME}: Hello {customer_name}! Welcome to {BUSINESS}.")
        answered_by_rules += 1

    elif "hours" in message or "open" in message or "close" in message:
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")
        answered_by_rules += 1

    elif "where" in message or "location" in message:
        print(f"{BOT_NAME}: We are on Main Boulevard, near the central market.")
        answered_by_rules += 1

    elif "deliver" in message:
        print(f"{BOT_NAME}: We deliver for {DELIVERY_FEE:,} PKR, free from {FREE_DELIVERY_LIMIT:,} PKR.")
        answered_by_rules += 1

    elif "price" in message or "fee" in message or "cost" in message:
        print(f"{BOT_NAME}: Type /quote for an exact price with discount and delivery.")
        answered_by_rules += 1

    elif "pay" in message:
        print(f"{BOT_NAME}: We accept cash and bank transfer.")
        answered_by_rules += 1

    else:
        # Smart fallback: clean, cut, estimate, route
        question = message.capitalize()[:MAX_QUESTION_CHARS]
        tokens = round(len(question) / 4)  # rough rule: 1 token is about 4 characters

        # Private details must stay on our own computer, so they go local
        if "phone" in message or "cnic" in message or "address" in message:
            model = f"{LOCAL_MODEL} (local, private)"
            cost = 0.0
        else:
            model = "small cloud model (cheap)"
            cost = tokens / 1000 * CLOUD_PRICE_PER_1K

        total_ai_cost += cost
        unanswered += 1
        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{tokens} tokens)")
        print(f"""     Prompt: You are the assistant of {BUSINESS}.
     Answer {customer_name} in 2 short lines. Question: {question}""")

# Session report: always prints because it sits after the loop
print("=" * 50)
print("Session report")
print(f"Messages: {messages} | Answered by rules: {answered_by_rules} | Unanswered: {unanswered}")
print(f"Quotes: {quotes} | Quoted value: {quoted_value:,} PKR | Complaints: {complaints}")
print(f"Estimated AI cost for unanswered questions: {total_ai_cost:.4f} PKR")
print("=" * 50)