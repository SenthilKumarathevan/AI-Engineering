WHAT THIS PROJECT REALLY IS (Simple Explanation)
This project is an Agentic Automated Data Quality Tester.
Meaning:
👉 It reads your data,
👉 generates data-quality rules,
👉 creates dbt tests,
👉 runs the tests,
👉 detects failures, and
👉 uses an LLM to automatically fix the rules
when they are too strict, wrong, or unrealistic.
And all of this happens completely automatically.
You don’t write tests.

You don’t update rules.

The system does it by itself.
🟩 WHY WE BUILT THIS
In real projects:
Data changes every day
Rules change often
Teams forget to update dbt tests
Strict rules break easily
No one has time to manually fix test failures
This system solves that by making data quality self-managing.
🟧 MAIN IDEA IN ONE SENTENCE
➤ “Your dbt tests keep themselves healthy using AI.”
The system is like a self-driving car, but for dbt tests.
🟦 WHAT COMPONENTS ARE USED (Very Simple)
Here are the components in plain words:
1️⃣ scenario_data (CSV files)
Your input data.

The AI reads this and creates rules.
2️⃣ Coverage Generator
Looks at the data and creates rules like:
values must not be null
amounts must be positive
emails must contain “@”
dates must not be in future
statuses must be from allowed list
This generates rules.json.
3️⃣ Test Generator
Converts rules into dbt tests:
schema tests
data tests
relationship tests
business rule tests
Writes SQL files into the tests/ folder.
4️⃣ dbt (DuckDB)
Runs all the tests.

Tells us which rules are failing.
5️⃣ LLM Agent (Foundry Local)
Reads dbt failures and asks:
“Is the rule wrong? Should we fix the rule?”
If yes, it updates rules.json with a patch like:
order_amount >= 0 OR status='refunded'
This is called LLM-healing.
6️⃣ Test Re-run Loop
After every heal:
regenerate tests
re-run dbt
check failures again
heal more if needed
This is the agentic loop, meaning the system learns & adapts.
7️⃣ Chroma Memory
Stores:
past failures
past fixes
past patches
scenario metadata
This helps future decisions.
8️⃣ Dashboard (Streamlit)
Shows:
coverage %
dbt results
LLM healing history
generated scenarios
🟪 HOW IT WORKS END‑TO‑END (Super Simple)
Step 1: Load Data
Your CSVs are loaded into dbt seeds.
Step 2: Auto Rule Generation
AI scans the data and creates rules.json.
Example rules:
email must contain “@”
order_amount >= 0
status in [active, pending, processing]
Step 3: Auto Test Generation
AI converts rules → dbt tests:
YAML tests
SQL tests
Step 4: Run dbt Tests
dbt tells us:
✔ which tests passed

❌ which tests failed

❌ which rules are wrong

❌ which data patterns break rules
Step 5: LLM Reads Failures
LLM sees lines like:
FAIL: order_amount > 0 (3 rows failed)
And decides:
“This rule is too strict because refunded orders have negative amounts.”
Step 6: LLM Updates Rules
LLM writes a JSON patch:
"order_amount >= 0 OR status='refunded'"
Step 7: Tests Regenerated
AI regenerates dbt tests using the new rule.
Step 8: Tests Re-run
dbt tests run again:
fewer failures
healed rules
improved rules.json
Step 9: Loop Continues
This repeats until everything stabilises.
🟦 KEY BENEFITS OF THIS SYSTEM
✔ No need to manually write dbt tests
✔ No need to manually fix dbt failures
✔ Rules improve themselves with LLM
✔ Bad rules are healed
✔ Good rules stay
✔ All automated
✔ Runs fully local (Foundry Local + DuckDB)
✔ Perfect for demos, POCs, and real production
🟨 YOUR CURRENT STATUS
Right now:
You successfully showed ENUM healing

(processing + refunded added automatically)
You successfully showed test generation → dbt → heal loop
Remaining failures come from:
multiple conflicting AGG-MAX numeric rules
date rules not yet healable
a wrong generated unique rule
You are now very close to a full LLM-heal demonstration.
 
