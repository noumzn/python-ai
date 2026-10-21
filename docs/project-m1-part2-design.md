# Project M1 Part 2: Design (Sweet Crumbs Desk)

Business: Sweet Crumbs bakery. Problem: staff answer the same questions all day, make mistakes on price quotes, and the owner does not know what customers really ask.

## Intents

Rules are checked in this order, top to bottom. The first match wins.

| Order | Intent | Keywords | Reply |
|---|---|---|---|
| 1 | Empty input | (nothing typed) | Asks again, not counted as a message |
| 2 | Goodbye | `bye` (exact match) | Goodbye + session report |
| 3 | Complaint | refund, complaint, ` late ` (whole word) | A manager will call you within 1 hour |
| 4 | Quote | `/quote` (exact match) | Starts the price calculator |
| 5 | Greeting | `hi` (exact), starts with `hi `, `hello`, `salam` | Welcome message with the customer's name |
| 6 | Hours | hours, open, close | Open 9 am to 10 pm, every day |
| 7 | Location | where, location | Main Boulevard, near the central market |
| 8 | Delivery | deliver | Delivery 200 PKR, free from 3,000 PKR |
| 9 | Price / fees | price, fee, cost | Type /quote for an exact price |
| 10 | Payment | pay | Cash and bank transfer |
| 11 | Fallback | anything else | Clean, cut to 150 chars, estimate tokens, route to a model |

Why this order: the complaint rule is first so an unhappy customer always reaches a human. Greetings use `==` / `.startswith()` because "hi" hides inside "which". The complaint word "late" is matched as a whole word because "chocolate" contains "late".

## Business rules

| Rule | Value |
|---|---|
| Item prices | cupcake 250 PKR, brownie 300 PKR, chocolate cake 1,500 PKR |
| Bulk discount | 10% off for 10 or more items |
| Delivery | 200 PKR, free when the amount after discount is 3,000 PKR or more |
| Private words | phone, cnic, address |
| Cloud price (example) | 0.1 PKR per 1,000 tokens |
| Local model | llama3.2, cost 0 |
| Token estimate | characters / 4, rounded |
| Question limit | 150 characters |

Quote order: subtotal, then discount, then the delivery check on the discounted amount, then total. Example: 12 cupcakes = 3,000 PKR, minus 300 discount = 2,700 PKR, which is below 3,000, so delivery is still charged. Total 2,900 PKR.

## Rule tests

| You type | Expected | Actual | Pass? |
|---|---|---|---|
| ` WHAT are your hours ` | Hours (capitals and spaces handled) | We are open 9 am to 10 pm, every day. | Yes |
| `which cake is best?` | Fallback, not a greeting | Routed to small cloud model (~5 tokens) | Yes |
| `my order is late` | Manager reply (complaint rule first) | Manager will call within 1 hour; complaint counted | Yes |
| `/quote`, chocolate cake, 1 | Delivery fee charged | 1,500 + 200 delivery = 1,700 PKR | Yes |
| `/quote`, chocolate cake, 3 | Delivery free | 4,500 PKR, delivery 0 | Yes |
| `/quote`, cupcake, 10 | Discount applied | 2,500 - 250 + 200 = 2,450 PKR | Yes |
| `/quote`, pizza, 2 | "Not on our menu", no crash | Sorry, pizza is not on our menu. | Yes |
| `can I change my phone number on the order?` | Local model, cost 0 | llama3.2 (local, private), cost 0.0000 | Yes |
| Press Enter with no text | Asks again | Please type a question, /quote or bye. | Yes |
| `BYE` | Goodbye + session report | Goodbye + report printed | Yes |

Extra tests:

| You type | Expected | Actual | Pass? |
|---|---|---|---|
| `/quote`, cupcake, `abc` | Polite message, no crash | Please enter a whole number of 1 or more. | Yes |
| `I want a chocolate cake` | Fallback, not a complaint ("chocolate" contains "late") | Routed to small cloud model | Yes |
| Full example session (7 messages) | Report: 7 / 3 / 2, 1 quote, 2,900 PKR, 0.0007 PKR | Matches | Yes |

Tests were run by feeding each input to `uv run code/project_m1_front_desk.py`. Re-run them yourself before submitting and correct any row that differs on your machine.