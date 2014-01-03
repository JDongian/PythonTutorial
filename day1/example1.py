"""File I/O and string manipulation example.
The program queries the user for the name of a file, then outputs a summary of
the internal contents of the file.
"""

def get_file_contents(relative_path):
    """Return the contents of the given file as a string.
    """
    data = ""
    # The file is opened using "with open(...) as _" syntax.
    # This ensures safety (the filestream gets closed automatically) as well
    # as flexibility (you can change the 'r' read mode to 'w' write mode if
    # needed.
    with open(relative_path, 'r') as data_in:
        data = data_in.read()
    return data

def gen_summary(filedata):
    """Return a summary of the given file.
    """
    # Play around with the array splicing and see what you get.
    # Fun examples:
    # [:50:-1]
    # [len(filedata)/2: 50]
    # [-250::5]
    #
    # Challenge:
    # Fix the bug that occurs when the file is too short.
    # There are many ways to handle this - choose one you like best.

    beginning = filedata[:50]
    end = filedata[-50:]
    summary = "File summary:\n%s\n.\n.\n.\n%s\nEOF" % (beginning, end)
    return summary

if __name__ == "__main__":
    filename = input("Input a file name to summarize: ")
    filedata = get_file_contents(filename)
    file_summary = gen_summary(filedata)
    print(file_summary)

# Note that the above code has a pedagogical style to it.
# When doing this casually, 
#
# data = open(raw_input("Input a file name to summarize: ")).read()
# print("File summary:\n%s\n.\n.\n.\n%s\nEOF" % (data[:100], data[-100:]))
#
# Produces the same effect, but is more readable because there are only two
# lines to read.
#
# A note for people coming from python2: raw_input() was renamed to input() (PEP 3111).
