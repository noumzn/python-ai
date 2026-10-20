
"""Lesson 1.8: Rule-Based Truck Dispatch Helper Bot"""

BOT = "Dispatch Helper Bot"

print(f"{BOT}: Welcome to Truck Dispatch Support!")
print(
    f"{BOT}: I can help with load status, rate confirmations, "
    "POD/BOL and detention."
)
print(f"{BOT}: Type 'bye' to end the chat.")

# MEMORY: remember the user's name
name = input("Bot: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"Bot: Nice to meet you, {name}!")

# COUNTERS: track messages and unanswered questions
count = 0
unanswered = 0

# MAIN CHAT LOOP
while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    # 1. EXIT RULE
    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Drive safe.")
        break

    # 2. EMPTY MESSAGE
    elif message == "":
        print(f"{BOT}: Please type your dispatch question.")

    # 3. COMPLAINT RULE — KEEP THIS BEFORE NORMAL RULES
    elif (
        "complaint" in message
        or "problem" in message
        or "unhappy" in message
        or "angry" in message
        or "late" in message
        or "issue" in message
    ):
        print(
            f"{BOT}: Sorry for the inconvenience, {name}. "
            "Please review the issue and escalate it to your dispatcher "
            "or manager for follow-up."
        )

    # 4. LOAD STATUS / TRACKING
    elif (
        "load status" in message
        or "tracking" in message
        or "gps" in message
        or "driver update" in message
        or "eta" in message
    ):
        print(
            f"{BOT}: Check the driver's latest location and ETA, "
            "then send an accurate update to the broker."
        )

    # 5. RATE CONFIRMATION
    elif (
        "ratecon" in message
        or "rate confirmation" in message
        or "rate con" in message
    ):
        print(
            f"{BOT}: Check the agreed rate, pickup and delivery details. "
            "Request the rate confirmation if it has not been received."
        )

    # 6. POD / BOL DOCUMENTS
    elif (
        "pod" in message
        or "bol" in message
        or "proof of delivery" in message
        or "bill of lading" in message
    ):
        print(
            f"{BOT}: Check the load's document requirements. "
            "Request the missing POD or BOL from the responsible party."
        )

    # 7. DETENTION / LAYOVER
    elif (
        "detention" in message
        or "layover" in message
        or "waiting time" in message
    ):
        print(
            f"{BOT}: Record arrival and departure times, "
            "keep supporting documents, and request approval "
            "according to the rate confirmation."
        )

    # 8. PAYMENT / QUICK PAY
    elif (
        "quickpay" in message
        or "quick pay" in message
        or "payment" in message
        or "invoice" in message
    ):
        print(
            f"{BOT}: Review the payment terms and required documents. "
            "Confirm any quick-pay fee with the broker before agreeing."
        )

    # 9. PICKUP / DELIVERY APPOINTMENT
    elif (
        "pickup" in message
        or "delivery" in message
        or "appointment" in message
        or "receiver" in message
    ):
        print(
            f"{BOT}: Verify the appointment time, address, "
            "and any special instructions with the rate confirmation."
        )

    # 10. GREETING — EXACT MATCH AVOIDS ACCIDENTAL MATCHES
    elif (
        message == "hi"
        or message == "hello"
        or message == "hey"
        or message.startswith("salam")
    ):
        print(
            f"{BOT}: Hello, {name}! "
            "What dispatch issue can I help you with?"
        )

    # 11. FALLBACK — UNKNOWN QUESTION
    else:
        unanswered += 1

        prompt = (
            "You are a professional US truck dispatch assistant. "
            "Answer clearly and professionally. Do not invent "
            "driver locations, ETAs, rates, or payment approvals. "
            f"User question: {message}"
        )

        print(
            f"{BOT}: I don't have a rule for that question yet."
        )
        print(f"{BOT}: Future AI prompt: {prompt}")

# FINAL CHAT SUMMARY
print("=" * 45)
print(f"Chat summary for {name}")
print(f"Total messages: {count}")
print(f"Unanswered questions: {unanswered}")
print("End of dispatch support session.")
