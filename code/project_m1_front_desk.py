
"""AI Front Desk for a local clinic.

Answers common patient questions, calculates exact service quotes,
prepares AI-ready prompts, routes private questions locally, and
prints a session report for the clinic owner.
"""

# The clinic owner can update these settings without changing the logic.
BOT_NAME = "Clinic Front Desk"
BUSINESS = "Family Care Clinic"
CITY = "Lahore"
CONSULTATION_FEE = 1500
FOLLOW_UP_FEE = 1000
DENTAL_CHECKUP_FEE = 2000
DELIVERY_FEE = 0
FREE_DELIVERY_LIMIT = 3000
BULK_MIN_QTY = 10
BULK_DISCOUNT_PERCENT = 10
CLOUD_PRICE_PER_1K = 0.1  # Example estimate in PKR per 1,000 tokens
LOCAL_MODEL = "llama3.2"
MAX_QUESTION_CHARS = 150

# Show the clinic name and collect the customer's name once.
print("=" * 50)
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("=" * 50)
print("Ask a question, type /quote for fees, or bye to exit.")

customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()
if customer_name == "":
    customer_name = "Patient"

# Counters help the clinic owner understand what patients ask.
messages = 0
answered_by_rules = 0
unanswered = 0
quotes = 0
quoted_value = 0
total_ai_cost = 0.0
complaints = 0
human_handovers = 0

while True:
    message = input(f"{customer_name}: ").strip().lower()

    # Empty input should not count as a message.
    if message == "":
        print(f"{BOT_NAME}: Please type a question, /quote, or bye.")
        continue

    messages += 1
    padded = " " + message + " "

    # Complaints come first so unhappy patients are handled respectfully.
    if (
        "refund" in message
        or "complaint" in message
        or " late " in padded
        or "delay" in message
    ):
        print(
            f"{BOT_NAME}: We're sorry for the inconvenience. "
            "Our clinic staff will contact you to discuss your concern."
        )
        answered_by_rules += 1
        complaints += 1

    # Optional bonus: transfer requests to a human end the conversation.
    elif (
        message == "agent"
        or message == "human"
        or "speak to a person" in message
    ):
        print(f"{BOT_NAME}: Connecting you to a clinic staff member...")
        answered_by_rules += 1
        human_handovers += 1
        break

    elif message == "bye":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        answered_by_rules += 1
        break

    # Check exact words or the start of the message to avoid false greetings.
    elif (
        message == "hi"
        or message.startswith("hi ")
        or message.startswith("hello")
        or message.startswith("salam")
        or message.startswith("assalam")
    ):
        print(
            f"{BOT_NAME}: Hello {customer_name}! "
            f"Welcome to {BUSINESS}, {CITY}."
        )
        answered_by_rules += 1

    elif (
        "hours" in message
        or "open" in message
        or "closing time" in message
    ):
        print(f"{BOT_NAME}: Our example opening hours are 9 AM to 6 PM, Monday to Saturday.")
        answered_by_rules += 1

    elif "where" in message or "location" in message or "address" in message:
        # Do not expose private patient addresses; clinic location is public.
        print(f"{BOT_NAME}: We are in {CITY}. Please contact reception for directions.")
        answered_by_rules += 1

    elif "appointment" in message or "booking" in message:
        print(
            f"{BOT_NAME}: Please contact clinic reception "
            "to check appointment availability."
        )
        answered_by_rules += 1

    elif "deliver" in message:
        print(
            f"{BOT_NAME}: This clinic does not offer delivery. "
            "Please contact reception for available services."
        )
        answered_by_rules += 1

    elif (
        "price" in message
        or "fee" in message
        or "cost" in message
        or "charges" in message
    ):
        print(f"{BOT_NAME}: Type /quote to calculate an example service fee.")
        answered_by_rules += 1

    elif "payment" in message or "pay" in message:
        print(
            f"{BOT_NAME}: Please contact reception to confirm "
            "currently accepted payment methods."
        )
        answered_by_rules += 1

    elif "doctor" in message or "available" in message:
        print(
            f"{BOT_NAME}: Please contact reception to confirm "
            "doctor availability."
        )
        answered_by_rules += 1

    elif message == "/quote":
        item = input(
            f"{BOT_NAME}: Choose consultation, follow-up, or dental checkup: "
        ).strip().lower()
        qty_text = input(f"{BOT_NAME}: How many visits? ").strip()

        # Validate quantity before int() so letters do not crash the program.
        if not qty_text.isdigit() or int(qty_text) < 1:
            print(f"{BOT_NAME}: Please enter a whole number of 1 or more.")
            continue

        quantity = int(qty_text)

        if item == "consultation":
            unit_price = CONSULTATION_FEE
        elif item == "follow-up":
            unit_price = FOLLOW_UP_FEE
        elif item == "dental checkup":
            unit_price = DENTAL_CHECKUP_FEE
        else:
            unit_price = 0

        if unit_price == 0:
            print(f"{BOT_NAME}: Sorry, {item} is not on our service list.")
        else:
            subtotal = unit_price * quantity

            # Apply the example bulk discount only at the configured quantity.
            if quantity >= BULK_MIN_QTY:
                discount = subtotal * BULK_DISCOUNT_PERCENT // 100
            else:
                discount = 0

            after_discount = subtotal - discount

            # This is an example clinic service quote, not a medical bill.
            delivery = DELIVERY_FEE
            total = after_discount + delivery

            print(
                f"{BOT_NAME}: {quantity} x {item} = "
                f"{subtotal:,} PKR"
            )
            print(
                f"     Discount: -{discount:,} PKR | "
                f"Extra fee: {delivery:,} PKR"
            )
            print(f"     Example total: {total:,} PKR")

            quotes += 1
            quoted_value += total

    else:
        # Clean and limit the question before estimating its token usage.
        question = message.capitalize()[:MAX_QUESTION_CHARS]
        tokens = round(len(question) / 4)

        # Personal information stays on the local route at zero cloud cost.
        if (
            "phone" in message
            or "cnic" in message
            or "my address" in message
        ):
            model = f"{LOCAL_MODEL} (local, private)"
            cost = 0.0
        else:
            model = "small cloud model (cheap)"
            cost = tokens / 1000 * CLOUD_PRICE_PER_1K

        total_ai_cost += cost
        unanswered += 1

        print(
            f"{BOT_NAME}: Good question! Routed to: "
            f"{model} (~{tokens} tokens)"
        )
        print(
            f"""     Prompt: You are the front desk assistant of {BUSINESS} in {CITY}.
     Answer {customer_name} in 2 short, polite lines.
     Do not diagnose, invent fees, promise appointments, or request private medical details.
     If unsure, ask the patient to contact clinic staff.
     Question: {question}"""
        )

# This report runs after the conversation ends.
print("=" * 50)
print("Clinic session report")
print(f"Messages: {messages}")
print(f"Answered by rules: {answered_by_rules}")
print(f"Unanswered / AI-ready prompts: {unanswered}")
print(f"Quotes: {quotes} | Example quoted value: {quoted_value:,} PKR")
print(f"Complaints: {complaints} | Human handovers: {human_handovers}")
print(f"Estimated AI cost: {total_ai_cost:.4f} PKR")
print("=" * 50)
