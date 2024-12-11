# Read in a .wav file as binary data
def read_file_as_binary(filename):
    with open(filename, 'rb') as f:
        binary_data = f.read()
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string
    
binary_data = read_file_as_binary('sound/white_noise.wav')
#print("The file in binary data form:")
#print(binary_string)

test_binary_data = "0110001111000001111110000000111111110000000001111111111000000000001001110000111110000001111111000000001111111110000000000111111111110100111010100100000111010101001010100010000100100001100000001111110100011110010110100001010111110101100001000001011010000000101000100010001111111110110010010100001000110110000010101011110100111101001111001000111011000111100000111111000000011111111000000000111111111100000000000"

test_alpha_data = "BEAAACDBCEADADDEEBEBBABEAADDABCCCADEDEDCABDEABAEBCCDDEBCBBCEBAEEBEDDDBDDBADCEAADCBECADBEACBDCCBDBEEDDDECDEEDEEECEDECCBBACACEDEBCEADAABACCEBECDDEAEBECAEEAACCADBBDABAABDEBBCAABBCADEEBECDADBBBABCADBDBEDEAECADBEEADEDDCDCBCAEECADABDBDACDDDDECBAABBDABCECDDCBEAAEBDEACBEEBCBCEDECADAEDAADBEBECCCABACDCCDBABDCEDCEBEADADEAECDEEBCDAEEEEDABECAEDCDBBDADBECBCAACAEADBCCDBAACCCCDCDACABEEABEEBCAEABCEBADCBBABDBEDABCCACBBCBCCEDCDCABECBCBADBCCDCEEAAAEDBCCBAEBABAACDCEBEADDDAECCCEDECDDABEABBEACEEAADEAACECCABEBEACCBEADDADBEBCAAEEDBBBCCCBECDEEECCACBCECABCBAADAABDDABABADBDACEBAACAAADBAEDBAAEBDDBAEAAEDDDEECACCABDBAAEABABEEECBEBABCEDADBECBEABABCBBCEECAEDEDABEEBACBDEEDCBDAEAEBDCAECEABDDADDCCDDBDAAACADDEBEDBCBBDDDEAABDBBABEADAACDAEDCEDDBCDCBABACBDCCAABBBBDCDDCDBCEDCDAEDBABDDDABAEEDEAEAABBCBDDCACECEBDEDEDCEEECCCEDEAACBACBECCCDCBBDCEBEEDACECAAEEAABAAADBAEEACEADEDCDEDACECDEEDAEADBEAEDCADDEBBEBAEAACCDAADECADBACADEBCDEBCAEBEDAAEDBCCEEBBBCDBBCDCDACCDAEDBEAAADDEDCECBBAEDECEBCBDDDEBEBCCBCAEBABEACAAECBCEDCDDCAEDEDBBDDEDEECCC"

# This is done to make it readable and to keep me sane
def convert_to_alpha(binary_string):
    alpha_string = ""
    for n in binary_string:
        if n == "0":
            alpha_string += str("o")
        if n == "1":
            alpha_string += str("i")
    return alpha_string

# This will count sequences of repeating of 1s and 0s
def run_length_encoding_alphanumeric(alpha_string):
    encoded_string = ""
    last_char = alpha_string[0]
    count = 0
    for c in alpha_string:
        if c == last_char:
            count +=1
        else:
            encoded_string += str(last_char)
            encoded_string += str(count)
            last_char = c
            count = 1
    encoded_string += str(last_char)
    encoded_string += str(count)      
    
    #print("Alpha string:")
    #print(alpha_string)
    #print("Encoded String:")
    #print(encoded_string)
    return encoded_string
    
# This will compress strings of 1s and 0s
def run_length_encoding_binary(binary_string):
    encoded_string = ""
    count = 0
    last_char = "0"
    for c in binary_string:
        if c == "0":
            if last_char == "1":
                #encoded_string += str(".")
                encoded_string += str(count)
                count = 0
            count += 1
            last_char = "0"
            
        elif c == "1":
            if last_char == "0":
                #encoded_string += str(".")
                encoded_string += str(count)
                count = 0
            count += 1
            last_char = "1"
    encoded_string += str(".")
    encoded_string += str(count)
    print("First 1000 characters of the source Binary String:")
    binary_print_string = binary_string[:1000]
    print(binary_print_string)
    print("First 1000 characters of the Run Length Encoded String:")
    encoded_print_string = encoded_string[:1000]
    print(encoded_print_string)
    return encoded_string


run_length_encoding_alphanumeric(test_alpha_data)
rle_data = run_length_encoding_binary(binary_data)

# Test the Huffman encoding on a small scale first.
test_string_data = "AAABBBBCCCCGGGGAAAAAAAAABBBCCCDDDDEEEEEEEEEEEEFFFFFFFFFFFFFFFFFGGG"
character_binary_mapping = {}

# Define the Huffman node as part of a larger tree
class Huffman_Node:
    def __init__(self, frequency, data, left_node, right_node):
        self.frequency = frequency
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# Creates Huffman Tree
def create_tree(mapping_key):
    # Gets keys in the frequency map of characters
    keyset = mapping_key.keys()
    priority_queue = []
    
    for c in keyset:
        node = Huffman_Node(mapping_key[c], c, None, None)
        priority_queue.append(node)
        # Sort all nodes by frequency the character appears
        priority_queue = sorted(priority_queue, key = lambda x:x.frequency)
        
    priority_queue.reverse()

    while len(priority_queue) > 1:
        first = priority_queue.pop(0)
        second = priority_queue.pop(0)
        merge_node = Huffman_Node(first.frequency + second.frequency, '-', first, second)
        # Add merge node to priority queue then sort
        priority_queue.append(merge_node)
        priority_queue = sorted(priority_queue, key = lambda x:x.frequency)
        
    # Return the root node
    return priority_queue.pop()
        

# Function to create the binary encoding for each node, based on its position in the tree.
def create_binary_code(node, string_data):
    if not node is None:
        if node.left_node is None and node.right_node is None:
            character_binary_mapping[node.data] = string_data
        
        # Left
        string_data += '0'
        create_binary_code(node.left_node, string_data)
        string_data = string_data[:-1]
        
        # Right
        string_data += '1'
        create_binary_code(node.right_node, string_data)
        string_data = string_data[:-1]
        
    
# Creates Huffman encoding
def huffman_encode(string_data):
    # Maps all of the characters in the input string and counts their frequency
    mapping_key = {}
    for c in string_data:
        if not c in string_data:
            #mapping_key[c] = 1
            mapping_key.update({c: 1})
        else:
            #mapping_key[c] += 1
            mapping_key.update({c: 1})
    
    # Calls the function to create the Huffman tree and takes the root
    root = create_tree(mapping_key)
    # Creates the binary code
    create_binary_code(root, '')

    # This is only here to print to the console the encoding scheme
    print("Huffman encoding scheme for optimal binary encoding efficiency:")
    print(" Character | Huffman code")
    for char in mapping_key:
        print(' %-9r |%12s' % (char, character_binary_mapping[char]))

    # Create the full binary code for the Huffman encoded string
    final_binary_string = ''
    for c in string_data:
        final_binary_string += character_binary_mapping[c]
    return final_binary_string
    

encoded_huffman_string = huffman_encode(rle_data)

#print(huffman_encode(rle_data))

print("First 1000 characters of the Huffman Encoded String:")
print_huffman_string = encoded_huffman_string[:1000]
print(print_huffman_string)

print("Original file length:")
print(len(binary_data))

print("RLE file length:")
print(len(rle_data))

print("Huffman Encoded file length:")
print(len(encoded_huffman_string))