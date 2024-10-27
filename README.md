# AI Code Assistant Evaluation Project

## Project Overview
This project evaluates the security and effectiveness of AI-based code assistants (GitHub Copilot, Codeium, and Tabnine) in generating secure Python code and identifying potential vulnerabilities. The project integrates static code analysis with SonarQube and SonarLint to provide an objective assessment of these tools' reliability and security impact.

## Objectives
- **Security Evaluation**: Identify and assess the types of vulnerabilities (e.g., Cross-Site Scripting, SQL Injection) that can arise from AI-generated code.
- **Tool Comparison**: Evaluate GitHub Copilot, Codeium, and Tabnine in terms of code quality, security practices, and stability.
- **Best Practices**: Develop usage recommendations to help developers maximize benefits while minimizing risks when using AI code assistants.

## Project Structure
1. **Tool Configuration**
   - **IDE (PyCharm)**: Configured as the main development environment.
   - **AI Code Assistants**: GitHub Copilot, Codeium, and Tabnine are set up in PyCharm.
   - **Static Code Analysis**: Integrated SonarQube (via Docker) and SonarLint for identifying security issues and ensuring code quality.

2. **Example Code Files**
   - `example_codeium.py`: Code generated using Codeium.
   - `example_copilot.py`: Code generated using GitHub Copilot.
   - `example_tabnine.py`: Code generated using Tabnine.

3. **Analysis Methodology**
   - **Snippet Selection**: Carefully selected code snippets are used to examine each tool’s performance and security implications.
   - **Documentation of Vulnerabilities**: Identifying specific cases where tools introduce vulnerabilities.
   - **Comparative Scenarios**: Highlighting "best-case" (secure) and "worst-case" (vulnerable) outputs for each assistant.

4. **Results and Findings**
   - **Example Showcases**: Specific examples where the tools either met security expectations or introduced vulnerabilities.
   - **Vulnerability Statistics**: Summarized data on the frequency and types of vulnerabilities detected per tool.
   - **Practical Recommendations**: Guidelines for developers on safely integrating AI code assistants, particularly in security-sensitive environments.

## Use of Analysis Tools
SonarQube and SonarLint were incorporated to provide detailed security scans of generated code, supporting a clear, unbiased analysis of potential risks.

## Requirements
- **Python**: Primary language for code generation and testing.
- **Docker**: Necessary for running SonarQube.
- **PyCharm**: The main development environment for implementing and testing code assistant suggestions.

