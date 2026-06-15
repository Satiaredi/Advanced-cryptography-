# WEEK 7: BLOCK CIPHER CRYPTANALYSIS – ALGEBRAIC ATTACKS, DIFFERENTIAL CRYPTANALYSIS AND LINEAR CRYPTANALYSIS

## Learning Objectives
By the end of this week, students should be able to:
1. Define cryptanalysis and explain its importance in cryptography
2. Understand how attackers analyze block ciphers
3. Explain algebraic attacks on block ciphers
4. Describe differential cryptanalysis
5. Describe linear cryptanalysis
6. Identify weaknesses in poorly designed block ciphers
7. Analyze the security strength of modern block cipher systems
8. Perform basic cryptanalysis experiments using Python

---

## Introduction
Designing an encryption algorithm is only one side of cryptography. The other side involves evaluating whether the algorithm can resist attacks. This process is known as cryptanalysis.

Cryptanalysis helps researchers discover weaknesses before attackers do. Modern encryption standards such as AES have survived years of cryptanalysis, making them trusted worldwide.

This week focuses on three major cryptanalytic techniques used against block ciphers:
1. **Algebraic Attacks**
2. **Differential Cryptanalysis**
3. **Linear Cryptanalysis**

These methods are among the most important tools used by security researchers to evaluate cipher security.

---

## Key Definitions

### Cryptanalysis
Cryptanalysis is the science of studying and breaking cryptographic systems without knowing the secret key.

**Objectives of Cryptanalysis:**
- Recover secret keys
- Recover plaintext
- Predict future encrypted values
- Evaluate cipher security

---

### Block Cipher Cryptanalysis
The process of examining a block cipher to identify vulnerabilities that could allow attackers to recover information or secret keys.

**Examples of targeted ciphers:**
- DES
- AES
- Blowfish
- Twofish
- Serpent

---

### Attack Model
An attack model describes the information available to an attacker.

**Common attack models:**

| Attack Type | Description |
|-------------|-------------|
| **Ciphertext-Only Attack** | Attacker only has ciphertext |
| **Known Plaintext Attack** | Attacker knows some plaintext and ciphertext pairs |
| **Chosen Plaintext Attack** | Attacker chooses plaintexts and observes ciphertext |
| **Chosen Ciphertext Attack** | Attacker chooses ciphertexts and observes decrypted output |

---

## Algebraic Attacks

### Definition
An algebraic attack attempts to express the encryption process as a set of mathematical equations and solve them to recover the secret key.

### Basic Idea
Many encryption algorithms perform mathematical operations repeatedly. Attackers attempt to:
1. Observe outputs
2. Create equations
3. Solve equations
4. Recover keys

### Example
Suppose:
```
C = P XOR K
```

Where:
- P = Plaintext
- K = Secret Key
- C = Ciphertext

If enough information is available, an attacker may derive:
```
K = P XOR C
```

Poorly designed ciphers may expose such relationships.

### Advantages for Attackers
- Faster than brute force attacks
- Exploits mathematical weaknesses
- Can recover keys efficiently

### Weaknesses Exploited
- Low non-linearity
- Weak S-Boxes
- Predictable structures
- Simple algebraic relationships

---

## Differential Cryptanalysis

### Definition
Differential cryptanalysis studies how differences in plaintext affect differences in ciphertext. It is one of the most powerful attacks against block ciphers.

### Main Idea
Attackers compare:
- Two similar plaintexts
- Their corresponding ciphertexts

to discover patterns.

### Example
```
Plaintext 1: HELLO
Plaintext 2: HELLP
```

Only one character changes. The attacker analyzes how that change propagates through encryption.

### Goal
Determine:
- Secret keys
- Internal cipher behavior
- Weak rounds

### Differential Characteristics
A differential characteristic tracks how differences move through encryption rounds.

Strong ciphers make differences spread rapidly.

---

## Linear Cryptanalysis

### Definition
Linear cryptanalysis uses linear approximations to describe relationships among:
- Plaintext bits
- Ciphertext bits
- Key bits

### Main Idea
Instead of solving exact equations, attackers search for statistical relationships.

**Example:**
```
P_1 XOR P_2 XOR C_3 = K_1
```

If this relationship occurs more frequently than expected by chance, information about the key may be revealed.

### Requirements
- Large amounts of plaintext-ciphertext pairs
- Statistical analysis

### Goal
Recover secret key information through probability.

---

## Differential vs Linear Cryptanalysis

| Aspect | Differential Cryptanalysis | Linear Cryptanalysis |
|--------|----------------------------|-----------------------|
| **Method** | Uses input differences | Uses linear approximations |
| **Analysis** | Examines plaintext changes | Examines statistical bias |
| **Effective Against** | Weak S-Boxes | Weak linear properties |
| **Introduced By** | Biham and Shamir | Matsui |

---

## Security Measures Against Cryptanalysis

Modern block ciphers defend against attacks using:

### Strong S-Boxes
- High non-linearity
- No predictable patterns

### Multiple Rounds
- Increase complexity
- Improve diffusion

### Avalanche Effect
- A small input change causes significant output changes

