# MEFL Language Specification — Addendum

This document expands on the core MEFL specification with examples, clarifications, and implementation notes for each section.

---

## Table of Contents

- [1. Introduction — Addendum](#1-introduction--addendum)  
- [2. Data Types — Addendum](#2-data-types--addendum)  
  - [2.1 Primitive Types](#21-primitive-types)  
  - [2.2 Ethics Domain Types](#22-ethics-domain-types)  
- [3. Syntax Rules — Addendum](#3-syntax-rules--addendum)  
  - [3.1 Variable Declaration](#31-variable-declaration)  
  - [3.2 Identifiers](#32-identifiers)  
  - [3.3 Expressions](#33-expressions)  
  - [3.4 Statements](#34-statements)  
  - [3.5 Control Flow](#35-control-flow)  
  - [3.6 Functions](#36-functions)  
  - [3.7 Comments](#37-comments)  
- [4. Ethics-Specific Constructs — Addendum](#4-ethics-specific-constructs--addendum)  
  - [4.1 Duty, Virtue, Principle, Value Declarations](#41-duty-virtue-principle-value-declarations)  
  - [4.2 Conflict Detection](#42-conflict-detection)  
  - [4.3 Priority Assignment](#43-priority-assignment)  
- [5. Input/Output — Addendum](#5-inputoutput--addendum)  
- [Appendix: Example MEFL Program](#appendix-example-mefl-program)  

---

## 1. Introduction — Addendum

- **Purpose:**  
  MEFL is designed for formal ethical modeling with a programmer-friendly syntax.

- **Use cases:**  
  Ethical AI reasoning, compliance modeling, decision analysis.

---

## 2. Data Types — Addendum

### 2.1 Primitive Types

- **Numbers:** Support integers and floating-point numbers internally as JavaScript `number`.  
- **Strings:** UTF-8 support with escaped characters using `\`.  
- **Booleans:** Only `true` and `false` supported.

### 2.2 Ethics Domain Types

- Represented as first-class objects with metadata like description and priority.  
- Future extensions might add types such as `MoralAgent` or `Consequence`.

---

## 3. Syntax Rules — Addendum

### 3.1 Variable Declaration

- Variables are immutable by default to encourage safer modeling.  
- Future support may include `var` for mutable variables.

**Example:**

```mefl
let dutyTruth = duty("always tell truth");

