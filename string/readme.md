## Built-in methods String

### Semua list methods pada string
- [x] [capitalize](#1-capitalize)
- [ ] [casefold](#2-casefold)
- [x] [center](#3-center)
- [x] [count](#4-count)
- [x] [encode](#5-encode)
- [x] [endswith](#6-endswith)
- [ ] [expandtabs](#7-expandtabs)
- [x] [find](#8-find)
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

### 1. capitalize

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



### 2. casefold

### 3. center

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
  - **fillchar (Opsional)** - karakter yang digabungkan
    
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

### 4. count

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

### 5. encode

- Definisi

> `encode` method mengembalikan encoded version dari string yang diberikan

- Syntax

    ```python
    string.encode(encoding='UTF-8', errors='strict')
    ```

- Parameters

    Secara default, method `encode()` tidak memerlukan parameter apapun.\
    Method ini akan mengembalikan sebuah versi `utf-8` dari string. Jika ada kegagalan,\
    method ini membangkitkan sebuah `UnicodeDecodeError` exception.

    Akan tetapi method ini bisa menggunakan dua parameter:
    * **encoding** - tipe pengkodean `(encoding)` yang mana string akan dikonversikan
    * **errors** - respon ketika pengkodean gagal. Ada 6 tipe dari respon error
        - strict - respon bawaan yang akan mengangkat sebuah `UnicodeDecodeError` exception ketika error
        - ignore - mengabaikan unicode yang tidak dapat dikodekan dari hasilnya
        - replace - mengganti unicode yang tidak dapat dikodekan menjadi tanda tanya **?**
        - xmlcharrefreplace - memasukkan XML karakter alih-alih unicode yang tidak dapat dikodekan
        - backslashreplace - memasukkan `\uNNNN` escape sequence alih-alih unicode yang tidak dapat dikodekan
        - namereplace - memasukkan sebuah `\N{...}` escape sequence alih-alih unicode yang tidak dapat dikodekan

- Contoh

1. Encode menggunakan default Utf-8 Encoding

    ```python
    # unicode string
    string = "pythön!"

    # print string
    print("Stringnya adalah:", string)

    # default encoding to utf-8
    string_utf = string.encode()

    # print result
    print("Versi encodednya adalah:", string_utf)
    ```

    ***Output:***
    ```text
    Stringnya adalah: pythön!
    Versi encodednya adalah: b'pyth\xc3\xb6n!'
    ```

2. Encoding dengan parameter error

    ```python
    # unicode string
    string = "pythön!"

    # print string
    print("Stringnya adalah:", string)

    # ignore error
    print("Versi encodednya (dengan ignore) adalah:", string.encode("ascii", "ignore"))

    # replace error
    print("Versi encodednya (dengan replace) adalah:", string.encode("ascii", "replace"))
    ```

    ***Output:***
    ```text
    Stringnya adalah: pythön!
    Versi encodednya (dengan ignore) adalah: b'pythn!'
    Versi encodednya (dengan replace) adalah: b'pyth?n!'
    ```


- Tambahan
    > Sejak python 3.0, string disimpan sebagai Unicode, yaitu setiap karakter pada string direpresentasikan dengan 
    > sebuah code point. Jadi, setiap string hanya merupakan sebuah urutan dari Unicode code points.

    > Untuk efisiensi penyimpanan dari string, urutan-urutan dari code points itu dikonversi ke sebuah set dari bytes. 
    > Proses ini dikenal dengan `encoding.`

    > Ada berbagai _encoding_ yang ada yang memperlakukan string secara berbeda.
    > _encoding_ yang populer adalah _utf-8_, _ascii_, dan lain-lain.


### 6. endswith

- Definisi
> `endswith` method akan mengembalikan `True` jika sebuah string berakhiran dengan akhiran yang spesifik.
> Jika tidak, maka akan mengembalikan nilai `False`

- Syntax

    ```python
    string.endswith(suffix, start, end)
    ```

- Parameters\
    `endswith()` method mengambil tiga parameter
    * **suffix** - String atau tuple dari akhiran yang akan dicek
    * **start (Opsional)** - Posisi awal dimana akhiran akan dicek di dalam string
    * **end (Opsional)** - Posisi akhir dimana akhiran akan dicek di dalam string

- Return value\
    method ini hanya akan mengembalikkan sebuah boolean (*True* atau *False*)
    * return `True` apabila sebuah string berakhir dengan spesifik akhiran
    * return `False` apabila sebuah string tidak berakhir dengan spesifik akhiran

- Contoh:

1. Menggunakan method `endswith` tanpa `start` dan `end` parameter

    ```python
    text = "Pyhton itu sangat mudah dipelajari."

    result = text.endswith("dipelajari")
    print(result)

    result = text.endswith("dipelajari.")
    print(result)

    result = text.endswith("Python itu sangat mudah dipelajari.")
    print(result)
    ```
    ***Output:***
    ```text
    False
    True
    True
    ```

2. Menggunakan method `endswith` dengan `start` dan `end` parameter

    ```python
    text = "Python itu sangat mudah dipelajari."

    # start param: 11
    # "sangat mudah dipelajari." string yang dicari
    result = text.endswith("dipelajari.", 11)
    print(result)

    # start & end dipakai
    # start: 11 dan end: 23
    # "sangat mudah" string yang dicari
    result = text.endswith("sangat", 11, 23)
    # return False
    print(result)

    result = text.endswith("mudah", 11, 23)
    # return True
    print(result)
    ```

    ***Output:***
    ```text
    True
    False
    True
    ```

3. Menggunakan tuple untuk `endswith`

    Sangat mungkin untuk menggunakan sebuah tuple sebagai nilai *suffix* pada parameter `endswith`.\
    Jika string yang dicari berakhiran dengan nilai tuple apapun, maka `endswith` akan mengembalikan nilai `True`.
    Jika tidak, maka method ini akan mengembalikan nilai `False`.

    contoh:
    ```python
    text = "Python itu sangat mudah"

    result = text.endswith(("Python", "sangat"))
    # return False
    print(result)

    result = text.endswith(("Python", "mudah", "go"))
    # return True
    print(result)

    # dengan start dan end
    # "Python itu" string yang dicari
    result = text.endswith(("itu", "py"), 0, 10)
    # return True
    print(result)
    ```

    ***Output:***
    ```text
    False
    True
    True
    ```

### 7. expandtabs


### 8. find

- Definisi
> method `find()` akan mengembalikkan nilai index pertama dari kemunculan substring (jika ditemukan).
> Jika tidak, maka ia akan mengembalikkan nilai -1

- Syntax

    ```python
    string.find(sub, start, end)
    ```

- Parameters\
    method `find()` dapat menggunakan maksimal tiga parameter, yaitu:
    * **sub** - Substring yang akan dicari pada string
    * **start & end** - Rentang string[start:end] dimana substring dicari.

- Return value\
    Method ini akan mengembalikkan sebuah nilai ***integer***:
    * Jika substring didapati didalam string, maka method ini akan mengembalikkan nilai index dari kemunculan substring
    * Jika substring tidak didapati didalam string, maka akan mengembalikkan nilai -1

- Contoh

1. `find()` tanpa `start` dan `end` argumen

    ```python
    quote = "sudahi saja, sudahi saja, cukup sudahi saja"

    # kedapatan pertama kata `saja`
    result = quote.find("saja")
    print("Substring 'saja':", result)

    # megembalikkan nilai -1 jika substring tidak ditemukkan
    result = quote.find("semua")
    print("Substring 'semua':", result)

    # cara menggunakan find()
    if (quote.find("cukup") != -1):
        print("terdapat substring 'cukup' pada quote")
    else:
        print("tidak terdapat substring 'cukup'")
    ```

    ***Output:***
    ```text
    Substring 'saja': 7
    Substring 'semua': -1
    terdapat substring 'cukup' pada quote
    ```

2. `find()` dengan argumen `start` dan `end`

    ```python
    quote = "Lakukanlah hal-hal kecil dengan cinta yang besar"

    # substring dicari pada kalimat 'hal kecil dengan cinta yang besar'
    print(quote.find("hal-hal", 15))

    # substring dicari pada kalimat ' hal-hal kecil dengan cinta yang besar'
    print(quote.find("hal kecil", 10))

    # substring dicari pada kalimat ' hal-hal kecil '
    print(quote.find("cinta", 10, 25))

    # substring dicari pada kalimat 'hal-hal kecil dengan cinta'
    print(quote.find("hal", 11, 37))
    ```

    ***Output:***
    ```text
    -1
    15
    -1
    11
    ```
