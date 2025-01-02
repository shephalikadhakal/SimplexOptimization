# Simplex Optimization Program with GUI

This Python program implements a simplex optimization algorithm with a graphical user interface (GUI) using `tkinter` and `PuLP`. It allows the user to solve linear programming problems by inputting the coefficients for the objective function and constraints, and then optimizing the solution.

## Features

- **Objective Function**: Maximize a linear objective function with three variables (X1, X2, X3).
- **Constraints**: Support for multiple constraints, including `<=`, `>=`, and `=`.
- **Graphical Interface**: User-friendly interface built with `tkinter`.
- **Linear Programming**: The optimization is handled using `PuLP`.

## Installation

### Requirements

To run the program, you'll need Python 3.x and the following packages:

- **PuLP** (for linear programming)
- **tkinter** (for GUI, typically included with Python)

### Step-by-Step Installation

1. **Install Python**:
   - Download and install Python 3.x from [python.org](https://www.python.org/).

2. **Install `pip`** (if not already installed):
   - `pip` is usually installed by default with Python. To verify, run:
     ```bash
     pip --version
     ```

3. **Install Dependencies**:
   - Open a terminal or command prompt and run the following command to install PuLP:
     ```bash
     pip install pulp
     ```
   - `tkinter` is included by default with Python, but if you encounter issues, you may need to install it separately (especially on Linux).

4. **Clone the Repository**:
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/<your-username>/simplex-optimization.git
     ```
   - Replace `<your-username>` with your actual GitHub username.

## Running the Program

1. Navigate to the project directory:
   ```bash
   cd SimplexOptimization
   ```
2. Run the python file
   ```bash
   python Optimization.py
   ```
