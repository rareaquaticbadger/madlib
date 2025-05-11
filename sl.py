import streamlit as st

# Title of the app
st.title("Madlib Story Generator: The Fantastic Family of Kuldeep")

# Extra amusing words list
extra_words = [
    "playfully", "zany", "quirky", "ridiculously", "supercalifragilistic",
    "flamboyantly", "majestically", "whimsically", "uproariously",
    "exuberantly", "absurdly", "magnificently", "splendidly",
    "bamboozlingly", "hilariously"
]

# Sidebar: select extra words
st.sidebar.header("Make it more amusing")
selected_words = st.sidebar.multiselect(
    "Select extra words to add at the start:",
    extra_words
)

# Main inputs
st.header("Fill in the blanks for your story")
adjective1 = st.text_input("Adjective for Kuldeep (e.g., 'fantastic', 'amazing'): ")
verb1 = st.text_input("Verb (present tense) for Kuldeep (e.g., 'juggle', 'whisper'): ")
activity = st.text_input("Fun activity (e.g., 'dance', 'paint'): ")
place = st.text_input("Place (e.g., 'moon', 'playground'): ")
adverb = st.text_input("Adverb (e.g., 'gracefully', 'loudly'): ")
adjective2 = st.text_input("Adjective for the big plan (e.g., 'brilliant', 'absurd'): ")
object1 = st.text_input("Funny object (e.g., 'rubber chicken', 'glitter gun'): ")
verb2 = st.text_input("Action taught to squirrels (e.g., 'tap dance', 'breakdance'): ")
emotion = st.text_input("Emotion felt by squirrels (e.g., 'ecstatic', 'confused'): ")
# Inputs for father Mark
clumsy_action = st.text_input("Action (present tense) (e.g., 'walk', 'run'): ")
problem = st.text_input("object (e.g., 'shoes', 'toys'): ")
solution_verb = st.text_input("Verb for Kuldeep solving it (e.g., 'rescue', 'fix'): ")
# New inputs for extra skills and circus
skill1 = st.text_input("First additional skill for squirrels (e.g., 'karaoke'): ")
skill2 = st.text_input("Second additional skill for squirrels (e.g., 'juggling'): ")
circus_name = st.text_input("Name for a circus (e.g., 'The Great Stromboli's'): ")
fortune = st.text_input("What they became (e.g., 'millionaires', 'infamous'): ")

# Generate button
if st.button("Generate Story"):
    # Compose prefix
    prefix = ""
    if selected_words:
        prefix = " ".join(selected_words).capitalize() + "...\n"
    # Story template with updated placeholders
    story = f"""{prefix}
Once upon a time, there was a {adjective1 or 'fantastic'} mother named Kuldeep.
Every morning she would {verb1 or 'juggle'} with her two children, Dev and Asha, and {activity or 'paint'} with them full of joy.
One day they decided to go to the {place or 'park'} to play.
Suddenly, Kuldeep {adverb or 'heroically'} pulled out a {object1 or 'marvelous gadget'} and taught nearby squirrels how to {verb2 or 'tap dance'}.
The squirrels, feeling {emotion or 'ecstatic'}, began to dance in a circle.
Meanwhile, their father Mark tried to {clumsy_action or 'walk'} while distracted by the squirrels, and instead caused a gigantic mess!
Jam everywhere!  {problem or 'shoes'} ruined! The whole scene was chaotic.
Quick-thinking Kuldeep stepped in to {solution_verb or 'save the day'}, mopping up jam and untangling toys with her signature flair.
Then she challenged Dev and Asha to teach the squirrels additional skills, like {skill1 or 'karaoke'} and {skill2 or 'juggling'}.
With this {adjective2 or 'brilliant'} plan, they opened the first ever circus, {circus_name or 'squirrel circus'}, and became {fortune or 'millionaires'}.
And so, thanks to Kuldeep’s quick wits (and despite Mark’s blunders), they all lived happily ever after!"""
    # Display the story
    st.write(story)
