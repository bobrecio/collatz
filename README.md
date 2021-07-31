# Collatz Conjecture using Python
[wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)

*Requires that you have Python 3 installed on your computer

1. Download the `collatz.py` file to your computer
2. Run `python3 collatz.py`
3. You will be promputed for an integer; enter an integer in the input field
4. The script will run the function for the number that you entered, display the iteration and the resulting next number until it reaches 1

The function is basically...
```
while n > 1:
  if n is ever: n = n /2
  if n is odd: n = (n*3) + 1
```
