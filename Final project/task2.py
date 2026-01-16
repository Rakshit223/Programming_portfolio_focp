import random
import sys

def password_security_check():
    # 1. Get password input
    password = input("Enter your password: ")
    
    # 2. Length check (Must be at least 9 characters)
    if len(password) < 9:
        print("Password too short.")
        return # Exit the program

    # 3. Random Character Verification
    # We need to perform the check 3 times
    for _ in range(3):
        # Generate a random position (1 to length of password)
        # Note: We use 1-based indexing to match the user's view
        pos = random.randint(1, len(password))
        
        char_input = input(f"Enter letter at position {pos}: ")
        
        # Check if the input matches the character at that position
        # We subtract 1 from 'pos' because Python indexing starts at 0
        if char_input == password[pos - 1]:
            print("Correct")
        else:
            print("\nSecurity check failed.")
            sys.exit() # Exit immediately on failure

    # 4. Success message if all 3 checks pass
    print("Security check passed.")

if __name__ == "__main__":
    password_security_check()