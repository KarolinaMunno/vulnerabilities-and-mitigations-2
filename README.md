Secure Coding Examples: Vulnerable vs. Mitigated

This project illustrates common software security vulnerabilities and how to properly mitigate them. Each issue is demonstrated with a vulnerable version and a securely coded alternative, helping developers recognize poor coding practices and apply secure solutions.

Covered Vulnerabilities:

- Improper Restriction of Excessive Authentication Attempts
  Language: Python
  Demonstrates brute-force protection using retry limits.

- Use of One-Way Hash Without Salt
  Language: Python
  Highlights the importance of salting hashes for password security.

- Restricted Directory Access (Directory Traversal)
  Language: Python
  Shows how to validate file paths to prevent unauthorized access.

- Use of Dangerous Functions (e.g., gets() in C)
  Language: C
  Replaces unsafe input functions with secure alternatives.

How to Use:

Each file is self-contained. You can review and run both the vulnerable and mitigated versions to compare behaviors and understand the impact of secure coding practices.

Disclaimer:

All examples are for educational purposes only. The data and file names used are fictitious.
