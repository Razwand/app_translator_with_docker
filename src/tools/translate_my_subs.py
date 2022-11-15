
import os.path, sys
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer

def initialize_model_and_tokens():
    model_checkpoint = "razwand/opus-mt-en-mul-finetuned_en_sp_translator"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

    return(model, tokenizer)

def translate(line, model, tokenizer):
    'Using model to translate a line'
    text = tokenizer([line],return_tensors="pt")
    output_text = model.generate(text['input_ids'])
    output = tokenizer.decode(output_text.squeeze(), skip_special_tokens=True)
    return(output)

def main_translator(text):
    '''
    This main function reads the original file and calls the rest of the translation flow to
    write the translated subtitle into the new file with name <file_name>_SP.srt.
    '''
    model, tokenizer = initialize_model_and_tokens()
    translated_text = translate(text, model, tokenizer)

    dict_res = {}
    dict_res['Translated_Text'] = translated_text
    
    return dict_res
    
                
