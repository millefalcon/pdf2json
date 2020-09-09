pdf2json
########
A simple pdf resume to json converter.

Create JSON from Resume PDF from the command line.

Requires the Pdfminer.six_ library. Should work on 3.6+.

.. _Pdfminer.six: https://github.com/pdfminer/pdfminer.six


Install
=======

Install from github::

   $ python3 -m venv .env # create a virtualenv
   $ .env/bin/pip install git+https://github.com/millefalcon/pdf2json.git@master#egg=pdf2json


Usage
=====

General usage::

   $ pdf2json --help
   usage: pdf2json [-h] -i INFILE [-o OUTFILE]

   Convert Resume PDF to JSON

   optional arguments:
     -h, --help            show this help message and exit
     -i INFILE, --infile INFILE
                           input file name of the PDF for the converter
     -o OUTFILE, --outfile OUTFILE
                           output file name to save JSON

Convert command::

   By default, the JSON is written to stdout.

   $ pdf2json -i data/Interview_sample_data.pdf
   dict_keys(['name', 'phone', 'email', 'address', 'Education', 'Leadership Experience', 'Professional Experience', 'Additional Projects', 'Skills & Interests'])
   {
       "name": "Burk Lee",
       "phone": "(XXX) XXX-XXX",
       "email": "burk.lee@gmail.com",
       "address": "City, State Zip Code",
       "Education": "May 2023University of California, BerkeleyGPA: 3.7Intended: Bachelor of Arts in PsychologyBalboa High School, San FranciscoHigh School DiplomaRelevant Coursework:program development, research methodsdata analysis, child development and adolescence, public services, administration,June 2019",
       "Leadership Experience": "ASUC Student Union Event Services – Berkeley, CAAugust 2019-PresentEvent Planning Assistant● Assist with the quality of services for students and staff at UC Berkeley campus.● Organize and prepare the materials and equipment needed for events serving over 100+ guests.● Maintain a positive guest experience by ensuring all event requests were met in a timely manner.Barany Consulting- Berkeley, CAExternshipDecember 2019-January 2020● Explored work environments aligned to personal career and educational goals in social services byparticipating in training, presentations, and workshops to enhance communication skills.● Assisted staff to complete administrative projects: emails, phone transfers, printing, scanning.● Connected with alumni to explore opportunities for personal and professional growth within theconsulting industry.",
       "Professional Experience": "Target- San Francisco, CAMay 2018- June 2019Sales Associate● Monitored inventory and restocked items as requested by store manager and team.● Provided memorable customer service by assisting with merchandise to meet demands of company.● Multitasked in a face pace environment to produce high volume of sales to meet weekly benchmarks.● Operated computerized cash register and processed membership accounts.",
       "Additional Projects": "June 2018Child Development Research● Collected data from online reports to analyze the findings to present a 15-page research paper.● Interviewed with students on campus to record over 50 responses to gain insight of their perceptions onthe developmental stages of children.● Presented a 10-minute presentation while facilitating a Q&A panel regarding research results.",
       "Skills & Interests": "Proficient with Microsoft Suite, Adobe Photoshop and Illustrator, Google PlatformsTechnical:Language:Basic Tagalog (written and verbal)Community Service with over 100+ volunteer hours, traveler to over 5 countries in Asia.Interests:"
   }


Write output tot a file::

   $ pdf2json -i data/Interview_sample_data.pdf -o out.json
   $ cat out.json
   {
       "name": "Burk Lee",
       "phone": "(XXX) XXX-XXX",
       "email": "burk.lee@gmail.com",
       "address": "City, State Zip Code",
       "Education": "May 2023University of California, BerkeleyGPA: 3.7Intended: Bachelor of Arts in PsychologyBalboa High School, San FranciscoHigh School DiplomaRelevant Coursework:program development, research methodsdata analysis, child development and adolescence, public services, administration,June 2019",
       "Leadership Experience": "ASUC Student Union Event Services – Berkeley, CAAugust 2019-PresentEvent Planning Assistant● Assist with the quality of services for students and staff at UC Berkeley campus.● Organize and prepare the materials and equipment needed for events serving over 100+ guests.● Maintain a positive guest experience by ensuring all event requests were met in a timely manner.Barany Consulting- Berkeley, CAExternshipDecember 2019-January 2020● Explored work environments aligned to personal career and educational goals in social services byparticipating in training, presentations, and workshops to enhance communication skills.● Assisted staff to complete administrative projects: emails, phone transfers, printing, scanning.● Connected with alumni to explore opportunities for personal and professional growth within theconsulting industry.",
       "Professional Experience": "Target- San Francisco, CAMay 2018- June 2019Sales Associate● Monitored inventory and restocked items as requested by store manager and team.● Provided memorable customer service by assisting with merchandise to meet demands of company.● Multitasked in a face pace environment to produce high volume of sales to meet weekly benchmarks.● Operated computerized cash register and processed membership accounts.",
       "Additional Projects": "June 2018Child Development Research● Collected data from online reports to analyze the findings to present a 15-page research paper.● Interviewed with students on campus to record over 50 responses to gain insight of their perceptions onthe developmental stages of children.● Presented a 10-minute presentation while facilitating a Q&A panel regarding research results.",
       "Skills & Interests": "Proficient with Microsoft Suite, Adobe Photoshop and Illustrator, Google PlatformsTechnical:Language:Basic Tagalog (written and verbal)Community Service with over 100+ volunteer hours, traveler to over 5 countries in Asia.Interests:"
   }  


Develop
=======

Clone from github::
   
   $ python3 -m venv .env # create a virtualenv
   $ git clone https://github.com/millefalcon/pdf2json
   $ cd pdf2json/
   $ .env/bin/pip install -e .
   $ .env/bin/python -m unittest pdf2json
   ..
   ----------------------------------------------------------------------
   Ran 2 tests in 0.901s

   OK

Happy hacking!

