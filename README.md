# ICC Job Gender Decoder

This is a simple job ad checker for gender coded words.

Steps to run:
  - Feminine coded words should be added to feminine.txt (one word per line)
  - Masculine coded words should be added to masculine.txt (one word per line)
  - List of ads should be added to urls.txt

```sh
$ python3 -m venv venv && source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 job_check.py
```

Example output:

```sh
{
    "job_title": "Chief Technology Officer",
    "job_url": "https://www.unicc.org/working-with-icc/chief-technology-officer/",
    "masculine_coded_words": [],
    "feminine_coded_words": [
        {
            "word": "interpersonal",
            "count": 1
        },
        {
            "word": "sharing",
            "count": 1
        },
        {
            "word": "support",
            "count": 7
        },
        {
            "word": "understand",
            "count": 1
        }
    ],
    "masculine_coded_words_total": 0,
    "feminine_coded_words_total": 4
}
```

License
----

MIT

