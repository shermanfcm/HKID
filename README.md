# Hong Kong Identity Card Number Algorithm
## HKID Number Format
```
N999999(A)
```
where
- `N` is 1 or 2 capital letter between `A` and `Z`
- `9` is 1 numerical digit between `0` and `9`
- `A` is 1 check digit, a number between `0` and `9` or the capital letter `A`

## Regular Expression
```
^[A-Z]{1,2}[0-9]{6}\([0-9A]\)$
```
Omitting parentheses:
```
^[A-Z]{1,2}[0-9]{6}[0-9A]$
```

## HKID Number Validation
1. Convert the letters to a number representing their relative positions in the alphabet, starting from `10`. (i.e. A=10, B=11, ..., Z=35)
2. If only 1 leading letter exists, the first empty character is converted to `36`.
2. Multiply each number with their position counting from the right, starting from `1`.
3. Sum the products.
4. Calculate the remainder of dividing the sum by 11.
5. HKID number is valid if and only if the remainder of the division is `0`.

## Character Conversion Table
|Character|Value|Character|Value|Character|Value|
|--|--|--|--|--|--|
|0|0|D|13|Q|26|
|1|1|E|14|R|27|
|2|2|F|15|S|28|
|3|3|G|16|T|29|
|4|4|H|17|U|30|
|5|5|I|18|V|31|
|6|6|J|19|W|32|
|7|7|K|20|X|33|
|8|8|L|21|Y|34|
|9|9|M|22|Z|35|
|A|10|N|23|[empty]|36|
|B|11|O|24|
|C|12|P|25|

## Example
```
F543210(A)
```
1. Convert leading empty character to 36 and `F` to 15.
2. Convert check digit `A` to 10.
3. Multiply:

|HKID||F|5|4|3|2|1|0|A|
|--|--|--|--|--|--|--|--|--|--|
|Conversion|36|15|5|4|3|2|1|0|10|
|Multiply by|9|8|7|6|5|4|3|2|1|
|Product|324|120|35|24|15|8|3|0|10

4. Sum: 324+120+35+24+15+8+3+0+10 = 539
5. Remainder: 539 mod 11 = 0
6. `F543210(A)` is a valid HKID number.

## Source Code
Original source code from [CuMask+](https://www.qmask.gov.hk) registration website [[1]](#ref1):
```javascript
S = function(e, a) {
  var t = !0;
  if ("" !== e && "" !== a) {
    var n = e.toUpperCase().match(/^([A-Z]{1,2})([0-9]{6})$/);
    if (null === n)
      t = !1;
    else {
      var r = n[1],
          o = n[2],
          i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          l = 0;
      2 === r.length ? (l += 9 * (10 + i.indexOf(r.charAt(0))), l += 8 * (10 + i.indexOf(r.charAt(1)))) : (l += 324, l += 8 * (10 + i.indexOf(r)));
      for (var s = 0, c = 7; s < o.length; s += 1, c -= 1)
        l += c * o.charAt(s);
      var m = l % 11,
          u = 0 === m ? 0 : 11 - m;
      t = u.toString() === a || 10 === u && "A" === a
    }
  }
  return t
};
```

## References
<a id="ref1"></a> [1] Office of the Government Chief Information Officer, the Government of the Hong Kong Special Administrative Region (13 May 2020), [CuMask+ Registration](https://www.qmask.gov.hk/reginfo/static/js/main.fb5c0196.chunk.js), retrieved 17 May 2020, [archived](https://web.archive.org/web/20200517044214/https://www.qmask.gov.hk/reginfo/static/js/main.fb5c0196.chunk.js) on 17 May 2020.
