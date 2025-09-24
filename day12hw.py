def get_feedback():
    try:
        user = input("Please enter your name: ")
        feedback = input("Please enter your feedback: ")

        if not user or not feedback:
            raise ValueError("Name and feedback cannot be empty.")

        print(f"\nThank you, {user}, for your feedback!")
        print(f"Your feedback: \"{feedback}\" has been recorded.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    finally:
        print("\nFeedback session ended.")
get_feedback()
    