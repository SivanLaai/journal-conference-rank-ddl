# jours && conference cli

WIP

## install

```bash
pip install -r req.txt
```

## usage

```bash
python3 ./cli/crawler.py --sql_url mysql+pymysql://username:password@host:port/database?charset=utf8mb4 --source_url web_url
```

| Argument | Type  | Description                          | Example            |
| -------- | ----- | ------------------------------------ | ------------------ |
| `--sql_url` | str | A url to connect mysql.  | `--sql_url url` |
| `--source_url`  | str | source url. | `--source_url http://example.com `      |
