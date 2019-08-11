# apt – Algorithm Practice Tool

When it comes to algorithms, why be inapt?

`apt` is a 60 line shell script for pseudocode algorithm creation, retrieval, and management. Written with the intention of printing out with a randomized array of numbers, to be practiced over a cup of coffee.

## Usage

    ./apt n:    #new algorithm
    ./apt e:    #edit algorithm
    ./apt d:    #delete algorithm
    ./apt p:    #send algorithm and random array to stdout

To send `apt`'s output to a printer, I recommend piping instructions into `apt`, then `apt` to a print command like `lpr`, e.g.

    echo -e "y\ny\n" | ./apt p | lpr -P $printername    #send random algorithm to printer

## Installation:

- Bash is required.
- Open `apt` and change the first few variables; adjacent comments denote their function.

## Planned Upgrades:

- automagically add line numbers to raw algorithm file after creation, accordingly revise with edits (use `nl`)
- command parsing: something like `!array on/off` to toggle array in output. Useful for outputting dfs/bfs with no need for arrays.
