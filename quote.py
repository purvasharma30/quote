import random

def get_random_quote():
    quotes = [
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
        # Add more quotes as needed
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    input("Press Enter to get a random quote...")
    quote = get_random_quote()
    print(f"\n{quote}")
