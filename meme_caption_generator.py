import random
import re
from dataclasses import dataclass


@dataclass
class MemeResult:
    topic: str
    mood: str
    captions: list
    hashtags: list


def _clean_topic(topic: str) -> str:
    """Clean and normalize topic text."""
    topic = topic.strip()
    topic = re.sub(r"\s+", " ", topic)
    return topic[:60] if len(topic) > 60 else topic


def meme_caption_generator(topic: str, mood: str = "chaotic", k: int = 5) -> MemeResult:
    """
    Generate meme-style captions based on a topic and mood.

    Parameters:
    topic (str): Subject of the meme (e.g., 'final exams', 'group projects')
    mood (str): One of {'wholesome', 'sarcastic', 'chaotic', 'motivational', 'tired'}
    k (int): Number of captions to generate (1–10)

    Returns:
    MemeResult: Generated captions and hashtags
    """

    topic = _clean_topic(topic)
    mood = mood.lower().strip()
    k = max(1, min(int(k), 10))

    caption_bank = {
        "wholesome": [
            "Me realizing {topic} is hard… but I’m harder 💪",
            "Small progress on {topic} today = big win tomorrow 🌱",
            "POV: You didn’t quit {topic}. Proud of you 🫶",
            "Reminder: You don’t need perfect {topic}, you need consistent {topic} ✅",
        ],
        "sarcastic": [
            "I love {topic}. By love, I mean I tolerate it aggressively 🙂",
            "My relationship with {topic}: it’s complicated.",
            "If {topic} wanted me to succeed, it would stop being {topic}.",
            "I opened {topic} and immediately needed a break.",
        ],
        "chaotic": [
            "POV: You start {topic} at 11:59 PM like it’s a lifestyle.",
            "Me: ‘I’ll do {topic} early.’ Also me: *inventing new procrastination hobbies*",
            "I touched {topic} once. Now it’s emotionally attached.",
            "Brain during {topic}: buffering… buffering… buffering…",
        ],
        "motivational": [
            "Today’s {topic} struggle is tomorrow’s skill set 🚀",
            "One step at a time — {topic} doesn’t stand a chance.",
            "Consistency > motivation. {topic} is getting done. Period.",
            "You’re not behind. You’re building. Keep going with {topic}.",
        ],
        "tired": [
            "I put {topic} on my to-do list so it could feel included.",
            "Energy level for {topic}: 2%. Confidence: 98%.",
            "I’m not avoiding {topic}. I’m just… strategically resting.",
            "If {topic} was a person, I’d mute them.",
        ],
    }

    if mood not in caption_bank:
        mood = "chaotic"

    templates = caption_bank[mood]
    selected = random.sample(templates, k=min(k, len(templates)))
    captions = [template.format(topic=topic) for template in selected]

    hashtags = [
        f"#{re.sub(r'[^a-zA-Z0-9]+', '', topic.title())}",
        "#meme",
        "#coding",
        "#productivity",
        "#studentlife",
    ]

    return MemeResult(
        topic=topic,
        mood=mood,
        captions=captions,
        hashtags=hashtags,
    )


if __name__ == "__main__":
    result = meme_caption_generator("final exams", mood="chaotic", k=4)

    print(f"Topic: {result.topic} | Mood: {result.mood}\n")
    for i, caption in enumerate(result.captions, 1):
        print(f"{i}. {caption}")
    print("\nHashtags:", " ".join(result.hashtags))
