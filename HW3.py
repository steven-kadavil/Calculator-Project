# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None  #if top is none then stack empty

    def __len__(self): 
        # YOUR CODE STARTS HERE
        # This is like iterating through a linked list until there is no more elements in it
        count = 0
        current = self.top
        while(current != None):
            count += 1
            current = current.next
        return count

    def push(self,value):
        # YOUR CODE STARTS HERE
        #pushes node into stack first checking if stack is empty
        new_node = Node(value)
        if(self.isEmpty()):
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

     
    def pop(self):
        # YOUR CODE STARTS HERE
        # checks if stack is empty and then returns value if not empty and removes from stack
        if(self.isEmpty()):
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value
        

    def peek(self):
        # YOUR CODE STARTS HERE
        #checks if empty returns self.top
        if(self.isEmpty()):
            return None
        else:
            return self.top.value


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
        except:
            return False
        return True

        ''' 
    def _isvalid(self,txt):
        lst = txt.split(" ")
        for i in range(len(lst)):
            if(i<= len(lst) - 2 and self._isNumber(lst[i]) and self._isNumber(lst[i])+1):
                return None
            elif(i<= len(lst)- 2 and (lst[i] in dict and lst[i] not in groupings) and (lst[i+1] in dict and lst[i+1] not in groupings)):
                return None
            elif(i == len(lst)-1 and (lst[i] in dict and lst[i] not in groupings)):
                return None
            elif(lst[i] not in dict and lst[i] not in groupings.values() and self._isNumber(lst[i]) == False and lst [i] != ""):
                return None
        '''
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3' )
            '2.1 5.0 * 3.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('3 ^ 5 ^ 2')
            '3.0 5.0 2.0 ^ ^'
           

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('[ [ 5.6 [ 85 + 6 ] } } ^ 0.5 - -26.58 { 85 + 6 }')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        dict = {"(":1, "{":1,"<":1, "[": 1, "^":4, "/":3, "*":3, "-":2, "+":2} #operator precedence
        groupings  = {"(":")","{":"}", "[":"]","<":">"} #grouping symbols and correlated values 
        og_lst = txt.split(" ")
        postfix = "" #postfix text
        lst = og_lst.copy() #copy for implicit multiplication changes
        numbers = 0
        operators = 0  
        balance = Stack()
        balanced = True
        changes = 0

        for i in range (len(og_lst)):
            # for loop first checks for implict multiplication 5(number) [()* ()] and checks for balanced parantheses using a stack from module 5 case study
            if(i >= 1 and i<= len(og_lst) -2 and og_lst[i] in groupings and self._isNumber(og_lst[i-1])):
                
                lst.insert(i + changes,"*")
                changes += 1
            if(i >= 1 and i<= len(og_lst) -2 and og_lst[i] in groupings and og_lst[i-1] in groupings.values()):
             
                lst.insert(i+changes,"*")
                changes += 1
            if(og_lst[i] in groupings):
                balance.push(og_lst[i])
            elif(og_lst[i] in groupings.values()):
                if(balance.isEmpty()):
                    return None
                elif(groupings[balance.pop()] == og_lst[i]):
                    balanced = True
                else:
                    balanced = False
        if(balanced == False or balance.isEmpty() == False): # parantheses are not balanced
            
            return None
        
        for i in range(len(lst)):
            #for loop that checks for invalid expression by counting number of operators and numbers and consecutives (operators and numbers) and unknown symbols
            if(self._isNumber(lst[i])):
                numbers += 1
            elif(lst[i] in dict and lst[i] not in groupings):
                operators += 1

            if(i<= len(lst) - 2 and self._isNumber(lst[i]) and self._isNumber(lst[i+1])):
                #print("my")
                return None
            elif(i<= len(lst)- 2 and (lst[i] in dict and lst[i] not in groupings) and (lst[i+1] in dict and lst[i+1] not in groupings)):
                #print("yo")
                return None
            elif(i == len(lst)-1 and (lst[i] in dict and lst[i] not in groupings)):
                #print("boy")
                return None
            elif(lst[i] not in dict and lst[i] not in groupings.values() and self._isNumber(lst[i]) == False and lst [i] != ""):
                #print("girl")
                return None
        if(operators != (numbers- 1)): # 1 less operator than numbers

           
            return None
     
    
        for i in range (len(lst)):
          
            if lst[i] in dict: # if operator
                
                 
                if(postfixStack.isEmpty()): #have to push if stack is empty
                    postfixStack.push(lst[i])
                


            
                elif(lst[i] == "^" and postfixStack.top.value == "^"): # right associative exponentiation
                    postfixStack.push(lst[i])
                elif(lst[i] == '(' or lst[i] == "<" or lst[i] == "{" or lst[i] == "["): #groupings just get pushed
                    postfixStack.push(lst[i])
                
                else: # pop until run into operator with less priority
                    while(postfixStack.isEmpty() == False and dict[lst[i]] <= dict[postfixStack.peek()]):
                        postfix += postfixStack.pop() + " "
                    postfixStack.push(lst[i])
            elif(lst[i] == ')' or lst[i] == ">" or lst[i] == "}" or lst[i] == "]"): #if closing symbol pop from stack till opening symbol encountered
                top = postfixStack.peek()
                while(top != "(" and top != "<" and top != "{" and top != "[" and postfixStack.isEmpty() == False):
                    postfix += postfixStack.pop() + " "
                    top = postfixStack.peek()
                postfixStack.pop()
            
            elif self._isNumber(lst[i]): # if number just add it to postfix string
                postfix += str(float(lst[i])) + " " 
            
        # if operators still in stack then pop until postfixStack is empty  this also removes uncessary white space
        if(postfixStack.top == None): 
            if(postfix[len(postfix)-1] == " "):
                postfix = postfix[0:len(postfix)-1]
            return postfix
        else:
            while(postfixStack.top.next != None):
                postfix += postfixStack.pop() + " "
        postfix += postfixStack.pop()
        if(postfix[len(postfix)-1] == " "):
            postfix = postfix[0:len(postfix)-1]
        return postfix

       
        






    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * < 5 - 3 ^ 2 > + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * < 4 > ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('[ 1 + 1 ] [ 1 + 1 ]')
            >>> x.setExpr('2 ^ ( 1 + 1 )')
            >>> x.calculate
            4.0
            >>> x.setExpr('4 + ( 6 - 7 ) ^ 0.5')
            >>> x.calculate
            >>> x.setExpr('0 / 0 ')
            >>> x.calculate
            >>> x.setExpr('[ [ 5.6 [ 85 + 6 ] } } ^ 0.5 - -26.58 { 85 + 6 }')
            >>> x.calculate

            
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        #txt = self._getPostfix(self.__expr)
        #print(txt)
        if(self._getPostfix(self.__expr) == None): # checks for invalid expression
            return None
        lst = self._getPostfix(self.__expr).split(" ")
        dict = {"(":1, "{":1,"<":1, "[": 1, "^":4, "/":3, "*":2, "-":2, "+":2}
        #print(lst)
        for i in lst:
            
            if(calcStack.isEmpty() or calcStack.top.next == None): #if empty then must push numbers in
                calcStack.push(float(i))
            elif self._isNumber(i): # every number gets pushed into stack
                calcStack.push(float(i))
            
            elif(i in dict):
                # if run into operator in lst traversal pop twice from stack do the operation then push back into stack
                if(i == "^"):
                    x1 = calcStack.pop()
                    x2 = calcStack.pop()
                    if(float(x1) != int and float(x2) < 0): #cannot do sqrt(-1)
                        return None
                    x = x2 ** x1
                    calcStack.push(x)
                elif(i== "*"):

                    x = calcStack.pop() * calcStack.pop()
                    calcStack.push(x)
                elif(i == "/"):
                    
                    x1 = calcStack.pop() 
                    x2 = calcStack.pop()
                    if(float(x1) == 0.0): # checks for zero division
                        return None
                    x = x2/x1
                    calcStack.push(x)
                
                
                elif(i == "+"):
                    x = calcStack.pop() + calcStack.pop()
                    calcStack.push(x)
                elif(i == "-"):
                    x1 = calcStack.pop() 
                    x2 = calcStack.pop()
                    x = x2 - x1
                    calcStack.push(x)
        value = calcStack.pop()
        return value
        



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        valid = True
        if word[0].isalpha(): # checks if first letter is a alphabet
            valid = True
        else:
            return False
        word = word[1:]
        for i in word:
            if(i.isalpha() or i.isalnum()):
                valid = True
            else: #unknown sybol that is not a alphabet or number
                return False
        return valid #boolean variable that keeps track of if all conditions passed
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        dict = {"(":1, "{":1,"<":1, "[": 1, "^":4, "/":3, "*":3, "-":2, "+":2}
        groupings  = {"(":")","{":"}", "[":"]","<":">"}
       
        changed = False
        lst =  expr.split(" ")
        for i in range (len(lst)):
            if(Calculator._isNumber(self,lst[i]) == False and lst[i] not in dict and lst[i] not in groupings.values() and lst[i] != " "):
                if(self._isVariable(lst[i]) == False): # if it is not a number grouping or operators and it is not a variable then invalid
                    return None
            if (lst[i] in self.states): 
                lst[i] = str(self.states[lst[i]]) #lst[i] is replaced with correspond variable
                changed = True
            if(self._isVariable(lst[i]) and lst[i] not in self.states): #checks for undefined variables
                return None
        new_expr = " ".join(lst)
        if(changed == False): # checks if variables have been replaced
            return expr
        else:
            return new_expr

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        dict = {}
        copy = self.expressions.split(";")
        equations = self.expressions.split(";")
        # copy and equations are used so that I can make changes while keeping the value of the expressions stored in equations

        for i in range(len(copy)):
            copy[i] = copy[i].split("=") # split by equal sign
       
        for i in range(len(copy)): 
            if(i< len(copy)-1): #check if not last element in list

                copy[i][0] = copy[i][0].strip() #copy.strip() so white spaces dont get in the way of calculations
                copy[i][1] = copy[i][1].strip()   

                problem = self._replaceVariables(copy[i][1]) #self.replace vairables is in the 2nd part of the list in the  2d list
               
                if(problem == None): # chekcs if replace variables returned an error
                    self.states = {}
                    return None
                calcObj.setExpr(problem) # give it to calculator object so it calculate
                self.states[copy[i][0]] = calcObj.calculate # self.states variable is updated
                
                dict[equations[i]] = self.states.copy() #expressions is added to dict as key with current version of self.states as value
            
            else:
                copy[i][0] = copy[i][0].strip() 
             
                problem = copy[i][0][6: ].strip() # strip again to remove white spaces
                problem = self._replaceVariables(problem) 
                if(problem == None): # check again to see if replace returned an error 
                    self.states = {}
                    return None
                
                calcObj.setExpr(problem)
                dict['_return_'] = calcObj.calculate #last case of return part of calculate expressions.
    
        return dict

    

   



def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(Calculator._getPostfix, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()