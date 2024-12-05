# Hockey Data Analysis with Pandas

This project involves analyzing hockey game data using Python and Pandas. It focuses on answering specific questions using data manipulation, analysis, and visualization techniques.

## 📝 Introduction

The project explores hockey event data and expected goals (xG) to gain insights into team performance. Analysis includes determining game winners, examining successful passes, identifying blueline coordinates, and visualizing shot locations.

---

## ⚙️ Project Requirements

### Libraries
The project uses the following Python libraries:
- `numpy`
- `pandas`
- `matplotlib` or `plotly` (for data visualization)
- `sklearn` (optional, for advanced statistical analysis)

# 📂 Data Description

The project uses two datasets:

- **Event Data**: Contains event details such as shots, passes, goals, and coordinates adjusted so both teams shoot in the same direction.
- **Expected Goals (xG) Data**: Provides xG values for shots that successfully hit the net.

### 📌 Data Highlights:
- **X/Y Coordinates**: Represent event locations (in feet).
- **Binary Columns**: Use `1` for "Yes" and `0` for "No".
- **Special Events**: Includes Line Carry events when the puck is carried over specific lines.

---

## ❓ Questions Addressed

The analysis focuses on answering the following:

1. **Game Winner & Score**: Which team won the game, and what was the score?
2. **Expected Goals (xG) Battle**: Which team had a higher xG total?
3. **Performance Insights**: What do the results reveal about team performance?
4. **Successful Passes**: Which possession had the highest total successful passes, and why?
5. **Blueline Identification**: What are the likely x-coordinates of the bluelines?
6. **Shot Visualization**: Where were each team's shots located, and how do goals compare?

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hockey-data-analysis.git
   cd hockey-data-analysis


Ensure all libraries are installed using:
```bash
pip install numpy pandas matplotlib scikit-learn
```
![Plot Image](Plot%20Image.png)
