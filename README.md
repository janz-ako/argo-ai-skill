# ARGO Excel Skill for Claude Code and Codex

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Claude Code](https://img.shields.io/badge/Claude-Code-blue)
![Codex](https://img.shields.io/badge/OpenAI-Codex-black)
![Status](https://img.shields.io/badge/status-active-success)

A reusable AI Agent Skill for building, repairing, reviewing, and explaining Monte Carlo simulation models created with the Booz Allen Hamilton ARGO Excel add-in.

The skill helps AI coding agents understand ARGO formulas, troubleshoot workbooks, validate simulation models, and apply Monte Carlo best practices for engineering, construction, finance, and risk analysis.

## Who is this for?

This skill is intended for:
- Risk analysts
- Financial analysts
- Project finance teams
- Construction professionals
- Engineers
- Monte Carlo practitioners
- Anyone using the ARGO Excel add-in with AI coding assistants

## Features

- ARGO formula generation and repair
- Distribution selection guidance
- Val parameter reference
- Op function reference
- Monte Carlo modelling best practices
- Construction and project finance examples
- Excel locale awareness (comma/semicolon)
- Static ARGO formula validator
- Validation checklists
- Ready for Claude Code and Codex

## Repository Structure

```text
.
├── SKILL.md
├── references/
├── examples/
├── templates/
├── tests/
├── scripts/
├── README.md
├── LICENSE
└── NOTICE.md
```

## Installation

### Claude Code (Personal)

Create the skills directory if it doesn't already exist:

```bash
mkdir -p ~/.claude/skills
```

Copy the skill into your Claude skills folder:

```bash
cp -R argo-excel ~/.claude/skills/
```

Your directory should look like:

```text
~/.claude/
└── skills/
    └── argo-excel/
        ├── SKILL.md
        ├── references/
        ├── examples/
        ├── templates/
        ├── tests/
        └── scripts/
```

Restart Claude Code if it is already running.

The skill will automatically be loaded whenever Claude detects that the task involves ARGO, Monte Carlo modelling, or ARGO Excel formulas.

### Claude Code (Project)

Copy the skill into your project:

```text
my-project/
└── .claude/
    └── skills/
        └── argo-excel/
```

The skill is then available only within that repository.

## Codex

### Personal Installation

```bash
mkdir -p ~/.agents/skills
cp -R argo-excel ~/.agents/skills/
```

### Repository Installation

```text
my-project/
└── .agents/
    └── skills/
        └── argo-excel/
```

## Example Prompts

```
Review this ARGO workbook.
```

```
Fix this RtaTriangular formula.
```

```
Convert this deterministic Excel model into an ARGO Monte Carlo model.
```

```
Recommend the most appropriate probability distribution.
```

```
Explain these simulation results to a CFO.
```

```
Find modelling mistakes in this workbook.
```

## Formula Validator

Run the included static validator:

```bash
python scripts/validate_argo_formula.py '=RtaTriangular(F5,D5,G5,ValName("Construction Cost"),ValPointEstimate(D5))'
```

The validator checks common syntax and modelling mistakes. It does **not** execute Excel or ARGO.

## Compatibility

This skill supports the publicly available ARGO Excel add-in.

Because ARGO is an archived project, the skill intentionally follows the published documentation and avoids generating undocumented functions or unsupported syntax.

## License

This project is released under the MIT License.

It is an independent community project and is **not affiliated with or endorsed by Booz Allen Hamilton**.

This repository contains original documentation, workflows, examples, prompts, and supporting code. It does **not** contain the ARGO software or binaries.