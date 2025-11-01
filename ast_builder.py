from sys import exit

class Node:
    left = None
    right = None
    term = None
    fourse = None
    value_term = None
    def __init__(self,expr,byteType):
        self.expr = expr
        self.byteType = byteType

def nerest_end_sep(order_line,location,end):
    stop = 0
    loc = 0
    start = 0
    print(order_line[location+1:end])
    for token in order_line[location:end+1]:
        if token[1] == "sep":
            if stop == 0:
                start = loc
            if token[2] == "(":
                stop += 1
            elif token[2] == ")":
                stop -= 1
        
        loc += 1 
    if stop == 0 and loc != 0:
        return loc, start
    print("the sep did not end.")
    exit(1)

def AST_builder(ordered_line: list) -> Node:
    # lowest num finder

    if ordered_line == []:
        return None

    current_EOL = 0
    loc = 0
    Node_main = None

    for tok in ordered_line:
        if tok[1] == "EOL":
            current_EOL = loc
            break
        loc += 1    
    del loc

    
    location_target = 0
    loc = 0
    lowest_target = 200
    for ord_token in ordered_line:
        if ord_token[0] != None:
            if lowest_target > ord_token[0]:
                lowest_target = ord_token[0]
                location_target = loc
                
        loc += 1
    if ordered_line[location_target][1] == "opr":
        Node_main = Node(ordered_line[location_target][2],"OPR")
        if ordered_line[location_target][2] == "=":
            Node_main.fourse = "SETV" # set values
        elif ordered_line[location_target][2] == "+":
            Node_main.fourse = "ADDI" # addition
        elif ordered_line[location_target][2] == "-":
            Node_main.fourse = "SUPT" # suptraction
        elif ordered_line[location_target][2] == "*":
            Node_main.fourse = "MULT" # multiplecation
        elif ordered_line[location_target][2] == "/":
            Node_main.fourse = "DIVI" # division
        elif ordered_line[location_target][2] == "%":
            Node_main.fourse = "MODL" # modlue
       
        if Node_main.fourse == "SETV":
            if location_target <= 1:
                print("no element behind")
                exit(1)
            elif ordered_line[location_target-1][1] != "elm":
                print("no element behind")
                exit(1)

            Node_main.term = ordered_line[location_target-1][2]
            Node_main.value_term = AST_builder(ordered_line[location_target+1:current_EOL+1])
            Node_main.left = AST_builder(ordered_line[location_target+1:current_EOL+1])
        
        else:
            Node_main.right = AST_builder(ordered_line[location_target:current_EOL])
            Node_main.left = AST_builder(ordered_line[:location_target])
            if Node_main.right == Node(None,""):
                print("NO astrebute aveible")
                exit(1)
            elif Node_main.right == Node(None,""):
                print("NO astrebute aveible")
                exit(1)
    elif ordered_line[location_target][1] == "keyword":
        Node_main = Node(ordered_line[location_target][2],"KEYWORD")
        if ordered_line[location_target][2] == "func":
            location, start_loc = nerest_end_sep(ordered_line,location_target,current_EOL)
            print(ordered_line[start_loc])
            Node_main.term = AST_builder(ordered_line[start_loc:location-1])
            
    elif ordered_line[location_target][1] == "int":
        Node_main = Node(ordered_line[location_target][2],"int32")
    
    elif ordered_line[location_target][1] == "str":
        Node_main = Node(ordered_line[location_target][2],"str")

    return Node_main