# Read from the file file.txt and output the tenth line to stdout.
sed -n "10p" file.txt

-sed: operates on an input file line by line, and edits each line according to the instructions
-n: nly print lines explicitly indicated by the command
-p: print

Reference: https://phpfog.com/3-ways-to-get-the-nth-line-of-a-file-in-linux/
