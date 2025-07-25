# Mean-Variance-Standard Deviation Calculator

This is the first project of the freeCodeCamp "Data Analysis with Python" course.

## 📌 Project Goal

Build a function named `calculate()` that takes a list of 9 numbers and returns a dictionary with the mean, variance, standard deviation, min, max, and sum, calculated both row-wise, column-wise, and for the entire 3×3 matrix.

## 📁 Files Included

- `mean_var_std.py` &mdash; Main Python file with the `calculate()` function.

## 🧮 Example

```python
>>> calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])

# Returns:
{
  'mean': [[3.666..., 5.0, 3.333...], [3.333..., 4.0, 4.0], 3.888...],
  'variance': [[9.555..., 0.666..., 9.555...], [7.555..., 4.0, 6.888...], 6.987...],
  'standard deviation': [[3.092..., 0.816..., 3.092...], [2.748..., 2.0, 2.625...], 2.643...],
  'max': [[8, 6, 7], [6, 8, 7], 8],
  'min': [[1, 4, 0], [2, 0, 1], 0],
  'sum': [[11, 15, 10], [10, 12, 12], 35]
}
```

## 🛠 Technologies Used

- Python 3
- NumPy

## ✅ How to Run

1. Make sure Python is installed on your system.
2. Open the terminal in this project folder.
3. Run the following command:

   ```bash
   python mean_var_std.py
   ```

## 🎯 Learning Outcome

- How to use NumPy for matrix operations
- Understanding of basic statistics in Python

---

This project is part of the freeCodeCamp Data Analysis with Python

## 👤 Author
Hafizur Rahman 
hafizurrahman5004@gmail.com