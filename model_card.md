# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

    My current scoring logic can create a filter bubble around energy level because energy closeness is weighted much more heavily than genre or mood matches. A song with very close energy to the user's target can outrank a song that better matches their genre or mood preference, which means users get pulled into one energy band repeatedly. Additionally, the system uses exact string matching for genre and mood, so related concepts like "sad" and "melancholic" are treated as completely different, and users with rare or missing genres in the catalog fall back to energy-based recommendations only. Finally, some stored user preferences like likes_acoustic are ignored entirely by the scoring logic, making personalization incomplete for users who care about sound texture or instrumentation.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested five different user profiles to evaluate how the system behaves:
- High-Energy Pop — someone who wants happy, upbeat pop music (energy: 0.9)
- Chill Lofi — someone who wants relaxing, focused lofi tracks (energy: 0.35)
- Deep Intense Rock — someone who wants intense, energetic rock (energy: 0.95)
- Edge Case: Sad But High Energy — someone with conflicting preferences (pop + sad + high energy)
- Edge Case: Unknown Genre — someone asking for a genre not in the catalog (opera)

The biggest surprise was why "Gym Hero" kept showing up for the "Happy Pop" user, even though "Gym Hero" has the mood "intense," not "happy." At first this seemed like a bug, but then I realized the problem: "Gym Hero" has an energy level of 0.93, which is almost perfect for a user targeting 0.9. Because my scoring gives energy closeness a weight of 3.0,  compared to only 1.0 for mood, the system rewards the near-perfect energy match so heavily that it outweighs the mood mismatch. So a user just looking for happy pop gets a song called "Gym Hero" that is intense and pumped-up, even though the vibe is totally different. It's like the recommender is saying, "You want pop + happy + high energy, and here's a song with pop + high energy, so close enough!" — but it misses that the actual feeling is wrong. This showed me that my system can accidentally ignore what the user actually feels when their preference for energy is strong.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
