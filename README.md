# Concatenator for your C++ projects

Made for situations when you properly split a program into headers and source code, but to test your solution you need to send just a single file to a contest system (in my case, Yandex.Contest)

## Usage

Run the script in the project directory (may not work for more complex structures, I need more testing material) with

`python contatenator.py`

Parameters defined in the script:

`main` variable contains the name of the file with `int main` from which recursive descend starts

`united` variable contains the name of the output file

## Abilities

The script is able to:

1. concatenate .cpp, .hpp, .h and .inl files;

2. traverse nested directories;

3. move common defines and stdlib includes to the top;

4. delete header guardians

## Limitations:

1. Each header must have no more than one corresponding source file! and the corresponding file must have the same name! If I were to write more general algorithm, I would have to parse Makefile, which is too complicated and I'm too lazy

to be continued...
