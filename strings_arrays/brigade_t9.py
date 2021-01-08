
# // Inputs
# //   phoneNumber, eg "4653"
# //   dictionary, eg ["ACTOR", "APPLE", ...]
# // Output ["GOLF", "HOLD", "HOLE"]
# // eg "4" -> ['G', 'H', 'I'], "6" -> ['M', 'N', 'O'], "5" -> ['J', 'K', 'L'], "3" -> ['D', 'E', 'F']
# 
# 
# "4653" => [["GOLF", "HOLD", "HOLE"]]
# 
# inputs [0-9]
# 
# 4,6,5,3
# 
# 

# G -> O -> L -> F
# 
#  0 1 2 3 [4] 5 6 7 8 9
#  
#         [0 1 2 3 4 5 [6] 7 8 9]
#                     
#                      [0 1 2 3 4 [5] 6 7 8 9]
#                      
#                                 [0 1 2 [3] 4 5 6 7 8 9]
# 

# implement prefix trie

keypad_dict = {
    0:[], 
    1:[], 
    2:['A','B','C'], 
    3:['D','E','F'], 
    4:['G','H','I'], 
    5:['J','K','L'], 
    6:['M', 'N', 'O'],
    7:['P','Q','R','S'], 
    8:['T','U','V'], 
    9:['W','X','Y','Z'] 
}

# input = ['4','6','5', '3'] 
def generate_combos(input):
    if not input:
        return []
    
    first_combos = [input[0] + tail for tail in generate_combos(input[1:])]
    # 44, 46, 45, 43 
    rest_combos = generate_combos()
    
    