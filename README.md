# Finite Automata for Real-Time Applications
## FLA – Assessment Task 2

This independent project demonstrates three input validators using finite-state
ideas: password verification, email-format validation, and four-digit ATM PIN
verification. It uses Python and a small browser-based demonstration.

## Requirements
- Python 3.9 or newer
- Visual Studio Code (recommended)

No external Python packages are required.

## Folder structure
```text
FLA_Task2_Automata_Validators/
├── automata/
│   └── diagrams/             # State diagrams (SVG)
├── docs/
│   └── DESIGN_NOTE.md        # Assignment design documentation
├── validators/
│   ├── password.py
│   ├── email.py
│   └── atm_pin.py
├── tests/
│   ├── test_password.py
│   ├── test_email.py
│   └── test_atm_pin.py
├── web/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── app.py                   # Python menu application
└── README.md
```

## Run in VS Code
1. Extract the ZIP file.
2. Open VS Code.
3. Select **File → Open Folder** and choose `FLA_Task2_Automata_Validators`.
4. Open **Terminal → New Terminal**.
5. Run `python --version` to check Python is installed.
6. Run `python app.py` to use the terminal application.
7. Run the tests using the commands below.

### Run all tests
```bash
python -m unittest discover -s tests -v
```

### Run one test file
```bash
python -m unittest tests.test_password -v
python -m unittest tests.test_email -v
python -m unittest tests.test_atm_pin -v
```

### Open the browser demonstration
Open `web/index.html` in a browser, or use the VS Code Live Server extension.
Choose a validator, enter a value, and click **Validate**.

## Defined rules
- Password: 8–16 characters; at least one uppercase, lowercase, digit and
  permitted special character from `!@#$%^&*()-_+=`; no whitespace.
- Email: a deliberately limited regular-language subset described in
  `docs/DESIGN_NOTE.md`.
- ATM PIN: exactly four ASCII digits (0–9).

## Important model limitations
These validators check only the rules defined for this assignment. They do not
prove that a password is secure, that an email address exists, or that an ATM
PIN is authorized. A complete email implementation has additional standards
and internationalization rules. Real ATM authentication also needs secure
backend verification, rate limiting and encryption.

## Academic note
Use the design note and diagrams to understand and explain the automata.
Change examples or assumptions if your instructor specifies different rules.
