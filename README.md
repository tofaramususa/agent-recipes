# Agent Recipes 🤖

A collection of practical and ready-to-use LLM agent patterns inspired by Anthropic's research. This repository provides implementation examples for common agent architectures to help you build better LLM applications.

## Overview

This repository contains implementation examples for various LLM agent patterns, each designed to solve specific types of problems:

### 1. Prompt Chaining 📝
- Sequential processing where output from one LLM feeds into another
- Enables structured reasoning and step-by-step task completion
- Ideal for complex tasks requiring multiple stages of processing

### 2. Routing 🔄
- Low-latency dynamic routing of inputs to specialized LLM instances
- Optimizes efficiency by matching tasks to the most appropriate model configuration
- Perfect for applications requiring fast response times and specialized handling

### 3. Parallelization ⚡
- Concurrent execution of multiple LLM tasks
- Aggregates results from parallel operations
- Excellent for handling complex or large-scale operations efficiently

### 4. Orchestrator-Workers 🎯
- Implements a central orchestrator managing multiple worker LLMs
- Coordinates complex operations across multiple specialized agents
- Ideal for tasks requiring multiple specialized subtasks

### 5. Evaluator-Optimizer 🎯
- Implements feedback loops for continuous improvement
- Evaluates and refines LLM outputs iteratively
- Perfect for applications requiring high accuracy and quality control

### 6. Autonomous Agent (Coming Soon) 🚀
- Self-directing agent architecture
- Implements continuous learning and adaptation
- Ideal for complex, long-running tasks requiring autonomy

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Poetry for dependency management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/tofaramususa/agent-recipes.git
cd agent-recipes
```

2. Install dependencies using Poetry:
```bash
poetry install
```

### Dependencies
- together >= 1.3.14
- asyncio >= 3.4.3

## Usage

Each pattern is implemented in its own directory with example code and documentation. Navigate to the specific pattern directory to see implementation details and usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by Anthropic's research on LLM agent patterns
- Built with [Together AI](https://together.ai/)

## Contact

Tofara Mususa - jtofaramususa@gmail.com

---
Powered by [Together AI](https://together.ai/)
