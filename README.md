# HXXPXXH
HXXPXXH is a tool that scrapes web pages.  It is split in to two tools, HXXP
and PXXH.

# HXXP
HXXP connects to a url, issues an HTTP request, and recieves an HTTP resonse.
The headers and body is extracted from the response and stored in a SQLITE database along with the timestamp.
The timestamp is in format YYYYMMDD

# PXXH
Used to retrieve records stored by HXXP by timestamp.
If record exists, url,header,and body are printed out for corresponding record

## Usage

HXXP is executed as follows:

```
python hxxp.py --db <DB_PATH> <URL>
```

Concretely,

```
python hxxp.py --db sqlite.db https://www.example.com
```

PXXH is executed as follows:

```
python pxxh.py --db <DB_PATH> <TIMESTAMP: YYYYMMDD>
```

Concretely,

```
python pxxh.py --db sqlite.db 20180530
```

## Definitions

DB_PATH is a sqlite database (default: sqlite.db).
URL is an HTTP or HTTPS url to connect to (e.g. https://www.example.com).
TIMESTAMP is a 4-digit Year, 2-digit Month, 2-digit Day formatted timestamp.

