"""
AI Prompt Kit for Clinics

This tool asks a clinic owner for basic business details and creates
three ready-to-use AI prompts for marketing, patient customer service,
and low-cost business growth ideas. It is intended for small clinics.
"""

# Ask for five details so each prompt fits the clinic.
business_name = input("Clinic name: ")
business_type = input("Clinic type (e.g. family clinic): ")
city = input("City: ")
main_customers = input("Main patients (e.g. families): ")
monthly_budget = int(input("Monthly AI/marketing budget (PKR): "))

# A clear header makes the generated prompt kit easy to read.
print("\n" + "=" * 45)
print(f"AI Prompt Kit for {business_name}")
print("=" * 45)

# Naming the audience and tone helps make marketing content more specific.
marketing_prompt = (
    f"You are a healthcare marketing assistant for {business_name}, "
    f"a {business_type} in {city}. Write one short social media post "
    f"for {main_customers}. Use a warm, clear, professional tone and "
    "include one call to action to contact the clinic for appointment "
    "information. Do not promise cures, make unsupported medical claims, "
    "or disclose patient information."
)

# A role, situation, and privacy boundary help guide a respectful reply.
customer_service_prompt = (
    f"You are the patient service representative at {business_name}, "
    f"a {business_type} in {city}. Draft a polite reply to a patient "
    "who is unhappy because their appointment was delayed. Apologize "
    "for the inconvenience, acknowledge their concern, and invite them "
    "to contact the clinic privately to discuss next steps. Do not ask "
    "for or reveal sensitive medical information. Keep it concise."
)

# A fixed number of ideas and an explicit budget make the request actionable.
growth_prompt = (
    f"Suggest 3 low-cost AI ideas for {business_name}, a {business_type} "
    f"in {city}. The clinic mainly serves {main_customers} and has a "
    f"monthly budget of {monthly_budget} PKR. For each idea, explain "
    "the use case, estimated cost range, and first step. Clearly label "
    "costs as estimates and do not invent exact prices. Protect patient "
    "privacy, require staff review for patient-facing content, and do not "
    "use AI to diagnose patients or replace qualified medical professionals."
)

print("\n[1] Marketing")
print("-" * 45)
print(marketing_prompt)

print("\n[2] Patient Customer Service")
print("-" * 45)
print(customer_service_prompt)

print("\n[3] Clinic Growth")
print("-" * 45)
print(growth_prompt)

print("\n" + "=" * 45)
print("Your 3 clinic AI prompts are ready!")
print("=" * 45)
