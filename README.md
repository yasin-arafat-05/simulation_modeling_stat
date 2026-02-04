# Statistical Distribution Simulator

A comprehensive interactive web application for visualizing and exploring continuous and discrete probability distributions. Built with Python Dash, this tool provides real-time, interactive visualizations of various statistical distributions commonly used in simulation modeling and statistics.

## 🎯 Features

### Continuous Distributions

- **Uniform Distribution** - Equal probability across a range
- **Exponential Distribution** - Time between events in a Poisson process
- **Gamma Distribution** - Sum of exponentially distributed random variables
- **Weibull Distribution** - Reliability analysis and life data analysis
- **Normal Distribution** - Bell curve for natural phenomena
- **Log-Normal Distribution** - Product of many independent random variables
- **Beta Distribution** - Probabilities and proportions
- **Pearson Type V Distribution** - Skewed distributions
- **Log-Logistic Distribution** - Survival analysis
- **Johnson SB Distribution** - Bounded distributions

### Discrete Distributions

- **Bernoulli Distribution** - Binary outcomes
- **Binomial Distribution** - Number of successes in fixed trials
- **Poisson Distribution** - Rare events over time/space
- **Discrete Uniform Distribution** - Equal discrete probabilities

## 🚀 Live Demo

Visit the live application: [Statistical Distribution Simulator](https://statistical-distribution-simulator.onrender.com)

## 📋 Prerequisites

- Python 3.8 or higher
- `uv` package manager or `pip`

## 🔧 Local Installation

### 1. Clone

```bash
git clone https://github.com/yasin-arafat-05/simulation_modeling_stat/
```

### 2. Sync

```bash
uv sync
```

### 3. Run

```bash
uv run app.py
```

> The application will be available at `http://127.0.0.1:8050/`

## 🌐 Production Mode

### 1. Clone

```bash
git clone https://github.com/yasin-arafat-05/simulation_modeling_stat/
```

### 2. Dependency

```bash
pip install -r requirements.txt
```

> It's recommended to run in a virtual environment!

### 3. Deploy

```bash
gunicorn app:server --bind 0.0.0.0:8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Note**: This application is for educational and research purposes. Ensure you understand the statistical properties and appropriate use cases for each distribution.
