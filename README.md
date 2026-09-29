# Ethical Keylogger Simulation

A controlled Python-based keylogger simulation developed as part of the **B.Y.T.E by Arithmatrix CyberSecurity Internship — Task 3**.

The project demonstrates how keyboard events can be captured, encrypted, stored locally, and securely purged while keeping the monitoring scope limited to the application's own visible text box.

---

## Ethical Scope

This project is intentionally designed as a **local-only educational simulation**.

The application:

* Captures keystrokes only inside its own visible text box.
* Encrypts captured data before storing it.
* Stores the encrypted log locally.
* Provides a purge option to delete the log.
* Does not transmit data over a network.
* Does not monitor other applications.
* Does not use hidden or stealth behavior.
* Does not establish persistence or start automatically.
* Does not collect real credentials.

Testing must be performed only on an owned device or a device for which explicit permission has been given.

**Only dummy test data should be used during demonstrations.**

---

## Features

* Visible graphical interface using Python Tkinter.
* Local-only keyboard event capture.
* Captures events only from the application's text box.
* Handles normal characters and selected special keys.
* Encrypts every captured event before storage.
* Uses Fernet authenticated encryption.
* Generates a local encryption key.
* Stores encrypted data in a local file.
* Provides an encrypted-log purge function.
* Includes test cases.
* Includes a consent and ethics declaration.
* Includes a sanitized encrypted-log sample.

---

## How the Simulation Works

The application follows this process:

```text
User types inside the application
            ↓
    Keyboard event detected
            ↓
       Event processed
            ↓
      Event encrypted
            ↓
   Stored in keystrokes.enc
```

The application does **not** install a system-wide keyboard hook.

Therefore, typing in another application is outside the scope of this simulation.

---

## Technology Used

| Technology            | Purpose                     |
| --------------------- | --------------------------- |
| Python                | Main programming language   |
| Tkinter               | Visible graphical interface |
| Cryptography / Fernet | Authenticated encryption    |
| Local file storage    | Encrypted log storage       |

---

## Requirements

* Python 3.x
* `cryptography`

Tkinter is normally included with standard Python installations on Windows.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Mohamed-MKM/CS_3_EthicalKeyloggerSimulation_byte.git
```

Move into the project directory:

```bash
cd CS_3_EthicalKeyloggerSimulation_byte
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run:

```bash
python ethical_keylogger.py
```

A visible application window will open.

Click inside the text box and enter **dummy test data**, for example:

```text
Test123
Hello World
CyberLab
```

The application will capture the keyboard events generated inside its own text box and store encrypted records locally.

---

## Encryption

The project uses:

```python
from cryptography.fernet import Fernet
```

Fernet provides authenticated symmetric encryption.

When the program starts, it creates an encryption key if one does not already exist.

The key is stored locally in:

```text
encryption.key
```

Captured events are encrypted before being written to:

```text
keystrokes.enc
```

The stored file therefore does not contain the captured keystrokes as readable plaintext.

### Important

The generated files:

```text
encryption.key
keystrokes.enc
```

should **not** be committed to a public GitHub repository when they contain data from an actual demonstration.

Only the sanitized sample file should be included in the repository.

---

## Special Keys

The simulation converts selected keyboard events into readable representations before encryption.

| Keyboard Event     | Representation |
| ------------------ | -------------- |
| Space              | ` `            |
| Enter              | `[ENTER]`      |
| Backspace          | `[BACKSPACE]`  |
| Tab                | `[TAB]`        |
| Other special keys | `[KEY_NAME]`   |

These representations are encrypted before being stored.

---

## Purge Function

The application includes a:

```text
Purge Encrypted Log
```

button.

When selected, the program deletes:

```text
keystrokes.enc
```

This provides a simple mechanism for removing the locally stored demonstration log.

If no log exists, the program informs the user that there is no encrypted log to delete.

---

## Test Cases

The repository contains `test_cases.txt` with tests covering:

* Normal text input
* Spaces
* Enter
* Tab
* Backspace
* Encrypted storage
* Log purging
* Local-only behavior
* Scope isolation

Example:

```text
Test Case 1 - Normal Text

Input:
Hello

Expected:
- "Hello" appears in the visible text box.
- An encrypted local log is created.
- Captured events are not stored as plaintext.
```

Another test verifies the scope of the application:

```text
Test Case - Scope Isolation

Action:
Type in another application while the simulation is not focused.

Expected:
The simulation does not capture those keystrokes.
```

