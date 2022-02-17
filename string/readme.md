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

**1. capitalize**

- Definisi
  > Pada python, method capitalize mengubah karakter pertama pada sebuah string menjadi
  > huruf kapital dan mengubah karakter lainnya menjadi huruf kecil (jika ada).

- syntax pada capitalize() adalah:
    ```python
    string.capitalize()
    ```

- parameter\
    Fungsi `capitalize()` tidak menggunakan parameter apapun
  

- Return value dari capitalize()\
    Fungsi `capitalize()` me-return sebuah string dengan karakter pertama menjadi kapital dan
    karakter lainnya menjadi huruf kecil. Fungsi ini tidak mengubah string aslinya.

  
- Contoh:
1. Capitalize sebuah kalimat
    ```python
    string = "python sangat bagus"
    capialize_string = string.capitalize()
    print("Original string: ", string)
    print("Capitalized string: ", capialize_string)
    ```
   ***Output:***
    ```text
   Original string: pyton sangat bagus
   Capitalize string: Python sangat bagus
    ```
   
2. Karakter pertama yang bukan alphabetic:
    ```python
    string = "% adalah operator modulus"
    capialize_string = string.capitalize()
    print("Original string: ", string)
    print("Capitalized string: ", capialize_string)
    ```
    ***Output:***
    ```text
    Original string: % adalah operator modulus
    Capitalize string: % adalah operator modulus
    ```



**2. casefold**

**3. center**

- Definisi:
  > `center` method me-return sebuah string yang diisi dengan karakter 
  > yang ditentukan
  
- Syntax:
    ```python
    string.center(width, fillchar)
    ```

- Parameters\
  `center()` membutuhkan dua argument:
  - **width** - panjang string dengan karakter yang digabungkan
  - **fillchar** (Opsional) - karakter yang digabungkan\
    
  `fillchar` argument bersifat opsional. Apabila tidak ditentukan maka akan diisi
  dengan `spasi` sebagai argument bawaan (default)
  

- Return value\
  `center()` method mengembalikan sebuah string yang sudah digabungkan
  dengan `fillchar` spesifik. Method ini tidak akan memodifikasi string original


- Contoh:
1. `center()` method dengan `Default fillchar`
    ```python
    string = "python itu istimewa"
    centered_string = string.center()
    print("Centered string: ", centered_string)
    ```
   ***Output:***
    ```text
    Centered string:    python itu istimewa    
    ```

2. `center()` method dengan ~ fillchar
    ```python
    string = "python itu istimewa"
    centered_string = string.center(26, "$")
    print("Centered string: ", centered_string)
    ```
   ***Output:***
    ```text
    Centered string: ~~~python itu istimewa~~~~'
    ```