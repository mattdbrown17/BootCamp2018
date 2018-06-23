#ExceptionsAndIO.py

#Exercise 1
def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
    "digits differ by 2 or more: ")
    step_1 = int(step_1)
    if step_1 > 999 or step_1 < 100:
        raise ValueError("You must give a three digit number")
    ''' Get the digit values for step 1 '''
    str_step_1 = str(step_1)
    dig1 = int(str_step_1[0])
    dig2 = int(str_step_1[1])
    dig3 = int(str_step_1[2])
    if dig1 - dig3 < 2 and dig3 - dig1 < 2:
        raise ValueError('''The number's first and last digits must
                         differ by at least two''')

    step_2 = input("Enter the reverse of the first number, obtained "
    "by reading it backwards: ")
    str_step_2 = step_2
    step_2 = int(step_2)
    ''' I'll pull the individual digits. '''
    dig1s2 = int(str_step_2[0])
    dig2s2 = int(str_step_2[1])
    dig3s2 = int(str_step_2[2])
    if dig1s2 != dig3 or dig2s2 != dig2 or dig3s2 != dig1 \
    or step_2 > 999:
        ''' The last statement is so I get an error if step 1 were 135
        and step 2 is 531023928432, for example. '''
        raise ValueError("You must input the previous number backwards")

    step_3 = input("Enter the positive difference of these numbers: ")
    if int(step_3) != abs(step_1 - step_2):
        print(step_3, abs(step_1 - step_2))
        raise ValueError('''Check your subtraction! Please enter the
                         positive difference of the numbers''')

    step_4 = input("Enter the reverse of the previous result: ")
    '''I have no need to keep step_3 or step 4 as integers, so I'll
    do this check more quickly: '''
    if step_3[0] != step_4[2] or step_3[1] != step_4[1] or \
    step_3[2] != step_4[0] or len(step_4) > 3:
        raise ValueError("You must input the previous number backwards")
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

# arithmagic()

'''
------------------------------------------------------------------------
'''

# Exercise 2

from random import choice
def random_walk(max_iters=1e12):
    try:
        walk = 0
        directions = [1 , -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
        print("Process Completed")
        return walk
    except KeyboardInterrupt:
        print("Process interrupted at iteration ", i)
        return walk

# random_walk()

'''
------------------------------------------------------------------------
'''

# Exercise 3
class ContentFilter:
    '''
    This class accepts the name of an object to be read. Once it
    recieves a valid object, it stores the contents of the object and
    some other statistics as attributes.

    Attributes:
    content (str): The contents of the file listed as a string.
    chars (str): The number of characters in the file.
    alpha (str): The number of alphabetical characters in the file.
    numer (str): The number of numerical characters in the file.
    wtspace (str): The number of whitespace characters in the file.
    lines (str) : The number of lines in the file.
    '''
    def __init__(self, filename):
        '''
        Reads in file if name is valid. Turns contents from list into
        string. Also creates attributes.
        '''
        self.filename = filename
        x = True
        while x:
            try:
                myfile = open(self.filename, 'r')
                contents = myfile.readlines()
                x = False
            except (FileNotFoundError, TypeError, OSError) as e:
                new_name = input("Please enter a valid name: ")
                self.filename = new_name
        self.contents = ''.join(contents)
        myfile.close()

        ''' Here I create the "number of characters" attribute '''

        self.chars = len(self.contents)

        '''
        The next three loops are very similar: They use a counter to
        track how many alphabetical, numerical, or whitespace Characters
        there are and then store them as attributes.
        '''

        z = 0
        for i in range(0, self.chars):
            if self.contents[i].isalpha():
                z += 1
        self.alpha = z

        z = 0
        for i in range(0, self.chars):
            if self.contents[i].isdigit():
                z += 1
        self.numer = z

        z = 0
        for i in range(0, self.chars):
            if self.contents[i].isspace():
                z += 1
        self.wtspace = z

        ''' For the lines attribute, I start at z = 1 because otherwise
        I would miss the first line! '''

        z = 1
        for i in range(0, self.chars):
            if self.contents[i] == '\n':
                z += 1
        self.lines = z

    def uniform(self, writename, mode = 'w', case = 'upper'):
        '''
        uniform accepts inputs writename, mode, and case. writenname is
        the name of the file that I am writing to. Mode is the second
        argument of the open function (default is 'w'). Case tells me
        whether I am writing the letters all in uppercase or lowercase
        (default is upper).

        The function takes self, modifies its contents appropriately,
        and writes these to writename.
        '''
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("The mode is invalid ('w', 'x', or 'a')")
        if case == 'upper':
            casecontent = self.contents.upper()
        elif case == 'lower':
            casecontent = self.contents.lower()
        else:
            raise ValueError("The case must be upper or lower.")
        with open (writename, mode) as writein:
            writein.write(casecontent)

    def reverse(self, writename, mode='w', unit='line'):
        '''
        reverse accepts inputs writename, mode, and unit. writenname is
        the name of the file that I am writing to. Mode is the second
        argument of the open function (default is 'w') Unit tells me
        whether I'm going backwards by line or by word (default is line)

        the function takes self, slices it up by line and/or word,
        and uses for-loops to write it into writename in the appropriate
        order.
        '''
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("The mode is invalid ('w', 'x', or 'a')")
        if unit == 'line':
            listcon = self.contents.split('\n')
            with open (writename, mode) as writein:
                for i in range(0, len(listcon)):
                    writein.write(listcon[len(listcon)-i-1])
                    writein.write('\n')
        elif unit == 'word':
            listcon = self.contents.split('\n')
            with open (writename, mode) as writein:
                for i in range(0, len(listcon)):
                    currentline = listcon[i]
                    currentline = currentline.split(' ')
                    for j in range (0, len(currentline)):
                        writein.write(currentline[len(currentline)-j-1])
                        writein.write(' ')
                    writein.write('\n')
        else:
            raise ValueError("The unit must be line or word.")

    def transpose(self, writename, mode='w'):
        '''
        transpose accepts inputs writename and mode. writenname is
        the name of the file that I am writing to. Mode is the second
        argument of the open function (default is 'w') Unit tells me
        whether I'm going backwards by line or by word (default is line)

        the function takes self, slices it up by line and/or word,
        and uses for-loops to write it into writename in the appropriate
        order.
        '''
        if mode != 'w' and mode != 'x' and mode != 'a':
            raise ValueError("The mode is invalid ('w', 'x', or 'a')")
        listcon = self.contents.split('\n')
        with open (writename, mode) as writein:
            firstline = listcon[0].split(' ') #(just to get the length)
            for j in range(0, len(firstline)):
                for i in range(0, len(listcon)):
                    currentline = listcon[i]
                    currentline = currentline.split(' ')
                    writein.write(currentline[j])
                    writein.write(' ')
                writein.write('\n')

    def __str__(self):
        ''' Returns a string detailing the properties of self '''
        return(f'''
              Source file: \t {self.filename} \n \
              Total characters: \t {self.chars} \n \
              Alphabetic Characters: \t {self.alpha} \n \
              Whitespace Characters: \t {self.wtspace} \n \
              Number of lines: \t {self.lines} \n \
              ''')



a = ContentFilter("hello_world.txt")
print(a)
#print("# of alphabetical Characters is:", sum[isalpha() for k in a.contents])
#a.uniform("newfile.txt", "w", "lower")
print(a.contents.split('\n'))
a.transpose("newfile.txt", "w")
#b = ''.join(a.contents)
#print(b)
'''
------------------------------------------------------------------------
'''

# Exercise 4