---

## Sanitized Encrypted Log

The repository contains:

```text
sample_encrypted_log.txt
```

This file contains a sanitized example of encrypted output.

It is provided only to demonstrate the format of encrypted records.

It does **not** contain:

* Real passwords
* Personal information
* Authentication credentials
* Private messages
* Sensitive user data

The encryption key used to generate the sample is intentionally not included.

---

## Consent and Ethics Declaration

The project contains:

```text
signed_declaration.md
```

The declaration confirms that the project is intended for authorized educational testing.

It establishes that:

1. Testing must be performed on an owned or explicitly authorized device.
2. Only dummy/test information should be used.
3. Real passwords and sensitive information should not be collected.
4. The application is intended to remain local-only.
5. Captured data should not be transmitted to unauthorized systems.

The student should add the required date and signature before submission.

---

## Security and Privacy Considerations

A keylogging system can expose highly sensitive information if used outside an authorized environment.

For this reason, this project deliberately avoids functionality such as:

* System-wide keyboard monitoring
* Hidden execution
* Remote logging
* Data exfiltration
* Persistence
* Credential harvesting
* Monitoring other applications

The project is intended to demonstrate the **security concepts surrounding keyboard-event capture and protected local storage**, rather than to provide covert monitoring functionality.

---

## Limitations

This is an educational simulation rather than a production security-monitoring system.

The main limitations are:

### 1. Local Encryption Key

The encryption key is stored locally on the same machine as the encrypted log.

If an attacker obtains both the key and encrypted log, the protection provided by encryption is significantly reduced.

### 2. Limited Capture Scope

The application only receives keyboard events from its own text box.

It cannot monitor keyboard activity in other applications.

### 3. No Remote Storage

The application intentionally has no network communication.

### 4. Basic Purge

The purge operation removes the encrypted log file but is not intended to represent a forensic-grade secure deletion mechanism.

---

## Privacy Guidelines

Never use this project to collect:

* Real passwords
* Banking credentials
* Authentication codes
* Private conversations
* Personal secrets
* Another person's information without explicit authorization

Use dummy data such as:

```text
Test123
Hello World
CyberLab
DemoPassword123
```

Do not use passwords from real accounts during testing.

---

## Project Structure

```text
CS_3_EthicalKeyloggerSimulation_byte/
│
├── ethical_keylogger.py
├── requirements.txt
├── test_cases.txt
├── sample_encrypted_log.txt
├── signed_declaration.md
├── demonstration.png
└── README.md
```

---

## Demonstration

The demonstration should show the application running in a visible window.

Recommended demonstration steps:

### Step 1 — Start the application

```bash
python ethical_keylogger.py
```

### Step 2 — Enter dummy data

For example:

```text
Test123
```

### Step 3 — Verify encrypted storage

Confirm that:

```text
keystrokes.enc
```

has been created.

The contents should appear as encrypted data rather than readable plaintext.

### Step 4 — Demonstrate special keys

Use:

* Space
* Enter
* Backspace
* Tab

### Step 5 — Demonstrate purge

Click:

```text
Purge Encrypted Log
```

Confirm that the encrypted log is deleted.

### Screenshot

The final repository should contain an actual screenshot of the student's local program execution at:

```text
demonstration.png
```

The screenshot should preferably show:

* The application title.
* The visible text box.
* Dummy test data.
* The purge button.
* Evidence that the application is running normally.

---

## Internship Requirements

This repository is designed to fulfill the required **Task 3 — Ethical Keylogger Simulation** deliverables:

* [x] Public GitHub repository
* [x] Local-only key capture simulation
* [x] Encrypted local storage
* [x] Secure purge option
* [x] Prominent ethics and consent section
* [x] Signed declaration template
* [x] Sanitized encrypted log
* [x] Test cases
* [x] README documentation
* [x] Actual demonstration screenshot captured from the student's local execution


---

## Repository Naming Convention

The required repository name is:

```text
CS_3_EthicalKeyloggerSimulation_byte
```

This follows the internship naming convention:

```text
DomainShortHand_TaskNumber_TaskTitle_byte
```

Where:

```text
CS
→ CyberSecurity

3
→ Task Number

EthicalKeyloggerSimulation
→ Task Title

byte
→ Internship naming suffix
```

---

## Author

**Mohamed MK**

CyberSecurity Internship — **B.Y.T.E by Arithmatrix**
