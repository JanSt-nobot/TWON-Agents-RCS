def get_explicit_agent_config():
    return {
        "model": "tiiuae/falcon-7b-instruct",
        "prompts": {
            "read": "Decide with yes or no, {character}, if the person would read the following text: '''{content}'''",
            "like": "Decide with yes or no, {character}, if the person would like the following text: '''{content}'''",
            "share": "Decide with yes or no, {character}, if the person would share the following text: '''{content}'''",
            "reply": "Reply, {character}, in the form of a tweet to the following text: '''{content}'''"
        }
    }


def get_explicit_agent_definition():
    return {
        'base': {
            "label": "🤖 Plain Model",
            "persona": ""
        },
        "agreeing": {
            "label": "🙆 Agreeing Agent",
            "persona": "while imagining you are an individual agreeing with the content"
        },
        "disagreeing": {
            "label": "🙅 Disagreeing Agent",
            "persona": "while imagining you are an individual disagreeing with the content"
        },
        "conspiracy_theorist": {
            "label": "🛸 Conspiracy Theorist",
            "persona": "while imagining you are a conspiracy theorist"
        },
        "nobel_prize_winner": {
            "label": "🏅 Nobel Prize Winner",
            "persona": "while imagining you are a nobel prize winner"
        },
        "us_congress_member": {
            "label": "🏛️ US Congress Member",
            "persona": "while imagining you are a member of the U.S. congress"
        }
    }
