import os
import openai
from decouple import config

from latex_compiler import generate_letter
from indeed_scraper import get_job_data

job_data = get_job_data(['data', 'engineer'], location='United+States')
api_key = config('OPENAI_API_KEY')
job_letters = {}

for k,v in job_data.items():
  v_clean = v.replace('\n', ' ')
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"""
  generate a letter applying to the following job.

  job description: {v_clean}


  application:""",
  
  temperature=0.3,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
  )
  print(response)

  written_application = response.choices[0]['text']
  ## add my name

  job_letters[k] = written_application.replace('[Your name]', 'Mark Zurbruegg')

  generate_letter(job_letters[k], k)

  