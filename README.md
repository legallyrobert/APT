# apt – Algorithm Practice Tool

Algorithm creation, retrieval, and management in 60 lines of shell script. Written with the intention of practicing sorting algorithms on a randomized array of numbers, sent to a physical printer to be done over a cup of coffee.

## Usage

    ./apt n:    #Make a new algorithm
    ./apt e:    #Edit an existing algorithm
    ./apt d:    #Delete an algorithm
    ./apt p:    #Print (stdout) a chosen or random algorithm and random array (default on)

To send `apt`'s output to a printer, I recommend piping instructions into `apt`, then `apt` to a print command like `lpr`, e.g.

    echo -e "y\ny\n" | ./apt p | lpr -P $printername    #send random algorithm to printer

## Installation:

- Bash is required.
- Open `apt` and change the first few variables; adjacent comments denote their function.

## Planned Upgrades:

- automagically add line numbers to raw algorithm file after creation, accordingly revise with edits (use `nl`)
