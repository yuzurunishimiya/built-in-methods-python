## Semua Built-in Fungsi di Python

Semua list abs
- [x] abs()
- [ ] all()
- [ ] any()
- [ ] ascii()
- [ ] bin()
- [ ] bool()
- [ ] breakpoint
- [ ] bytearra()
- [ ] bytes()
- [ ] callable()
- [ ] chr()
- [ ] classmethods()
- [ ] compile()
- [ ] complex()

### 1. abs()
> Method abs(x) akan me-return nilai absolut dari sebuah nomor. Argument bisa saja berupa sebuah nomor bertipe integer, floating point, atau sebuah object implementing `__abs__()`. Jika argumen adalah sebuah complex number, maka itu akan me-return magnitude.

example:
```python
a, b, c = -10, -2.5, 4-5j
abs_a, abs_b, abs_c = abs(a), abs(b), abs(c)
print("nilai abs() dari -10 adalah:", abs_a)
print("nilai abs() dari -2.5 adalah:", abs_b)
print("nilai abs() dari 4-5j adalah:", abs_c)
```