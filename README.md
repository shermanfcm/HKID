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
Original source code from [COVID-19 Universal Community Testing Programme](https://www.communitytest.gov.hk) booking system [[1]](#ref1) and [COVID-19 Vaccination Programme](https://www.covidvaccine.gov.hk) booking system [[2]](#ref2):
```javascript
function IsHKID(str) {
  var strValidChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (str.length < 8)
  { 
    return false;
  }
  str = str.toUpperCase();    
  var hkidPat = /^([A-Z]{1,2})([0-9]{6})([A0-9])$/;
  var matchArray = str.match(hkidPat);    
  if (matchArray == null)
  {
    return false;
  }
  var charPart = matchArray[1];
  var numPart = matchArray[2];
  var checkDigit = matchArray[3];    
  var checkSum = 0;
  if (charPart.length == 2) {
    checkSum += 9 * (10 + strValidChars.indexOf(charPart.charAt(0)));
    checkSum += 8 * (10 + strValidChars.indexOf(charPart.charAt(1)));
  } else {
    checkSum += 9 * 36;
    checkSum += 8 * (10 + strValidChars.indexOf(charPart));
  }

  for (var i = 0, j = 7; i < numPart.length; i++, j--)
  {
    checkSum += j * numPart.charAt(i);
  }
  var remaining = checkSum % 11;
  var verify = remaining == 0 ? 0 : 11 - remaining;
  return verify == checkDigit || (verify == 10 && checkDigit == 'A');
}
```

## References
<a id="ref1"></a> [1] Hong Kong Special Administrative Region Government (29 Aug 2020), [COVID-19 Universal Community Testing Programme Booking System](https://booking.communitytest.gov.hk/form/assets/js/application_mo.js), retrieved 30 Aug 2020, [archived](https://web.archive.org/web/20200830081912/https://booking.communitytest.gov.hk/form/assets/js/application_mo.js) on 30 Aug 2020.

<a id="ref2"></a> [2] Hong Kong Special Administrative Region Government (18 Mar 2022), [COVID-19 Vaccination Programme Booking System](https://booking.covidvaccine.gov.hk/forms/assets/js/application_mo.js), retrieved 28 Mar 2022, [archived](https://web.archive.org/web/20220328132257/https://booking.covidvaccine.gov.hk/forms/assets/js/application_mo.js) on 28 Mar 2022.
