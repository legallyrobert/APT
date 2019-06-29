# APT
## Algorithm Practice Tool

APT is a simple Python script that randomly selects a text file in `algorithms/` and generates a corresponding unsorted array of numbers of size 4 ≤ n ≤ 8. It then prints to a local printer, ready for the array to be sorted with the selected algorithm over a cup of morning coffee. Graphing algorithms (BFS, DFS) are included in `algorithms/`, with the later intention of associating a simple example graph with each.

APT was designed and deployed on Linux, with no testing done on Windows. Some support for Windows has been appended, albeit based on [poorly documented code][1]. Worst case scenario, you could write a batch file to run something like `python APT.py; #print out.txt`

The printer name will need to be manually configured per network, regardless of OS.

[1]: <https://smallbusiness.chron.com/sending-things-printer-python-58655.html> "Sending Things to a Printer in Python"
