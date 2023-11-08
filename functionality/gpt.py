import openai
from data.data import Data
import data.credentials

openai.api_key = credentials.openai_api_key

def api_calling(prompt: str):
    copmletions = openai.Completion.create(
        engine = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    message = copmletions.choices[0].text
    return message

def bot_output(input):
    reply = []
    s = list(sum(reply, ()))
    s.append(input)
    inp = ' '.join(s)
    output = api_calling(inp)
    reply.append((input, output))
    return reply  

def last_opp(files):
    file_paths = [file.name for file in files]
    return file_paths

def create_prompt_from_file(files):
    f = open(files.name, 'r')
    tekst = f.read()
    prompter = "Skriv en bildebeskrivelse som kan sendes til StableDiffusion basert på teksten under. Start på beskrivelsen med en gang.\n\n" + tekst
    svar = bot_output(prompter)
    return svar

def create_prompt_from_text(text: str) -> str:
    prompter = "Lag en bildebeskrivelse med nøkkelord basert på av teksten under. Start på beskrivelsen med en gang. Teksten skal være på engelsk. Maks 300 tegn.\n\n" + text
    svar = bot_output(prompter)
    return svar

def create_summary_from_file(files):
    f = open(files.name, 'r')
    tekst = f.read()
    sammendrag = "Lag et sammendrag av teksten under:\n\n" + tekst
    svar = bot_output(sammendrag)
    return svar

def create_summary_from_text(text: str) -> str:
    sammendrag = "Lag et sammendrag av teksten under:\n\n" + text
    svar = bot_output(sammendrag)
    return svar

def hent_svar(prompt):
    svar = api_calling(prompt)
    print (svar)
    return svar

def skip_bot(fil):
    bildebeskrivelse = hent_svar(fil)
    return bildebeskrivelse