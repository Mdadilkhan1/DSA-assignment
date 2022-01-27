{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d64433f4",
   "metadata": {},
   "source": [
    "# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d880acda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 7) (4, 6) "
     ]
    }
   ],
   "source": [
    "Array = [1,2,5,3,4,6,7]\n",
    "sum = 10\n",
    "\n",
    "def sum_pairs(array,n):\n",
    "    '''array = Array of integers. \\n n = The required sum. \\n \\t Returns all pairs of integers from array whose sum is equal to n.'''\n",
    "\n",
    "    for a in array:\n",
    "        if n-a in array[array.index(a)+1:] :\n",
    "            print((a,n-a), end=' ')\n",
    "    \n",
    "sum_pairs(Array,sum)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1641b50",
   "metadata": {},
   "source": [
    "# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3951c6e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "Array_2=[1,2,3,4,5,6,7,8,9]\n",
    "\n",
    "class arrays:\n",
    "    \n",
    "    def __init__(self,arr):\n",
    "        self.show_array=arr\n",
    "    \n",
    "    \n",
    "    # Function to Reverse the Array in place    \n",
    "    def reverse_inplace(self):\n",
    "        l=len(self.show_array)\n",
    "        for i in range((l//2)):\n",
    "            self.show_array[i],self.show_array[l-i-1] = self.show_array[l-i-1],self.show_array[i]\n",
    "            \n",
    "        return 'Array is Reversed'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9e20ede0",
   "metadata": {},
   "outputs": [],
   "source": [
    "Ar= arrays(Array_2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "add5e452",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Ar.show_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a7d32b39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 8, 7, 6, 5, 4, 3, 2, 1]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Ar.reverse_inplace()\n",
    "Ar.show_array"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "145f6adf",
   "metadata": {},
   "source": [
    "# Q3. Write a program to check if two strings are a rotation of each other?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "00914931",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_rotation(str1,str2):\n",
    "    '''Checks if str2 is rotation of str1'''\n",
    "    temp=str1*2\n",
    "    if str2 in temp and len(str1)==len(str2):\n",
    "        return 'Strings are rotation'\n",
    "    else:\n",
    "        return 'Strings are not rotation'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a8a6a0b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Strings are rotation'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str1='hello'\n",
    "str2='llohe'\n",
    "check_rotation(str1,str2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3a54ae0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Strings are not rotation'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str3='lolhe'\n",
    "check_rotation(str1,str3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8cfed668",
   "metadata": {},
   "source": [
    "# Q4. Write a program to print the first non-repeated character from a string?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "11626f57",
   "metadata": {},
   "outputs": [],
   "source": [
    "string='program to print'\n",
    "\n",
    "def first_nonrepeated(string):\n",
    "    '''Prints the first character in the string that is not repeated in the string'''\n",
    "    \n",
    "    for i in string:\n",
    "        \n",
    "        if i not in string[string.index(i)+1:] :      # if spaces are not to be considered as character \"and i!=' '\"  should be added after ] in this line \n",
    "            print(i)\n",
    "            return\n",
    "    else:\n",
    "        print('There is no non-repeated character in the string')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "94b51a48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "g\n"
     ]
    }
   ],
   "source": [
    "first_nonrepeated(string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5ef1d2cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There is no non-repeated character in the string\n"
     ]
    }
   ],
   "source": [
    "first_nonrepeated('hello hero rollo')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b070ce0a",
   "metadata": {},
   "source": [
    "# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4effba19",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Tower_of_Hanoi:\n",
    "    '''n : It is the number of Disks'''\n",
    "    \n",
    "    \n",
    "    def __init__(self,n):\n",
    "        self.disks=n\n",
    "        self.start='Tower A'\n",
    "        self.end='Tower C'\n",
    "        self.extra='Tower B'\n",
    "        \n",
    "    def __move(self,n,a,b,c):\n",
    "        if n==1:\n",
    "            print('Move Disk {} from {} to {}'.format(n,a,b))\n",
    "            return\n",
    "        self.__move(n-1,a,c,b)\n",
    "        print('Move Disk {} from {} to {}'.format(n,a,b))\n",
    "        self.__move(n-1,c,b,a)\n",
    "            \n",
    "    def solve(self):\n",
    "        self.__move(self.disks,self.start,self.end,self.extra)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2d3213e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "Game=Tower_of_Hanoi(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f40dd2d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Move Disk 1 from Tower A to Tower C\n",
      "Move Disk 2 from Tower A to Tower B\n",
      "Move Disk 1 from Tower C to Tower B\n",
      "Move Disk 3 from Tower A to Tower C\n",
      "Move Disk 1 from Tower B to Tower A\n",
      "Move Disk 2 from Tower B to Tower C\n",
      "Move Disk 1 from Tower A to Tower C\n"
     ]
    }
   ],
   "source": [
    "Game.solve()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8f24ec7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Move Disk 1 from Tower A to Tower B\n",
      "Move Disk 2 from Tower A to Tower C\n",
      "Move Disk 1 from Tower B to Tower C\n",
      "Move Disk 3 from Tower A to Tower B\n",
      "Move Disk 1 from Tower C to Tower A\n",
      "Move Disk 2 from Tower C to Tower B\n",
      "Move Disk 1 from Tower A to Tower B\n",
      "Move Disk 4 from Tower A to Tower C\n",
      "Move Disk 1 from Tower B to Tower C\n",
      "Move Disk 2 from Tower B to Tower A\n",
      "Move Disk 1 from Tower C to Tower A\n",
      "Move Disk 3 from Tower B to Tower C\n",
      "Move Disk 1 from Tower A to Tower B\n",
      "Move Disk 2 from Tower A to Tower C\n",
      "Move Disk 1 from Tower B to Tower C\n"
     ]
    }
   ],
   "source": [
    "Game2=Tower_of_Hanoi(4)\n",
    "Game2.solve()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23349386",
   "metadata": {},
   "source": [
    "# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1a447f70",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Post_to_Pre(exp):\n",
    "    '''Converts a Postfix Expression to Prefix Expression'''\n",
    "    temp=[]\n",
    "    for i in exp:\n",
    "        if i in '+-*/^()':\n",
    "            t1=temp.pop()\n",
    "            t2=temp.pop()\n",
    "            t3=i+t2+t1\n",
    "            temp.append(t3)\n",
    "        else:\n",
    "            temp.append(i)\n",
    "    pre=''\n",
    "    for i in temp:\n",
    "        pre+=i\n",
    "            \n",
    "    print('Prefix expression : ',pre)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1eb49542",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prefix expression :  +AB-CD\n"
     ]
    }
   ],
   "source": [
    "Post_to_Pre('AB+CD-')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e7a0e536",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prefix expression :  *-A/BC-/AXY\n"
     ]
    }
   ],
   "source": [
    "Post_to_Pre('ABC/-AX/Y-*')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79b45d60",
   "metadata": {},
   "source": [
    "# Q7. Write a program to convert prefix expression to infix expression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "dff9733d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Pre_to_In(exp):\n",
    "    '''Converts a Prefix Expression to Infix Expression'''\n",
    "    temp=[]\n",
    "    for i in exp[::-1]:\n",
    "        if i in '+-*/^()':\n",
    "            t1='('+temp.pop()+i+temp.pop()+')'\n",
    "            temp.append(t1)\n",
    "        else:\n",
    "            temp.append(i)\n",
    "    In=''\n",
    "    for i in temp:\n",
    "        In+=i\n",
    "    print('Infix expression : ',In)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3eef05d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Infix expression :  ((A-(B/C))*((A/K)-L))\n"
     ]
    }
   ],
   "source": [
    "Pre_to_In('*-A/BC-/AKL')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2390fa5",
   "metadata": {},
   "source": [
    "# Q8. Write a program to check if all the brackets are closed in a given code snippet."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "86f6b5bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def balanced_brackets(exp):\n",
    "    '''Returns whether an expression has closed brackets or not'''\n",
    "    \n",
    "    brackets= []\n",
    "    br_dict={'(':')','[':']','{':'}'}\n",
    "    \n",
    "    for i in exp:\n",
    "        if i in '({[':\n",
    "            brackets.append(i)\n",
    "        else:\n",
    "            if not brackets:\n",
    "                return 'Not Closed'\n",
    "            temp = brackets.pop()\n",
    "            if br_dict[temp] != i:\n",
    "                return 'Not Closed'\n",
    "    if brackets:\n",
    "        return 'Not Closed'\n",
    "    else:\n",
    "        return 'Closed'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "da2894fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Closed'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "balanced_brackets('{[()]}[]()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dd267a55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Not Closed'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "balanced_brackets('{[(]}[]')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6301f29",
   "metadata": {},
   "source": [
    "# Q9. Write a program to reverse a stack."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "09c917a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# defining a simple stack for this and next question\n",
    "class Stack():\n",
    "    def __init__(self):\n",
    "        self.data=[]\n",
    "        self.min=[]\n",
    "                \n",
    "    def push(self,item):\n",
    "        self.data.append(item)\n",
    "        if self.min:\n",
    "            if self.min[-1] > item:\n",
    "                self.min.append(item)\n",
    "        else:\n",
    "            self.min.append(item)\n",
    "                    \n",
    "    def pop(self):\n",
    "        if self.data:\n",
    "            t=self.data.pop()\n",
    "            if t==self.min[-1]:\n",
    "                self.min.pop()\n",
    "            return t\n",
    "    \n",
    "    def top(self):\n",
    "        if self.data:\n",
    "            return self.data[-1]\n",
    "        else:\n",
    "            return None\n",
    "        \n",
    "    def display(self):\n",
    "        print('printing items in the Stack...\\n')\n",
    "        for i in self.data[::-1]:\n",
    "            print(i)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "3a5d6d51",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining a function for reversing the stack \n",
    "def reverse(self):\n",
    "    temp=[]\n",
    "    while self.data :\n",
    "        temp.append(Stack.pop(self))\n",
    "    for i in temp:\n",
    "        Stack.push(self,i)\n",
    "    print('Stack is Reversed')\n",
    "    \n",
    "# Assigning this function to Stack as method\n",
    "\n",
    "Stack.reverse = reverse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "7f607874",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Declaring a class instance\n",
    "obj=Stack()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "91fb31bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pushing data into a Stack\n",
    "for i in range(1,11):\n",
    "    obj.push(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "75fb6d2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "printing items in the Stack...\n",
      "\n",
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "obj.display()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9caa7e8b",
   "metadata": {},
   "source": [
    "# Q10. Write a program to find the smallest number using a stack."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "118b2ba5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining a function for printing minimum number from a stack (Stack is defined in previous question)\n",
    "\n",
    "def minimun(self):\n",
    "    return self.min[-1]\n",
    "\n",
    "\n",
    "# Assigning this function to Stack as method\n",
    "\n",
    "Stack.min_no = minimun"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "102ca762",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Finding minimum from obj stack previously defined\n",
    "obj.min_no()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15526583",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
