from sum import add
from difference import subtract
from multiply import multiply
from divide import divide
from modulus import modulus

def main():
    a = 10
    b = 3
    
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))
    print("Modulus:", modulus(a, b))

if __name__ == "__main__":
    main()