### Strong Key Schedules
- Generate secure round keys

---

## Why AES Remains Secure

AES is designed with:
- Strong S-Boxes
- High diffusion
- Multiple rounds (10, 12, or 14 depending on key size)
- Excellent avalanche properties
- Resistance to known differential and linear attacks
- **No practical attack currently breaks full AES encryption**

---

## Class Demonstrations

### Demonstration 1: XOR-Based Analysis
```python
plaintext = 12
key = 5
ciphertext = plaintext ^ key
recovered = ciphertext ^ plaintext
print("Recovered Key:", recovered)
```
**Expected Learning:** Observe how XOR relationships can expose information in simple systems.

### Demonstration 2: Measuring Differences
```python
p1 = 10
p2 = 11
difference = p1 ^ p2
print("Difference:", difference)
```
**Discussion:** This demonstrates the concept of input differences used in differential cryptanalysis.

### Demonstration 3: Avalanche Effect Observation
```python
text1 = "HELLO"
text2 = "HELLo"
print(hash(text1))
print(hash(text2))
```
**Discussion:** A small change produces a completely different output.

### Demonstration 4: Frequency Analysis
```python
from collections import Counter
data = "ABABABABCCCCDDD"
count = Counter(data)
print(count)
```
**Expected Learning:** Understand statistical bias used in cryptanalysis.

### Demonstration 5: Simple Probability Calculation
```python
successes = 75
total = 100
probability = successes / total
print("Probability:", probability)
```
**Discussion:** Linear cryptanalysis relies heavily on probability and statistical patterns.

---

## Class Activities

### Activity 1: Differential Observation Exercise
**Students should:**
1. Encrypt two similar messages
2. Compare ciphertexts
3. Identify differences

**Skills Developed:**
- Pattern analysis
- Differential analysis

### Activity 2: Algebraic Relationship Exploration
**Students should:**
1. Create simple XOR equations
2. Solve for unknown values
3. Discuss weaknesses

**Expected Skills:**
- Mathematical reasoning
- Security analysis

### Activity 3: Attack Comparison
**Compare:**
- Brute Force Attack
- Algebraic Attack
- Differential Cryptanalysis
- Linear Cryptanalysis

**Evaluate:**
- Speed
- Complexity
- Practicality
- Success Rate

---

## Practical Tasks

### Task 1: Differential Cryptanalysis Simulation
Develop a Python program that:
1. Accepts two plaintext inputs
2. Computes differences
3. Displays observations

**Deliverables:**
- Source Code
- Screenshots
- Analysis Report

### Task 2: Block Cipher Security Research
Research and explain:
1. Differential Cryptanalysis
2. Linear Cryptanalysis
3. Algebraic Attacks

**Report Requirements:**
- 3–5 pages
- Real-world examples
- References included

### Task 3: Security Evaluation of AES
Investigate:
- Why AES is resistant to differential attacks
- Why AES is resistant to linear attacks
- Modern research findings on AES security

Prepare a summary report.

---

## Advanced Programming Tasks
Develop a mini cryptanalysis toolkit that:
1. Calculates input differences
2. Performs frequency analysis
3. Measures statistical bias
4. Displays results automatically

---

## Challenge Task
Create a **Block Cipher Security Analyzer** that includes:

**Features:**
- Avalanche Effect Testing
- Difference Analysis
- Frequency Distribution
- Statistical Reporting

**Bonus Features:**
- Graphical Charts
- Export Results
- User-Friendly Interface

---

## Recommended Tools

| Activity | Suggested Tools |
|----------|------------------|
| Programming | Python IDLE, VS Code |
| Data Analysis | NumPy, Pandas |
| Visualization | Matplotlib |
| Research | Google Scholar |
| Documentation | MS Word, Google Docs |
| Version Control | GitHub |

---

## Weekly Reflection Questions
1. What is cryptanalysis?
2. Why is cryptanalysis important in cryptography?
3. How do algebraic attacks work?
4. What is differential cryptanalysis?
5. What is linear cryptanalysis?
6. Why are strong S-Boxes important?
7. How does the avalanche effect improve security?
8. Why is AES considered resistant to modern cryptanalytic attacks?

---

## Practical Portfolio Task

Create a GitHub repository named:
```
BIT4138-Week7-Cryptanalysis
```

Upload:
- Python Programs
- Screenshots
- Practical Reports
- Research Findings
- Reflection Notes

---

## Industry Insight

Every modern encryption standard undergoes extensive cryptanalysis before adoption. Organizations such as:
- National Institute of Standards and Technology
- Governments
- Banks
- Cloud providers
- Cybersecurity companies

continuously test cryptographic systems against new attack methods.

Understanding cryptanalysis helps students think like both **defenders and attackers**. Whether you become a:
- Software Engineer
- Network Administrator
- Data Scientist
- Cloud Engineer
- AI Specialist
- Digital Forensics Analyst
- Cybersecurity Professional

The ability to evaluate security weaknesses is a highly valuable skill.

**Modern technology depends on secure cryptography, making cryptanalysis one of the most fascinating and rewarding areas of computing.**
