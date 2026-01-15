from transformers import pipeline

summarizer = pipeline("summarization")
text = """
This project sounds fun, and it’s right in my wheelhouse. I work with AI image generation and visual compositing tools to create realistic, high-quality character integrations, and I’m confident I can recreate the Jon Hamm “Baby Turn the Lights Off” meme with your full-body image blended naturally into the scene.

From a technical side, I use diffusion-based AI models (such as Stable Diffusion workflows), combined with prompt engineering, image-to-image generation, ControlNet/pose guidance, and multi-reference conditioning to maintain accurate likeness. I also handle manual post-processing (lighting correction, shadow matching, proportion fixes) to ensure the final result looks realistic—not obviously AI-generated.

I’ve created similar AI-driven memes and character recreations, where realism and timing are key. I’ll use the multiple reference photos you provide to match body proportions, facial structure, and overall style, and I can match the original meme length or extend it slightly if needed. I’m happy to share portfolio samples that show my experience with realistic AI composites and meme-style content.
"""

summary = summarizer(
    text,
    max_length=20,
    min_length=10,
    do_sample=False
    # truncation=true # tokenizer automatically cut off the input text at the model's maximum token limit
)

print(summary[0]["summary_text"])

# define a summarization function

def summarize_text(text, max_len=80):
    return summarizer(
        text,
        max_length = max_len,
        min_length = max_len // 2,
        do_sample = False
    )[0]["summary_text"]

summary = summarize_text(text)
print("The Summarization : ", summary)