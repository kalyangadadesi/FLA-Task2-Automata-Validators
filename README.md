# FLA Task 2 – Designing Automata for Real-Time Applications

## 1. Introduction

Formal Language and Automata is an important subject in computer science that explains how computers recognize and process different patterns of input.

This project, **Designing Automata for Real-Time Applications**, focuses on using Finite Automata concepts to build simple validation systems that are commonly used in our daily lives.

In many applications, users enter different types of information, such as passwords, email addresses, and ATM PINs. Before accepting these inputs, the system must check whether they follow the required rules.

Finite Automata can help us understand how these input patterns are recognized and classified as valid or invalid.

In this project, we have designed three different validation applications:

1. Password Verification System
2. Email Format Validator
3. ATM PIN Verification System

Each application follows a set of predefined rules and checks whether the given input satisfies those rules.

## 2. Project Objectives

The main objectives of this project are:

- To understand the practical use of Finite Automata in real-world applications.
- To design automata for different input validation systems.
- To define the alphabet and language for each application.
- To identify accepted and rejected input strings.
- To understand how states and transitions work in an automaton.
- To implement validation logic using Python.
- To test the applications with different valid and invalid inputs.
- To understand the limitations of Finite Automata in real-world validation systems.

## 3. Applications Implemented

### 3.1 Password Verification System

A password verification system checks whether a password follows the required password rules.

In this project, the password is checked based on predefined conditions such as:

- Minimum password length.
- Presence of uppercase letters.
- Presence of lowercase letters.
- Presence of numbers.
- Presence of special characters.

The system accepts passwords that satisfy the defined rules and rejects passwords that do not meet them.

**Example:**

Accepted passwords:
- Hello@123
- Welcome#45
- Python@2026
- Secure$789
- Abcd@1234

Rejected passwords:
- hello
- 123456
- password
- HELLO123
- abc@12

**Automata Concept:**

The automaton checks the input characters and tracks whether the required conditions are satisfied. An input is accepted only when all the required conditions are met.

### 3.2 Email Format Validator

An email format validator checks whether an email address follows a specified email format.

A valid email address generally contains:
- A username.
- An @ symbol.
- A domain name.
- A valid domain extension.

The system checks whether these parts are arranged in the correct order.

**Example:**

Accepted email addresses:
- student@gmail.com
- user123@yahoo.com
- admin@outlook.com
- hello123@gmail.com
- test.user@example.com

Rejected email addresses:
- studentgmail.com
- @gmail.com
- user@
- user@gmail
- user@@gmail.com

**Automata Concept:**

The automaton reads the email address character by character and checks whether the required pattern is followed. It moves between states according to the characters received and accepts or rejects the input based on the defined rules.

### 3.3 ATM PIN Verification System

An ATM PIN verification system checks whether the entered PIN follows the required numeric format.

In this project, the PIN is validated based on the predefined length and numeric conditions.

For example, if the system uses a 4-digit PIN, the input must contain exactly four numeric digits.

**Example:**

Accepted PINs:
- 1234
- 5678
- 9087
- 2468
- 1357

Rejected PINs:
- 123
- 12345
- 12ab
- abcd
- 12@4

**Automata Concept:**

The automaton reads each digit and moves through different states. When exactly four numeric digits are received, it reaches the final accepting state. If the input contains letters, special characters, or an incorrect number of digits, it is rejected.

## 4. Technologies Used

- **Python:** Used to implement the validation programs.
- **Formal Language and Automata Theory:** Used to understand the concepts of alphabets, languages, states, and transitions.
- **Finite Automata:** Used to represent and understand the input validation process.
- **Regular Expressions:** Can be used to define and check input patterns.

## 5. Working Process

The project follows a simple validation process:

1. The user enters an input such as a password, email address, or ATM PIN.
2. The system receives the input.
3. The input is checked against the predefined validation rules.
4. The program determines whether the input satisfies the conditions.
5. If all required conditions are satisfied, the input is accepted.
6. Otherwise, the input is rejected.

This process helps us understand how automata recognize different input patterns.

## 6. Important Concepts of Automata Used

### Alphabet (Σ)
An alphabet is a set of symbols used to form strings. For example, the ATM PIN validator uses numeric digits from 0 to 9.

### String
A string is a sequence of symbols taken from an alphabet. For example, 1234 is a string containing four numeric digits.

### Language
A language is a collection of strings that satisfy particular rules. In this project, each validator defines a language of accepted inputs.

### States
States represent the different conditions of an automaton while processing an input.

### Transitions
Transitions describe how an automaton moves from one state to another based on the input symbol.

### Initial State
The initial state is the starting point of an automaton.

### Final State
The final state represents an accepting condition. If the input reaches an accepting state after processing the complete string, it is accepted.

## 7. Testing and Validation

Each application is tested using different input strings to check whether the validation rules work correctly.

For every application, at least five accepted examples and five rejected examples are considered.

Testing helps to:
- Identify incorrect inputs.
- Check whether valid inputs are accepted.
- Verify that invalid inputs are rejected.
- Understand the working of the designed automata.

## 8. Real-Time Applications

The concepts used in this project are useful in many real-world systems.

- **Password Validation:** Used in websites, mobile applications, and user account registration.
- **Email Validation:** Used in online registration forms, communication platforms, and account creation.
- **ATM PIN Validation:** Used in banking systems to check the format of a PIN entered by a user.

These examples show how automata concepts are connected to everyday computer applications.

## 9. Limitations of the Project

Although Finite Automata are useful for checking input patterns, they have some limitations.

- They can check predefined patterns but cannot understand the meaning of an input.
- Basic automata cannot verify whether an email address actually exists.
- Password format validation does not determine whether a password is strong against every type of attack.
- ATM PIN format validation does not confirm whether the PIN belongs to the actual bank account.
- Additional processing and database verification are required for real-world security and business rules.

Therefore, Finite Automata are useful for syntax and format validation, while additional processing is needed for complete real-time verification.

## 10. Conclusion

This project demonstrates how the concepts of Formal Language and Automata can be applied to practical input validation problems.

By designing three applications, namely Password Verification, Email Format Validation, and ATM PIN Verification, we understand how Finite Automata can recognize valid and invalid input patterns.

The project provides practical knowledge about alphabets, strings, languages, states, transitions, and accepting conditions.

It also helps us understand the importance of automata in computer science and how theoretical concepts can be connected to real-world applications.

Overall, this project improves our understanding of Finite Automata and demonstrates their usefulness in building simple and efficient validation systems.

---

**Course Details**

- Course Name: Formal Language and Automata
- Course Code: 21CSC301T
- Assessment: Continuous Learning Assessment – 2
- Assessment Task: Task 2
- Academic Year: 2026–2027
- Department: Artificial Intelligence and Machine Learning
