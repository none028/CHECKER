# Checker
## validEmail.py
#### Purpose
```
Check the valid email ID based on .txt file.
Convert .txt file to .csv file
```
#### How to use
```
python validEmail.py -t {target file path} -l {the limit of raw data} -o {target name}
```
#### Example
Input: test.txt
```
none028@gmail.com,1234
1234,213114
000@gmail.com,123141
!@#!@#@gmail.com,123124
```
Run: python validEmail.py -t test.txt -l 1 -o "my_data"
Output: 2020-09-12_my_data.csv
```
none028@gmail.com,1234
```
