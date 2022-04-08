import os
import openai
from decouple import config

api_key = config('OPENAI_API_KEY')

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="""
  write a job application for the following job description

job description: "Job Description

General Summary:

The Cell Biology and Protein Biochemistry Senior Research Scientist works with some independence and is adept at conceptually outlining studies to design and execute focused research projects or a series of complex experimental procedures. These may include mammalian cell culture manipulation and maintenance, generation and use of cell lines derived from ex vivo material and differentiated stem cells as well as performing cellular and protein-based assays. Completes work in a resourceful, self-sufﬁcient manner and is able to design alternative approaches to achieve desired outcomes. Keeps current on the scientiﬁc literature relevant to scientiﬁc methodology or ﬁeld(s) of technical expertise. This level captures both the Research organization’s entry level for staff with a research doctoral degree (PhD) and the advanced experimental expert leading one or more critical laboratory functions with high impact on drug discovery projects.

Key Duties and Responsibilities:

Designs and conducts elaborate, conceptually connected, multi-component experiments which use a variety of techniques acquired from cellular biology and protein sciences, which could include:
Mammalian cell culture, manipulation, and maintenance
Generation and use of cell lines derived from ex vivo material and differentiated stem cells
Protein science techniques including mutagenesis and recombinant protein production
Molecular biology techniques including genotyping, PCR, and cloning
Gene expression approaches including qPCR, FACS, ICC, and Western blot
In vitro phenotyping methods including ELISA and other assays
Collates and interprets data systematically, and synthesizes results into a cohesive body of conclusions or recommendations to guide Project decisions and new research activities
Exercises solid judgment to prioritize studies, considering feasibility and Project impact
Performs advanced experimental troubleshooting
Scours relevant scientiﬁc literature and routinely incorporates new insights into research activities
Identiﬁes, prioritizes and introduces relevant emerging technologies in ﬁeld of expertise to advance the existing technology platforms and create/maintain a competitive advantage
Explores the feasibility of applying new scientiﬁc principles/concepts or implements and validates new experimental approaches and technologies to achieve project goals
Independently prepares study presentations and presents experimental conclusions at internal Group/Department or Project Team research meetings
Performs other duties as assigned"


job application:""",
  
  temperature=0.3,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)
print(response)

response.keys()
response['choices'][0]