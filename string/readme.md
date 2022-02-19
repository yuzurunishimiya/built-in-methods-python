## Built-in methods String

### Semua list methods pada string
- [x] capitalize
- [ ] casefold
- [x] center
- [x] count
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
  - **fillchar (Opsional)** - karakter yang digabungkan\
    
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
    Centered string: ~~~python itu istimewa~~~~
    ```

**4. Count**

- Definisi
> `count` method ini mengembalikan jumlah kemunculan substring
> dalam string yang diberikan

- Syntax

    ```python
    string.count(substring, count=..., end=...)

    ```

- Parameters

    `count` method hanya memerlukan satu parameter untuk dieksekusi, tapi method ini\
    juga memiliki dua parameter opsional:

    * **substring** - string yang akan ditemukan & dihitung
    * **start (Opsional)** - indeks awal dalam string dimana pencariannya dimulai
    * **end (Opsional)** - indeks akhir dalam string dimana pencariannya berakhir

    > Note: Index pada python dimulai dari 0, bukan 1

- Return value\
    `count` method mengembalikan jumlah kemunculan substring dalam string yang diberikan

- Contoh:
1. Menghitung jumlah kemunculan substring dari string

    ```python
    string = "Python itu mudah, bukan?"
    substring = "u"

    count = string.count(substring)

    # print jumlah
    print("Jumlah huruf u:", count)
    ```
    
    ***Output:***
    ```text
    Jumlah huruf u: 3
    ```

2. Menghitung jumlah kemunculan substring dari string menggunakan `start` dan `end`

    ```python
    string = "Python itu mudah, bukan?"
    substring = "u"


    count = string.count(substring, 12, 18)

    print("Jumlah huruf u:", count)
    ```

    ***Output:***
    ```text
    Jumlah huruf u: 1
    ```
