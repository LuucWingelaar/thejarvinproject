import ollama # Teacher Erik suggested using the Groq API, but I'm going to run an LLM locally! Better for privacy, and even better: it's completely free! No strings attached! Hope this works out too, if not: I'll hear about it :)

'''
First experiment for the minor Big Data & Design
CLI based song generator using a local LLM! 
The use of a local LLM is because this is better for privacy, and it's totally free! Win-win!
'''


class SongGenerator:
    def __init__(self, model = "llama3"): # We don't like hardcoding, but having a base value is always a nice thing to just run things
        self.model = model
    def generate_song(self, topic="love", style="pop", language="English", verses=2):
        # Prompt for generating the song
        prompt = (
            f"""Write a {style} song about {topic} in {language} language.
            Include {verses} verses and a chorus
            Make it sound as natural and flowing as possible
            """
        )
        response = ollama.chat(model=self.model, messages=
        [{"role": "system", "content": """
        You are a creative and talented songwriter. 
        Your job is to assist the user in creating a song with their chosen preferences. 
        """},
        {"role": "user", "content": prompt}])
        return response["message"]["content"]

def main():
    print("🎵 Welcome to the Local Song Generator 🎵")
    generator = SongGenerator(model="llama3")

    while True:
        print("\nNew Song")
        topic = input("Enter a song topic (e.g. love, nostalgia, freedom): ").strip()
        style = input("Enter a musical style (e.g. pop, rock, rap, folk): ").strip()
        language = input("Enter a language (e.g. English): ").strip()
        verses_amount = input("How many verses_amount should the song have? (default 2): ").strip()
        verses_amount = int(verses_amount) if verses_amount.isdigit() else 2 # 2 is default, since it's quite common

        print("\nGenerating your song... please wait\n")
        song = generator.generate_song(topic=topic, style=style, language=language, verses=verses_amount) # using explicit value initialisation and assignment, so the arrangement doesn't matter, seeing as implicit assignment can become an issue when working with a larger amount of parameters
        print("Your Generated Song\n")
        print(song)

        # Ask the user if they want to generate another one
        again = input("\nWould you like to generate another song? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\n👋 Thanks for using the Song Generator! Goodbye!")
            break


if __name__ == "__main__":
    main()