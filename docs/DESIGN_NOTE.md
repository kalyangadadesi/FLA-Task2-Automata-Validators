# Design Note – Finite Automata for Real-Time Applications

## 1. Objective
The project models three syntax-validation tasks with deterministic finite
automata (DFA). A DFA is described by states, an input alphabet, a start state,
accepting states and transitions. An input is accepted only if its complete
scan ends in an accepting state.

## 2. Password verification

**Assumptions / language.** A password is accepted when it has 8–16 characters,
contains at least one uppercase ASCII letter, one lowercase ASCII letter, one
digit and one character from `!@#$%^&*()-_+=`. Whitespace and all other
characters are rejected.

**Alphabet.** Partition the character alphabet into U (uppercase), L
(lowercase), D (digit), S (allowed special), and X (whitespace or unsupported).
The DFA tracks a length counter from 0 through 16, four Boolean flags
(U-seen, L-seen, D-seen, S-seen), and a dead/reject state. This is a finite
state construction: at most 17 × 16 summary combinations plus the dead state.
Transitions update the relevant flag and length; X or a seventeenth character
goes to the dead state. Accepting states have length 8–16 and all four flags set.

**Examples accepted (5):** `Hello@123`, `Welcome@1`, `Abcd#789`,
`Pass_word9!`, `Qwerty$12`.

**Examples rejected (5):** `hello123` (no uppercase/special), `HELLO@123`
(no lowercase), `HelloWorld@` (no digit), `Hi@12` (too short),
`Hello 123@` (contains a space).

**Limitations.** The rule is a teaching example, not a password-strength
assessment. It does not check breached passwords, common words or entropy.

## 3. Email-format validation

**Assumptions / regular-language subset.** The accepted pattern is:
- local part: 1–64 characters; ASCII letters/digits and `_ % + -` may appear
  in atoms separated by single dots; no leading, trailing or consecutive dot.
- exactly one `@`.
- domain: at least two dot-separated labels; each label is 1–63 characters,
  begins and ends with an ASCII letter or digit, and may contain hyphens inside.
- final extension: at least two ASCII letters.
- no whitespace.

**Alphabet.** ASCII letters, digits, `.`, `@`, `_`, `%`, `+`, `-`, and all
other characters (rejecting class). The scanner tracks whether it is in the
local part or domain, whether the previous local character was a dot, the
current domain-label boundary condition, number of `@` separators, and whether
a valid dot-separated extension has been reached. These are finite flags and
finite control states. The Python implementation checks these conditions in
a single scan plus bounded structural checks.

**Examples accepted (5):** `student@gmail.com`, `abc@yahoo.in`,
`ronav.js+fla@example.org`, `a_b-9@sub.domain.co`,
`first.last@college.edu`.

**Examples rejected (5):** `@gmail.com` (empty local part), `abc@gmail`
(no domain extension), `abc@@gmail.com` (two @ symbols),
`a..b@gmail.com` (consecutive dots), `abc@-gmail.com` (domain label starts
with hyphen).

**Limitations.** This is intentionally a subset for a classroom DFA exercise.
It does not cover every legal address form in the full email specifications,
internationalized addresses, quoted local parts or comments. It validates
syntax only; it cannot establish that a mailbox exists or can receive mail.

## 4. ATM PIN verification

**Assumptions / language.** A PIN consists of exactly four characters, each
from 0–9. Leading zeroes are allowed.

**Alphabet.** Σ = {0,1,2,3,4,5,6,7,8,9}. Any non-digit causes rejection.

**States.** q0 is the start state (zero digits read); q1, q2 and q3 mean one,
two and three digits read; q4 is the only accepting state (four digits read).
Any fifth digit or non-digit goes to a dead state. The DFA accepts only when
the input ends at q4.

**Examples accepted (5):** `1234`, `5678`, `0000`, `9081`, `2468`.

**Examples rejected (5):** `123` (too short), `12345` (too long),
`12a4` (letter), `12 4` (space), empty string (no digits).

**Limitations.** The DFA checks PIN format only. It does not compare the PIN
with a bank record, identify a customer, limit failed attempts or authorize
transactions. Those require secure application/backend logic.

## 5. Syntax validation versus semantic/business validation
A finite automaton is suitable when acceptance depends on a regular pattern
and a finite amount of memory, such as character classes, separators and
bounded lengths. It can check whether a string has the required shape.
Additional processing is required for semantic or business rules: whether an
email account exists, whether a password is compromised, or whether a PIN
matches an account and has not exceeded attempt limits.

## 6. Conclusion
The three examples demonstrate how finite-state control can recognize useful
regular patterns. The models are intentionally limited and should be combined
with application-level security and semantic checks in real deployments.
