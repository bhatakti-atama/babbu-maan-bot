def read_prompt(path="./LLM_prompts/system_prompt.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()