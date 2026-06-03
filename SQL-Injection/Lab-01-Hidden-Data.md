# SQL Injection - Hidden Data Retrieval

## Lab Name
SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

## OWASP Category
Injection

## Description
SQL Injection occurs when user input is interpreted as part of a database query, allowing an attacker to modify the intended SQL logic.

## Root Cause
Unsanitized user input was incorporated directly into an SQL query.

## Impact
- Data disclosure
- Authentication bypass
- Data modification
- Database compromise

## Detection Method
Manipulated input parameters and observed changes in application behavior.

## Tools Used
- Burp Suite Repeater

## Key Learning
User-controlled input can alter SQL query logic and expose sensitive information when proper validation is missing.

## Mitigation
- Parameterized queries
- Prepared statements
- Input validation
- Least privilege principle

## Skills Practiced
- Burp Suite
- SQL Injection Testing
- Vulnerability Analysis
- OWASP Top 10
- SQL Injection Testing
- Vulnerability Analysis
- OWASP Top 10
