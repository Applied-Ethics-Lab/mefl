# MEFL — Moral Ethics Functional Language

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

MEFL is a lightweight functional programming language and interpreter designed to formalize and evaluate ethical reasoning. It integrates core ethical concepts such as duties and virtues, enabling users to model and assess the morality of actions programmatically.

This project is developed by the Applied Ethics Lab.

---

## Features

- **Ethical Modeling:** Encode duties (perfect and imperfect) and virtues with customizable traits.
- **Ethical Evaluation:** Assess actions based on duty compliance and virtue development.
- **Functional Language Core:** Support for functions, variables, expressions, and built-in evaluators.
- **Extensible:** Easily add new duties, virtues, and built-in functions.
- **Python-based Interpreter:** Easy to install, modify, and extend.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

Clone the repository:

\`\`\`bash
git clone https://github.com/Applied-Ethics-Lab/mefl.git
cd mefl
\`\`\`

(Optional) Create and activate a virtual environment:

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

Install dependencies if any (currently none required):

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Usage

Run MEFL programs with the interpreter:

\`\`\`bash
python mefl-lang/main.py path/to/your_program.mefl
\`\`\`

### Sample Usage

Here is a quick example that evaluates the ethics of an action involving lying:

\`\`\`mefl
let action = {"actions": ["lie"]}
print(is_ethical(action))
\`\`\`

This will output \`False\` because lying violates the perfect duty of No Lying.

---

## Project Structure

- \`mefl-lang/\` — Interpreter and language core files
- \`ethics/\` — Ethical concepts and evaluators (duties, virtues, ethical scoring)
- \`stdlib/\` — Built-in functions and standard library bindings

---

## Extending MEFL

- Add new duties or virtues by modifying files in the \`ethics/\` directory.
- Define new built-in functions in \`stdlib/builtins.py\`.
- Extend interpreter capabilities by modifying \`interpreter.py\`.

---

## Contributing

We welcome contributions and suggestions! Please submit issues and pull requests via GitHub.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Contact

Applied Ethics Lab  
GitHub: [Applied-Ethics-Lab](https://github.com/Applied-Ethics-Lab)
