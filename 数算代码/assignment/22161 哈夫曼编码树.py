import heapq
class TreeNode:
    def __init__(self, val, char=None):
        self.val = val
        self.char = char
        self.left = None
        self.right = None
        
def build_huffman_tree(char_freq):
    pq = []
    for char, freq in char_freq:
        heapq.heappush(pq, (freq, TreeNode(freq, char)))
    while len(pq) > 1:
        freq1, node1 = heapq.heappop(pq)
        freq2, node2 = heapq.heappop(pq)
        merged_node = TreeNode(freq1 + freq2)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(pq, (freq1 + freq2, merged_node))
    return pq[0][1]

def generate_codes(root):
    def dfs(node, code, result):
        if node:
            if node.char:
                result[node.char] = code
            dfs(node.left, code + '0', result)
            dfs(node.right, code + '1', result)
    codes = {}
    dfs(root, '', codes)
    return codes

def encode_string(string, codes):
    return ''.join(codes[char] for char in string)

def decode_string(encoded_string, root):
    decoded_string = ''
    node = root
    for bit in encoded_string:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            decoded_string += node.char
            node = root
    return decoded_string

n = int(input())
char_freq = []
for _ in range(n):
    char, freq = input().split()
    char_freq.append((char, int(freq)))
root = build_huffman_tree(char_freq)
codes = generate_codes(root)
while True:
    try:
        line = input().strip()
        if line.isdigit():
            print(decode_string(line, root))
        else:
            print(encode_string(line, codes))
    except EOFError:
        break