## Built-in methods String

### Semua list methods pada string
- [x] capitalize
- [ ] casefold
- [ ] center
- [ ] count
- [ ] encode
- [ ] endswith
- [ ] expandtabs
- [ ] find
- [ ] format
- [ ] format_map
- [ ] index
- [ ] isalnum
- [ ] isalpha
- [ ] isdecimal
- [ ] isdigit
- [ ] isidentifier
- [ ] islower
- [ ] isnumeric
- [ ] isprintable
- [ ] isspace
- [ ] istitle
- [ ] isupper
- [ ] join
- [ ] ljust
- [ ] lower
- [ ] lstrip
- [ ] maketrans
- [ ] partition
- [ ] replace
- [ ] rfind
- [ ] rindex
- [ ] rjust
- [ ] rpartition
- [ ] rsplit
- [ ] rstrip
- [ ] split
- [ ] spitlines
- [ ] startswith
- [ ] strip
- [ ] swapcase
- [ ] title
- [ ] translate
- [ ] upper
- [ ] zfill

#### 1. capitalize

- Definisi
    > Pada python, method capitalize mengubah karakter pertama pada sebuah string menjadi
    > huruf kapital dan mengubah karakter lainnya menjadi huruf kecil (jika ada).

- syntax pada capitalize() adalah:
    ```python
    string.capitalize()
    ```

- parameter\
    Fungsi `capitalize()` tidak menggunakan parameter apapun
  

- Return value dari capitalize()
    Fungsi `capitalize()` me-return sebuah string dengan karakter pertama menjadi kapital dan
    karakter lainnya menjadi huruf kecil. Fungsi ini tidak mengubah string aslinya.

  
- Contoh:
1. Capitalize sebuah kalimat
    ##### Input:
    ```python
    string = "python sangat bagus"
    capialize_string = string.capitalize()
    print("Original string: ", string)
    print("Capitalized string: ", capialize_string)
    ```
   ##### Output:
    ```text
   Original string: pyton sangat bagus
   Capitalize string: Python sangat bagus
    ```
   
2. Karakter pertama yang bukan alphabetic:
    ##### Input:
    ```python
    string = "% adalah operator modulus"
    capialize_string = string.capitalize()
    print("Original string: ", string)
    print("Capitalized string: ", capialize_string)
    ```
    ##### Output:
    ```text
    Original string: % adalah operator modulus
    Capitalize string: % adalah operator modulus
    ```