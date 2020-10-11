# Exercism
[My exercism profile: c6p](https://exercism.io/profiles/c6p)

### acronym

=== "python"
    Convert a phrase to its acronym. - [view](https://exercism.io/tracks/python/exercises/acronym)
    ```python
    import re


    def abbreviate(words):
        """Abbreviates words

        First alphabetic character succeeding nonalphabetic characters is captured,
        then uppercased.
        """
        return re.sub(r'[^A-Za-z]*([A-Za-z])[A-Za-z\']*', r'\1', words).upper()

    ```

### all-your-base

=== "javascript"
    Convert a number, represented as a sequence of digits in one base, to any other base. - [view](https://exercism.io/tracks/javascript/exercises/all-your-base)
    ```javascript
    export function convert(arr, from, to) {
      if (!Number.isInteger(from) || from < 2)
        throw Error('Wrong input base')
      if (!Number.isInteger(to) || to < 2)
        throw Error('Wrong output base')
      else if (arr.length === 0
        || (arr[0] === 0 && arr.length !== 1)
        || arr.some(x => x < 0 || x >= from))
        throw Error('Input has wrong format')

      let base10 = arr.reduce((acc, n) => acc * from + n, 0)
      if (base10 === 0) return arr

      const exp = Math.floor(Math.log(base10) / Math.log(to))
      return [...Array(exp + 1).keys()].reduceRight(({ arr, n }, e) => {
        const pow = to ** e
        return { arr: [...arr, Math.floor(n / pow)], n: n % pow }
      }, { arr: [], n: base10 }).arr
    }
    ```

### allergies

=== "python"
    Given a person's allergy score, determine whether or not they're allergic to a given item, and their full list of allergies. - [view](https://exercism.io/tracks/python/exercises/allergies)
    ```python
    class Allergies(object):
        allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                     'tomatoes', 'chocolate', 'pollen', 'cats']

        def __init__(self, score):
            self.lst = [Allergies.allergens[i]
                        for i in range(8) if (score >> i) & 1]

        def allergic_to(self, item):
            return item in self.lst

    ```

### anagram

=== "python"
    Given a word and a list of possible anagrams, select the correct sublist. - [view](https://exercism.io/tracks/python/exercises/anagram)
    ```python
    from collections import Counter


    def find_anagrams(word, candidates):
        word = word.lower()
        counter = Counter(word)

        def is_anagram(candidate):
            candidate = candidate.lower()
            if word == candidate:
                return False
            return counter == Counter(candidate)

        return [c for c in candidates if is_anagram(c)]

    ```

=== "rust"
    An anagram is a rearrangement of letters to form a new word. - [view](https://exercism.io/tracks/rust/exercises/anagram)
    ```rust
    use std::collections::HashSet;
    extern crate itertools;
    use itertools::Itertools;

    fn chars_lowercase(word: &str) -> impl Iterator<Item = String> + Clone + '_ {
        word.chars().map(|c| c.to_lowercase().to_string())
    }

    fn anagram_for(word: &str, possible: &str) -> bool {
        let (w, p) = (chars_lowercase(word), chars_lowercase(possible));
        w.clone().ne(p.clone()) && w.sorted().eq(p.sorted())
    }

    pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
        possible_anagrams.iter().filter(|p| anagram_for(word, p)).cloned().collect()
    }

    ```

### armstrong-numbers

=== "javascript"
    An [Armstrong number](https://en.wikipedia.org/wiki/Narcissistic_number) is a number that is the sum of its own digits each raised to the power of the number of digits. - [view](https://exercism.io/tracks/javascript/exercises/armstrong-numbers)
    ```javascript
    export function validate(input) {
      return [...input.toString()]
        .reduce((sum, digit, _, arr) =>
          sum + digit ** arr.length, 0) === input
    }
    ```

=== "python"
    An [Armstrong number](https://en.wikipedia.org/wiki/Narcissistic_number) is a number that is the sum of its own digits each raised to the power of the number of digits. - [view](https://exercism.io/tracks/python/exercises/armstrong-numbers)
    ```python
    def is_armstrong(number):
        digits = str(number)
        l = len(digits)
        return number == sum((int(d)**l for d in digits))

    ```

=== "rust"
    An [Armstrong number](https://en.wikipedia.org/wiki/Narcissistic_number) is a number that is the sum of its own digits each raised to the power of the number of digits. - [view](https://exercism.io/tracks/rust/exercises/armstrong-numbers)
    ```rust
    pub fn is_armstrong_number(num: u32) -> bool {
      let digits = num.to_string();
      let exp = digits.len() as u32;
      digits
        .chars()
        .map(|x| x.to_digit(10).unwrap().pow(exp))
        .sum::<u32>() == num
    }

    ```

### atbash-cipher

=== "rust"
    Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East. - [view](https://exercism.io/tracks/rust/exercises/atbash-cipher)
    ```rust
    const A: u8 = b'a';
    const Z: u8 = b'z';
    const SEP_LEN: usize = 5;

    fn invert_and_lowercase_letters(string: &str) -> impl Iterator<Item = char> + '_ {
        string.chars().filter_map(|c| match c {
            '0'..='9' => Some(c),
            'a'..='z' => Some((Z - (c as u8) + A) as char),
            'A'..='Z' => Some((Z - (c.to_ascii_lowercase() as u8) + A) as char),
            _ => None,
        })
    }

    /// "Encipher" with the Atbash cipher.
    pub fn encode(plain: &str) -> String {
        invert_and_lowercase_letters(plain)
            .scan(0, |sep_len, c| match *sep_len {
                SEP_LEN => { *sep_len = 1;  Some(vec![' ', c]) }
                _ =>       { *sep_len += 1; Some(vec![c]) }
            })
            .flatten()
            .collect()
    }

    /// "Decipher" with the Atbash cipher.
    pub fn decode(cipher: &str) -> String {
        invert_and_lowercase_letters(cipher).collect()
    }

    ```

### bank-account

=== "python"
    Simulate a bank account supporting opening/closing, withdrawals, and deposits - [view](https://exercism.io/tracks/python/exercises/bank-account)
    ```python
    from threading import Lock


    def with_lock(func):
        LOCK = '_lock'

        def wrapped(self, *args):
            if not hasattr(self, LOCK):
                setattr(self, LOCK, Lock())
            with getattr(self, LOCK):
                return func(self, *args)
        return wrapped


    def is_open(_func=None, opened=True):
        def check_open(func):
            def wrapped(self, *args):
                if (self.balance is None) ^ (not opened):
                    raise ValueError(
                        f"Account is not {'opened' if opened else 'closed'}!")
                return func(self, *args)
            return wrapped

        if _func is None:
            return check_open
        else:
            return check_open(_func)


    class BankAccount(object):
        def __init__(self):
            self.balance = None

        @is_open
        def get_balance(self):
            return self.balance

        @is_open(opened=False)
        @with_lock
        def open(self):
            self.balance = 0

        @is_open
        @with_lock
        def deposit(self, amount):
            if amount < 0:
                raise ValueError("Cannot deposit negative!")
            self.balance += amount

        @is_open
        @with_lock
        def withdraw(self, amount):
            if amount < 0 or amount > self.balance:
                raise ValueError("Cannot withdraw negative or more than balance!")
            self.balance -= amount

        @is_open
        @with_lock
        def close(self):
            self.balance = None

    ```

### beer-song

=== "rust"
    Recite the lyrics to that beloved classic, that field-trip favorite: 99 Bottles of Beer on the Wall. - [view](https://exercism.io/tracks/rust/exercises/beer-song)
    ```rust
    pub fn verse(n: i32) -> String {
      match n {
        0 => "No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 99 bottles of beer on the wall.
    "
          .to_owned(),
        1 => "1 bottle of beer on the wall, 1 bottle of beer.
    Take it down and pass it around, no more bottles of beer on the wall.
    "
          .to_owned(),
        2 => "2 bottles of beer on the wall, 2 bottles of beer.
    Take one down and pass it around, 1 bottle of beer on the wall.
    "
          .to_owned(),
        n => format!(
          "{} bottles of beer on the wall, {} bottles of beer.
    Take one down and pass it around, {} bottles of beer on the wall.
    ",
          n,
          n,
          n - 1
        ),
      }
    }

    pub fn sing(start: i32, end: i32) -> String {
      let mut verses = String::new();
      for i in (end..=start).rev() {
        verses += &verse(i);
        if i != end {
          verses += "\n";
        }
      }
      verses
    }

    ```

### bob

=== "javascript"
    Bob is a lackadaisical teenager. In conversation, his responses are very limited. - [view](https://exercism.io/tracks/javascript/exercises/bob)
    ```javascript
    export const hey = (message) => {
      message = message.trim()
      const isQuestion = message[message.length - 1] === '?'
      const isYelling = message.match(/[A-Z]/) && message === message.toUpperCase()

      if (message === '')
        return 'Fine. Be that way!'
      else {
        if (isYelling)
          return isQuestion
            ? "Calm down, I know what I'm doing!"
            : 'Whoa, chill out!'
        else if (isQuestion)
          return 'Sure.'
      }
      return 'Whatever.'
    };

    ```

=== "python"
    Bob is a lackadaisical teenager. In conversation, his responses are very limited. - [view](https://exercism.io/tracks/python/exercises/bob)
    ```python
    def response(hey_bob):
        hey_bob = hey_bob.strip()
        if not hey_bob:
            return "Fine. Be that way!"
        is_yell = hey_bob.isupper()
        if hey_bob.endswith('?'):  # is_question
            if is_yell:
                return "Calm down, I know what I'm doing!"
            return "Sure."
        elif is_yell:
            return "Whoa, chill out!"
        return 'Whatever.'

    ```

=== "rust"
    Bob is a lackadaisical teenager. In conversation, his responses are very limited. - [view](https://exercism.io/tracks/rust/exercises/bob)
    ```rust
    extern crate regex;
    use regex::Regex;

    pub fn reply(message: &str) -> &str {
      let special_chars = Regex::new(r"[0-9%@#$(,*^! \t]*").unwrap();
      let ask_question = Regex::new(r"^.*\?\s*$").unwrap();
      let yell = Regex::new(r"^[A-Z]+\s*$").unwrap();
      let yell_question = Regex::new(r"^[A-Z]+\?\s*$").unwrap();
      let address = Regex::new(r"^\s*$").unwrap();

      if address.is_match(message) {
        "Fine. Be that way!"
      } else {
        match &special_chars.replace_all(message, "") {
          m if yell_question.is_match(m) => "Calm down, I know what I'm doing!",
          m if ask_question.is_match(m) => "Sure.",
          m if yell.is_match(m) => "Whoa, chill out!",
          _ => "Whatever.",
        }
      }
    }

    ```

### clock

=== "rust"
    Implement a clock that handles times without dates. - [view](https://exercism.io/tracks/rust/exercises/clock)
    ```rust
    use modulo::Mod;
    use std::fmt;
    use num_integer::Integer;

    const MINS_PER_HOUR: i32 = 60;
    const MINS_PER_DAY: i32 = 24 * MINS_PER_HOUR;

    #[derive(PartialEq, Debug)]
    pub struct Clock {
        hours: i32,
        minutes: i32,
    }

    impl Clock {
        pub fn new(hours: i32, minutes: i32) -> Self { Clock { hours, minutes }.add_minutes(0) }

        pub fn add_minutes(&self, minutes: i32) -> Self {
            let total_minutes = (self.hours * MINS_PER_HOUR + self.minutes + minutes).modulo(MINS_PER_DAY);
            let (hours, minutes) = total_minutes.div_rem(&MINS_PER_HOUR);
            Clock { hours, minutes }
        }
    }

    impl fmt::Display for Clock {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "{:02}:{:02}", self.hours, self.minutes)
        }
    }

    ```

### collatz-conjecture

=== "rust"
    The Collatz Conjecture or 3x+1 problem can be summarized as follows: - [view](https://exercism.io/tracks/rust/exercises/collatz-conjecture)
    ```rust
    pub fn collatz(n: u64) -> Option<u64> {
      match n {
        0 => None, // 1 is not reachable
        _ => (0..)
          .try_fold(n, |i, step| match i {
            1 => Err(step), // reached 1 at step
            _ => Ok(match i % 2 {
              0 => i / 2,
              _ => 3 * i + 1,
            }),
          })
          .err(),
      }
    }

    ```

### darts

=== "javascript"
    Write a function that returns the earned points in a single toss of a Darts game. - [view](https://exercism.io/tracks/javascript/exercises/darts)
    ```javascript
    const targets = [1,  5**2, 10**2],
          points  = [10, 5,    1]

    export function solve(x, y) {
      const r2 = x ** 2 + y ** 2
      return points[targets.findIndex(t => t >= r2)] || 0
    }
    ```

### difference-of-squares

=== "python"
    Find the difference between the square of the sum and the sum of the squares of the first N natural numbers. - [view](https://exercism.io/tracks/python/exercises/difference-of-squares)
    ```python
    def square_of_sum(number):
        return sum(range(number+1)) ** 2


    def sum_of_squares(number):
        return sum(i**2 for i in range(number+1))


    def difference_of_squares(number):
        return square_of_sum(number) - sum_of_squares(number)

    ```

=== "rust"
    Find the difference between the square of the sum and the sum of the squares of the first N natural numbers. - [view](https://exercism.io/tracks/rust/exercises/difference-of-squares)
    ```rust
    pub fn square_of_sum(n: u32) -> u32 {
      (1..=n).fold(0, |acc, x| acc + x).pow(2)
    }

    pub fn sum_of_squares(n: u32) -> u32 {
      (1..=n).fold(0, |acc, x| acc + x.pow(2))
    }

    pub fn difference(n: u32) -> u32 {
      square_of_sum(n) - sum_of_squares(n)
    }

    ```

### diffie-hellman

=== "rust"
    Diffie-Hellman key exchange. - [view](https://exercism.io/tracks/rust/exercises/diffie-hellman)
    ```rust
    extern crate num;
    extern crate rand;
    use num::bigint::BigUint;
    use num::traits::cast::ToPrimitive;
    use rand::Rng;

    pub fn private_key(p: u64) -> u64 {
      rand::thread_rng().gen_range(2, p)
    }

    pub fn public_key(p: u64, g: u64, a: u64) -> u64 {
      BigUint::from(g)
        .modpow(&BigUint::from(a), &BigUint::from(p))
        .to_u64()
        .unwrap()
    }

    pub fn secret(p: u64, b_pub: u64, a: u64) -> u64 {
      public_key(p, b_pub, a)
    }

    ```

### dnd-character

=== "python"
    For a game of [Dungeons & Dragons][DND], each player starts by generating a - [view](https://exercism.io/tracks/python/exercises/dnd-character)
    ```python
    from random import randint

    ABILITIES = ['strength', 'dexterity', 'constitution',
                 'intelligence', 'wisdom', 'charisma']


    def modifier(constitution):
        return (constitution - 10) // 2


    class Character:

        def __init__(self):
            for ability in ABILITIES:
                setattr(self, ability, self.ability())
            self.hitpoints = 10 + modifier(self.constitution)

        def ability(self):
            return sum(sorted([randint(1, 6) for _ in range(4)])[1:])

    ```

### error-handling

=== "python"
    Implement various kinds of error handling and resource management. - [view](https://exercism.io/tracks/python/exercises/error-handling)
    ```python
    def handle_error_by_throwing_exception():
        raise Exception('Error message')


    def handle_error_by_returning_none(variable):
        try:
            return int(variable)
        except ValueError:
            return None


    def handle_error_by_returning_tuple(string):
        result = handle_error_by_returning_none(string)
        return (result is not None, result)


    def filelike_objects_are_closed_on_exception(file_object):
        with file_object as f:
            f.do_something()

    ```

### gigasecond

=== "javascript"
    Given a moment, determine the moment that would be after a gigasecond - [view](https://exercism.io/tracks/javascript/exercises/gigasecond)
    ```javascript
    const GIGASECOND = 1e12

    export const gigasecond = (date) => {
      return new Date(date.getTime() + GIGASECOND)
    };

    ```

=== "python"
    Calculate the moment when someone has lived for 10^9 seconds. - [view](https://exercism.io/tracks/python/exercises/gigasecond)
    ```python
    from datetime import timedelta
    GIGASECOND = timedelta(seconds=10**9)


    def add_gigasecond(moment):
        return moment + GIGASECOND

    ```

=== "rust"
    Calculate the moment when someone has lived for 10^9 seconds. - [view](https://exercism.io/tracks/rust/exercises/gigasecond)
    ```rust
    extern crate chrono;
    use chrono::{DateTime, TimeZone, Utc};

    // Returns a Utc DateTime one billion seconds after start.
    pub fn after(start: DateTime<Utc>) -> DateTime<Utc> {
      return Utc.timestamp(start.timestamp() + 1_000_000_000, 0);
    }

    ```

### grains

=== "python"
    Calculate the number of grains of wheat on a chessboard given that the number - [view](https://exercism.io/tracks/python/exercises/grains)
    ```python
    def on_square(n):
        if n < 1 or n > 64:
            raise ValueError('Not an integer in [1-64]')
        return 2 ** (n-1)


    def total_after(n):
        if n < 1 or n > 64:
            raise ValueError('Not an integer in [1-64]')
        return 2 ** n - 1

    ```

=== "rust"
    Calculate the number of grains of wheat on a chessboard given that the number - [view](https://exercism.io/tracks/rust/exercises/grains)
    ```rust
    pub fn square(s: u32) -> u64 {
      match s {
        1...64 => 2u64.pow(s - 1),
        _ => panic!("Square must be between 1 and 64"),
      }
    }

    pub fn total() -> u64 {
      (1..=64).map(|s| square(s)).sum()
    }

    ```

### hamming

=== "python"
    Calculate the Hamming difference between two DNA strands. - [view](https://exercism.io/tracks/python/exercises/hamming)
    ```python
    def distance(strand_a, strand_b):
        if len(strand_a) != len(strand_b):
            raise ValueError('not of equal length')
        return len([1 for a, b in zip(strand_a, strand_b) if a != b])

    ```

### hello-world

=== "javascript"
    The classical introductory exercise. Just say "Hello, World!". - [view](https://exercism.io/tracks/javascript/exercises/hello-world)
    ```javascript
    export const hello = () => {
      return "Hello, World!"
    };

    ```

=== "python"
    The classical introductory exercise. Just say "Hello, World!". - [view](https://exercism.io/tracks/python/exercises/hello-world)
    ```python
    def hello():
        return 'Hello, World!'

    ```

=== "rust"
    The classical introductory exercise. Just say "Hello, World!". - [view](https://exercism.io/tracks/rust/exercises/hello-world)
    ```rust
    pub fn hello() -> &'static str {
        "Hello, World!"
    }

    ```

### high-scores

=== "python"
    Manage a game player's High Score list. - [view](https://exercism.io/tracks/python/exercises/high-scores)
    ```python
    class HighScores(object):
        def __init__(self, scores):
            self.scores = scores

        def latest(self):
            return self.scores[-1]

        def personal_best(self):
            return max(self.scores)

        def personal_top(self):
            return sorted(self.scores, reverse=True)[:3]

        def report(self):
            latest, best = self.latest(), self.personal_best()
            short_of = f" {best - latest} short of " if best > latest else " "
            return f"Your latest score was {latest}. That's{short_of}your personal best!"

    ```

### isbn-verifier

=== "python"
    The [ISBN-10 verification process](https://en.wikipedia.org/wiki/International_Standard_Book_Number) is used to validate book identification - [view](https://exercism.io/tracks/python/exercises/isbn-verifier)
    ```python
    import re
    from operator import mul


    isbn_pattern = re.compile(
        r'^(\d)-?(\d)(\d)(\d)-?(\d)(\d)(\d)(\d)(\d)-?([\dX])$')


    def is_valid(isbn):
        return sum(map(mul, (int(i) for i in isbn), range(10, 0, -1))) % 11 == 0


    def verify(isbn):
        m = isbn_pattern.match(isbn)
        if m:
            x = [i for i in m.group(*range(1, 11))]
            if x[-1] == 'X':
                x[-1] = 10
            return is_valid(x)
        return False

    ```

### isogram

=== "python"
    Determine if a word or phrase is an isogram. - [view](https://exercism.io/tracks/python/exercises/isogram)
    ```python
    def is_isogram(string):
        letters = set()
        is_alpha = str.isalpha
        add = letters.add
        for c in string.lower():
            if not is_alpha(c): continue
            if c in letters: return False
            add(c)
        return True

    ```

=== "rust"
    Determine if a word or phrase is an isogram. - [view](https://exercism.io/tracks/rust/exercises/isogram)
    ```rust
    use itertools::sorted;

    pub fn check(candidate: &str) -> bool {
      sorted(candidate.to_ascii_lowercase().as_bytes())
        .filter(|x| match **x as char {
          ' ' | '-' => false,
          _ => true,
        })
        .try_fold(
          0 as u8,
          |prev, &curr| {
            if prev == curr {
              Err(curr)
            } else {
              Ok(curr)
            }
          },
        )
        .is_ok()
    }

    ```

### kindergarten-garden

=== "python"
    Given a diagram, determine which plants each child in the kindergarten class is - [view](https://exercism.io/tracks/python/exercises/kindergarten-garden)
    ```python
    from numpy import array

    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


    class Garden:
        def __init__(self, diagram, students=STUDENTS):
            self.students = sorted(students)
            self.diagram = array([list(row) for row in diagram.split('\n')])

        def plants(self, student):
            i = self.students.index(student) * 2
            return [PLANTS[p] for p in self.diagram[:, i:i + 2].flatten()]

    ```

### largest-series-product

=== "python"
    Given a string of digits, calculate the largest product for a contiguous - [view](https://exercism.io/tracks/python/exercises/largest-series-product)
    ```python
    from functools import reduce
    from operator import mul


    def product(series):
        return reduce(lambda acc, i: acc*int(i), series, 1)


    def largest_product(series, size):
        if size < 0:
            raise ValueError("Span should be positive!")
        length = len(series)
        return max(product(series[i:i+size]) for i in range(length-size+1))

    ```

### leap

=== "javascript"
    Given a year, report if it is a leap year. - [view](https://exercism.io/tracks/javascript/exercises/leap)
    ```javascript
    export function isLeap(year) {
      return year % 4 === 0
        && (year % 100 !== 0 || year % 400 === 0)
    }
    ```

=== "python"
    Given a year, report if it is a leap year. - [view](https://exercism.io/tracks/python/exercises/leap)
    ```python
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    ```

=== "rust"
    Given a year, report if it is a leap year. - [view](https://exercism.io/tracks/rust/exercises/leap)
    ```rust
    pub fn is_leap_year(year: i32) -> bool {
      return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }

    ```

### linked-list

=== "javascript"
    Implement a doubly linked list. - [view](https://exercism.io/tracks/javascript/exercises/linked-list)
    ```javascript
    class Node {
      constructor({ val = null, prev = null, next = null }) {
        Object.assign(this, { val, prev, next })
      }
    }

    export class LinkedList {
      constructor() {
        this.first = null
        this.last = this.first
      }

      push(val, last = 'last', prev = 'prev', next = 'next') {
        if (this[last] === null)
          this.first = this.last = new Node({ val })
        else {
          let node = { val, [prev]: this[last] }
          this[last] = new Node(node)
          node[prev][next] = this[last]
        }
      }
      unshift(val) { this.push(val, 'first', 'next', 'prev') }

      pop(first = 'first', last = 'last', prev = 'prev', next = 'next') {
        const val = this[last].val
        this[last] = this[last][prev]
        if (this[last] === null)
          this[first] = this[last]
        else
          this[last][next] = null
        return val
      }
      shift() { return this.pop('last', 'first', 'next', 'prev') }

      delete(val) {
        let item = this.first
        while (item) {
          if (item.val === val) {
            if (item.next) item.next.prev = item.prev
            else this.last = item.prev
            if (item.prev) item.prev.next = item.next
            else this.first = item.next
            return
          }
          item = item.next
        }
      }

      count() {
        let [c, item] = [0, this.first]
        while (item) {
          c++
          item = item.next
        }
        return c
      }
    }

    ```

### matching-brackets

=== "rust"
    Given a string containing brackets `[]`, braces `{}`, parentheses `()`, - [view](https://exercism.io/tracks/rust/exercises/matching-brackets)
    ```rust
    fn close_bracket(c: char) -> char {
        match c {
            '{' => '}',
            '[' => ']',
            '(' => ')',
            _ => panic!("No matching close bracket!"),
        }
    }

    pub fn brackets_are_balanced(string: &str) -> bool {
        let mut unbalanced = Vec::<char>::new();
        for c in string.chars() {
            match c {
                '{' | '[' | '(' => unbalanced.push(close_bracket(c)),
                '}' | ']' | ')' => {
                    if unbalanced.pop() != Some(c) {
                        return false;
                    }
                }
                _ => (),
            }
        }
        unbalanced.is_empty()
    }

    ```

### matrix

=== "javascript"
    Given a string representing a matrix of numbers, return the rows and columns of - [view](https://exercism.io/tracks/javascript/exercises/matrix)
    ```javascript
    export class Matrix {
      constructor(matrix) {
        this.m = matrix.split('\n').map(row => row.split(' ').map(col => Number(col)))
      }

      get rows() { return this.m }

      get columns() {
        return this.t = this.t || this.m[0].map((_, i) => this.m.map(row => row[i]))
      }
    }

    ```

=== "python"
    Given a string representing a matrix of numbers, return the rows and columns of - [view](https://exercism.io/tracks/python/exercises/matrix)
    ```python
    class Matrix():
        def __init__(self, matrix_string):
            self.rows = [[int(num) for num in line.split(' ')]
                         for line in matrix_string.split('\n')]

        def row(self, index):
            return self.rows[index-1]

        def column(self, index):
            return [row[index-1] for row in self.rows]

    ```

### meetup

=== "python"
    Calculate the date of meetups. - [view](https://exercism.io/tracks/python/exercises/meetup)
    ```python
    from calendar import monthrange, day_name
    from datetime import date


    class MeetupDayException(Exception):
        pass


    def meetup(year, month, week, day_of_week):
        weekday = dict(zip(day_name, range(7)))[day_of_week]
        firstday, max_days = monthrange(year, month)
        days = range((weekday - firstday) % 7 + 1, max_days + 1, 7)

        if week == "teenth":
            day = next(i for i in days if i >= 13 and i <= 19)
        elif week == 'last':
            day = days[-1]
        else:   # week in ["1st", "2nd", "3rd", "4th", "5th"]:
            try:
                day = days[int(week[0]) - 1]
            except:
                raise MeetupDayException("No {0} {1}!".format(week, day_of_week))

        return date(year, month, day)

    ```

### nth-prime

=== "rust"
    Given a number n, determine what the nth prime is. - [view](https://exercism.io/tracks/rust/exercises/nth-prime)
    ```rust
    pub fn nth(n: usize) -> u32 {
      fn is_prime(x: u32, factors: &Vec<u32>) -> bool {
        return !factors.iter().any(|&i| x % i == 0);
      }
      const FIRST_PRIME: u32 = 2;
      let mut primes = vec![FIRST_PRIME];
      let mut num = FIRST_PRIME;
      while primes.len() <= n {
        num += 1;
        if is_prime(num, &primes) {
          primes.push(num);
        }
      }
      primes[n]
    }

    ```

### pangram

=== "javascript"
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, - [view](https://exercism.io/tracks/javascript/exercises/pangram)
    ```javascript
    const ALPHABET = 'abcdefghijklmnopqrstuvwxyz'.split('')

    export const isPangram = (sentence) => {
      let s = sentence.toLowerCase()
      return ALPHABET.every(c => s.includes(c))
    }

    ```

=== "python"
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, - [view](https://exercism.io/tracks/python/exercises/pangram)
    ```python
    def is_pangram(sentence):
        diff = ord('z') - ord('a')
        try:
            pangram = sorted(set(sentence.lower()))
            return diff == pangram.index('z') - pangram.index('a')
        except:
            return False

    ```

### pascals-triangle

=== "javascript"
    Compute Pascal's triangle up to a given number of rows. - [view](https://exercism.io/tracks/javascript/exercises/pascals-triangle)
    ```javascript
    export class Triangle {
      constructor(n) {
        if (n < 1) throw new Error("Minimum rows for Pascals Triangle is 1")

        this.tri = [...Array(n)].map(_ => [1])  // init n rows

        for (let i = 1; i < this.tri.length; i++) {
          this.tri[i] = [...Array(i + 1)].map((_, j) =>
            j === 0 || j === i
              ? 1 // first and last columns are 1
              : this.tri[i - 1][j - 1] + this.tri[i - 1][j])
        }
      }

      get lastRow() { return this.tri[this.tri.length - 1] }

      get rows() { return this.tri }
    }

    ```

### perfect-numbers

=== "python"
    Determine if a number is perfect, abundant, or deficient based on - [view](https://exercism.io/tracks/python/exercises/perfect-numbers)
    ```python
    def factors(number):
        if number == 1:
            return
        elif number < 1:
            raise ValueError("Not a positive integer!")

        yield 1
        for div in range(2, 1+int(number**0.5)):
            quo, rem = divmod(number, div)
            if not rem:
                yield div
                if quo is not div:
                    yield quo


    def classify(number):
        diff = sum(factors(number)) - number
        return "perfect" if diff == 0 else "abundant" if diff > 0 else "deficient"

    ```

### phone-number

=== "python"
    Clean up user-entered phone numbers so that they can be sent SMS messages. - [view](https://exercism.io/tracks/python/exercises/phone-number)
    ```python
    import re


    class Phone(object):
        _pattern = re.compile(r'''
            \+?1?               # country code
            \s*?                # optional spaces
            \(?([2-9]\d{2})\)?  # area code \1
            [ .-]*?             # optional seperators
            ([2-9]\d{2})        # subscriber code \2
            [ .-]*?             # optional seperators
            (\d+).*             # subscriber number \3
        ''', re.VERBOSE)

        def __init__(self, phone_number):
            self.number = self._pattern.sub(r'\1\2\3', phone_number)
            if len(self.number) == 10:
                self.area_code = self.number[:3]
            else:
                raise ValueError("Invalid Phone Number!")

        def pretty(self):
            return f'({self.area_code}) {self.number[3:6]}-{self.number[6:]}'

    ```

### prime-factors

=== "python"
    Compute the prime factors of a given natural number. - [view](https://exercism.io/tracks/python/exercises/prime-factors)
    ```python
    def prime_factors(number):
        factors, d = [], 2
        while number > 1:
            while True:
                q, r = divmod(number, d)
                if r:
                    d += 1 if d == 2 else 2  # skip evens
                else:
                    factors.append(d)
                    number = q
                    break
        return factors

    ```

=== "rust"
    Compute the prime factors of a given natural number. - [view](https://exercism.io/tracks/rust/exercises/prime-factors)
    ```rust
    pub fn factors(mut n: u64) -> Vec<u64> {
      let mut factors = Vec::new();
      while n > 1 {
        let factor = (2..=n).find(|x| n % x == 0).unwrap();
        factors.push(factor);
        n /= factor
      }
      factors
    }

    ```

### protein-translation

=== "javascript"
    Translate RNA sequences into proteins. - [view](https://exercism.io/tracks/javascript/exercises/protein-translation)
    ```javascript
    const codons = (() => {
      let AUG, UUU, UUC, UUA, UUG, UCU, UCC, UCA, UCG, UAU, UAC, UGU, UGC, UGG, UAA, UAG, UGA
      AUG = 'Methionine'
      UUU = UUC = 'Phenylalanine'
      UUA = UUG = 'Leucine'
      UCU = UCC = UCA = UCG = 'Serine'
      UAU = UAC = 'Tyrosine'
      UGU = UGC = 'Cysteine'
      UGG = 'Tryptophan'
      UAA = UAG = UGA = 'STOP'
      return Object.freeze({ AUG, UUU, UUC, UUA, UUG, UCU, UCC, UCA, UCG, UAU, UAC, UGU, UGC, UGG, UAA, UAG, UGA })
    })()

    export function translate(rna = '') {
      let proteins = []
      for (let i = 0; i < rna.length; i += 3) {
        const protein = codons[rna.slice(i, i + 3)]
        if (protein === undefined) throw new Error('Invalid codon')
        if (protein === 'STOP') break
        proteins.push(protein)
      }
      return proteins
    }
    ```

=== "python"
    Translate RNA sequences into proteins. - [view](https://exercism.io/tracks/python/exercises/protein-translation)
    ```python
    from itertools import takewhile

    codons = {
        'AUG': "Methionine",
        'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine',
        'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }


    def proteins(strand):
        codon_gen = (strand[i:i+3] for i in range(0, len(strand), 3))
        protein_gen = (codons[codon] for codon in codon_gen)
        return list(takewhile(lambda p: p != 'STOP', protein_gen))

    ```

### proverb

=== "rust"
    For want of a horseshoe nail, a kingdom was lost, or so the saying goes. - [view](https://exercism.io/tracks/rust/exercises/proverb)
    ```rust
    pub fn build_proverb(list: Vec<&str>) -> String {
      match list.as_slice() {
        [] => "".to_owned(),
        _ => list
          .iter()
          .zip(list.iter().skip(1))
          .map(|(a, b)| format!("For want of a {} the {} was lost.", a, b))
          .chain(std::iter::once(format!(
            "And all for the want of a {}.",
            list[0]
          )))
          .collect::<Vec<String>>()
          .join("\n"),
      }
    }

    ```

### pythagorean-triplet

=== "python"
    A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for - [view](https://exercism.io/tracks/python/exercises/pythagorean-triplet)
    ```python
    from math import sqrt


    def triplets_with_sum(number):
        return set(gen_triplets(number))


    def gen_triplets(number):
        # limit at a==b
        for a in range(1, 1 + int(number / (2 + sqrt(2)))):
            b_plus_c = number - a
            n = b_plus_c**2 - a**2
            d = b_plus_c * 2
            if n % d == 0:
                b = n // d
                c = b_plus_c - b
                yield (a, b, c) if a < b else (b, a, c)

    ```

=== "rust"
    A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for - [view](https://exercism.io/tracks/rust/exercises/pythagorean-triplet)
    ```rust
    use rayon::prelude::*;
    use std::collections::HashSet;

    pub fn find(sum: u32) -> HashSet<[u32; 3]> {
      (1_u32..(sum / 3_u32))
        .into_par_iter()
        .map(|a| {
          let b_plus_c = sum - a;
          (a, b_plus_c, b_plus_c.pow(2) - a.pow(2), b_plus_c * 2)
        })
        .filter(|(_a, _b_plus_c, n, d)| n % d == 0)
        .map(|(a, b_plus_c, n, d)| {
          let b = n / d;
          let c = b_plus_c - b;
          match a < b {
            true => [a, b, c],
            false => [b, a, c],
          }
        })
        .collect::<HashSet<[u32; 3]>>()
    }

    ```

### raindrops

=== "python"
    Convert a number to a string, the contents of which depend on the number's factors. - [view](https://exercism.io/tracks/python/exercises/raindrops)
    ```python
    PL_NG = {3: 'Pling', 5: 'Plang', 7: 'Plong'}


    def raindrops(number):
        return ''.join([speak for factor, speak in PL_NG.items()
                        if number % factor == 0]) or str(number)

    ```

=== "rust"
    Convert a number to a string, the contents of which depend on the number's factors. - [view](https://exercism.io/tracks/rust/exercises/raindrops)
    ```rust
    const PLING: &str = "Pling";
    const PLANG: &str = "Plang";
    const PLONG: &str = "Plong";

    fn factor(x: u32, n: u32) -> bool {
      n % x == 0
    }

    pub fn raindrops(n: u32) -> String {
      let mut s = String::new();
      if factor(3, n) {
        s += PLING;
      }
      if factor(5, n) {
        s += PLANG;
      }
      if factor(7, n) {
        s += PLONG;
      }
      if s.is_empty() {
        return n.to_string();
      }
      s
    }

    ```

### rational-numbers

=== "python"
    A rational number is defined as the quotient of two integers `a` and `b`, called the numerator and denominator, respectively, where `b != 0`. - [view](https://exercism.io/tracks/python/exercises/rational-numbers)
    ```python
    from __future__ import division


    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)


    class Rational(object):
        def __init__(self, numer, denom):
            d = gcd(numer, denom)
            self.numer = numer / d
            self.denom = denom / d

        def __eq__(self, other):
            return self.numer == other.numer and self.denom == other.denom

        def __repr__(self):
            return '{}/{}'.format(self.numer, self.denom)

        def __add__(self, other):
            return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

        def __sub__(self, other):
            return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

        def __mul__(self, other):
            return Rational(self.numer * other.numer, self.denom * other.denom)

        def __truediv__(self, other):
            return Rational(self.numer * other.denom, self.denom * other.numer)

        def __abs__(self):
            return Rational(abs(self.numer), abs(self.denom))

        def __pow__(self, power):
            numer, denom = (self.denom, self.numer) if power < 0 else (
                self.numer, self.denom)
            power = abs(power)
            return Rational(numer**power, denom**power)

        def __rpow__(self, base):
            return base ** (self.numer / self.denom)

    ```

### resistor-color

=== "javascript"
    Resistors have color coded bands, where each color maps to a number. The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number. - [view](https://exercism.io/tracks/javascript/exercises/resistor-color)
    ```javascript
    export const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    export function colorCode(color) {
      return COLORS.indexOf(color)
    }
    ```

### resistor-color-duo

=== "javascript"
    If you want to build something using a Raspberry Pi, you'll probably use _resistors_. For this exercise, you need to know two things about them: - [view](https://exercism.io/tracks/javascript/exercises/resistor-color-duo)
    ```javascript
    const COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    export function value(bands) {
      return Number(bands.reduce((val, band) => val + COLORS.indexOf(band), ''))
    }
    ```

### reverse-string

=== "python"
    Reverse a string - [view](https://exercism.io/tracks/python/exercises/reverse-string)
    ```python
    def reverse(text):
        return text[::-1]

    ```

=== "rust"
    Reverse a string - [view](https://exercism.io/tracks/rust/exercises/reverse-string)
    ```rust
    extern crate unicode_segmentation;
    use unicode_segmentation::UnicodeSegmentation;

    pub fn reverse(input: &str) -> String {
      input.graphemes(true).rev().collect()
    }

    ```

### rna-transcription

=== "javascript"
    Given a DNA strand, return its RNA complement (per RNA transcription). - [view](https://exercism.io/tracks/javascript/exercises/rna-transcription)
    ```javascript
    const COMPLEMENT = { G: 'C', C: 'G', T: 'A', A: 'U' }

    export const toRna = (dna) =>
      dna.split('').reduce((rna, c) => rna + (COMPLEMENT[c] || ''), '')

    ```

=== "python"
    Given a DNA strand, return its RNA complement (per RNA transcription). - [view](https://exercism.io/tracks/python/exercises/rna-transcription)
    ```python
    rna = str.maketrans("GCTA", "CGAU")


    def to_rna(dna_strand):
        return dna_strand.translate(rna)

    ```

### robot-name

=== "python"
    Manage robot factory settings. - [view](https://exercism.io/tracks/python/exercises/robot-name)
    ```python
    import random

    MOD = (26*10**3, 10**3, 10**2, 10, 1)
    MAX = 26**2 * 10**3
    A = ord('A')


    def name_generator():
        global A, MOD, MAX
        num = random.randint(0, MAX)
        # in AA111 format
        for i in range(5):
            d, num = divmod(num, MOD[i])
            yield chr(A+d) if i < 2 else str(d)
        return


    class Robot(object):
        names = set()

        def __init__(self):
            self.reset()

        def reset(self):
            while True:
                name = self.gen_name()
                if name not in self.names:
                    self.names.add(name)
                    break
            self.name = name

        def gen_name(self):
            return ''.join(name_generator())

    ```

### roman-numerals

=== "javascript"
    Write a function to convert from normal numbers to Roman Numerals. - [view](https://exercism.io/tracks/javascript/exercises/roman-numerals)
    ```javascript
    const NUMERALS = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }

    function roman5(n, unit, left, right) {
      return n == 4
        ? `${unit}${right}`
        : `${left}${unit.repeat(n)}`
    }
    function roman10(n, one, five, ten) {
      const [ONE, FIVE, TEN] = [one, five, ten].map(x => NUMERALS[x])
      return n >= 5
        ? roman5(n % 5, ONE, FIVE, TEN)
        : roman5(n, ONE, '', FIVE)
    }

    export function toRoman(n) {
      return [1000, 100, 10, 1].reduce((acc, I) => {
        const MAX = 10 * n,
              num = Math.floor(n % (10*I) / I)
        return I <= MAX
          ? acc + roman10(num, I, 5*I, 10*I)
          : acc
      }, '')
    }
    ```

### run-length-encoding

=== "javascript"
    Implement run-length encoding and decoding. - [view](https://exercism.io/tracks/javascript/exercises/run-length-encoding)
    ```javascript
    export function encode(txt) {
      return txt.replace(/(.)\1+/g,
        (run) => run.length + run[0])
    }

    export function decode(txt) {
      return txt.replace(/(\d+)(.)/g,
        (_, run, char) => char.repeat(run))
    }
    ```

### saddle-points

=== "python"
    Detect saddle points in a matrix. - [view](https://exercism.io/tracks/python/exercises/saddle-points)
    ```python
    def saddle_points(matrix):
        if not matrix:
            return [{}]
        row_length = len(matrix[0])
        if [1 for row in matrix if row_length != len(row)]:
            raise ValueError("Irregular Matrix!")

        col_mins = [min(col) for col in zip(*matrix)]
        return [{"row": r, "column": c}
                for r, row_max in enumerate(map(max, matrix), 1)
                for c, col_min in enumerate(col_mins, 1)
                if row_max == col_min] or [{}]

    ```

=== "rust"
    Detect saddle points in a matrix. - [view](https://exercism.io/tracks/rust/exercises/saddle-points)
    ```rust
    pub fn find_saddle_points(input: &[Vec<u64>]) -> Vec<(usize, usize)> {
      let len: usize = if input.len() > 0 { input[0].len() } else { 0 };
      let row_max: Vec<_> = input.iter().filter_map(|v| v.iter().max()).collect();
      let col_min: Vec<_> = (0..len)
        .filter_map(|i| input.iter().flatten().skip(i).step_by(len).min())
        .collect();

      input
        .iter()
        .enumerate()
        .flat_map(|(i, v)| v.iter().enumerate().map(move |(j, v)| (i.to_owned(), j, v)))
        .filter_map(|(i, j, v)| {
          if v >= row_max[i] && v <= col_min[j] {
            Some((i, j))
          } else {
            None
          }
        })
        .collect()
    }

    ```

### say

=== "python"
    Given a number from 0 to 999,999,999,999, spell out that number in English. - [view](https://exercism.io/tracks/python/exercises/say)
    ```python
    SAY = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
     }


    def _say_postfix(number, divisor, postfix):
        quo, rem = divmod(number, divisor)
        return f"{_say(quo)} {postfix}" + (f" {_say(rem)}" if rem else '')


    def _say(number):
        if number < 20:
            return SAY[number]
        elif number < 100:
            ten, rem = divmod(number, 10)
            return SAY[ten * 10] + (f"-{SAY[rem]}" if rem else '')
        elif number < 1e3:
            return _say_postfix(number, 100, "hundred")

        for divisor, postfix in [(1e3, "thousand"), (1e6, "million"), (1e9, "billion")]:
            if number < 1e3 * divisor:
                return _say_postfix(number, divisor, postfix)


    def say(number):
        if number < 0 or number >= 1e12:
            raise ValueError("Out of range")
        else:
            return _say(number)

    ```

### scrabble-score

=== "python"
    Given a word, compute the scrabble score for that word. - [view](https://exercism.io/tracks/python/exercises/scrabble-score)
    ```python
    from enum import IntEnum


    class Score(IntEnum):
        A = E = I = O = U = L = N = R = S = T = 1
        D = G = 2
        B = C = M = P = 3
        F = H = V = W = Y = 4
        K = 5
        J = X = 8
        Q = Z = 10


    def score(word):
        return sum(Score[c] for c in word.upper())

    ```

### series

=== "python"
    Given a string of digits, output all the contiguous substrings of length `n` in - [view](https://exercism.io/tracks/python/exercises/series)
    ```python
    def slices(series, length):
        if length <= 0 or len(series) < length:
            raise ValueError("Invalid length")
        return [series[i:i+length] for i in range(len(series)+1-length)]

    ```

=== "rust"
    Given a string of digits, output all the contiguous substrings of length `n` in - [view](https://exercism.io/tracks/rust/exercises/series)
    ```rust
    pub fn series(digits: &str, len: usize) -> Vec<String> {
      (0..digits.len().checked_sub(len - 1).unwrap_or(0))
        .map(|i| digits[i..i + len].to_owned())
        .collect()
    }

    ```

### sgf-parsing

=== "python"
    Parsing a Smart Game Format string. - [view](https://exercism.io/tracks/python/exercises/sgf-parsing)
    ```python
    import re


    class SgfTree(object):
        def __init__(self, properties=None, children=None):
            self.properties = properties or {}
            self.children = children or []

        def __eq__(self, other):
            if not isinstance(other, SgfTree):
                return False
            for k, v in self.properties.items():
                if k not in other.properties:
                    return False
                if other.properties[k] != v:
                    return False
            for k in other.properties.keys():
                if k not in self.properties:
                    return False
            if len(self.children) != len(other.children):
                return False
            for a, b in zip(self.children, other.children):
                if a != b:
                    return False
            return True

        def __ne__(self, other):
            return not self == other


    # TOKENs
    VAR_BEGIN, VAR_END, NEXT_LVL, KEY, VALUE, ELSE = (re.compile(s) for s in [
        r'\(',                  # VAR_BEGIN
        r'\)',                  # VAR_END
        r';',                   # NEXT_LVL
        r'(?<=[];])[A-Z]+',     # KEY
        r'\[(.+?)(?<!\\)\]',    # VALUE \1
        r'[^);]'                # ELSE
    ])


    def escape(s): return s.replace('\n', '\\n')


    def unescape(s):
        return s.replace(r'\n', '\n').replace('\t', ' ').replace('\\', '')


    def match(pattern, s, pos, action=None):
        m_peek = pattern.match(s, pos)
        if m_peek:
            if action:
                action(m_peek)
            return m_peek.end(), True
        return pos, False


    def add_node(parent):
        node = SgfTree()
        if parent:
            parent.children.append(node)
        else:
            parent = node


    def parse_key_value(s, parent, pos):
        m = KEY.match(s, pos)
        if not m:
            return pos, False
        pos, key, values = m.end(), m.group(0), []
        while True:
            pos, matched = match(VALUE, s, pos,
                                 lambda m: values.append(unescape(m.group(1))))
            if not matched:
                break
        if values:
            parent.properties[key] = values
        else:
            raise ValueError("Error: No delimiter!")
        return pos, True


    def parse_variation(s, parent=None, pos=0):
        m = VAR_BEGIN.match(s, pos)
        if not m:
            return m.end(), False, parent
        pos, node = m.end(), parent
        while True:
            pos, matched = match(VAR_END, s, pos)
            if not matched:
                break
            pos, matched = match(NEXT_LVL, s, pos)
            pos, matched = parse_key_value(s, node, pos)
            if matched:
                node = SgfTree()
                if parent:
                    parent.children.append(node)
                else:
                    parent = node
                continue
            pos, matched, _ = parse_variation(s, node, pos)
            if matched:
                continue
            _, matched = match(ELSE, s, pos)
            if matched:
                raise ValueError("Error!")
        return pos, True, parent


    def parse(input_string):
        _, _, root = parse_variation(escape(input_string))
        if not root:
            raise ValueError("No nodes!")
        return root


    parse('(;A[\\]b\nc\nd\t\te \n\\]])')

    ```

### sieve

=== "python"
    Use the Sieve of Eratosthenes to find all the primes from 2 up to a given - [view](https://exercism.io/tracks/python/exercises/sieve)
    ```python
    def primes(limit):
        numbers = list(range(2, limit + 1))
        prime_gen = (n for n in numbers if n)

        while True:
            prime = next(prime_gen, None)
            if not prime:
                break
            for i in range(prime * 2, len(numbers) + 2, prime):
                numbers[i - 2] = 0    # mark multiples of prime

        return [n for n in numbers if n]    # primes

    ```

### simple-cipher

=== "python"
    Implement a simple shift cipher like Caesar and a more secure substitution cipher. - [view](https://exercism.io/tracks/python/exercises/simple-cipher)
    ```python
    from itertools import cycle
    from string import ascii_lowercase
    from random import choice

    A, Z = ord('a'), ord('z')


    def wrap_chr(val):
        return chr((val - A) % (Z - A + 1) + A)


    class Cipher(object):
        def __init__(self, key=None):
            self.key = key or ''.join(choice(ascii_lowercase) for _ in range(100))

        def encode(self, text, reverse=False):
            return ''.join(wrap_chr(A - ord(k) + ord(c) if reverse else
                                    ord(k) - A + ord(c))
                           for c, k in zip(text, cycle(self.key)))

        def decode(self, text):
            return self.encode(text, reverse=True)


    class Caesar(Cipher):
        def __init__(self):
            super().__init__('d')

    ```

### space-age

=== "javascript"
    Given an age in seconds, calculate how old someone would be on: - [view](https://exercism.io/tracks/javascript/exercises/space-age)
    ```javascript
    const EARTH_YEAR_IN_SECONDS = 31557600
    const YEAR_IN_EARTH_YEARS = {
      mercury: 0.2408467,
      venus: 0.61519726,
      earth: 1.0,
      mars: 1.8808158,
      jupiter: 11.862615,
      saturn: 29.447498,
      uranus: 84.016846,
      neptune: 164.79132,
    }


    export const age = (planet, age_in_seconds) => {
      const year_in_seconds = YEAR_IN_EARTH_YEARS[planet] * EARTH_YEAR_IN_SECONDS
      return Number((age_in_seconds / year_in_seconds).toFixed(2))
    }

    ```

=== "python"
    Given an age in seconds, calculate how old someone would be on: - [view](https://exercism.io/tracks/python/exercises/space-age)
    ```python
    class SpaceAge(object):
        PLANET_ORBITS = [(p, o * 31557600) for p, o in (
            ('earth', 1.0),
            ('mercury', 0.2408467),
            ('venus', 0.61519726),
            ('mars', 1.8808158),
            ('jupiter', 11.862615),
            ('saturn', 29.447498),
            ('uranus', 84.016846),
            ('neptune', 164.79132)
        )]

        def __init__(self, seconds):
            self.seconds = seconds
            for planet, orbit in self.PLANET_ORBITS:
                setattr(self, 'on_' + planet,
                        lambda orbit=orbit: round(self.seconds / orbit, 2))

    ```

### sum-of-multiples

=== "python"
    Given a number, find the sum of all the unique multiples of particular numbers up to - [view](https://exercism.io/tracks/python/exercises/sum-of-multiples)
    ```python
    def sum_of_multiples(limit, multiples):
        return sum({i for m in multiples if m > 0
                    for i in range(m, limit, m)})

    ```

=== "rust"
    Given a number, find the sum of all the unique multiples of particular numbers up to - [view](https://exercism.io/tracks/rust/exercises/sum-of-multiples)
    ```rust
    pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
      (1..limit)
        .filter(|num| factors.iter().any(|factor| num % factor == 0))
        .fold(0, |sum, multiple| sum + multiple)
    }

    ```

### twelve-days

=== "python"
    Output the lyrics to 'The Twelve Days of Christmas'. - [view](https://exercism.io/tracks/python/exercises/twelve-days)
    ```python
    thing = ["a Partridge", "two Turtle Doves", "three French Hens", "four Calling Birds",
             "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking",
             "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]
    ordinal = ["first", "second", "third", "fourth", "fifth", "sixth",
               "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]


    def things(n):
        if n == 0:
            return thing[n]
        return ", ".join(thing[i] for i in range(n, 0, -1)) + ", and " + thing[0]


    def recite(start_verse, end_verse):
        return [f"On the {ordinal[i]} day of Christmas my true love gave to me: {things(i)} in a Pear Tree."
                for i in range(start_verse-1, end_verse)]

    ```

### two-fer

=== "javascript"
    `Two-fer` or `2-fer` is short for two for one. One for you and one for me. - [view](https://exercism.io/tracks/javascript/exercises/two-fer)
    ```javascript
    export function twoFer(name = 'you') {
      return `One for ${name}, one for me.`
    }
    ```

=== "python"
    `Two-fer` or `2-fer` is short for two for one. One for you and one for me. - [view](https://exercism.io/tracks/python/exercises/two-fer)
    ```python
    def two_fer(name="you"):
        return f"One for {name}, one for me."

    ```

### word-count

=== "python"
    Given a phrase, count the occurrences of each _word_ in that phrase. - [view](https://exercism.io/tracks/python/exercises/word-count)
    ```python
    from collections import Counter
    from re import sub


    def count_words(sentence):
        words = sub(r"[^'0-9A-Za-z]|(?<!\w)'|'(?!\w)",
                    ' ', sentence).lower().split()
        return Counter(words)

    ```

### yacht

=== "python"
    Score a single throw of dice in *Yacht* - [view](https://exercism.io/tracks/python/exercises/yacht)
    ```python
    # Score categories
    # Change the values as you see fit
    YACHT = 0
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    LITTLE_STRAIGHT = 9
    BIG_STRAIGHT = 10
    CHOICE = 11


    def score(dice, category):
        def count_all():
            count = [0]*6
            for d in dice:
                count[d-1] += 1
            return count

        if category is YACHT:
            return 50 if count_all().count(0) == 5 else 0   # there is not any of other five
        elif category is LITTLE_STRAIGHT:
            return 30 if all(count_all()[:5]) else 0
        elif category == BIG_STRAIGHT:
            return 30 if all(count_all()[1:]) else 0
        elif category is FULL_HOUSE:
            counts = count_all()
            return sum(dice) if all(count in counts for count in [2, 3]) else 0
        elif category is FOUR_OF_A_KIND:
            try:
                # there is more than 4 of any
                return 4 * next(i+1 for i, c in enumerate(count_all()) if c >= 4)
            except StopIteration:
                return 0
        elif category is CHOICE:
            return sum(dice)
        else:   # ONES, TWOS, THREES, FOURS, FIVES, SIXES
            return category * dice.count(category)

    ```


