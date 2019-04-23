"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r') as f:
    content = f.read();
    print(content)
## writing it as print(f.read()) gives me an error about the file already being closed. 
## possibly closes just before print, which is run before f.read() in this case?

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as b:
    b.write('\n\nOutside, the wind ceased.\n Owls halted in mid-flight.\n Well, maybe they did, maybe they didn’t, certainly the central heating chose that moment to shut down, unable perhaps to cope with the supernatural chill that suddenly whipped through the room.')

with open('bar.txt', 'r') as b:
    content = b.read();
    print(content)

## How to do the above with r+?
